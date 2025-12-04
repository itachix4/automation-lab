# Notification Engine Workflow - Sample Code

def send_alert(message: str):
    print("🔔 ALERT:", message)

def notification_engine(data: dict):
    if data.get("status") == "urgent":
        send_alert("High-priority issue detected!")

    if data.get("value", 0) > 100:
        send_alert("Value exceeded threshold!")

    if data.get("task_completed"):
        send_alert("Task completed successfully ✓")


# Example run
payload = {"status": "urgent", "value": 150, "task_completed": False}
notification_engine(payload)
