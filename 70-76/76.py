import matplotlib.pyplot as plt
numeros_base = [1, 2, 3, 4, 5]
valores_objetivo = [2, 4, 1, 8, 7]
plt.plot(numeros_base, valores_objetivo, marker="o", linestyle="-")
plt.title("Relación entre Números y Valores")
plt.xlabel("Números base")
plt.ylabel("Valores objetivo")
plt.savefig("grafica.png")
plt.show()
