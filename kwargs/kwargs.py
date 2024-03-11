
list_of_obj = []

class Player:
    def __init__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            if key != 'class':
                setattr(self, key, val)
class Club:
    def __init__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            if key != 'class':
                setattr(self, key, val)

class League:
    def __init__(self, **kwargs) -> None:
        for key, val in kwargs.items():
            if key != 'class':
                setattr(self, key, val)

def create(**kwargs):
    obj = kwargs['class'](**kwargs)
    list_of_obj.append(obj)



db_list = [{"class": Player, "age": 19,"name": 'Othman Kasmi'},
           {"class": Player, "age": 25},
           {"class": League, "num_clubs": 16},
           {"class": Club, "num_player": 26},
           {"class": Player, "age": 34}]

for item in db_list:
    create(**item)

for obj in list_of_obj:
    print(f'class name: {obj.__class__.__name__}\n\t{obj.__dict__}')
