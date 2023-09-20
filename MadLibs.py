class MadLibsGenerator:
    def __init__(self, template):
        self.template = template

    def Generate(self, words):
        madlibs = self.template.format(*words)
        return madlibs

    def Save(self, filename):
        with open(filename, 'a') as file:
            file.write(f"{self.__class__.__name__},{self.template}\n")

    @staticmethod
    def Load(filename):
        generators = []
        with open(filename, 'r') as file:
            lines = file.readlines()
            for line in lines:
                generator_data = line.strip().split(',')
                generator_type = generator_data[0]
                template = generator_data[1]
                if generator_type == "MadLibsGenerator":
                    generator = MadLibsGenerator(template)
                else:
                    raise ValueError("Invalid generator type")
                generators.append(generator)
        return generators


generators = [MadLibsGenerator("I am keen on {0} and {1}"), MadLibsGenerator("I was used to {0}")]

for generator in generators:
    generator.Save("generators.txt")

loaded_generators = MadLibsGenerator.Load("generators.txt")

words = ["driving", "sleeping"]
for generator in loaded_generators:
    madlibs = generator.Generate(words)
    print(madlibs)