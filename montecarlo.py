import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

st.subheader ("Montecarlo Simulation- OOIP")

c1,c2,c3 = st.columns(3)

mode_poro = c1.number_input("Porosity Mode", value=0.21)
mode_swi = c2.number_input("Swi Mode", value=0.25)
mode_h = c3.number_input("payzone Mode", value=40)

size_slider = st.slider("Change for size of distribution", min_value=8000, max_value=100000, value=10000)


poro = np.random.triangular (0.15, mode_poro, 0.25, size=size_slider)
swi = np.random.triangular (0.2, mode_swi, 0.4, size=size_slider)
pay = np.random.triangular (30, mode_h, 100, size=size_slider)

OOIP = 7758*12500*pay*poro*(1-swi)/1.05

#fig, ax = plt.subplots(figsize=(10,5))
#ax.hist(OOIP, bins=100, ec="black", color="green")
#ax.set_title("Oiriginal Oil In Place Distribution")
#ax.grid()
#st.pyplot(fig)


# Calcula los percentiles
P10 = np.percentile(OOIP, 10)
P50 = np.percentile(OOIP, 50)
P90 = np.percentile(OOIP, 90)

# Crea la figura y el histograma
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(OOIP, bins=100, ec="black", color="green")

# Dibuja líneas verticales para los percentiles
ax.axvline(P10, color='red', linestyle='dashed', linewidth=2)
ax.axvline(P50, color='blue', linestyle='dashed', linewidth=2)
ax.axvline(P90, color='purple', linestyle='dashed', linewidth=2)

# Añade texto con los valores de los percentiles divididos entre un millón
ax.text(P10, plt.ylim()[1] * 0.95, f'P10: {P10/1e6:.2f} MM', color='red', ha='center')
ax.text(P50, plt.ylim()[1] * 0.85, f'P50: {P50/1e6:.2f} MM', color='blue', ha='center')
ax.text(P90, plt.ylim()[1] * 0.75, f'P90: {P90/1e6:.2f} MM', color='purple', ha='center')

# Ajusta el título y la cuadrícula
ax.set_title("Original Oil In Place Distribution")
ax.grid()

# Muestra la figura en Streamlit
st.pyplot(fig)