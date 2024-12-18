import simpy
from entities import Theater, Movie, Customer

""" def run_simulation(environment, theaters, customers, duration):
    while environment.now < duration:
        for customer in customers:
            if not customer.has_ticket:
                movie = customer.buy_ticket(theaters)
                if movie:
                    print(f"Customer {customer.customer_id} bought {customer.tickets_purchased} "
                          f"tickets for '{movie.title}' at time {environment.now}.")
                else:
                    print(f"Customer {customer.customer_id} couldn't buy tickets at time {environment.now}.")
        yield environment.timeout(1) """

def run_simulation(environment, theaters, customers, duration):
    while environment.now < duration:
        for theater in theaters:
            for movie in theater.showings:
                if environment.now == movie.start_time:
                    print(f'Movie {movie.title} is starting at Theater {theater.name}!')
                if environment.now % movie.runtime == 0:
                    theater.leave_theater(theater.current_capacity)
        for customer in customers:
            print(f"{customer.customer_id}")
        yield environment.timeout(1)

"""             if not customer.has_ticket:
                customer.buy_ticket(theaters) """