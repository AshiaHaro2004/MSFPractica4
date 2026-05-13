[![Open in MATLAB Online](https://www.mathworks.com/images/responsive/global/open-in-matlab-online.svg)](https://matlab.mathworks.com/open/github/v1?repo=Osiris-1904/MSFPractica4)
# Práctica 4: Modelo del sistema endocrino

## Información del estudiante
Osiris Jaylin Chavez Hernandez \[23210697]; l23210697@tijuana.tecn.mx

Modelado de Sistemas Fisiológicos

Ingeniería Biomédica

## Docente
Dr. Paul Antonio Valle Trujillo; paul.valle@tectijuana.edu.mx

Departamento de Ingeniería Eléctrica y Electrónica, Tecnológico Nacional de México/IT Tijuana, Blvd. Alberto Limón Padilla s/n, Tijuana, C.P. 22454, B.C., México.

## Descripción de la asignatura

El modelizado de sistemas fisiológicos es una herramienta importante en Ingeniería Biomédica, permite comprender el funcionamiento del cuerpo humano, así como diseñar y evaluar terapias y dispositivos médicos; se define como el proceso de formular modelos matemáticos o computacionales que representan el comportamiento y la interacción de los sistemas biológicos y fisiológicos. Esta asignatura pretende aportar al perfil del Ingeniero Biomédico la capacidad de realizar investigación científica en el área de Biología de Sistemas con la finalidad de dirigir y participar en equipos de trabajo interdisciplinarios en contextos nacionales e internacionales, así como de proporcionar soluciones informáticas para resolver problemas en el campo de la Ingeniería Biomédica con ética profesional; lo anterior al proporcionar al estudiante bases sólidas para modelizar sistemas y diseñar controladores para la solución de problemas en las áreas de atención médica y del sector industrial médico. La construcción de analogías entre circuitos eléctricos y sistemas fisiológicos para la formulación de modelos matemáticos y el diseño de controladores mediante la experimentación in silico brindan herramientas de gran aplicación en el quehacer profesional del Ingeniero Biomédico.

La asignatura de Modelado de Sistemas Fisiológicos forma parte del plan de estudios de la carrera en Ingeniería Biomédica con la siguiente competencia general del curso: Utiliza las propiedades de los circuitos RLC para describir la dinámica de sistemas fisiológicos, obtener modelos matemáticos y aplicar el control clásico, esto con el objetivo de integrar los principios de la Ingeniería de Control, la Electrónica Analógica y las Ciencias de la Computación con la Anatomía y Fisiología del cuerpo humano para proporcionar descripciones cuantitativas y cualitativas de sistemas fisiológicos complejos con el objetivo de modelizar, analizar, controlar, ilustrar y predecir su dinámica tanto en el corto como en el largo plazo.

## Objetivos

1. Calcular la función de transferencia.
2. Determinar el modelo de ecuaciones integro-diferenciales.
3. Establecer el sistema de ecuaciones diferenciales ordinarias lineales de primer orden.
4. Emular la respuesta del circuito RLC en Simulink/Simscape al escalón, impulso, rampa y función sinusoidal.
5. Simular la respuesta de los modelos matemáticos en Simulink/MATLAB al escalón, impulso, rampa y función sinusoidal.
6. Sintonizar las ganancias de un controlador PID para eliminar el error entre la entrada y la salida del sistema.
7. Obtener la respuesta en lazo abierto y en lazo cerrado con el controlador PID en Spyder/Python con la función de transferencia.

## Descripción detallada del sistema

Un circuito RLC puede representar, de manera simplificada, la dinámica del sistema endocrino, ya que permite modelar cómo una señal hormonal se produce, se transporta y genera una respuesta en el organismo. En esta analogía, el resistor R representa la resistencia o dificultad en la regulación metabólica y en la respuesta de los tejidos ante una hormona; el capacitor C representa la capacidad de almacenamiento o acumulación hormonal en el sistema; y el inductor L representa la inercia o retardo fisiológico en la respuesta hormonal. El objetivo del modelo eléctrico es analizar cómo cambia la salida del sistema ante una señal de entrada, simulando el comportamiento de las glándulas endocrinas, la liberación de hormonas y los mecanismos de retroalimentación hormonal que mantienen la homeostasis.

Palabras clave: Hormonas; Glándulas endocrinas; Regulación metabólica; Homeostasis; Retroalimentación hormonal.

## Lista de archivos incluidos en el repositorio
1. Cuaderno computacional de MATLAB [.mlx].
2. Modelo de Simulink [.slx].
3. Archivos de Spyder [.py].
4. Imagen con los parámetros del controlador.
5. Imagénes de las simulaciones [.pdf].

## Referencias
\[1] P. A. Valle, Syllabus para Modelado de Sistemas Fisiológicos, Tecnológico Nacional de México / Instituto Tecnológico de Tijuana, Tijuana, B.C., México, 2025. Permalink: https://biomath.xyz/course/

\[2] M. C. Khoo, Physiological Control Systems Analysis Simulation, and Estimation, 2nd ed. Piscataway, New Jersey, USA: IEEE Press, 2018, Section 4, Page 93.

\[3] N. S. Nise, Control Systems Engineering, 8th ed. Hoboken, New Jersey, USA: John Wiley & Sons, 2020.
