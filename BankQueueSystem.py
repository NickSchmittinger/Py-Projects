
import simpy
import random

RANDOM_SEED = 24
NEW_CUSTOMERS = 25
CUSTOMER_INTERVAL = 10.0
MIN_PATIENCE = 1
MAX_PATIENCE = 3


def source(env, num, interval, counter):
    for i in range(num):
        c = customer(env, f'Customer{i:02d}', counter, time_in_bank=12.0)
        env.process(c)
        t = random.expovariate(1.0 / interval)
        yield env.timeout(t)


def customer(env, name, counter, time_in_bank):
    arrive = env.now
    print(f'{arrive:7.4f} {name}: Has Arrived')

    with counter.request()as req:
        patience = random.uniform(MIN_PATIENCE,MAX_PATIENCE)
        results = yield req | env.timeout(patience)
        wait = env.now - arrive
        if req in results:
            print(f'{env.now:7.4f} {name}: Finished.')
            tib = random.expovariate(1.0 / time_in_bank)
            yield env.timeout(tib)
            print(f'{env.now:7.4f} {name}: RENEGED after {wait:6.3f}')
        else:
            print(f'{env.now:7.4f} {name}: RENEGED after {wait:6.3f}')

print('Bank Renege')
random.seed(RANDOM_SEED)
env = simpy.Environment()

counter = simpy.Resource(env, capacity=1)
env.process(source(env, NEW_CUSTOMERS, CUSTOMER_INTERVAL, counter))
env.run()