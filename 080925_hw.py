# -*- coding: utf-8 -*-
from typing import List

class Passenger:
    def __init__(self,  name, destination):
        self.name = name
        self.destination = destination


class Transport:
    def __init__(self, speed):
        self.speed = speed

    def move(self, destination, distance):
        if distance <= 0:
            raise ValueError("Distance must be a positive number.")
        time_to_destination = distance / self.speed
        print(f"From {destination} "
              f"to {destination} at a speed of {self.speed} km/h.")
        print(f"Time taken: {time_to_destination:.2f} hours.")


class Bus(Transport):
    def __init__(self, speed, passengers, capacity):
        super().__init__(speed)
        self.passengers: List[Passenger] = passengers if passengers else []
        self.capacity = capacity

    def board_passenger(self, passenger: Passenger):
        if len(self.passengers) >= self.capacity:
            print("The bus is already full.")
            return
        self.passengers.append(passenger)
        print(f"Boarding {passenger.name} to {passenger.destination}.")

    def move(self, destination, distance):
        super().move(destination, distance)
        print(f"Number of passengers: {len(self.passengers)}.")