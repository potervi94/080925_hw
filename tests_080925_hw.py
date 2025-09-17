# test_080925_hw.py
import io
import math
import unittest
from contextlib import redirect_stdout
import importlib.util
import pathlib
import sys

module_path = pathlib.Path(__file__).with_name("080925_hw.py")
spec = importlib.util.spec_from_file_location("hw_module", module_path)
hw_module = importlib.util.module_from_spec(spec)
sys.modules["hw_module"] = hw_module
spec.loader.exec_module(hw_module)

Passenger, Transport, Bus = hw_module.Passenger, hw_module.Transport, hw_module.Bus


class TestPassenger(unittest.TestCase):
    def test_passenger_attributes(self):
        p = Passenger(name="Ivan", destination="Kyiv")
        self.assertEqual(p.name, "Ivan")
        self.assertEqual(p.destination, "Kyiv")


class TestTransport(unittest.TestCase):
    def test_move_time_and_output(self):
        t = Transport(speed=60)
        buf = io.StringIO()
        with redirect_stdout(buf):
            t.move(destination="Lviv", distance=120)
        out = buf.getvalue()
        # Перевіряємо наявність рядка з часом
        self.assertIn("Time taken:", out)
        # Перевіряємо коректне обчислення часу
        # 120 / 60 = 2.00
        self.assertIn("2.00", out)
        # Додаткові перевірки нового функціоналу:
        # має бути початкова локація Unknown та відстань у першому рядку
        self.assertIn("From Unknown to Lviv (120 km) at a speed of 60 km/h.", out)
        # формат год:хв
        self.assertIn("Time taken (hh:mm): 02:00", out)

    def test_move_invalid_distance_raises(self):
        t = Transport(speed=50)
        with self.assertRaises(ValueError):
            t.move(destination="Odesa", distance=0)
        with self.assertRaises(ValueError):
            t.move(destination="Odesa", distance=-10)

    def test_move_with_initial_location_and_distance_and_hhmm(self):
        # Перевіряємо, що друкується коректна початкова локація та відстань
        t = Transport(speed=80, initial_location="Kyiv")
        buf = io.StringIO()
        with redirect_stdout(buf):
            t.move(destination="Lviv", distance=240)
        out = buf.getvalue()
        self.assertIn("From Kyiv to Lviv (240 km) at a speed of 80 km/h.", out)
        # 240 / 80 = 3.00 год
        self.assertIn("Time taken: 3.00 hours.", out)
        self.assertIn("Time taken (hh:mm): 03:00", out)


class TestBus(unittest.TestCase):
    def test_board_passenger_until_capacity(self):
        capacity = 3
        bus = Bus(speed=40, passengers=[], capacity=capacity)

        buf = io.StringIO()
        with redirect_stdout(buf):
            for i in range(capacity):
                bus.board_passenger(Passenger(name=f"P{i+1}", destination="Kyiv"))
            # Спроба посадити понад місткість
            bus.board_passenger(Passenger(name="Extra", destination="Kyiv"))

        self.assertEqual(len(bus.passengers), capacity)
        out = buf.getvalue()
        self.assertIn("The bus is already full.", out)

    def test_move_unboards_only_matching_destination(self):
        # Троє пасажирів, двоє хочуть вийти в 'Lviv', один в 'Kyiv'
        p1 = Passenger("A", "Lviv")
        p2 = Passenger("B", "Kyiv")
        p3 = Passenger("C", "Lviv")
        bus = Bus(speed=60, passengers=[p1, p2, p3], capacity=10)

        buf = io.StringIO()
        with redirect_stdout(buf):
            bus.move(destination="Lviv", distance=120)

        # Після висадки в 'Lviv' має залишитись лише той, хто їде до 'Kyiv'
        self.assertEqual(len(bus.passengers), 1)
        self.assertEqual(bus.passengers[0].name, "B")
        self.assertEqual(bus.passengers[0].destination, "Kyiv")

        out = buf.getvalue()
        # Перевіряємо, що було виведено час
        self.assertIn("Time taken:", out)
        # 120 / 60 = 2.00
        self.assertIn("2.00", out)

    def test_move_unboards_all_matching_destination_edge_case(self):
        # Усі троє мають однаковий destination — перевіряємо, що ВСІ будуть висаджені.
        # Цей тест допомагає виявити можливу проблему з видаленням елементів із списку під час ітерації.
        p1 = Passenger("P1", "Odesa")
        p2 = Passenger("P2", "Odesa")
        p3 = Passenger("P3", "Odesa")
        bus = Bus(speed=80, passengers=[p1, p2, p3], capacity=10)

        buf = io.StringIO()
        with redirect_stdout(buf):
            bus.move(destination="Odesa", distance=80)

        # Очікування за вимогою задачі: всі, хто має співпадаюче призначення, мають бути висаджені
        # Якщо у реалізації є проблема з видаленням під час ітерації, тут може залишитися 1 пасажир.
        self.assertEqual(
            len(bus.passengers),
            0,
            msg="Очікувалось, що всі пасажири будуть висаджені в 'Odesa'. "
                "Схоже, що при видаленні під час ітерації хтось залишився."
        )


if __name__ == "__main__":
    unittest.main()
