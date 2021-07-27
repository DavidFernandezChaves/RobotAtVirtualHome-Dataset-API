""" Robot@VirtualHome Python API """
import math

__author__ = "David Fernandez Chaves"
__contact__ = "davfercha[at]uma.es"
__copyright__ = "Copyright 2020, David Fernandez-Chaves"
__date__ = "2021/04/01"
__license__ = "MIT"


class VirtualObject:
    def __init__(self, _id, _color, _room, _room_type, _type, _global_position, _rotation, _seed):
        self.id = _id
        self.room = _room
        self.roomType = _room_type
        self.type = _type
        self.seed = int(_seed)

        _color = _color[5:_color.find(')')].split(',')
        self.color = (round(float(_color[0]) * 255), round(float(_color[1]) * 255), round(float(_color[2]) * 255))

        pose = _global_position[1:_global_position.find(')')].split(',')
        self.globalPosition = (float(pose[0]), float(pose[1]), float(pose[2]))

        _rotation = _rotation[1:_rotation.find(')')].split(',')
        self.rotation = (float(_rotation[0]), float(_rotation[1]), float(_rotation[2]))

    def __str__(self):
        return self.id + "{ Color: " + str(
            self.color) + ", Room: " + self.room + ", type: " + self.type + ", seed: " + str(self.seed) + "}"
