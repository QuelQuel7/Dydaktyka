import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import fsolve

def f(x):
    return x**2

def test(xa, length):
    d = -(length)**2 + xa**2 + xa**4
    c = -2*xa
    b = 1 - 2*xa**2 
    a = 1
    coeff = [a, 0, b, c, d]
    return coeff

# Tworzymy zakres wartości x, to możesz zmieniać, teoretycznie im większy zakres tym dokładniejszy wynik
X = np.linspace(-4, 4, 1028*8)

Y = X**2

length = 4

plt.plot(X, Y, label='f(x) = x^2')

midpointsX = []
midpointsY = []

for x in X:
    temp = test(x, length)
    roots = np.roots(temp)
    
    for root in roots:
        if np.isreal(root) and root <= x and root >= x - length:
            xb = root
            yb = f(xb)
            midpointsX.append((x + xb) / 2.)
            midpointsY.append((f(x) + yb) / 2.)

plt.scatter(midpointsX, midpointsY, color='red', marker='.', label='Środki odcinków')

# Dodajemy etykiety osi i tytuł
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Wykres funkcji f(x) = x^2 z odcinkami')

# Dodajemy legendę
plt.legend()

# Wyświetlamy wykres
plt.show()

#Na wszelki wypadek sortuje żeby m. trapezów działała
sorted_indices = np.argsort(midpointsX)
sorted_midpointsX = np.array(midpointsX)[sorted_indices]
sorted_midpointsY = np.array(midpointsY)[sorted_indices]

# Obliczanie całki przy użyciu metody trapezowej
integral = np.trapz(sorted_midpointsY, x=sorted_midpointsX)

#Teraz całka końcowa czyli różnica tego od f. kwadratowej
integralf =  1./3. * (sorted_midpointsX[-1]**3 - sorted_midpointsX[0]**3)

print("Wynik całki to: ", integral)
print("nalezy od tego odjąć: ", integralf)
print("Czyli wychodzi: ", integral - integralf)
