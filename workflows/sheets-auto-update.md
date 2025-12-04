# 📊 Google Sheets Auto-Update Workflow

## 🔍 Overview
This workflow updates a Google Sheet whenever new data is received from an external source.  
Useful for analytics, lead tracking, or reporting dashboards.

---

## ⚙️ Trigger
- **Event:** New entry submitted  
- **Target:** Google Sheets document  
- **Condition:** Data must include at least one required field  

---

## 🧠 Logic
1. Receive data from input form / API  
2. Append new row to Google Sheet  
3. Update:
   - Timestamp  
   - Data source  
   - Status field  
4. Send confirmation notification  

---

## 📁 Sheet Structure
| Timestamp | Name | Email | Source | Status |
|----------|------|-------|--------|--------|
| Auto     | Input | Input | API/Form | Updated |

---

## 📌 Status
Working concept – ready for integration testing  
