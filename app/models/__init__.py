from flask_login import UserMixin


class User(UserMixin):
    def __init__(self, obj):
        self.id = obj.id
        self.active = obj.active
        self.name = f"{obj.first_name} {obj.last_name}"
        self.email = obj.email
        self.msisdn = obj.msisdn
        self.group = obj.group
        self.roles = obj.group.roles
        self.prefs = {"DARK_MODE": 0}
        for x in obj.prefs:
            self.prefs[x.name] = x.value
        self.image = f"{obj.id}.jpg"

    def get_roles(self):
        return self.roles
