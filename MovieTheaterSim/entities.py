import random


class Theater:
    def __init__(self, name, capacity, environment):
        self.name = name
        self.capacity = capacity
        self.environment = environment
        self.current_capacity = 0
        self.showings = []
    def add_movie(self, movie):
        self.showings.append(movie)
    def is_full(self, additional_tickets=1):
        return self.current_capacity + additional_tickets > self.capacity
    def enter_theater(self, tickets):
        if not self.is_full(tickets):
            self.current_capacity += 1
            return True
        return False
    def leave_theater(self, tickets):
        self.current_capacity = max(0, self.current_capacity - tickets)
"""     def rotate_movies(self, new_movies, current_time):
        self.showings = [
            movie for movie in self.showings if movie.get_end_time() > current_time
        ]
        self.showings.extend(new_movies) """

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
        self.tickets_purchased = 0

    def buy_ticket(self, theaters):
        available_theaters = [theater for theater in theaters if theater.showings]
        if not available_theaters:
            print(f"Customer {self.customer_id}: No theaters available with movies.")
            return None
        selected_theater = random.choice(available_theaters)
        selected_movie = random.choice(selected_theater.showings)
        tickets_to_buy = random.randint(1,6)

        if not selected_theater.is_full(tickets_to_buy):
            self.has_ticket = True
            self.tickets_purchased = tickets_to_buy
            selected_theater.enter_theater(tickets_to_buy)
            print(f"Customer {self.customer_id} bought {tickets_to_buy} tickets for '{selected_movie.title}' at {selected_theater.name}.")
            #selected_theater.current_capacity += self.tickets_purchased
            selected_theater.enter_theater(self.tickets_purchased)
            return selected_movie
        else:
            print(f"Customer {self.customer_id}: '{selected_movie.title}' at {selected_theater.name} "
                  f"is full (Requested: {tickets_to_buy}, Available: {selected_theater.capacity - selected_theater.current_capacity}).")
        return None

    def buy_snacks(self):
        self.has_snacks = True