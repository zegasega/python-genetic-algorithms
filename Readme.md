# Genetic Algorithm for Chromosome Evolution

This Python script demonstrates a simple genetic algorithm (GA) that evolves a population of chromosomes to match a target chromosome defined by `TARGET_CHROMOSOME`.

![Genetic Algorithms Schema](https://miro.medium.com/v2/resize:fit:964/1*HP8JVxlJtOv14rGLJfXEzA.png)

# Genetic Algorithm for Chromosome Evolution

This Python script demonstrates a simple genetic algorithm (GA) that evolves a population of chromosomes to match a target chromosome defined by `TARGET_CHROMOSOME`.

## Initialization

- **Population Size (POPULATION_SIZE):** The size of the population.
- **Number of Elite Chromosomes (NUMB_OF_ELITE_CHROMOSOMES):** Number of elite chromosomes to retain in each generation.
- **Tournament Selection Size (TOURNAMENT_SELECTION_SIZE):** Number of chromosomes participating in tournament selection.
- **Target Chromosome (TARGET_CHROMOSOME):** The desired chromosome for evolution.
- **Mutation Rate (MUTATION_RATE):** Probability of gene mutation in each chromosome.

## Classes

### Chromosome Class

- Represents an individual chromosome in the population.
- Initializes a random chromosome with genes (0s and 1s).
- `get_genes()`: Returns the genes of the chromosome.
- `get_fitness()`: Calculates the fitness by counting matching genes with the target chromosome.
- `__str__()`: Returns the genes as a string.

### Population Class

- Manages a population of chromosomes.
- Initializes the population with random chromosomes.

### GeneticAlgorithm Class

- Contains main GA operations.
- `evolve(pop)`: Evolves the population through crossover and mutation.
- `_crossover_population(pop)`: Creates a new population through crossover on selected chromosomes.
- `_mutate_population(pop)`: Mutates genes based on the mutation rate.
- `_crossover_chromosomes(chromosomes1, chromosomes2)`: Performs crossover between two chromosomes.
- `_mutate_chromosome(chromosome)`: Mutates the genes in a chromosome.
- `_select_tournament_population(pop)`: Selects a subset of the population for tournament selection.
- `print_the_population(pop, gen_number)`: Prints population information.

## Usage

1. Clone the project.
2. Run `main.py` to start the genetic algorithm.

## Results

The algorithm iteratively evolves the population until the fittest chromosome matches the target chromosome.

## Note

This code provides a basic implementation of a genetic algorithm, and improvements can be made based on specific problem domains and goals.

## License

This project is licensed under the [License Name]. See the `LICENSE` file for more details.
