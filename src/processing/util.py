"""
Util functions
"""

from os.path import join, exists, isfile
from os import listdir
import json
import os


def has_files(path: str) -> bool:
    """
    Checks if there is any file in the given path.
    If not files, is not possible continue.

    :param path: A str like /to/path/
    :return: A bool True/False
    """
    assert exists(path), "--path is not correct"
    return any([j for j in listdir(path) if j.endswith('.jpg')])


def list_images(path: str) -> list:
    """
    Return a list of files that ends with .txt extension

    :param path: A str like /to/path/
    :return: A list that contains all found files
    """
    assert exists(path), "--path is not correct"
    return [j for j in listdir(path) if j.endswith('.jpg')]


def save_images_log(path: str) -> list:
    """
    Grab images list and save a log in a specific path.

    :param path: A str like /to/path/
    """
    assert exists(path), "--path is not correct"
    if not has_files(path):
        print("Not images found, try using other path or adding images")
        exit(0)  # If not images, exit, cause it is necessary to have xml and jpg together
    else:
        images = list_images(path)
        f = open(join(path, "image.txt"), 'w')
        [f.write("%s\n" % x) for x in images]
        f.close()
        return images


def read_json(dir_path: str, filename: str) -> json:
    """
    To read json files

    :param dir_path: A str like /to/path/
    :param filename: A str, json file name e.g data.json
    :return: A JSON file object
    """
    file = join(dir_path, filename)
    assert isfile(file), "-- check your path file"
    return json.load(open(file))


def remove_file(file_name: str):
    """
    Remove a given file, if not raises assert.

    :param file_name: A str like /to/path/file
    """
    assert isfile(file_name), "-- check your path file"
    os.remove(file_name)
    print("Deleting file %s" % file_name)
