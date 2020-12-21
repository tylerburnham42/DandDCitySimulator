


class Resource:

    def __init__(self, name, quantity, owner, quality, value, created):
        self.name = name
        self.quantity = quantity
        self.owner = owner
        self.quality = quality
        self.value = value
        self.created = created

    def __repr__(self):
        return "{} - {} - {}".format(self.name, self.quantity, self.value)