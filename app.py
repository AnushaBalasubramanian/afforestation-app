import streamlit as st
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Afforestation Impact Calculator 🌱")

# Title
st.title("🌿 Afforestation Impact Modeling")
st.markdown("""
This app estimates *CO₂ absorption* through afforestation over time.  
It models how many kilograms of CO₂ are absorbed based on the number of trees planted.
""")

# Inputs
st.sidebar.header("🌱 User Inputs")
trees = st.sidebar.number_input("Number of Trees Planted", min_value=1, value=100)
co2_per_tree = st.sidebar.number_input("CO₂ Absorbed per Tree per Year (kg)", min_value=1.0, value=21.77)
years = st.sidebar.slider("Projection Years", min_value=1, max_value=50, value=20)

# Calculations
years_array = np.arange(1, years + 1)
co2_absorbed = trees * co2_per_tree * years_array

# Output
st.subheader("📈 CO₂ Absorption Over Time")
fig, ax = plt.subplots()
ax.plot(years_array, co2_absorbed, marker='o', color='green')
ax.set_xlabel("Years")
ax.set_ylabel("Total CO₂ Absorbed (kg)")
ax.set_title("Projected CO₂ Absorption by Trees")
st.pyplot(fig)

import folium
from streamlit_folium import st_folium

st.subheader("📍 Tree Plantation Site (Chennai)")

# Create a map centered around Chennai
chennai_map = folium.Map(location=[13.0827, 80.2707], zoom_start=10)

# Add a marker for the plantation site
folium.Marker(
    location=[13.0827, 80.2707],
    popup="🌳 Trees Planted Here - Chennai",
    icon=folium.Icon(color="green", icon="leaf")
).add_to(chennai_map)

# Display the map in Streamlit
st_folium(chennai_map, width=700, height=500)

# Summary
total = co2_absorbed[-1]
st.success(f"🌍 By planting *{trees}* trees, you can absorb approximately *{total:,.2f} kg* of CO₂ over *{years} years*.")

# Awareness / Links
st.markdown("---")
st.markdown("### 🌐 Learn More & Take Action:")
st.markdown("- [One Tree Planted](https://onetreeplanted.org/)")
st.markdown("- [Plant-for-the-Planet](https://www.plant-for-the-planet.org/)")
st.markdown("- [Global Forest Watch](https://www.globalforestwatch.org/)")
