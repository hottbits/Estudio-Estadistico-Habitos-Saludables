# 📑 Estudio Estadístico: Hábitos Saludables en Universitarios

Este proyecto aplica el **método científico** y técnicas de **inferencia estadística** para analizar los hábitos de sueño y actividad física en una población de 100 estudiantes universitarios.

## 🎯 Objetivo de la Investigación
Determinar si la media de horas de sueño de los estudiantes es significativamente inferior a la recomendación de salud de 7 horas diarias, utilizando pruebas de hipótesis.

## 🛠️ Tecnologías Utilizadas
* **Python 3.13**
* **Pandas:** Estructuración del dataset simulado.
* **SciPy (stats):** Ejecución de Test de Hipótesis (T-Test) e Intervalos de Confianza.
* **Matplotlib & Seaborn:** Visualización de la distribución de los datos.

## 🧪 Metodología Aplicada
1. **Planteamiento de Hipótesis:** * $H_0$ (Hipótesis Nula): La media de sueño es $\geq$ 7 horas.
   * $H_1$ (Hipótesis Alternativa): La media de sueño es < 7 horas.
2. **Nivel de Confianza:** 95% ($\alpha = 0.05$).
3. **Prueba Estadística:** T-Test para una muestra.

## 📈 Resultados
El script genera un análisis que incluye:
* La media observada de la muestra.
* El **valor-p (p-value)** para determinar la significancia estadística.
* El **Intervalo de Confianza** donde se encuentra la verdadera media poblacional.

## 🚀 Cómo ejecutar
1. Instala las dependencias:
   ```bash
   pip install pandas scipy matplotlib seaborn
