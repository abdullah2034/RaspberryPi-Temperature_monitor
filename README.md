**Setup Instructions via SSH**
Step 1: Create and Save the Script
sudo nano ~/temp_monitor.py
Step 2: Make the Script Executable
sudo chmod +x ~/temp_monitor.py
Step 3: Test the Script
Test run (will run once then you can stop with Ctrl+C)
python3 ~/temp_monitor.py
Step 4: Create a Systemd Service for Auto-Start
sudo nano /etc/systemd/system/temp-monitor.service
Paste this service configuration and DONT FORGET TO REPLACE YOUR USERNAME IN BELOW SCRIPT:
[Unit]
Description=Raspberry Pi Temperature Monitor
After=network.target
[Service]
Type=simple
User=REPLACE_WITH_YOUR_USERNAME
WorkingDirectory=/home/REPLACE_WITH_YOUR_USERNAME
ExecStart=/usr/bin/python3 /home/REPLACE_WITH_YOUR_USERNAME/temp_monitor.py
Restart=always
RestartSec=10
[Install]
WantedBy=multi-user.target
Step 5: Enable and Start the Service
sudo systemctl daemon-reload
sudo systemctl enable temp-monitor.service
sudo systemctl start temp-monitor.service
Step 6: Check Service Status
sudo systemctl status temp-monitor.service
