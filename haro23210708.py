"""
Práctica 4: Sistema Endocrino.

Departamento de Ingeniería Eléctrica y Electrónica, Ingeniería Biomédica
Tecnológico Nacional de México [TecNM - Tijuana]
Blvd. Alberto Limón Padilla s/n, C.P. 22454, Tijuana, B.C., México

Nombre del alumno: Haro Najar Angelica Ashia
Número de control: 23210697
Correo institucional: l23210708@tectijuana.edu.mx

Asignatura: Modelado de Sistemas Fisiológicos
Docente: Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy import signal

# =========================================================
# PARÁMETROS
# =========================================================
F0 = 1.0
alpha = 0.25
Cg = 10e-6
Cp = 100e-6
R_control = 100
R_caso = 10e3

# =========================================================
# TIEMPO
# =========================================================
t = np.arange(0, 10.001, 1e-3)

# =========================================================
# ENTRADA
# =========================================================
A = F0 / (1 + alpha)

u = np.zeros_like(t)
u[(t >= 1) & (t <= 2)] = A

# =========================================================
# MODELOS
# =========================================================
def rc_ce(u, t, tau):
    y = np.zeros_like(u)
    dt = t[1] - t[0]
    a = np.exp(-dt / tau)
    for k in range(1, len(t)):
        y[k] = a * y[k - 1] + (1 - a) * u[k - 1]
    return y

def rc_ft(u, t, tau):
    sys = signal.TransferFunction([1], [tau, 1])
    _, y, _ = signal.lsim(sys, U=u, T=t)
    return y

tau_control = R_control * Cp
tau_caso = R_caso * Cp

F_control_CE = rc_ce(u, t, tau_control)
F_control_FT = rc_ft(u, t, tau_control)

F_caso_CE = rc_ce(u, t, tau_caso)
F_caso_FT = rc_ft(u, t, tau_caso)

# =========================================================
# PID
# =========================================================
def pid_response(u, t, tau, Kp, Ki, Kd):
    num = [Kd, Kp, Ki]
    den = [tau + Kd, 1 + Kp, Ki]
    sys = signal.TransferFunction(num, den)
    _, y, _ = signal.lsim(sys, U=u, T=t)
    return y

PID_caso = pid_response(u, t, tau_caso, 45, 120, 0.02)

# =========================================================
# ESTILO
# =========================================================
plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'cm'

fig, axs = plt.subplots(2, 1, figsize=(7.2, 5), facecolor='white')

# =======================
# SUBGRÁFICA 1: CONTROL
# =======================
axs[0].plot(
    t, F_control_CE,
    '-', lw=2.2, color='#6A5ACD',
    label=r'$F(t):\mathrm{Control\ CE}$'
)

axs[0].plot(
    t, F_control_FT,
    '--', lw=2.4, color='#FF69B4',
    label=r'$F(t):\mathrm{Control\ FT}$'
)

axs[0].set_title('Control: Individuo Sano', fontweight='bold')
axs[0].set_xlim(0, 10)
axs[0].set_ylim(-0.2, 1.2)
axs[0].set_xticks(np.arange(0, 11, 1))
axs[0].set_yticks(np.arange(-0.2, 1.21, 0.2))
axs[0].set_ylabel(r'$F(t)\ [V]$')
axs[0].set_xlabel(r'$t\ [s]$')

axs[0].legend(
    loc='lower center',
    bbox_to_anchor=(0.5, 1.2),
    ncol=2,
    frameon=False
)

# =======================
# SUBGRÁFICA 2: CASO vs CONTROL
# SOLO 4 LÍNEAS
# =======================
axs[1].plot(
    t, F_control_FT,
    '--', lw=3.0, color='#FFD700',
    label=r'$F(t):\mathrm{Control\ FT}$',
    zorder=5
)

axs[1].plot(
    t, F_caso_CE,
    '-', lw=2.2, color='#FF6F91',
    label=r'$F(t):\mathrm{Caso\ CE}$'
)

axs[1].plot(
    t, F_caso_FT,
    '--', lw=2.2, color='#00A8E8',
    label=r'$F(t):\mathrm{Caso\ FT}$'
)

axs[1].plot(
    t, PID_caso,
    '-', lw=3.5, color='#2E0854',
    label=r'$PID(t):\mathrm{Caso}$'
)

axs[1].set_title('Caso vs Control', fontweight='bold')
axs[1].set_xlim(0, 10)
axs[1].set_ylim(-0.2, 1.2)
axs[1].set_xticks(np.arange(0, 11, 1))
axs[1].set_yticks(np.arange(-0.2, 1.21, 0.2))
axs[1].set_ylabel(r'$F(t)\ [V]$')
axs[1].set_xlabel(r'$t\ [s]$')

axs[1].legend(
    loc='lower center',
    bbox_to_anchor=(0.5, 1.2),
    ncol=4,
    frameon=False
)

# =======================
# FORMATO GENERAL
# =======================
for ax in axs:
    ax.tick_params(direction='in', top=True, right=True)
    for spine in ax.spines.values():
        spine.set_linewidth(1.1)
    ax.grid(False)

plt.subplots_adjust(left=0.12, right=0.97, top=0.88, bottom=0.12, hspace=0.95)
plt.savefig('Sistema_Musculoesqueletico_final.pdf', format='pdf', bbox_inches='tight')
plt.show()