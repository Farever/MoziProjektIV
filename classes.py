class movie:
    def __init__(self, hall, chairs, title, date, genre, playtime):
        self.hall = hall
        self.chairs = chairs
        self.title = title
        self.date = date
        self.genre = genre
        self.playtime = playtime

class reservation:
    def __init__(self, id, orderId, last_name, first_name, hall, chair):
        self.id = id
        self.orderId = orderId
        self.lastName = last_name
        self.firstName = first_name
        self.hall = hall
        self.chair = chair