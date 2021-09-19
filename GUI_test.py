from game_assignmentv4_gui import Character
from game_assignmentv4_gui import *
import unittest

class TestCharacter(unittest.TestCase):
    def setUp(self):
        self.character = Character()

class TestInit(TestCharacter):
    def test_initial_attack(self):
        self.assertEqual(self.character.attack, 10)
    def test_initial_health(self):
        self.assertEqual(self.character.hp, 10)
    def test_initial_speed(self):
        self.assertEqual(self.character.speed, 10)
    def test_initial_money(self):
        self.assertEqual(self.character.money, 15)
    
class TestImprove(TestCharacter):
    def test_improve_attack(self):
        self.character.improve("attack")
        self.assertEqual(self.character.attack, 15)
    def test_improve_health(self):
        self.character.improve("health")
        self.assertEqual(self.character.hp, 15)    
    def test_improve_speed(self):
        self.character.improve("speed")
        self.assertEqual(self.character.speed, 15)
    def test_improve_multiple_times(self):
        for _ in range(3):
            self.character.improve("attack")
        self.assertEqual(self.character.money, 5)

