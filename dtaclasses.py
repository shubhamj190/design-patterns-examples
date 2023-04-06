from dataclasses import dataclass, field

@dataclass(order=True,frozen=True)
class Person:
    
    name : str
    email : str
    age : int
    sort_index : int = field(init=False,repr=False)
    strength : int = 100

    def __post_init__(self):
        # self.sort_index=self.age

    # TODO : when we are freezing the data class the dynamic values cannot be set directly so we can use set attribute dunder method for the same
        object.__setattr__(self, 'sort_index', self.age)
                                #   value to set  # which value to set

    # def __repr__(self):
    #     return f'the name is {self.name} it\'s email is {self.email} and it\'s age is {self.age} years'
    


p1=Person('shubham','shubham.jadhav@ufaber.com',26)
p2=Person('shubham','shubham.jadhav@ufaber.com',27)

print(p1)
print(p1<p2)
