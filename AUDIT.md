# 🔍 Audit Log Documentation

The **El-Mahrosa Sovereign System** is designed for **full auditability and compliance**. All critical operations are logged to `logs/audit.log`.

---

## 📜 Log Format

The audit log uses a **structured JSON format** for easy parsing and analysis:

```json
{
  "timestamp": "YYYY-MM-DDTHH\:mm\:ss.sssZ",
  "level": "INFO"   "WARN" | "ERROR" | "COMPLIANCE",
  "module": "compliance" | "treasury" | "sdg-mapping" | "api",
  "operation": "rule_check" | "transaction_intent" | "stake_update" | "data_query",
  "user_id": "Verified Contributor ID or API Key Hash",
  "status": "SUCCESS" | "FAILURE" | "VIOLATION",
  "details": "A human-readable message describing the event."
}


🗄 Retention Policy

Audit logs are retained for a minimum of 7 years on a separate, immutable storage system to meet regulatory compliance requirements.
Local development logs are for debugging only and should not be relied upon for official audits.
Copy



