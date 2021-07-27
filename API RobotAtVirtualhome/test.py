#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Robot@VirtualHome Python API """
from RobotAtVirtualHome import RobotAtVirtualHome

__author__ = "David Fernandez Chaves"
__contact__ = "davfercha[at]uma.es"
__copyright__ = "Copyright 2020, David Fernandez-Chaves"
__date__ = "2021/04/01"
__license__ = "MIT"


def main():
    # Examples of use
    # dataset = RobotAtVirtualHome('D:\RobotAtVirtualHome\House1\Wandering')
    # print(dataset)
    #
    # print("\r\n")
    # print("Rooms in this dataset: ")
    # print(dataset.get_name_rooms())
    #
    # print("\r\n")
    # print("Room types in this dataset: ")
    # print(dataset.get_types_room())
    #
    # print("\r\n")
    # print("Meta-images from Bathroom_1 in this dataset: ")
    # print(len(dataset.get_meta_images_from("Bathroom_1")))
    #
    # print("\r\n")
    # print("Objects in Bathroom_1 in this dataset: ")
    # print(len(dataset.get_objects_from_room("Bedroom_3")))
    #
    # print("Checking in which images of a room an object is visible:")
    # obj = dataset.objects[10]
    # print(obj)
    # meta_images = dataset.get_meta_images_from("Bathroom_1")
    # for meta_im in meta_images:
    #     print(obj.id + " in meta-image " + meta_im.id + ": " + str(meta_im.has_object(obj)))
    #
    # # Example of image acquisition:
    # meta_image = dataset.meta_images["0"]
    # image = meta_image.get_image("rgb")

    # Obtaining statistics
    print("\r\n")
    print("Robot@VirtualHome Dataset Statistics")
    print("==================================")

    for i in range(1, 31):
        n_objs = 0
        n_rooms = 0
        n_images = 0

        print('\r\nHouse ' + str(i))
        dataset = RobotAtVirtualHome('D:\RobotAtVirtualHome\Home' + "{:02d}".format(i) + '\Grid')

        for o in dataset.objects:
            if o.type != "Wall":
                n_objs += 1

        n_rooms += len(dataset.get_name_rooms())

        n_images += len(dataset.captures)
        print('Number of images GRID: ' + str(len(dataset.captures)))
        dataset = RobotAtVirtualHome('D:\RobotAtVirtualHome\Home' + "{:02d}".format(i) + '\Wandering')
        n_images += len(dataset.captures)
        print('Number of images Wander: ' + str(len(dataset.captures)))
        for ii in range(1, 4):
            dataset = RobotAtVirtualHome('D:\RobotAtVirtualHome\Home' + "{:02d}".format(i) + '\Wandering' + str(ii))
            n_images += len(dataset.captures)
            print('Number of images Wander' + str(ii) + ': ' + str(len(dataset.captures)))

        print('Number of objects: ' + str(n_objs))
        print('Number of rooms: ' + str(n_rooms))
        print('Number of images: ' + str(n_images))

    # print("\r\n")
    # print("Robot@VirtualHome Dataset Statistics")
    # print("==================================")
    #
    # objtype = {"Burner": 0, "Dishwasher": 0, "WashingMachine": 0, "Bathtub": 0, "Towel": 0, "Closet": 0,
    #            "Refrigerator": 0, "Washbasin": 0, "TV": 0, "Microwave": 0, "Keyboard": 0, "Laptop": 0, "Table": 0,
    #            "Nightstand": 0, "Bed": 0, "Chair": 0, "Toilet": 0, "Desk": 0, "Cabinet": 0, "Sofa": 0, "Armchair": 0,
    #            "Sink": 0}
    #
    # for i in range(1, 31):
    #     print('\r\nHouse ' + str(i))
    #     dataset = RobotAtVirtualHome('D:\RobotAtVirtualHome\Home' +"{:02d}".format(i) + '\Grid')
    #
    #     for o in dataset.objects:
    #         if o.type in objtype.keys():
    #             objtype[o.type] += 1
    #
    #     for id in objtype.keys():
    #         print(id, ": ", objtype[id])


if __name__ == "__main__":
    main()
