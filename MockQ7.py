class Airplane:
    def __init__(self, initX, initY, cons, init_fuel):
        self.initX = initX
        self.initY = initY
        self.cons = cons
        self.init_fuel = init_fuel
        self.position = [self.initX, self.initY]
        self.fuel_level = self.init_fuel

    def goto(self, X, Y):
        distance = ((X - self.initX)**2 + (Y - self.initY)**2)**0.5
        fuel_use = self.cons * distance
        if self.init_fuel >= fuel_use:
            self.init_fuel -= fuel_use
            self.position = [X, Y]
            self.fuel_level -= fuel_use
            return True
        else:
            return False

    def refuel(self, fuel_added):
        self.fuel_level += fuel_added