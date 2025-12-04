# Email Trigger Workflow - Sample Code

def validate_email(email: str) -> bool:
    return "@" in email and "." in email

def generate_reply(name: str) -> str:
    return f"Hi {name},\n\nThanks for contacting us. We'll get back to you soon.\n\nRegards,\nAutomation Bot"

def send_email(to: str, body: str):
    print(f"Sending email to {to}...")
    print("Email content:")
    print(body)
    print("Status: Sent ✓")

def email_trigger_workflow(entry: dict):
    if not validate_email(entry["email"]):
        print("Invalid email — cannot send.")
        return
    
    reply = generate_reply(entry["name"])
    send_email(entry["email"], reply)


# Example run
entry_data = {"name": "John", "email": "john@example.com"}
email_trigger_workflow(entry_data)
