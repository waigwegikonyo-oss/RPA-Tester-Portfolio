# Process Definition Document (PDD)
## Project: Automated Invoice Processing & Audit Validation System

### 1. Process Overview
Automate the ingestion, data extraction, rule validation, database cross-checking, and audit logging of incoming vendor invoices.

### 2. Business Rules & Rules Engine
- **BR-01 (Math Integrity):** `Subtotal + Tax Amount == Total Amount`.
- **BR-02 (Uniqueness):** `Invoice Number` must not exist in `processed_invoices` audit table.
- **BR-03 (Vendor Check):** `Vendor Name` must match an active record in `vendors` table.
- **BR-04 (PO Match):** Extracted `Total Amount` must match the corresponding `purchase_orders` record within a 0.00 tolerance.

### 3. Exception Handling Taxonomy
- **Business Exceptions:**
  - `BE-01`: Math mismatch (`Subtotal + Tax != Total`).
  - `BE-02`: Duplicate invoice detected.
  - `BE-03`: Unregistered vendor.
  - `BE-04`: Purchase order amount mismatch.
- **System Exceptions:**
  - `SE-01`: PDF file corrupted or unreadable OCR text.
  - `SE-02`: Database connection loss/timeout.
