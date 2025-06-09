# no GUI data-traccer

This is a simple Python-based Data Tracker that works via the command line (no GUI). It helps you monitor system data like CPU usage, memory usage, and network activity at regular intervals and logs the results in a text or CSV file.

✅ Features
Developed using pure Python

No GUI — lightweight and runs in any terminal

Tracks:

🔸 CPU usage (%)

🔸 Memory usage (%)

🔸 Network upload/download (KB)

Saves data in .csv or .txt format

Custom time interval for tracking

Easy to modify and extend

🛠️ Technologies Used
Python 3.x

Modules:

psutil – for monitoring system resources

time, datetime – for timing and logging

csv – for file handling

argparse – for command-line arguments

🧑‍💻 How to Run
1. Clone the Repository
bash
Copy
Edit
git clone https://github.com/yourusername/data-tracker.git
cd data-tracker
2. Install Required Packages
bash
Copy
Edit
pip install psutil
3. Run the Script
bash
Copy
Edit
python tracker.py --interval 5 --output data_log.csv
📌 Parameters:

--interval → Time gap (in seconds) between logs

--output → Output file path (CSV or TXT)

📁 Sample Output (CSV)
scss
Copy
Edit
Timestamp,CPU_Usage(%),Memory_Usage(%),Upload(KB),Download(KB)
2025-06-09 16:10:30,12.5,41.2,104.3,89.7
2025-06-09 16:10:35,11.1,39.9,107.2,90.3
🧰 Use Cases
Monitor server resource usage

Log network usage over time

Run in background on low-resource systems

Use as base for automation or data analytics

🚀 Future Scope
Add logging to database (SQLite or MySQL)

Auto-clean old log files

Add email/SMS alerts

Build optional GUI using Tkinter or Flask
