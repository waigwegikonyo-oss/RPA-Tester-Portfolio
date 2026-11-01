# Test Plan: Invoice Processing Automation

## 1. Scope & Strategy
Full end-to-end testing of data extraction, business rule validation, edge-case exception handling, multi-currency verification, and database state audit logging.

## 2. Test Environment & Tools
- **RPA Platform:** UiPath Studio Web
- **Input Storage:** OneDrive Integration
- **Database Layer:** PostgreSQL / SQLite (`invoice_audit_log`, `purchase_orders`, `vendors`)
- **Reporting Engine:** Local CSV / Excel Audit Log

## 3. Test Scenario Matrix
| Test Case ID | Scenario Name | Test Data / Condition | Expected Result | Expected Error Code |
| :--- | :--- | :--- | :--- | :--- |
| `TC-01` | Happy Path | Standard valid invoice, KES, matching PO | `PROCESSED` | `NONE` |
| `TC-02` | Math Mismatch | Subtotal + Tax != Total | `FAILED_VALIDATION` | `BE-01` |
| `TC-03` | Re-Submitted Invoice | Invoice Number already processed in DB | `FAILED_VALIDATION` | `BE-02` |
| `TC-04` | Unregistered Vendor | Vendor name not in database | `FAILED_VALIDATION` | `BE-03` |
| `TC-05` | PO Amount Mismatch | Invoice Total != PO Total | `FAILED_VALIDATION` | `BE-04` |
| `TC-06` | Currency Mismatch | Invoice in USD, PO in KES | `FAILED_VALIDATION` | `BE-05` |
| `TC-07` | Intra-Batch Duplicate | 2 files in same folder with ID `INV-999` | First: `PROCESSED`, Second: `FAILED_VALIDATION` | `BE-06` |

## 4. Exit Criteria
- 100% of functional test cases executed.
- All non-happy path cases properly routed to `FAILED_VALIDATION` without crashing the bot.
- Execution results verified against SQL database logs.
