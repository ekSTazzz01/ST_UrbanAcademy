import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0

    def __init__(self, speed):
        self.speed = speed
        self._cords = [0, 0, 0]


    def move(self, dx, dy, dz):
        x_cord = self._cords[0] + dx * self.speed
        y_cord = self._cords[1] + dy * self.speed
        z_cord = self._cords[2] + dz * self.speed
        if z_cord < 0:
            print("It's too deep, i can't dive :(")
        else:
            self._cords = [x_cord, y_cord, z_cord]


    def get_cords(self):
        print(f"X: {self._cords[0]}, Y: {self._cords[1]}, Z: {self._cords[2]}")


    def attack(self,):
        if self._DEGREE_OF_DANGER < 5:
          print("Sorry, i'm peaceful :)")
        else:
            print("Be careful, i'm attacking you 0_0")


class Bird(Animal):
    beak = True

    def lay_eggs(self):
        print(f"Here are(is) {random.randint (1, 4)} eggs for you")


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def dive_in(self, dz):
        z_cord = self._cords[2] - abs(dz) * self.speed / 2
        self._cords[2] = int(z_cord)


class PoisonousAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonousAnimal, Bird, AquaticAnimal):
    sound = "Click-click-click"


    def __init__(self, speed):
        super().__init__(speed)


    def speak(self):
       print(f'{self.sound}')




db = Duckbill(10)
print(Duckbill.mro())
print(db.live)
print(db.beak)

db.speak()
db.attack()

db.move(1, 2, 3)
db.get_cords()
db.dive_in(6)
db.get_cords()

db.lay_eggs()