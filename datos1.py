import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

# --- CONFIGURACIÓN ---
num_records_random = 5000 

# Lista de Gerentes
gerentes = [
    'Juliana Gómez', 'Claudia Méndez', 'William Paredes', 'Angela Torres',
    'Gilmar Rodríguez', 'Sandro Valdez', 'Marcos Batista',
    'Patricia Núñez', 'Esteban Jiménez', 'Verónica López'
]

# ASIGNACIÓN DE PERFILES (Para garantizar variedad en el dashboard)
# 3 Gerentes "Malos" (Rojo/Negativo), 4 "Promedio" (Amarillo), 3 "Buenos" (Verde)
perfil_gerente = {
    'Juliana Gómez': 'Alto', 'Claudia Méndez': 'Bajo', 'William Paredes': 'Medio',
    'Angela Torres': 'Alto', 'Gilmar Rodríguez': 'Bajo', 'Sandro Valdez': 'Medio',
    'Marcos Batista': 'Medio', 'Patricia Núñez': 'Alto', 'Esteban Jiménez': 'Bajo',
    'Verónica López': 'Medio'
}

planos = ['Prepago', 'Postpago', 'Empresarial', 'Premium']
lista_sexos = ['Masculino', 'Femenino']

temas_clientes = [
    'Apertura de cuenta bancaria', 'Préstamo personal aprobado', 'Tarjeta de crédito',
    'Reclamo resuelto satisfactoriamente', 'Migración a plan Claro Postpago',
    'Instalación de fibra óptica Claro', 'Renovación de contrato', 'Mejora de señal móvil',
    'Actualización de datos', 'Solicitud empresarial', 'Atención VIP',
    'Consulta de balance', 'Pago electrónico exitoso'
]

# --- GEOGRAFÍA ---
dr_locations = [
    {'Region': 'Ozama', 'Provincia': 'Distrito Nacional', 'Ciudad': 'Santo Domingo de Guzmán', 'Weight': 0.18},
    {'Region': 'Ozama', 'Provincia': 'Santo Domingo', 'Ciudad': 'Santo Domingo Este', 'Weight': 0.10},
    {'Region': 'Norte', 'Provincia': 'Santiago', 'Ciudad': 'Santiago de los Caballeros', 'Weight': 0.12},
    {'Region': 'Este', 'Provincia': 'La Altagracia', 'Ciudad': 'Punta Cana', 'Weight': 0.07},
    {'Region': 'Sur', 'Provincia': 'San Cristóbal', 'Ciudad': 'San Cristóbal', 'Weight': 0.05},
    # (Se pueden añadir más, simplificado para el ejemplo)
]
loc_weights = [l['Weight'] for l in dr_locations]

# --- DEFINICIÓN DE PROBABILIDADES POR PERFIL ---
# Indices: 0-6 (Det), 7-8 (Neu), 9-10 (Prom)

# 1. PERFIL BAJO (Crítico/Negativo): NPS aprox -20 a 0
# Muchos detractores (45%), pocos promotores (25%)
probs_bajo = np.array([
    0.10, 0.08, 0.07, 0.05, 0.05, 0.05, 0.05,  # Detractores: ~45%
    0.15, 0.10,                                # Neutros: ~25%
    0.15, 0.15                                 # Promotores: ~30%
])
probs_bajo = probs_bajo / probs_bajo.sum()

# 2. PERFIL MEDIO (Mejora): NPS aprox 20 a 40
# Balanceado: Neutros altos (35%), Promotores (45%), Detractores (20%)
probs_medio = np.array([
    0.02, 0.02, 0.03, 0.03, 0.03, 0.03, 0.04,  # Detractores: ~20%
    0.20, 0.15,                                # Neutros: ~35%
    0.20, 0.25                                 # Promotores: ~45%
])
probs_medio = probs_medio / probs_medio.sum()

# 3. PERFIL ALTO (Excelencia): NPS > 70
# Mayoría promotores (75%), Detractores mínimos (5%)
probs_alto = np.array([
    0.005, 0.005, 0.005, 0.005, 0.01, 0.01, 0.01, # Detractores: ~5%
    0.10, 0.10,                                   # Neutros: ~20%
    0.35, 0.40                                    # Promotores: ~75%
])
probs_alto = probs_alto / probs_alto.sum()

data = []
start_date = datetime(2023, 1, 1)
total_days = 365 * 3

print("Generando simulacion dinámica...")

for _ in range(num_records_random):
    # Seleccionar Gerente y su perfil
    gerente = random.choice(gerentes)
    perfil = perfil_gerente[gerente]
    
    # Elegir probabilidades según el perfil del gerente
    if perfil == 'Bajo':
        probs = probs_bajo
    elif perfil == 'Medio':
        probs = probs_medio
    else:
        probs = probs_alto

    # Fecha aleatoria
    fecha = start_date + timedelta(days=random.randint(0, total_days))
    
    # Simular Score
    score = np.random.choice(np.arange(0, 11), p=probs)
    
    # Clasificación
    if score >= 9: clasificacion = 'Promotor'
    elif score >= 7: clasificacion = 'Neutro'
    else: clasificacion = 'Detractor'

    # Edad (Correlación leve: gente mayor suele votar mejor en este ejemplo)
    if score <= 6: edad = random.randint(18, 40)
    else: edad = random.randint(25, 75)

    # Ubicación
    loc = random.choices(dr_locations, weights=loc_weights, k=1)[0]

    data.append([
        len(data) + 1, fecha, fecha.year, gerente, random.choice(lista_sexos),
        random.choice(planos), loc['Region'], loc['Provincia'], loc['Ciudad'], score,
        clasificacion, edad, random.choice(temas_clientes)
    ])

# --- EXPORTAR ---
cols = [
    'ID', 'Fecha', 'Ano', 'Gerente', 'Sexo', 'Plano', 
    'Region', 'Estado', 'Ciudad', 
    'NPS_Score', 'Clasificacion', 'Idade', 'Tema_Cliente'
]

df = pd.DataFrame(data, columns=cols)
archivo = "nps_dataset_rd_banca_claro.xlsx"
df.to_excel(archivo, index=False)

print(f"✅ Archivo generado: {archivo}")
print("✅ Lógica Aplicada:")
print("   - Gerentes 'Bajo' (ej. Claudia, Gilmar): Tendrán NPS Negativo/Rojo.")
print("   - Gerentes 'Medio' (ej. William, Sandro): Tendrán NPS Amarillo.")
print("   - Gerentes 'Alto' (ej. Juliana, Angela): Tendrán NPS Verde/Excelencia.")