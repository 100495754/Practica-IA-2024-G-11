import numpy as np
import matplotlib.pyplot as plt

# Define the membership functions
def young(age):
    if age <= 30:
        return 1
    elif 30 < age <= 40:
        return (40 - age) / 10
    else:
        return 0

def adult(age):
    if 20 < age <= 40:
        return (age - 20) / 20
    elif 40 < age <= 60:
        return (60 - age) / 20
    else:
        return 0

def elder(age):
    if age < 40:
        return 0
    elif 40 <= age <= 60:
        return (age - 40) / 20
    else:
        return 1

# Test the membership functions and plot them
ages = np.arange(0, 101, 1)
young_values = np.array([young(age) for age in ages])
adult_values = np.array([adult(age) for age in ages])
elder_values = np.array([elder(age) for age in ages])

# Plotting the membership functions
plt.figure(figsize=(10, 4))
plt.plot(ages, young_values, label='Young', color='blue')
plt.plot(ages, adult_values, label='Adult', color='green')
plt.plot(ages, elder_values, label='Elder', color='red')
plt.title('Fuzzy Membership Functions for Age')
plt.xlabel('Age')
plt.ylabel('Membership grade')
plt.legend()
plt.grid(True)
plt.show()






