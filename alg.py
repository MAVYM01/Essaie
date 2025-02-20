import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# Fonction pour calculer les courants dans le circuit RLC en parallèle avec des tenseurs
def rlc_parallel_simulation_tensors(R, L, C, V0=10):
    """
    Simulation d'un circuit RLC parallèle avec des tenseurs.
    R : Résistance en Ohms
    L : Inductance en Henry
    C : Capacité en Farad
    V0 : Tension d'entrée en Volts
    """
    # Temps (vecteur tenseur)
    t = np.linspace(0, 0.05, 500)  # 50 ms max

    # Tenseur de la tension (constante dans le cas idéal)
    V = np.full_like(t, V0)

    # Calcul des courants comme tenseurs
    I_R = V / R  # Courant dans la résistance (Ohm's law)
    I_L = V / L * np.exp(-t / (L / R))  # Courant dans l'inductance (exponentiel décroissant)
    I_C = C * np.gradient(V, t)  # Courant dans le condensateur (proportionnel à dV/dt)

    # Création d'un tenseur global pour tous les courants
    I_total = np.stack([I_R, I_L, I_C], axis=0)  # Tenseur de forme (3, len(t))

    return t, I_total

# Paramètres initiaux
R = 10  # Résistance constante en Ohms
L_init = 0.01  # Inductance initiale en Henry
C = 0.001  # Capacité en Farads

# Initialisation des données avec des tenseurs
t, I_total = rlc_parallel_simulation_tensors(R, L_init, C)

# Extraction des composantes du tenseur
I_R = I_total[0]
I_L = I_total[1]
I_C = I_total[2]
I_total_sum = I_R + I_L + I_C  # Somme totale des courants

# Création de la figure et des axes
fig, ax = plt.subplots()
plt.subplots_adjust(bottom=0.3)

# Tracés initiaux
line_R, = ax.plot(t, I_R, label="I_R (Résistance)", color="red")
line_L, = ax.plot(t, I_L, label="I_L (Inductance)", color="blue")
line_C, = ax.plot(t, I_C, label="I_C (Condensateur)", color="green")
line_total, = ax.plot(t, I_total_sum, label="I_total (Total)", color="black", linestyle="--")

# Configuration des axes
ax.set_xlabel("Temps (s)")
ax.set_ylabel("Courant (A)")
ax.set_title("Simulation d'un Circuit RLC en parallèle (Ajustement de L)")
ax.legend()

# Slider pour ajuster l'inductance
axcolor = 'lightgoldenrodyellow'
ax_L = plt.axes([0.25, 0.1, 0.65, 0.03], facecolor=axcolor)
L_slider = Slider(ax_L, 'Inductance (H)', 0.001, 0.1, valinit=L_init)

# Fonction pour mettre à jour les tracés
def update(val):
    L = L_slider.val
    t, I_total = rlc_parallel_simulation_tensors(R, L, C)

    # Mise à jour des composantes du tenseur
    I_R = I_total[0]
    I_L = I_total[1]
    I_C = I_total[2]
    I_total_sum = I_R + I_L + I_C

    # Mise à jour des courbes
    line_R.set_ydata(I_R)
    line_L.set_ydata(I_L)
    line_C.set_ydata(I_C)
    line_total.set_ydata(I_total_sum)

    # Redessiner le graphique
    fig.canvas.draw_idle()

# Lier le slider à la fonction de mise à jour
L_slider.on_changed(update)

# Afficher le graphique
plt.show()
