import random
import time
from random import randrange

'''
"altamente segura-0(RouteSafety0)", "segura-1(RouteSafety1)" , "aceitável-2(RouteSafety2)"
'''
gi
#Route is like a Interface in Java
class RouteSafety:
    _levels = {0: "HighlySafe", 1: "Safe", 2: "Acceptable"}
    def get_route_safety_level(self):
        raise NotImplementedError

    def move(self):
        raise NotImplementedError

class RouteSafety0(RouteSafety):

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

class RouteSafety1(RouteSafety):

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

class RouteSafety2(RouteSafety):

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

class Route:

    _name = None
    _route_safety = None
    def __init__(self, name, route_safety):
        self._name = name
        self._route_safety = route_safety

    def get_name(self):
        return self._name

    def get_route_safety(self):
        return self._route_safety.get_route_safety_level()

    def set_route_safety(self, route_safety):
        self._route_safety = route_safety

    def move(self):
        self._route_safety.move()


class Walker():

    _name = None
    _route = None

    def __init__(self, name, route):
        self._name = name
        self._route = route

    def set_route(self, current_safety):
        if current_safety == 0:
            self._route.set_route_safety(RouteSafety0())
        elif current_safety == 1:
            self._route.set_route_safety(RouteSafety1())
        else:
            self._route.set_route_safety(RouteSafety2())

    def print_current_route(self):
        print("Walker: {}; Current: {} {}".format(self._name, self._route.get_name(), self._route.get_route_safety()))

    def move(self):
        #move according to self._route assigned
        self._route.move()

if __name__ == '__main__':
    print("Starting navigation")

    route0 = Route("Route0", RouteSafety0())
    route1 = Route("Route1", RouteSafety1())
    route2 = Route("Route2", RouteSafety2())

    walkers = []
    walker0 = Walker("Walker0", route0)
    walkers.append(walker0)
    walker1 = Walker("Walker1", route1)
    walkers.append(walker1)
    walker2 = Walker("Walker2", route2)
    walkers.append(walker2)

    while (True):
        #set route safety for each walker,
        for walker in walkers:
            current_safety = randrange(3) #random route safety, 0=HighlySafe, 1=Safe, 2=Acceptable
            walker.set_route(current_safety)

        for walker in walkers:
            walker.move()
            walker.print_current_route()
        print("###########################")
        time.sleep(3)
