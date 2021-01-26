class Worker:

    def __init__(self, name, input_dict, output_dict):
        self.name = name
        self.input_dict = input_dict
        self.output_dict = output_dict

    def __repr__(self):
        return self.name

    def make(self, resources):
        resources.update_resources(self.input_dict, self.output_dict)
        #print(resources)
        return resources