# app/logger.py
import json
import time
from pathlib import Path

class EventLogger:
    """
    A structured event logger that writes events to a JSON Lines file.

    Each event is a JSON object on a new line, which is efficient for logging
    and easy to parse. This format is ideal for machine-readable logs that
    can be fed into data analysis pipelines.
    """
    def __init__(self, filename="output/events.jsonl"):
        """
        Initializes the logger and ensures the output directory exists.

        Args:
            filename (str): The path to the log file.
        """
        self.log_file = Path(filename)
        # Ensure the parent directory exists
        self.log_file.parent.mkdir(exist_ok=True)
        # Clear the log file at the start of a new session
        if self.log_file.exists():
            self.log_file.unlink()

    def event(self, event_type: str, data: dict = None):
        """
        Logs a new event to the file.

        The event record includes a precise timestamp, the event type, and any
        associated data.

        Args:
            event_type (str): A string identifying the type of event (e.g., "SIMULATION_START").
            data (dict, optional): A dictionary containing event-specific details.
        """
        record = {
            "timestamp": time.time(),
            "event": event_type,
            "data": data or {}
        }
        with self.log_file.open("a") as f:
            f.write(json.dumps(record) + "\n")