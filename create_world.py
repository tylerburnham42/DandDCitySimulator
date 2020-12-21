import random
from lumberjack import Lumberjack
from resource import Resource

V_FACTOR = .2


if __name__ == "__main__":
    resources = []
    resources.append(Resource("Tree", 1000, None, 5, 10, 0))

    lumberjack = Lumberjack(10, 100)

    for time in range(10):
        resources.extend(lumberjack.make(resources, time))
        print(resources)





