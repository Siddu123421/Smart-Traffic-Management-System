# Smart Traffic Management System with IoT and AI
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# ---------------------- PAGE CONFIG ----------------------
st.set_page_config(
    page_title="Smart Traffic Management System",
    page_icon="🚦",
    layout="wide"
)

# ---------------------- HEADER ----------------------
st.title("🚦 Smart Traffic Management System (IoT + AI)")
st.markdown("This app simulates an **AI-powered traffic control system** that predicts ideal signal timing based on live vehicle counts.")

st.divider()

# ---------------------- SIMULATION ----------------------
st.subheader("🔹 Step 1: IoT Sensor Simulation")

lanes = ["Lane 1", "Lane 2", "Lane 3", "Lane 4"]

vehicle_counts = {}
col_inputs = st.columns(4)
for i, lane in enumerate(lanes):
    vehicle_counts[lane] = col_inputs[i].number_input(
        f"{lane} Vehicle Count", min_value=0, max_value=200, value=np.random.randint(10,100)
    )

if st.button("Simulate IoT Data"):
    df = pd.DataFrame([vehicle_counts])
    df["Average_Vehicles"] = df.mean(axis=1)
    st.success("✅ IoT sensor data generated!")
    st.dataframe(df)
else:
    df = pd.DataFrame()

# ---------------------- MODEL ----------------------
if not df.empty:
    st.subheader("🔹 Step 2: AI Signal Time Prediction")

    # Train simple regression model (demo purpose)
    np.random.seed(42)
    data = pd.DataFrame({
        "Avg_Vehicles": np.arange(0, 120, 5)
    })
    data["Signal_Time"] = 20 + 0.3 * data["Avg_Vehicles"] + np.random.randn(len(data)) * 2

    model = LinearRegression().fit(data[["Avg_Vehicles"]], data["Signal_Time"])
    pred_time = model.predict([[df["Average_Vehicles"].values[0]]])[0]

    st.metric("Predicted Green Signal Duration", f"{pred_time:.1f} seconds")

    # Traffic status logic
    avg = df["Average_Vehicles"].values[0]
    if avg < 40:
        status, color = "Low Traffic – Normal Flow", "green"
    elif avg < 80:
        status, color = "Moderate Traffic – Adjusting Signal", "yellow"
    else:
        status, color = "High Traffic – Delays Expected", "red"

    st.subheader("🔹 Step 3: Traffic Condition")
    st.markdown(f"**Status:** {status}")

    # ---------------------- VISUALIZATION ----------------------
    st.subheader("🔹 Step 4: Visualization")

    fig, ax = plt.subplots(figsize=(3.5,3.5))
    circle = plt.Circle((0.5, 0.5), 0.3, color=color)
    ax.add_artist(circle)
    ax.axis("off")
    plt.title(status, fontsize=11)
    st.pyplot(fig)

    # ---------------------- EXPORT RESULTS ----------------------
    st.subheader("🔹 Step 5: Export Results")

    df["Predicted_Signal_Time"] = round(pred_time, 2)
    csv = df.to_csv(index=False).encode('utf-8')
    st.download_button("⬇️ Download Results as CSV", csv, "traffic_results.csv", "text/csv")

# ---------------------- FOOTER ----------------------
st.divider()
st.caption("Developed by Kadham Siddhartha | B.Tech CSE (AIML)")
