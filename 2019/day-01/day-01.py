import math as m
import pandas as pd

df = pd.read_csv("input.csv", header=None, names=["mass"])

# Part 1
def get_fuel(mass):
    return(m.floor(mass/3)-2)
df["fuel_for_mass"] = df["mass"].apply(lambda x: get_fuel(x))
print("Part 1: ",df["fuel_for_mass"].sum())

# Part 2
def get_fuel_for_fuel(fuel):
    total_fuel = 0
    while True:
        fuel_for_fuel = get_fuel(fuel)
        if fuel_for_fuel > 0:
            total_fuel += fuel_for_fuel
            fuel = fuel_for_fuel
        else:
            break
    return total_fuel
df["fuel_for_fuel"] = df["fuel_for_mass"].apply(lambda x: get_fuel_for_fuel(x))
print("Part 2: ",df["fuel_for_mass"].sum()+df["fuel_for_fuel"].sum())