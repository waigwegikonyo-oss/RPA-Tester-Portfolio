# Solution Design Document (SDD)
## Project: Automated Invoice Processing & Audit Validation System

### 1. Architecture Overview
- **Platform:** UiPath Studio Web
- **Pattern:** Linear Sequence wrapped inside a master `Try-Catch` block for global exception handling.
- **Integration Points:** OneDrive Integration (Input Invoices) and File System/Excel Automation (Audit Log Output).

### 2. Variable & Data Structure
| Variable Name | Type | Direction | Description |
| :--- | :--- | :--- | :--- |
| `in_OneDriveFolder` | String | Input | Target cloud path containing incoming invoice PDFs |
| `out_SummaryReportPath` | String | Output | Local path where execution CSV/Excel log is saved |
| `dt_InvoiceAudit` | DataTable | Internal | In-memory table storing execution state per invoice |
| `dt_VendorMaster` | DataTable | Internal | Reference lookup table for active vendors |
| `dt_POMaster` | DataTable | Internal | Reference lookup table for Purchase Orders |

### 3. Workflow Execution Phases
1. **Initialization:** Instantiate `dt_InvoiceAudit` with schema and load vendor/PO master data fixtures.
2. **Transaction Ingestion:** Query target OneDrive directory for unprocessed PDF files.
3. **Data Extraction & Business Validation:** Run extraction and evaluate business rules `BR-01` through `BR-04`.
4. **Exception Handling:** Route business exceptions to `FAILED_VALIDATION` state and system exceptions to `SYSTEM_ERROR`.
5. **Output Reporting & Cleanup:** Append execution summary to target CSV/Excel audit log file.
