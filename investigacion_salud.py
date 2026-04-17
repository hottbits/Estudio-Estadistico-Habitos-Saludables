import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SIMULACIÓN DE DATOS (Mínimo 100 registros como pide la consigna)
np.random.seed(42)
data = {
    'Estudiante_ID': range(1, 101),
    'Horas_Sueno': np.random.normal(6.5, 1.5, 100).clip(3, 12),
    'Actividad_Fisica_Min': np.random.randint(0, 120, 100),
    'Alimentacion_Saludable': np.random.choice(['Sí', 'No'], 100, p=[0.4, 0.6])
}
df = pd.DataFrame(data)

# 2. MÉTODO CIENTÍFICO: PLANTEAMIENTO DE HIPÓTESIS
# Hipótesis Nula (H0): Los estudiantes duermen 7 horas o más en promedio.
# Hipótesis Alternativa (H1): Los estudiantes duermen menos de 7 horas en promedio.
media_objetivo = 7

# 3. CÁLCULO DE INFERENCIA (Test de Hipótesis)
t_stat, p_value = stats.ttest_1samp(df['Horas_Sueno'], media_objetivo)

# 4. INTERVALOS DE CONFIANZA (95%)
confianza = 0.95
media, sigma = df['Horas_Sueno'].mean(), df['Horas_Sueno'].std()
intervalo = stats.t.interval(confianza, len(df)-1, loc=media, scale=stats.sem(df['Horas_Sueno']))

print("--- RESULTADOS DEL ESTUDIO CIENTÍFICO ---")
print(f"Media de sueño observada: {media:.2f} horas")
print(f"Intervalo de confianza (95%): {intervalo}")
print(f"Valor-p (Significancia): {p_value:.4f}")

if p_value < 0.05:
    print("Resultado: Se RECHAZA la hipótesis nula. Hay evidencia de falta de sueño.")
else:
    print("Resultado: NO se rechaza la hipótesis nula.")

# 5. VISUALIZACIÓN DE LA DISTRIBUCIÓN
plt.figure(figsize=(10,6))
sns.histplot(df['Horas_Sueno'], kde=True, color='green')
plt.axvline(media_objetivo, color='red', linestyle='--', label='Meta (7 hrs)')
plt.title('Distribución de Horas de Sueño en Universitarios')
plt.legend()
plt.savefig('distribucion_sueno.png')
plt.show()