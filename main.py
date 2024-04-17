import random
import time
from random import randrange

'''
"altamente segura-0(RouteSafety0)", "segura-1(RouteSafety1)" , "aceitável-2(RouteSafety2)"
'''

#Route is like a Interface in Java
class Route:
    _levels = {0: "HighlySafe", 1: "Safe", 2: "Acceptable"}
    def get_route_safety_level(self):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError

class RouteSafety0(Route):

    _instance = None

    # call only once, Singleton Class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_instance(self):
        return self._instance

    def get_route_safety_level(self):
        return "Current safety level is {}".format(super()._levels[0])

    def move(self):
        return "Safety Level {}".format(super()._levels[0])

class RouteSafety1(Route):

    _instance = None

    # call only once, Singleton Class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_instance(self):
        return self._instance

    def get_route_safety_level(self):
        return "Current safety level is {}".format(super()._levels[1])

    def move(self):
        return "Safety Level {}".format(super()._levels[1])

class RouteSafety2(Route):

    _instance = None

    # call only once, Singleton Class
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def get_instance(self):
        return self._instance

    def get_route_safety_level(self):
        return "Current safety level is {}".format(super()._levels[2])

    def move(self):
        return "Safety Level {}".format(super()._levels[2])
class Walker():

    _name = None
    _route = None

    def __init__(self, name, route):
        self._name = name
        self._route = route

    def set_route(self, route):
        self._route = route

    def print_current_route(self):
        print("Walker Name: {}; Current: {}".format(self._name, self._route.get_route_safety_level()))

    def move(self):
        #move according to self._route assigned
        self._route.move()

if __name__ == '__main__':
    print("Starting navigation")

    safety0 = RouteSafety0()
    safety1 = RouteSafety1()
    safety2 = RouteSafety2()

    walkers = []
    walker1 = Walker("Walker1", safety0)
    walkers.append(walker1)
    walker2 = Walker("Walker2", safety0)
    walkers.append(walker2)
    walker3 = Walker("Walker3", safety0)
    walkers.append(walker3)

    while (True):
        #set route safety for each walker,
        for walker in walkers:
            current_safety = randrange(3)
            if current_safety == 0:
                walker.set_route(safety0)
            elif current_safety == 1:
                walker.set_route(safety1)
            else:
                walker.set_route(safety2)

        for walker in walkers:
            walker.move()
            walker.print_current_route()
        print("###########################")
        time.sleep(3)
