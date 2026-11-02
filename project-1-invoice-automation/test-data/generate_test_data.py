import os, csv, json

BASE = os.path.dirname(os.path.abspath(__file__))
INV_DIR = os.path.join(BASE, "mock-invoices")
CASES_DIR = os.path.join(BASE, "..", "test-cases")
os.makedirs(INV_DIR, exist_ok=True)

VENDORS = [
    {"vendor_name": "Acme Logistics Ltd", "is_active": True},
    {"vendor_name": "Global Tech Supplies", "is_active": True},
    {"vendor_name": "Apex Stationers", "is_active": True},
]
PURCHASE_ORDERS = [
    {"po_number": "PO-2024-001", "currency": "KES", "total_amount": 1250.00},
    {"po_number": "PO-2024-002", "currency": "KES", "total_amount": 4300.50},
    {"po_number": "PO-2024-003", "currency": "KES", "total_amount": 680.00},
]
HISTORY = ["INV-2026-003"]  # already PROCESSED in an earlier run

def inv(tc, scenario, file_name, number, vendor, po, cur, sub, tax, tot, status, err):
    return {"tc_id": tc, "scenario": scenario, "file_name": file_name,
            "invoice_number": number, "vendor_name": vendor, "po_number": po,
            "currency": cur, "subtotal": sub, "tax": tax, "total": tot,
            "expected_status": status, "expected_error": err}

CASES = [
 inv("TC-01","Happy Path","INV_001_HappyPath.json","INV-2026-001","Acme Logistics Ltd","PO-2024-001","KES",1000.00,250.00,1250.00,"PROCESSED","NONE"),
 inv("TC-02","Math Mismatch","INV_002_MathError.json","INV-2026-002","Acme Logistics Ltd","PO-2024-001","KES",1000.00,100.00,1250.00,"FAILED_VALIDATION","BE-01"),
 inv("TC-03","Re-Submitted Invoice","INV_003_ReSubmitted.json","INV-2026-003","Acme Logistics Ltd","PO-2024-001","KES",1000.00,250.00,1250.00,"FAILED_VALIDATION","BE-02"),
 inv("TC-04","Unregistered Vendor","INV_004_UnknownVendor.json","INV-2026-004","Unknown Global Ltd","PO-2024-001","KES",1000.00,250.00,1250.00,"FAILED_VALIDATION","BE-03"),
 inv("TC-05","PO Amount Mismatch","INV_005_POMismatch.json","INV-2026-005","Acme Logistics Ltd","PO-2024-001","KES",2000.00,500.00,2500.00,"FAILED_VALIDATION","BE-04"),
 inv("TC-06","Currency Mismatch","INV_006_CurrencyMismatch.json","INV-2026-006","Global Tech Supplies","PO-2024-002","USD",4000.00,300.50,4300.50,"FAILED_VALIDATION","BE-05"),
 inv("TC-07A","Batch Duplicate (first file)","INV_007A_BatchDup.json","INV-2026-007","Apex Stationers","PO-2024-003","KES",600.00,80.00,680.00,"PROCESSED","NONE"),
 inv("TC-07B","Batch Duplicate (second file)","INV_007B_BatchDup.json","INV-2026-007","Apex Stationers","PO-2024-003","KES",600.00,80.00,680.00,"FAILED_VALIDATION","BE-06"),
]

INVOICE_FIELDS = ["file_name","invoice_number","vendor_name","po_number","currency","subtotal","tax","total"]

def main():
    invoices = []
    for c in CASES:
        invoice = {k: c[k] for k in INVOICE_FIELDS}
        invoices.append(invoice)
        with open(os.path.join(INV_DIR, c["file_name"]), "w") as f:
            json.dump(invoice, f, indent=4)

    with open(os.path.join(BASE, "Expected_Results.json"), "w") as f:
        json.dump([{k: c[k] for k in ("tc_id","scenario","file_name","invoice_number","expected_status","expected_error")} for c in CASES], f, indent=4)

    # Paste this file's contents into Studio Web as the workflow input
    with open(os.path.join(BASE, "workflow_input.json"), "w") as f:
        json.dump({"invoices": invoices, "vendors": VENDORS,
                   "purchase_orders": PURCHASE_ORDERS, "history": HISTORY}, f, indent=2)

    with open(os.path.join(CASES_DIR, "Functional_Test_Matrix.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Test_ID","Scenario","Invoice_Number","Vendor","PO_Number","Currency","Subtotal","Tax","Total","Expected_Status","Expected_Error"])
        for c in CASES:
            w.writerow([c["tc_id"],c["scenario"],c["invoice_number"],c["vendor_name"],c["po_number"],c["currency"],c["subtotal"],c["tax"],c["total"],c["expected_status"],c["expected_error"]])
    print(f"Generated {len(CASES)} invoices, expected results, matrix and workflow_input.json")

if __name__ == "__main__":
    main()
