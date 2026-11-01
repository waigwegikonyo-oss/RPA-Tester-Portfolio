# Process Definition Document (PDD)
## Project: Automated Invoice Processing & Audit Validation System

### 1. Process Overview
Automate the ingestion, OCR data extraction, rule validation, cross-currency & PO database verification, and audit logging of incoming multi-vendor invoices.

### 2. Business Rules & Rules Engine
- **BR-01 (Math Integrity):** `Subtotal + Tax Amount == Total Amount`.
- **BR-02 (Uniqueness):** `Invoice Number` must not exist in `invoice_audit_log` with state `PROCESSED`.
- **BR-03 (Vendor Check):** `Vendor Name` must match an active record in `vendors` table.
- **BR-04 (PO Match):** Extracted `Total Amount` must match the corresponding `purchase_orders` record.
- **BR-05 (Currency Alignment):** Extracted invoice currency code (`USD`, `EUR`, `KES`) must match the PO target currency.
- **BR-06 (Batch Uniqueness):** No two files within the same ingestion execution queue may share the same `Invoice Number`.

### 3. Exception Handling Taxonomy
- **Business Exceptions:**
  - `BE-01`: Math mismatch (`Subtotal + Tax != Total`).
  - `BE-02`: Duplicate invoice previously processed.
  - `BE-03`: Unregistered or inactive vendor.
  - `BE-04`: Purchase order amount mismatch.
  - `BE-05`: Currency mismatch between Invoice and PO.
  - `BE-06`: Intra-batch duplicate invoice ID detected.
- **System Exceptions:**
  - `SE-01`: PDF file corrupted or unreadable OCR text.
  - `SE-02`: Database connection loss/timeout.
