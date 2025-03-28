import streamlit as st
import pandas as pd
import plotly.express as px

# Datos detallados
DATA = pd.DataFrame({
    "Eje": [
        "Tuberculosis", "Tuberculosis", "Tuberculosis",
        "Planificación Familiar", "Planificación Familiar", "Planificación Familiar",
        "Vectores", "Vectores", "Vectores", "Vectores",
        "Alimentos", "Alimentos",
        "Agua Potable", "Agua Potable",
        "Vacunación", "Vacunación", "Vacunación", "Vacunación", "Vacunación",
        "Promoción Salud", "Promoción Salud", "Promoción Salud"
    ],
    "Actividad": [
        "Supervisiones", "Visitas seguimiento", "Kits alimentarios",
        "Visitas inspección", "Habilitación prestadores", "Notificaciones",
        "Fumigaciones", "Tapas barricas", "Mosquiteros", "Descacharrización",
        "Supervisiones comida", "Permisos alimentarios",
        "Tomas de cloro", "Inspecciones plantas",
        "Polio", "Neumococo", "Hepatitis B", "Difteria/Tétanos", "VPH",
        "Educación en salud", "Vitamina A", "Desparasitación"
    ],
    "2024": [
        48, 47, 47,
        70, 50, 26,
        501, 1218, 421, 591,
        1956, 827,
        440, 25,
        17140, 0, 0, 0, 0,
        30823, 4715, 41408
    ],
    "2025_Q1": [
        26, 24, 24,
        16, 15, 8,
        115, 127, 154, 147,
        692, 312,
        2088, 3,
        823, 226, 510, 3417, 218,
        4507, 843, 0
    ],
    "Impacto": [
        "Fortalecimiento de la atención integral en TB.",
        "Seguimiento directo que mejora la adherencia al tratamiento.",
        "Apoyo nutricional a pacientes con TB para mejorar recuperación.",
        "Supervisión del cumplimiento de protocolos en planificación.",
        "Ampliación del acceso a servicios reproductivos certificados.",
        "Monitoreo del cumplimiento de normativas de habilitación.",
        "Reducción del riesgo de arbovirosis en zonas críticas.",
        "Prevención de criaderos mediante control de almacenamiento de agua.",
        "Protección directa con barreras físicas contra vectores.",
        "Limpieza comunitaria para eliminar criaderos potenciales.",
        "Garantía de prácticas higiénicas en venta de alimentos.",
        "Regularización formal de negocios de expendio alimentario.",
        "Aseguramiento de calidad del agua para consumo humano.",
        "Control estructural en procesos de potabilización.",
        "Prevención de polio en la primera infancia.",
        "Protección a adultos mayores vulnerables.",
        "Reducción de hepatitis con enfoque preventivo.",
        "Cobertura extendida en población adulta contra enfermedades.",
        "Vacunación anticipada para adolescentes contra VPH.",
        "Educación sanitaria desde edades tempranas.",
        "Suplementación vitamínica esencial en la infancia.",
        "Reducción de parasitosis intestinal en escolares."
    ]
})

# Sidebar: selección del eje temático
st.sidebar.title("Exploración por Eje Temático")
eje = st.sidebar.selectbox("Selecciona un eje", DATA["Eje"].unique())

# Filtrar datos
subset = DATA[DATA["Eje"] == eje]

# Título principal
st.title(f"Actividades del eje: {eje}")

# Gráfico interactivo
fig = px.bar(
    subset,
    x="Actividad",
    y=["2024", "2025_Q1"],
    barmode="group",
    title=f"Comparación de Actividades en {eje} - 2024 vs 2025 Q1",
    labels={"value": "Cantidad", "variable": "Año"},
    color_discrete_sequence=px.colors.qualitative.Set2
)
st.plotly_chart(fig, use_container_width=True)

# Impacto por actividad
for _, row in subset.iterrows():
    with st.expander(f"Impacto de '{row['Actividad']}':"):
        st.write(row["Impacto"])
