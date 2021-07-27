#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Robot@VirtualHome Python API """
import csv

from Capture import Capture
from VirtualObject import VirtualObject

__author__ = "David Fernandez Chaves"
__contact__ = "davfercha[at]uma.es"
__copyright__ = "Copyright 2020, David Fernandez-Chaves"
__date__ = "2021/04/01"
__license__ = "MIT"


class RobotAtVirtualHome:
    def __init__(self, path):
        """
        Initialise a recorded track in Robot@VirtualHome

        Attributes
        =========

        path : Folder path of the recorded track to be loaded. For example: "House1/Wandering2".
        """

        self.path = path
        folder = path.split("\\")
        self.name = folder[-2]
        self.track = folder[-1]
        self.objects = []
        self.captures = {}

        try:
            with open(path + '\VirtualObjects.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                first = True
                for row in reader:
                    if first:
                        if row != ['id', 'color', 'room', 'roomType', 'type', 'globalPosition', 'rotation', 'seed']:
                            print(path + '\VirtualObjects.csv has an incorrect format.')
                        first = False
                    else:
                        self.objects.append(VirtualObject(row[0], row[1], row[2], row[3], row[4], row[5], row[6],
                                                          row[7]))
        except IOError:
            print(path + "\VirtualObjects.csv not accessible")

        try:
            nameFile = "\\LogImg.csv"
            if path.split("\\")[-1] == "Grid":
                nameFile = "\\InfoGrid.csv"

            with open(path + nameFile, newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=';')
                first = True
                for row in reader:
                    if first:
                        if row != ['photoID', 'robotPosition', 'robotRotation', 'cameraPosition', 'cameraRotation',
                                   'room']:
                            print(path + '\Info.csv has an incorrect format.')
                            return
                        first = False
                    else:
                        id = row[0][0:row[0].rfind('_')]
                        if not (id is self.captures.keys()):
                            self.captures[id] = Capture(id, row[1], row[2], row[3], row[4], row[5], path)
        except IOError:
            print(path + "\Info.csv not accessible")

    def __str__(self):
        s = "Robot@VirtualHome Dataset (v0.1.0)\r\n"
        s += "==================================\r\n"
        s += self.track + "-" + self.name + ": " + str(len(self.objects)) + " objects, " + str(
            len(self.captures)) + " meta-images"

        return s

    # Type acquisition
    def get_name_rooms(self):
        """Returns the name of all rooms found."""
        rooms = []
        for obj in self.objects:
            if not (obj.room in rooms):
                rooms.append(obj.room)
        return rooms

    def get_types_room(self):
        """Returns all different room types found."""
        room_types = []
        for obj in self.objects:
            if not (obj.roomType in room_types):
                room_types.append(obj.roomType)
        return room_types

    def get_meta_images_from(self, room):
        """Returns all meta-images taken in a room."""

        meta_images = []
        if not (room in self.get_name_rooms()):
            print("Room name not found.")
            return meta_images

        for im in self.captures:
            if self.captures[im].room == room:
                meta_images.append(self.captures[im])

        return meta_images

    # Objects adquisition
    def get_object_from_colour(self, color):
        """Returns an object from the given colour."""

        for obj in self.objects:
            if obj.color == color:
                return obj

        print("Colour not found.")
        return None

    def get_objects_from_colours(self, color):
        """Returns objects from a list of colours."""

        objects = []
        for c in color:
            objects.append(self.get_object_from_colour(c))

        return objects

    def get_objects_from_room(self, room):
        """Returns all objects in a room."""

        objs = []
        if not (room in self.get_name_rooms()):
            print("Room name not found.")
            return objs

        for obj in self.objects:
            if obj.room == room:
                objs.append(obj)

        return objs


def main():
    return 0


if __name__ == "__main__":
    main()
