## 🛠️ Setup Instructions via SSH

### Step 1: Create and Save the Script

```bash
sudo nano ~/temp_monitor.py
```

Paste your script content and save the file.

---

### Step 2: Make the Script Executable

```bash
sudo chmod +x ~/temp_monitor.py
```

---

### Step 3: Test the Script

Test run (will run once; stop with Ctrl+C):

```bash
python3 ~/temp_monitor.py
```

---

### Step 4: Create a Systemd Service for Auto-Start

```bash
sudo nano /etc/systemd/system/temp-monitor.service
```

Paste the following service configuration (❗replace `REPLACE_WITH_YOUR_USERNAME` in 3 places):

```ini
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
```

---

### Step 5: Enable and Start the Service

```bash
sudo systemctl daemon-reload
sudo systemctl enable temp-monitor.service
sudo systemctl start temp-monitor.service
```

---

### Step 6: Check Service Status

```bash
sudo systemctl status temp-monitor.service
```

---

✅ **Note**:  
The CSV files will now be created in:

```text
/home/REPLACE_WITH_YOUR_USERNAME/temp_logs/
```
