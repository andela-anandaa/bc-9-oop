
map_ = {
    'KE': 'Kenya',
    'NG': 'Nigeria',
    'UG': 'Uganda',
    'TZ': 'Tanzania'
}

class Student(object): #inheritance
    
    def __init__(self, fname, lname, cc='KE'):
        # generate sequential unique ID
        self.__id = id # fake private
        self.fname = fname
        self.lname = lname
        self.country = map_[cc]

    def atttend_class(self, **kwargs):
        '''
        default values:
            loc = 'Hogwarts'
            date = current_date
            teacher = 'Alex'
        '''
        pass






















