from PIL.JpegImagePlugin import JpegImageFile
import xml.etree.ElementTree as ET
from PIL import Image, ImageDraw
from src.config import settings
from src.processing import util
import numpy as np
import os
import cv2

dataset = os.path.join(settings.DEFAULT_DATA, "kangaroo-master")
annots_dir = os.path.join(dataset, "annots")
annots_1 = os.path.join(dataset, "annots/00001.xml")
images_dir = os.path.join(dataset, "images")

images_1 = os.path.join(images_dir, "00001.jpg")

images_gt = os.path.join(dataset, "images_gt")


def load_image_pil(image_path: str) -> JpegImageFile:
    """
    Function to load image using PIL. If not correct
    file path raises an error.

    :param image_path: A str like /to/path/file
    :return: JpegImageFile image
    """
    assert os.path.isfile(image_path), "-- check your path file"
    return Image.open(image_path)


def load_image_cv2(image_path: str):
    """
    Function to load image using OpenCV. If not correct
    file path raises an error.

    :param image_path: A str like /to/path/file
    :return: image - np array
    """
    assert os.path.isfile(image_path), "-- check your path file"
    return cv2.imread(image_path)


def draw_gt_pil(img_pil: JpegImageFile, img_name: str, xmin: int, ymin: int, xmax: int, ymax: int):
    color = 'black'
    thickness = 2

    draw = ImageDraw.Draw(img_pil)
    draw.line([(xmin, ymin), (xmin, ymax), (xmax, ymax),
               (xmax, ymin), (xmin, ymin)], width=thickness, fill=color)
    del draw
    img_pil.save(os.path.join(images_gt, img_name), "JPEG")


def draw_gt_cv2(image: np.ndarray, img_name: str, xmin: int, ymin: int, xmax: int, ymax: int):
    color = (0, 0, 0)  # decimal code (r,g,v)
    thickness = 2

    cv2.rectangle(image, (xmax, ymax), (xmin, ymin), color=color, thickness=thickness)
    cv2.imwrite(os.path.join(images_gt, img_name), image)


def read_xml_draw_gt(path_images: str, path_annotations: str, image_list: list):
    for img in image_list:
        name_xml = img.split('.jpg')[0] + '.xml'

        # use pil or opencv to load images
        image = load_image_cv2(os.path.join(path_images, img))
        # image = load_image_pil(images_1)

        root = ET.ElementTree(file=os.path.join(path_annotations, name_xml)).getroot()
        for child_of_root in root:
            if child_of_root.tag == 'object':
                for child_of_object in child_of_root:
                    if child_of_object.tag == 'bndbox':
                        for child_of_root in child_of_object:
                            if child_of_root.tag == 'xmin':
                                xmin = int(child_of_root.text)
                            if child_of_root.tag == 'xmax':
                                xmax = int(child_of_root.text)
                            if child_of_root.tag == 'ymin':
                                ymin = int(child_of_root.text)
                            if child_of_root.tag == 'ymax':
                                ymax = int(child_of_root.text)

                # use pil or cv2 to draw the ground truth
                draw_gt_cv2(image, img, xmin, ymin, xmax, ymax)
                #  draw_gt_pil(image, '00001.jpg', xmin, ymin, xmax, ymax)


if __name__ == "__main__":
    images_list = util.save_images_log(images_dir)
    read_xml_draw_gt(images_dir, annots_dir, images_list)
