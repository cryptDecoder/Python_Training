class GlobalValues:
    name = "Pruthviraj"
    def getName(self):
      global name
    name *= 2
    print(name)

g = GlobalValues()
g.getName()
