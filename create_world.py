import random
from worker import Worker
from resources import Resources

V_FACTOR = .2


if __name__ == "__main__":
    resources = Resources()
    trees = Worker("Forest", {}, {"Trees": 10})
    stone = Worker("Mts", {}, {"Stone": 5})

    lumberjack = Worker("Lumberjack", {"Trees": 1}, {"Wood": 10})
    mason = Worker("Mason", {"Stone": 1}, {"Brick": 5})
    axe_maker = Worker("Axe Maker", {"Wood": 1, "Stone": 1}, {"Axe": 1})

    worker_list = []
    worker_list.extend([trees, stone, lumberjack, mason, axe_maker])

    for i in range(100):
        random.shuffle(worker_list)
        for worker in worker_list:
            resources = worker.make(resources)
            #print(resources)

    print(resources)

    






