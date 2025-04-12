import matplotlib.pyplot as plt
def Lorentz_attractor(x, y, z, time):
    sigma = 10  # σ
    lambdA = 28 # λ
    beta = 8/3  # b

    dx = sigma * (y - x)
    dy = x * (lambdA - z) - y
    dz = x * y - beta * z

    x_new = x + dx * time
    y_new = y + dy * time
    z_new = z + dz * time

    return x_new, y_new, z_new

def print_figure(res_x,res_y,res_z):
    filename=input("Введіть назву файлу для збереження графіка (.png): ")

    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(res_x, res_y, res_z, lw=1, color='orange')
    ax.set_title("Аттрактор Лоренца", fontsize=20)
    ax.set_xlabel("X")
    ax.set_ylabel("Y")
    ax.set_zlabel("Z")
    plt.savefig(filename, dpi=500)
    plt.show()

def data_input():
    x = float(input("Введіть значення для початкової кординати Х: "))
    y = float(input("Введіть значення для початкової кординати Y: "))
    z = float(input("Введіть значення для початкової кординати Z: "))
    dt = 0.01

    res_x = []
    res_y = []
    res_z = []

    for i in range(10000):
      x, y, z = Lorentz_attractor(x, y, z, dt)
      res_x.append(x)
      res_y.append(y)
      res_z.append(z)
    print_figure(res_x,res_y,res_z)


if __name__ == '__main__':
    data_input()

