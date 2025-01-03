from __future__ import annotations

import random
import simpy

from typing import Dict, List, NamedTuple, Optional

RANDOM_SEED = 42
TICKETS = 50
SELLOUT_THRESHOLD = 2
SIM_TIME = 120

def moviegoer(env, movie, num_tickets, theater):
    with theater.counter.request() as my_turn:
        result = yield my_turn | theater.sold_out[movie]
        if my_turn not in result:
            theater.num_renegers[movie] += 1
            return
        if theater.available[movie] < num_tickets:
            yield env.timeout(0.5)
            return
        theater.available[movie] -= num_tickets
        if theater.available[movie] < SELLOUT_THRESHOLD:
            theater.sold_out[movie].succeed()
            theater.when_sold_out[movie] = env.now
            theater.available[movie] = 0
        yield env.timeout(1)

def customer_arrivals(env, theater):
    while True:
        yield env.timeout(random.expovariate(1 / 0.5))
        movie = random.choice(theater.movies)
        num_tickets = random.randint(1, 6)
        if theater.available[movie]:
            env.process(moviegoer(env, movie, num_tickets, theater))

class Theater(NamedTuple):
    counter: simpy.Resource
    movies: List[str]
    available: Dict[str, int]
    sold_out: Dict[str, simpy.Event]
    when_sold_out: Dict[str, Optional[float]]
    num_renegers: Dict[str, int]

print('Theater is open for business')
random.seed(RANDOM_SEED)
env = simpy.Environment()

movies = ['Python Goes Rogue', 'Mission Python', 'Python on a plane']
theater = Theater(counter=simpy.Resource(env, capacity=1),
                  movies=movies,
                  available={movie: TICKETS for movie in movies},
                  sold_out={movie: env.event() for movie in movies},
                  when_sold_out={movie: None for movie in movies},
                  num_renegers={movie: 0 for movie in movies},)

env.process(customer_arrivals(env, theater))
env.run(until=SIM_TIME)

for movie in movies:
    if theater.sold_out[movie]:
        sellout_time = theater.when_sold_out[movie]
        num_renegers = theater.num_renegers[movie]
        
        print(
            f'Movie "{movie}" sold out {sellout_time:.1f} minutes '
            f'after ticket counter opening.'
        )
        print(f' Number of people leaving queue when film sold out: {num_renegers}')