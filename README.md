# Bypass_Ideal_Monitor-BOT
A Python script that detects system idle time and performs automated actions to prevent inactivity. The script monitors keyboard and mouse activity, and when the system is idle for a specified duration, it executes a predefined action while logging the activity.


### Description
A Python script that detects system idle time and performs automated actions to prevent inactivity. The script monitors keyboard and mouse activity, and when the system is idle for a specified duration, it executes a predefined action while logging the activity.

### README

# Idle Activity Monitor

Idle Activity Monitor is a Python-based automation tool that monitors system inactivity and triggers predefined actions when a user is idle for a specified duration. The script can help keep systems active or simulate user activity, making it useful for scenarios where prolonged idle time is undesirable.

## Features

- **Idle Detection**: Monitors keyboard and mouse activity to determine idle time.
- **Automated Actions**: Executes predefined actions (e.g., mouse movement, keystrokes) to simulate activity.
- **Activity Logging**: Logs every triggered action with a timestamp in a JSON file.
- **Customizable Thresholds**: Configure idle time threshold and action intervals.
- **Failsafe Mechanism**: Ensures user safety by allowing escape from unexpected behavior with `pyautogui`'s failsafe.

## Requirements

- Python 3.6 or higher
- `pyautogui` library
- `pynput` library

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/your-username/idle-activity-monitor.git
    cd idle-activity-monitor
    ```

2. Install dependencies:

    ```bash
    pip install pyautogui pynput
    ```

3. (Optional) Modify script parameters to suit your needs.

## Usage

Run the script to start monitoring idle time:

```bash
python idle_monitor.py
```

### Parameters

- **`idle_threshold`**: Time in seconds before the system is considered idle (default: 2 minutes).
- **`action_interval`**: Time in seconds between repeated actions during inactivity (default: 2 seconds).
- **`LOG_FILE`**: File path where activity logs are saved (default: `/tmp/idle_monitor_log.json`).

### Actions Performed

When idle time exceeds the threshold:
1. Moves the mouse cursor.
2. Simulates a mouse click.
3. Simulates a key press (`Shift`).

The log file will record the date, time, and message for every action performed.

## Example

### Logs

The logs are saved in JSON format. Example log entry:

```json
[
    {
        "date": "2024-11-22",
        "time": "02:15:45 PM",
        "message": "Awake function called"
    },
    {
        "date": "2024-11-22",
        "time": "02:17:50 PM",
        "message": "Awake function called"
    }
]
```

### Idle Time Behavior

- If the user is inactive for more than the `idle_threshold`, the script will execute its actions every `action_interval` seconds until activity resumes.

## Stopping the Script

Press `Ctrl+C` in the terminal to stop the script manually.

## Contributing

Contributions are welcome! Feel free to:
- Submit issues for bug reports or feature suggestions.
- Fork the repository and create pull requests with improvements.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
