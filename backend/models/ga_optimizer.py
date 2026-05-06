import random

population_size = 10
mutation_rate = 0.1

population = [random.randint(1, 100) for _ in range(population_size)]


def fitness(x):
    return -(x - 50) ** 2


for generation in range(50):
    population = sorted(population, key=fitness, reverse=True)

    next_generation = population[:2]

    while len(next_generation) < population_size:
        parent1 = random.choice(population[:5])
        parent2 = random.choice(population[:5])

        child = (parent1 + parent2) // 2

        if random.random() < mutation_rate:
            child += random.randint(-5, 5)

        next_generation.append(child)

    population = next_generation

print('Optimized value:', population[0])