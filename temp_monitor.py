#!/usr/bin/env python3
"""
Raspberry Pi Temperature Monitor
Logs CPU temperature every minute to date-wise CSV files and an overall CSV file
Please must replace your username below on line 14
"""

import os
import csv
import time
from datetime import datetime

# Configuration
LOG_DIR = "/home/REPLACE_WITH_YOUR_USERNAME/temp_logs"  # Directory to store CSV files
TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"  # Pi temperature file

def get_cpu_temperature():
    """Read CPU temperature from system file"""
    try:
        with open(TEMP_FILE, 'r') as f:
            temp_str = f.read().strip()
            # Temperature is in millidegrees, convert to Celsius
            temp_celsius = float(temp_str) / 1000.0
            return round(temp_celsius, 2)
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None

def ensure_log_directory():
    """Create log directory if it doesn't exist"""
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR)
        print(f"Created log directory: {LOG_DIR}")

def write_to_csv(filename, timestamp, temperature):
    """Write temperature data to CSV file"""
    file_path = os.path.join(LOG_DIR, filename)
    file_exists = os.path.exists(file_path)
    
    try:
        with open(file_path, 'a', newline='') as csvfile:
            writer = csv.writer(csvfile)
            
            # Write header if file is new
            if not file_exists:
                writer.writerow(['DateTime', 'Temperature_C'])
            
            # Write data
            writer.writerow([timestamp, temperature])
            
    except Exception as e:
        print(f"Error writing to {filename}: {e}")

def log_temperature():
    """Main function to log temperature"""
    # Get current timestamp and temperature
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    date_str = now.strftime("%Y-%m-%d")
    
    temperature = get_cpu_temperature()
    
    if temperature is None:
        print(f"[{timestamp}] Failed to read temperature")
        return
    
    # Ensure log directory exists
    ensure_log_directory()
    
    # Generate filenames
    daily_filename = f"temp_{date_str}.csv"
    overall_filename = "overall.csv"
    
    # Write to both files
    write_to_csv(daily_filename, timestamp, temperature)
    write_to_csv(overall_filename, timestamp, temperature)
    
    print(f"[{timestamp}] Temperature: {temperature}°C - Logged to {daily_filename} and {overall_filename}")

def main():
    """Main execution function"""
    print("Raspberry Pi Temperature Monitor Started")
    print(f"Logging to directory: {LOG_DIR}")
    print("Press Ctrl+C to stop")
    
    try:
        while True:
            log_temperature()
            time.sleep(60)  # Wait 1 minute
    except KeyboardInterrupt:
        print("\nTemperature monitoring stopped by user")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()
