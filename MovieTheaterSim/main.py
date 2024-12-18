import simpy
import random
from entities import Theater, Movie, Customer
from simulation import run_simulation

def main():
    env = simpy.Environment()

    theater_1 = Theater('Theater 1', 50, env)
    theater_2 = Theater('Theater 2', 30, env)

    movie_1 = Movie('That Film', 60, 'Sci-fi', start_time=5)
    movie_2 = Movie('This Movie', 90, "Action", start_time=10)

    theater_1.add_movie(movie_1)
    theater_2.add_movie(movie_2)

    customers = [Customer(i, env) for i in range(1, 101)]

    env.process(run_simulation(env, [theater_1, theater_2], customers, duration=180))
    #env.process(dynamic_movie_update(env, [theater_1, theater_2]))
    env.run(until=180)

""" def dynamic_movie_update(environment, theaters):
    while True:
        for theater in theaters:
            new_movie = Movie(
                title=f"New Movie {environment.now}",
                runtime=random.randint(90, 150),
                genre=random.choice(["Drama", "Action", "Comedy", "Sci-fi"]),
                start_time=environment.now + random.randint(10, 20),
            )
            #theater.rotate_movies([new_movie], environment.now)
            theater.add_movie(new_movie)
            print(f"Added '{new_movie.title}' to {theater.name} at time {environment.now}.")
        yield environment.timeout(30) """

if __name__ == '__main__':
    main()