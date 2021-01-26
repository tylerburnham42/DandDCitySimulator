


class Resources:

    def __init__(self):
        self.resources = {}

    def __repr__(self):
        return "{}".format(self.resources)

    def add(self, name, quanity):
        if name in self.resources:
            self.resources[name] += quanity
        else:
            self.resources[name] = quanity

    def remove(self, name, quanity):
        if name in self.resources:
            self.resources[name] -= quanity

    def get_resources(self):
        return self.resources


    def get_quanity(self, name):
        if name in self.resources:
            return self.resources[name]
        else:
            return None

    def update_resources(self, in_dict, out_dict):
        canAdd = True
        for name in in_dict.keys():
            #print(name, self.resources[name], in_dict[name])
            if name not in self.resources or self.resources[name] < in_dict[name]:
                canAdd = False

        #print("Can Add", canAdd)
        if not canAdd:
            return False

        for name in in_dict.keys():
            self.remove(name, in_dict[name])
        
        for name in out_dict.keys():
            self.add(name, out_dict[name])

        return True



                