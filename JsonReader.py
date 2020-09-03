import json

class JsonReader:
    
    

    def __init__(self, path):
        self.path = path
        self.counter = 0
    
    def selectAll(self):
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                print("Nombre: "+ regs['nombre'])
                print("Edad: "+ str(regs['edad']))
                print("Activo: "+ str(regs['activo']))
                print("Promedio: "+ str(regs['promedio']))
    
    def selectSome(self, valstoselect):
        if "," not in valstoselect:
            value = [valstoselect]
        else:
            value = valstoselect.split(',')
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                print("-------------------------------------------------------------")
                print("-------------------------------------------------------------")
                for each in value:
                    print(each.capitalize()+": " + str(regs[each]))

    def selectAllCondition(self, condition):
        splitcond = condition.split('=')
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                if str(regs[splitcond[0]]) == splitcond[1].replace("\"",""):
                    print("-------------------------------------------------------------")
                    print("-------------------------------------------------------------")
                    print("Nombre: "+ regs['nombre'])
                    print("Edad: "+ str(regs['edad']))
                    print("Activo: "+ str(regs['activo']))
                    print("Promedio: "+ str(regs['promedio']))


    def selectSomeCondition(self, valstoselect, condition):
        splitcond = condition.split('=')
        if "," not in valstoselect:
            value = [valstoselect]
        else:
            value = valstoselect.split(',')
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                if str(regs[splitcond[0]]) == splitcond[1].replace("\"",""):
                    print("-------------------------------------------------------------")
                    print("-------------------------------------------------------------")
                    for each in value:
                        print(each.capitalize()+": " + str(regs[each]))

    def getValues(self, attribute):
        values = []
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                values.append(regs[attribute])
        return values

    def countRegs(self):
        i = 0
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                i += 1
        return i

    def getAllValues(self,howmany):
        values = []
        with open(self.path) as json_file:
            data = json.load(json_file)
            for regs in data:
                if self.counter < int(howmany):
                    auxarray = []
                    auxarray.append(regs['nombre'])
                    auxarray.append(regs['edad'])
                    auxarray.append(regs['activo'])
                    auxarray.append(regs['promedio'])
                    values.append(auxarray)
                    self.counter += 1
        return values

    def resetCounter(self):
        self.counter = 0

    def getCounter(self):
        return self.counter

    def setCounter(self,counter):
        self.counter = counter

