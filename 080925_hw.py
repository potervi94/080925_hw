# -*- coding: utf-8 -*-
from typing import List, Optional

class Passenger:
    def __init__(self,  name, destination):
        self.name = name
        self.destination = destination


class Transport:
    def __init__(self, speed, initial_location: Optional[str] = None):
        self.speed = speed
        # Поточна локація (остання зупинка). None, доки не здійснили перший рух
        self.location: Optional[str] = initial_location

    def move(self, destination, distance):
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
        time_to_destination = distance / self.speed
        from_location = self.location if self.location is not None else "Unknown"
        print(f"From {from_location} to {destination} ({distance} km) at a speed of {self.speed} km/h.")
        print(f"Time taken: {time_to_destination:.2f} hours.")
        # Додатковий вивід у форматі год:хв
        total_minutes = int(round(time_to_destination * 60))
        hh = total_minutes // 60
        mm = total_minutes % 60
        print(f"Time taken (hh:mm): {hh:02d}:{mm:02d}")
        # Після прибуття оновлюємо поточну локацію
        self.location = destination


class Bus(Transport):
    def __init__(self, speed, passengers, capacity: int = 40, initial_location: Optional[str] = None):
        super().__init__(speed, initial_location)
        self.passengers: List[Passenger] = passengers if passengers else []
        self.capacity = capacity

    @property
    def available_capacity(self) -> int:
        # Доступні місця = загальна місткість мінус кількість пасажирів
        return self.capacity - len(self.passengers)

    def board_passenger(self, passenger: Passenger):
        if len(self.passengers) >= self.capacity:
            print("The bus is already full.")
            return
        self.passengers.append(passenger)
        print(f"Boarding {passenger.name} to {passenger.destination}.")

    def unboard_passenger(self, passenger: Passenger, destination: str):
        if passenger not in self.passengers:
            print(f"{passenger.name} is not on the bus.")
            return
        if destination != passenger.destination:
            print(f"Cannot unboard {passenger.name} from {passenger.destination}.")
            return

        self.passengers.remove(passenger)
        print(f"Unboarding {passenger.name} from {passenger.destination}.")
        if not self.passengers:
            print("The bus is now empty.")

    def move(self, destination, distance):
        super().move(destination, distance)
        print(f"Number of passengers: {len(self.passengers)}.")
        print(f"Current passengers: {', '.join([passenger.name for passenger in self.passengers])}.")
        # Показуємо доступні місця з урахуванням поточної кількості пасажирів
        print(f"Current capacity: {self.available_capacity}/{self.capacity} (available/total).")

        # for passenger in self.passengers:
        #    self.unboard_passenger(passenger, destination)
        #
        # спочатку формуємо список пасажирів для висадки,
        # щоб не змінювати self.passengers під час ітерації
        to_unboard = [p for p in self.passengers if p.destination == destination]
        for passenger in to_unboard:
            self.unboard_passenger(passenger, destination)
        print(f"Number of passengers: {len(self.passengers)}.")
        print(f"Current capacity: {self.available_capacity}/{self.capacity} (available/total).\n")

if __name__ == "__main__":
    # Ініціалізація порожнього автобуса зі швидкістю 120 км/год
    bus = Bus(speed=120, passengers=[], capacity=10)  # створення порожнього автобусу

    # Створення пасажирів (усі роблять посадку у Києві)
    p1 = Passenger("Андрій", "Одеса")  # створення пасажирів
    p2 = Passenger("Володимир", "Львів")
    p3 = Passenger("Антон", "Черкаси")

    # Посадка у Києві
    bus.board_passenger(p1)
    bus.board_passenger(p2)
    bus.board_passenger(p3)
    print("Усі зробили посадку у Києві.")
    bus.location = "Київ"
    # Очікування: у автобусі 3 пасажири — Андрій(Одеса), Володимир(Львів), Антон(Черкаси)

    # Рух до Черкаси — висадяться всі, хто їде до Одеса (Андрій)
    bus.move(destination="Черкаси", distance=190)
    # Очікування: у автобусі залишиться лише Андрій(Одеса), Володимир(Львів)

    # Рух до Одеса — висадиться Андрій
    bus.move(destination="Одеса", distance=446)
    # Додамо ще одного пасажира з призначенням "Львів"
    new_p = Passenger("Ірина", "Львів")
    bus.board_passenger(new_p)
    # Очікування: у автобусі Володимир(Львів), Ірина(Львів)

    # Рух до Львова — висадяться всі, хто їде до Львова (Володимир і Ірина)
    bus.move(destination="Львів", distance=800)
    # Очікування: автобус порожній
