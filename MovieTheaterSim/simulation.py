import simpy
from entities import Theater, Movie, Customer

def run_simulation(environment, theaters, customers, duration):
    while True:
        for theater in theaters:
            for movie in theater.showings:
                if environment.now == movie.start_time:
                    print(f'Movie {movie.title} is starting at Theater {theater.name}!')
        for customer in customers:
            if not customer.has_ticket:
                selected_theater = theaters[0]
                selected_movie = selected_theater.showings[0]
                if not selected_theater.is_full():
                    customer.buy_ticket(selected_movie)
                    selected_theater.enter_theater()
                    print(f'Customer {customer.customer_id} bought a ticket for {selected_movie.title}.')
        yield environment.timeout(1)