"""
Práctica 3: Sistema Musculoesquelético

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


F0 = 1.0
t = np.arange(0, 10.001, 1e-3)

u = np.zeros_like(t)
u[t >= 1] = F0

R1_control = 1e3        
L_control = 100e-3      
R2_control = 100e3      
C_control = 1e-6        


R1_caso = 1e3           
L_caso = 100e-3         
R2_caso = 1e3           
C_caso = 1000e-6        



def rlc_ft(u, t, R1, L, R2, C):
    
    num = [R2]

    den = [
        L * C * R2,
        L + C * R1 * R2,
        R1 + R2
    ]

    sys = signal.TransferFunction(num, den)
    _, y, _ = signal.lsim(sys, U=u, T=t)

    return y, num, den


Ve_control, num_control, den_control = rlc_ft(
    u, t,
    R1_control,
    L_control,
    R2_control,
    C_control
)


Vs_caso, num_caso, den_caso = rlc_ft(
    u, t,
    R1_caso,
    L_caso,
    R2_caso,
    C_caso
)



def pid_rlc_response(u, t, R1, L, R2, C, Kp, Ki, Kd):

    a2 = L * C * R2
    a1 = L + C * R1 * R2
    a0 = R1 + R2

    num = [
        R2 * Kd,
        R2 * Kp,
        R2 * Ki
    ]

    den = [
        a2,
        a1 + R2 * Kd,
        a0 + R2 * Kp,
        R2 * Ki
    ]

    sys = signal.TransferFunction(num, den)
    _, y, _ = signal.lsim(sys, U=u, T=t)

    return y

PID_caso = pid_rlc_response(
    u, t,
    R1_caso,
    L_caso,
    R2_caso,
    C_caso,
    Kp=132.81296326735,
    Ki=3266.13831963624,
    Kd=0.180716891182534
)


plt.rcParams['font.family'] = 'serif'
plt.rcParams['mathtext.fontset'] = 'cm'

plt.figure(figsize=(6.2, 4.4), facecolor='white')

plt.plot(
    t, Ve_control,
    '-',
    lw=1.2,
    color='#B8A9F2',
    label=r'$Ve(t):\mathrm{Control}$'
)

plt.plot(
    t, Vs_caso,
    '-',
    lw=1.2,
    color='#F7C6D8',
    label=r'$Vs(t):\mathrm{Caso}$'
)

plt.plot(
    t, PID_caso,
    ':',
    lw=2.2,
    color='#9EDBFF',
    label=r'$PID(t)$'
)

plt.title('Control, Caso y PID', fontweight='bold', fontsize=12)

plt.xlim(0, 10)
plt.ylim(-0.2, 1.2)

plt.xticks(np.arange(0, 11, 1))
plt.yticks(np.arange(-0.2, 1.21, 0.2))

plt.xlabel(r'$t\ [s]$', fontsize=11)
plt.ylabel(r'$F(t)\ [V]$', fontsize=11)

plt.legend(
    loc='lower center',
    bbox_to_anchor=(0.5, 1.12),
    ncol=3,
    frameon=False,
    fontsize=10
)

plt.tick_params(direction='in', top=True, right=True)

plt.subplots_adjust(
    left=0.12,
    right=0.98,
    bottom=0.14,
    top=0.82
)

plt.savefig('endocrino_RLC_control_caso_PID.pdf', format='pdf', bbox_inches='tight')

plt.show()