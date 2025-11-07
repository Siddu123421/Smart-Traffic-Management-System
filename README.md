# Smart-Traffic-Management-System
IoT-based AI Traffic Signal Optimization using Python and ML
🚦 IoT based Smart Traffic Management System

💡 Project Overview
The IoT and Machine Learning Smart Traffic Management System orchestrates dynamic control of light signal timings based on real-time vehicle data.
This system predicts optimal green light durations to minimize congestion and waiting — introducing intelligence into urban traffic flow.

🧠 Key Features
🔗 IoT Data Integration: Mock sensor inputs for the number of vehicles at an intersection.
🤖 Machine Learning Prediction: Utilizes a linear regression model to predict optimal signal timing.
📊 Dynamic Decision Logic: Dynamically modifies the traffic signal duration according to the level of congestion.
- 💬 Interpretable Recommendations: Offers explicit recommendations such as
“Low Traffic → Keep default 20s” or “High Traffic → Delay clearance”.
🧹 Warning-Free Model: Fully adapted to avoid sklearn feature mismatching

⚙️ Tech Stack
| Component          | Technology                     |
| ------------------ | ------------------------------ |
| Language           | Python 3.10                    |
| ML Framework       | scikit-learn                   |
| Data Handling      | Pandas, NumPy                  |
| Visualization      | Matplotlib                     |
| IDE                | Google Colab                   |
| Hosting (optional) | Streamlit Cloud / GitHub Pages |

🧩 Project Workflow
Simulated Data: Simulate lane-based vehicle counts.
Model Training: Train a linear regression model on the mean vehicle count and signal time.
IoT Integration: Simulate reading sensor data and feeding it to the model.
Decision Logic: Classify traffic as Low, Moderate, or High.
Output: Display suggested signal duration in real time.

📈 Sample Output
Avg Vehicles: 25 → Low Traffic → Keep default 20s
Avg Vehicles: 55 → Moderate Traffic → Extend green to 36.4s
Avg Vehicles: 95 → High Traffic → Delay clearance, green ~ 49.0s

🧰 Installation & Usage
# Clone this project
git clone https://github.com/yourusername/Smart-Traffic-Management-IoT.git
# Install dependencies
pip install -r requirements. txt
# To run in Colab or local python
python traffic_system.py



