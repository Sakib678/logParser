# Cowrie Honeypot Log Analysis & Threat Intelligence Automation

### Overview
This project automates the analysis of **Cowrie honeypot logs** in order to make it easier to extract meaningful insights about real-world attack activity.  

---

### Objectives
- Understand **attacker behaviour** through log analysis  
- Identify **top IPs, usernames, and commands** used in brute-force attempts  
- Automate **threat reputation checks** via the AbuseIPDB API
  
###  Key Findings
After running the analysis for two days of Cowrie logs:
- **“root”** was by far the most common username, followed by **“admin”**  
- Several IPs had **AbuseIPDB confidence scores above 80**, confirming malicious behaviour  
- All attempts targeted **port 22 (SSH)** or **port 23 (Telnet)** 

> The insights from a honeypot can be used to detect brute-force attacks or strengthen firewall rules.

### Possible Future Improvements
- Real-time alerting for repeated attacks
- GeoIP mapping of attacker origins
- Visualising data automatically using a dashboard
- Export to CSV or JSON for reporting


