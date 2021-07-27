""" Robot@VirtualHome Python API """

from PIL import Image

__author__ = "David Fernandez Chaves"
__contact__ = "davfercha[at]uma.es"
__copyright__ = "Copyright 2020, David Fernandez-Chaves"
__date__ = "2021/04/01"
__license__ = "MIT"


class Capture:

    def __init__(self, _id, _robot_position, _robot_rotation, _camera_position, _camera_rotation, room, path):
        self.id = _id
        self.room = room
        self.path = path + "/" + _id

        position = _robot_position[1:_robot_position.find(')')].split(',')
        self.robotPosition = (float(position[0]), float(position[1]), float(position[2]))

        rotation = _robot_rotation[1:_robot_rotation.find(')')].split(',')
        self.robotRotation = (float(rotation[0]), float(rotation[1]), float(rotation[2]))

        camera_position = _camera_position[1:_camera_position.find(')')].split(',')
        self.cameraPosition = (float(camera_position[0]), float(camera_position[1]), float(camera_position[2]))

        camera_rotation = _camera_rotation[1:_camera_rotation.find(')')].split(',')
        self.cameraRotation = (float(camera_rotation[0]), float(camera_rotation[1]), float(camera_rotation[2]))

    def __str__(self):
        return "Image name: " + self.id

    # Images adquisition
    def get_image(self, _type):
        """Returns the image belonging to a meta-image."""

        if _type != "rgb" and _type != "mask" and _type != "depth":
            print("Type of image unknown.")
            return None

        return Image.open(self.path + "_" + _type + ".png").convert('RGB')

    def has_object(self, _objetc):
        """Check if an object is in the image."""
        im = self.get_image("mask")
        width, height = im.size
        im = im.load()
        for x in range(width):
            for y in range(height):
                if _objetc.color == im[x, y]:
                    return True

        return False

    def get_colors(self):
        """Gets the colour of all objects in the image."""
        colors = []
        im = self.get_image("mask")
        width, height = im.size
        im = im.load()
        for x in range(width):
            for y in range(height):
                if not(im[x, y] in colors):
                    colors.append(im[x, y])

        return False

