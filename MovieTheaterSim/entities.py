
class Theater:
    def __init__(self, name, capacity, environment):
        self.name = name
        self.capacity = capacity
        self.environment = environment
        self.current_capacity = 0
        self.showings = []
    def add_movie(self, movie):
        self.showings.append(movie)
    def is_full(self):
        return self.current_capacity >= self.capacity
    def enter_theater(self):
        if not self.is_full():
            self.current_capacity += 1
            return True
        return False
    def leave_theater(self):
        self.current_capacity = max(0, self.current_capacity - 1)

class Movie:
    def __init__(self, title, runtime, genre, start_time):
        self.title = title
        self.runtime = runtime
        self.genre = genre
        self.start_time = start_time
    def get_end_time(self):
        return self.start_time + self.runtime

class Customer:
    def __init__(self, customer_id, environment):
        self.customer_id = customer_id
        self.environment = environment
        self.has_ticket = False
        self.has_snacks = False
    def buy_ticket(self, movie):
        self.has_ticket = True
        return movie
    def buy_snacks(self):
        self.has_snacks = True