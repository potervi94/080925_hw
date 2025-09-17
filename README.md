# 080925_hw.py

## Курс: AI+Python 
### Модуль 11. ООП 
#### Тема: ООП.
#### Частина 6
#####  Завдання 1 
    Створіть клас Passenger з атрибутами 
     name – ім’я 
     destination – місце, куди прямує 
#####  Завдання 2 
    Створіть клас Transport з атрибутами 
     speed – швидкість 
    Методи 
     move(destination, distance) – рухається до місця 
    призначення, виводить інформацію як довго їхали 
#####  Завдання 3 
    Створіть клас Bus з атрибутами 
     passengers – список пасажирів(об’єкти класу Passenger) 
     capacity – максимальна можлива кількість пасажирів 
    Методи 
     board_passenger(passenger) – якщо є місце, додає 
    пасажира 
     move(destination, distance) – висаджує всіх пасажирів, які 
    хочуть вийти в даному місці(виводить їхню загальну 
    кількість) та викликає батьківський метод move()

# Консоль
    .\080925_hw.py 
    Boarding Андрій to Одеса.
    Boarding Володимир to Львів.
    Boarding Антон to Черкаси.
    Усі зробили посадку у Києві.
    From Київ to Черкаси (190 km) at a speed of 120 km/h.
    Time taken: 1.58 hours.
    Time taken (hh:mm): 01:35
    Number of passengers: 3.
    Current passengers: Андрій, Володимир, Антон.
    Current capacity: 7/10 (available/total).
    Unboarding Антон from Черкаси.
    Number of passengers: 2.
    Current capacity: 8/10 (available/total).
    
    From Черкаси to Одеса (446 km) at a speed of 120 km/h.
    Time taken: 3.72 hours.
    Time taken (hh:mm): 03:43
    Number of passengers: 2.
    Current passengers: Андрій, Володимир.
    Current capacity: 8/10 (available/total).
    Unboarding Андрій from Одеса.
    Number of passengers: 1.
    Current capacity: 9/10 (available/total).
    
    Boarding Ірина to Львів.
    From Одеса to Львів (800 km) at a speed of 120 km/h.
    Time taken: 6.67 hours.
    Time taken (hh:mm): 06:40
    Number of passengers: 2.
    Current passengers: Володимир, Ірина.
    Current capacity: 8/10 (available/total).
    Unboarding Володимир from Львів.
    Unboarding Ірина from Львів.
    The bus is now empty.
    Number of passengers: 0.
    Current capacity: 10/10 (available/total).
    
    
    Process finished with exit code 0

