# Genetik Algoritma ile Kromozom Optimizasyonu

Bu proje, genetik algoritma kullanarak belirli bir hedef kromozomun elde edilmesini amaçlayan bir Python uygulamasını içerir. Genetik algoritma, popülasyonları, mutasyonları ve çaprazlamaları kullanarak kromozomları geliştirir ve en uygun kromozomları seçer.


![Genetic Algorithms Schema](https://miro.medium.com/v2/resize:fit:964/1*HP8JVxlJtOv14rGLJfXEzA.png)

## Nasıl Kullanılır

1. Python yüklü olduğundan emin olun.
2. Kodu bu depodan indirin veya kopyalayın.
3. `main.py` dosyasını çalıştırın.

## Kodun İçeriği

Proje, aşağıdaki bölümlerden oluşur:

- `Chromosome`: Kromozom sınıfı, rastgele genler oluşturur ve uygunluk puanını hesaplar.
- `Population`: Popülasyon sınıfı, kromozomlar arasında popülasyonu yönetir.
- `GeneticAlgorithm`: Genetik algoritma işlemlerini yönetir.

## Parametreler

Bu projede bazı önemli parametreler bulunur:

- `POPULATION_SIZE`: Popülasyonun boyutu.
- `NUMB_OF_ELITE_CHROMOSOMES`: Her nesilde korunacak elit kromozomların sayısı.
- `TOURNAMENT_SELECTION_SIZE`: Turnuva seçiminde yer alacak kromozom sayısı.
- `TARGET_CHROMOSOME`: Hedef kromozom.
- `MUTATION_RATE`: Her bir kromozomdaki gen mutasyon olasılığı.
- `Population Class`: Kromozom populasyonunu yönetir,Rastgele kromozomlarla başlatılır.
- `GeneticAlgorithm`: Ana GA işlemlerini içerir.
- `evolve(pop)`:Popülasyonu önce çaprazlama ve sonra mutasyon uygulayarak evrimleştirir.
- `_crossover_population(pop)`:Seçilen kromozomlar üzerinde çaprazlama yaparak yeni bir populasyon oluşturur.
- `_mutate_population(pop)`:Mutasyon oranına dayalı olarak populasyondaki genleri mutasyona uğratır.
- `_crossover_chromosomes(chromosomes1, chromosomes2)`:İki kromozom arasında çaprazlama yapar.
- `_mutate_chromosome(chromosome)`:Mutasyon oranına dayalı olarak bir kromozomdaki genleri mutasyona uğratır.
- `_select_tournament_population(pop)`:Turnuva seçimi için populasyonun bir alt kümesini seçer ve bu alt kümeden en iyi kromozomu döndürür.
- `print_the_population(pop, gen_number)`:Popülasyon bilgilerini, nesil numarasını ve kromozom fitness'ini yazdırır.

## Katkı

Projeye katkıda bulunmak ve soru sormak isterseniz bana ulasabilirsiniz



---

Bu README dosyası, bu projenin amacını ve kullanımını anlamak için oluşturulmuştur. İyi çalışmalar!
