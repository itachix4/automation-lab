# AI Helper Prototype - Sample Code

def generate_email(name: str, subject: str, content: str):
    template = f"""
Subject: {subject}

Hi {name},

{content}

Regards,
AI Assistant
"""
    return template

# Example use
email_text = generate_email(
    name="Parth",
    subject="Your Request",
    content="Here is the information you asked for."
)

print(email_text)
