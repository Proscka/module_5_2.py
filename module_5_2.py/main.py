class House:
    def __init__(self,name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors
    def go_to(self,new_floor):
        if 1<= new_floor <= self.number_of_floors:
            for floor in range (1,new_floor +1):
                print(floor)
            else:
                print("Такого этажа не существует")

    def __str__(self):
        return f"{self. name}"
    def __len__(self):
        return self.number_of_floors



h1=House("ЖК Эльбрус",10)
h2=House("ЖК Акация",20)
print("Название: ЖК Эльбрус, кол-во этажей:10")
print("Название: ЖК Акация, кол-во этажей: 20")

print(len(h1))
print(len(h2))