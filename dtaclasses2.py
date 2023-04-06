from dataclasses import dataclass, field
import uuid

@dataclass(order=True, frozen=True)
class Person:

    name :  str
    address : str
    active : bool
    email_address_list: list[str] = field(default_factory=list)
    id : str = field(init=False, default_factory=uuid.uuid4)
    search_string : str = field(init=False, repr=False)

    def __post_init__(self):
        s_string=f'{self.name} {self.address}'
        object.__setattr__(self, 'search_string', s_string )

    
p1=Person('shubham','khadakpada', True)

print(p1)