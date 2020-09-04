# Write classes for the following class hierarchy:
#
#  [Vehicle]->[FlightVehicle]->[Starship]
#      |                |
#      v                v
# [GroundVehicle]      [Airplane]
#   |       |
#   v       v
# [Car]  [Motorcycle]
#
# Each class can simply "pass" for its body. The exercise is about setting up
# the hierarchy.
#
# e.g.
#
# class Whatever:
#     pass
#
# Put a comment noting which class is the base class

# Base class
class Vehicle:
    def __init__(self):
        self = self

# Base class: Vehicle
class FlightVehicle(Vehicle):
    def __init__(self):
        self = self

# Base class: FlightVehicle
class Starship(FlightVehicle):
    def __init__(self):
        self = self

# Base class: FlightVehicle
class Airplane(FlightVehicle):
    def __init__(self):
        self = self

# Base class: Vehicle
class GroundVehicle(Vehicle):
    def __init__(self):
        self = self

# Base class: GroundVehicle
class Car(GroundVehicle):
    def __init__(self):
        self = self

# Base class: GroundVehicle
class Motorcycle(GroundVehicle):
    def __init__(self):
        self = self