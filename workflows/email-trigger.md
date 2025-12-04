# 📧 Email Trigger Workflow

## 🔍 Overview
This workflow sends an automated email when a new form entry is received.  
It simulates how automation tools like Zapier trigger actions based on incoming data.

---

## ⚙️ Trigger
- **Event:** New form submission
- **Source:** Form API / Contact form
- **Condition:** Submission contains a valid email

---

## 🧠 Logic
1. Check if the submitted data includes:
   - name  
   - email  
   - message  
2. Validate email formatting  
3. Generate an auto-reply email  
4. Send email using an email API (SendGrid, Gmail API, etc.)

---

## 📤 Sample Auto-Reply Email
