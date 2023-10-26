import random

POPULATION_SIZE = 8
NUMB_OF_ELITE_CHROSOMOSOMES = 1
TOURNAMENT_SELECTION_SIZE = 4
TARGET_CHROMOSOME = [1, 1, 0, 1, 0, 0, 0, 1, 1, 0] #target chrosome degistirebilir her sefernde farkli degerler alinniyor
MUTATION_RATE = 0.25 #mutasyon orani %25 yeterli

class Chromosome: #genel fonksiyonlar init olarak cunku birden fazla kez farkli yerlerde kullaniyoruz
    def __init__(self):
        self.genes = []
        self.fitness = 0
        for i in range(len(TARGET_CHROMOSOME)):
            if random.random() >= 0.5: #generate the random gene here
                self.genes.append(1)
            else:
                self.genes.append(0)

    def get_genes(self):
        return self.genes

    def get_fitness(self): #fitnes degerlerini hesapla eger gendek random gendeki[i] target gendeki [i] ile eslesiyosa fitnessi 1 artir
        self.fitness = 0
        for i in range(len(self.genes)):
            if self.genes[i] == TARGET_CHROMOSOME[i]:
                self.fitness += 1
        return self.fitness

    def __str__(self):
        return str(self.genes)

class Population:
    def __init__(self, size): #populasyonu tuttugumuz yer
        self.chromosomes = []
        for _ in range(size):
            self.chromosomes.append(Chromosome())

    def get_chromosomes(self):
        return self.chromosomes

class GeneticAlgorithm: #burada farkli genetik algoritmalar kullanilabilir.saglikli varsayilan genlerden yeni genkler evolve(mutasyon veya evrim) ediliyor.

    @staticmethod
    def evolve(pop):
        return GeneticAlgorithm._mutate_population(GeneticAlgorithm._crossover_population(pop))

    @staticmethod
    def _crossover_population(pop):
        crossover_pop = Population(0)
        for i in range(NUMB_OF_ELITE_CHROSOMOSOMES):
            crossover_pop.get_chromosomes().append(pop.get_chromosomes()[i])
        i = NUMB_OF_ELITE_CHROSOMOSOMES
        while i < POPULATION_SIZE:
            chromosome1 = GeneticAlgorithm._select_tournament_population(pop).get_chromosomes()[0]
            chromosome2 = GeneticAlgorithm._select_tournament_population(pop).get_chromosomes()[0]
            crossover_pop.get_chromosomes().append(GeneticAlgorithm._crossover_chromosomes(chromosome1,chromosome2))
            i+=1

        return crossover_pop

    @staticmethod
    def _mutate_population(pop):
        for i in range(NUMB_OF_ELITE_CHROSOMOSOMES,POPULATION_SIZE):
            GeneticAlgorithm._mutate_chromosome(pop.get_chromosomes()[i])
        return pop

    @staticmethod
    def _crossover_chromosomes(chromosomes1,chromosomes2):
        crossover_chrom = Chromosome()
        for i in range(TARGET_CHROMOSOME.__len__()):
            if random.random() >= 0.5:
                crossover_chrom.get_genes()[i] = chromosomes1.get_genes()[i]

            else:
                crossover_chrom.get_genes()[i] = chromosomes2.get_genes()[i]
        return  crossover_chrom

    @staticmethod
    def _mutate_chromosome(chromosome):
        for i in range(TARGET_CHROMOSOME.__len__()):
            if random.random() <MUTATION_RATE:
                if random.random() < 0.5:
                    chromosome.get_genes()[i] = 1
                else:
                    chromosome.get_genes()[i] = 0

    @staticmethod
    def _select_tournament_population(pop):
        tournament_pop = Population(0)
        i = 0
        while i < TOURNAMENT_SELECTION_SIZE:
            tournament_pop.get_chromosomes().append(pop.get_chromosomes()[random.randrange(0, POPULATION_SIZE)])
            i += 1
        tournament_pop.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
        return tournament_pop



    @staticmethod
    def print_the_population(pop, gen_number): #console information
        print("\n------------------------------------------")
        print("Generation #", gen_number, "| Fittest chromosome fitness:", pop.get_chromosomes()[0].get_fitness())
        print("Target Chromosome:", TARGET_CHROMOSOME)
        print("----------------------------------------------")
        i = 0
        for x in pop.get_chromosomes():
            print("Chromosome #", i, ":", x, "| Fitness:", x.get_fitness())
            i += 1

# Create a Population
population = Population(POPULATION_SIZE)
population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
GeneticAlgorithm.print_the_population(population, 0)

generation_number = 1 # uretilen veya evolve edilen generation sayisi artrmak icin deger

while population.get_chromosomes()[0].get_fitness() < len(TARGET_CHROMOSOME): #burada fitnes deger max olana kadar dongu devam edyor  while evolved gene fitness == target gene
    population = GeneticAlgorithm.evolve(population)
    population.get_chromosomes().sort(key=lambda x: x.get_fitness(), reverse=True)
    fittest_chromosome = population.get_chromosomes()[0]
    GeneticAlgorithm.print_the_population(population,generation_number)
    generation_number += 1