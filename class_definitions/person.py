"""
*Person and Address classes provided by instructor*
Updated by Daniel Meeker to include a str and repr function.
"""


class Person:
    """Person class"""
    def __init__(self, lname, fname, addy=''):
        name_characters = set("ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'-")
        if not (name_characters.issuperset(lname) and name_characters.issuperset(fname)):
            raise ValueError
        self.last_name = lname
        self.first_name = fname
        self.address = addy

    def display(self):
        return (str(self.last_name) + ", " + str(self.first_name)
                + '\n' + self.address.display())

    def __str__(self):
        return str(self.last_name) + ", " + str(self.first_name)

    def __repr__(self):
        if self.address == '':
            return "{self.__class__.__name__}('{self.last_name}', '{self.first_name}')".format(self=self)
        else:
            return "{self.__class__.__name__}('{self.last_name}', '{self.first_name}', '{self.address}')".format(self=self)


class Address:
    """Address class for US addresses"""
    def __init__(self, st_number, st_name, st_type, city, state, zip, apt_num=''):
        self.street_number = st_number
        self.street_name = st_name
        self.street_type = st_type
        self.apartment_number = apt_num
        self.city = city
        self.state = state
        self.zip_code = zip

    def display(self):
        return(self.street_number + ' ' + self.street_name + ' ' + self.street_type + ' ' + self.apartment_number
               + '\n' + self.city + ', ' + self.state + ' ' + self.zip_code)


if __name__ == '__main__':
    addy1 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111')
    person1 = Person('Hammer', 'Martin', addy1)
    print(person1.display())
    addy2 = Address('123', 'Main', 'Street', 'Small Town', 'Iowa', '11111', '16B')
    person2 = Person('Hammer', 'Martin', addy2)
    print(person2.display())
    del(addy1, addy2)
    del(person1, person2)
