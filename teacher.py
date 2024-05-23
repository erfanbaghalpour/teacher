import secrets

class Character:
    
    def __init__(self, first_name, last_name, id = secrets.token_urlsafe(16), **kwargs):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name

        for key, value in kwargs.items():
            setattr(self, key, value)


class Teacher(Character):
    hour = 0
    payPerOneHour = 0

    def __init__(self, first_name, last_name):
        super().__init__(first_name, last_name)


    def get_hour(self):
        return self.hour

    def set_hour(self, value):
        self.hour = value
    
    def get_payPerOneHour(self):
        return self.payPerOneHour
    
    def set_payPerOneHour(self, value):
        if value > 0:
            self.payPerOneHour = value
        else:
            self.payPerOneHour = 0
    
    def payment(self):
        return self.hour * self.payPerOneHour
    
    def __str__(self):
        return "{}, {}, {}, {}, {}".format(self.id, self.first_name, self.last_name, self.hour, self.payPerOneHour)

    def __repr__(self):
        return "mr.{} object".format(self.last_name)