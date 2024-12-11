import simpy
from entities import Theater, Movie, Customer
from simulation import run_simulation

def main():
    env = simpy.Environment()

    theater_1 = Theater('Theater 1', 50, env)
    theater_2 = Theater('Theater 2', 30, env)

    movie_1 = Movie('Richard and Mortimer', 120, 'Sci-Fi', start_time=5)
    movie_2 = Movie('Sword Birth', 90, "Action", start_time=10)

    theater_1.add_movie(movie_1)
    theater_2.add_movie(movie_2)

    customers = [Customer(i, env) for i in range(1, 101)]

    env.process(run_simulation(env, [theater_1, theater_2], customers, duration=180))
    env.run(until=180)

if __name__ == '__main__':
    main()