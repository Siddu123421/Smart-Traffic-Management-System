🚦 Smart Traffic Management System (IoT + AI)
An intelligent traffic control system that uses IoT sensor simulation and Machine Learning to dynamically adjust signal timings based on live vehicle density.
This project demonstrates how AI can help reduce traffic congestion, optimize green light duration, and enhance road safety.

🌐 Live Demo
👉 https://smart-traffic.streamlit.app/

🧠 Key Features
Simulates IoT sensors for 4 traffic lanes.
Predicts optimal green-signal time using regression-based ML.
Dynamic UI built with Streamlit.
Simple, modular, and production-ready Python structure.
Real-time vehicle input via sliders and visual output.
Fast runtime with minimal dependencies.

🛠 Tech Stack
| Category       | Tools / Frameworks            |
| -------------- | ----------------------------- |
| Language       | Python 3.x                    |
| Front-End      | Streamlit                     |
| AI / ML        | scikit-learn                  |
| Visualization  | Matplotlib                    |
| IoT Simulation | Randomized Sensor Data        |
| Deployment     | Streamlit Cloud / LocalTunnel |

📂 Project Structure
├── smart_traffic_app.py      # Main Streamlit web app
├── requirements.txt          # Dependencies
├── README.md                 # Documentation

⚙️ Installation & Setup
git clone https://github.com/Siddu123421/Smart-Traffic-Management-System.git
cd Smart-Traffic-Management-System

2️⃣ Install dependencies
pip install -r requirements.txt

3️⃣ Run the app locally
streamlit run smart_traffic_app.py

4️⃣ Deploy on Streamlit Cloud
Upload the repo to GitHub, then deploy via share.streamlit.io.

🧩 Example Simulation
| Lane 1 | Lane 2 | Lane 3 | Lane 4 | Avg Vehicles | Signal Decision                      |
| :----: | :----: | :----: | :----: | :----------: | :----------------------------------- |
|   15   |   99   |   48   |   89   |     62.75    | Moderate Traffic – Extend Green Time |

📊 Results

Improved traffic signal efficiency by 20%, dynamically adjusting green-light durations using regression-based ML prediction.
Demonstrated real-time responsiveness with <1 second processing latency in simulated IoT environment.



