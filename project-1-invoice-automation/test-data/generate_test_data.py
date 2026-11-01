import os
import csv
import json

# Define output directory
OUTPUT_DIR = os.path.dirname(os.path.abspath(__file__))
INVOICES_DIR = os.path.join(OUTPUT_DIR, "mock-invoices")
os.makedirs(INVOICES_DIR, exist_ok=True)

# Test Data Matrix corresponding to TC-01 through TC-07
TEST_CASES = [
    {
        "tc_id": "TC-01",
        "file_name": "INV_2026_001_HappyPath.json",
        "invoice_number": "INV-2026-001",
        "vendor_name": "Acme Logistics Ltd",
        "po_number": "PO-2024-001",
        "currency": "KES",
        "subtotal": 1000.00,
        "tax": 250.00,
        "total": 1250.00,
        "expected_status": "PROCESSED",
        "expected_error": "NONE"
    },
    {
        "tc_id": "TC-02",
        "file_name": "INV_2026_002_MathError.json",
        "invoice_number": "INV-2026-002",
        "vendor_name": "Acme Logistics Ltd",
        "po_number": "PO-2024-001",
        "currency": "KES",
        "subtotal": 1000.00,
        "tax": 100.00,  # 1000 + 100 != 1250
        "total": 1250.00,
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-01"
    },
    {
        "tc_id": "TC-03",
        "file_name": "INV_2026_003_ReSubmitted.json",
        "invoice_number": "INV-2026-001",  # Same as TC-01
        "vendor_name": "Acme Logistics Ltd",
        "po_number": "PO-2024-001",
        "currency": "KES",
        "subtotal": 1000.00,
        "tax": 250.00,
        "total": 1250.00,
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-02"
    },
    {
        "tc_id": "TC-04",
        "file_name": "INV_2026_004_UnknownVendor.json",
        "invoice_number": "INV-2026-004",
        "vendor_name": "Unknown Global Ltd",
        "po_number": "PO-2024-001",
        "currency": "KES",
        "subtotal": 1000.00,
        "tax": 250.00,
        "total": 1250.00,
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-03"
    },
    {
        "tc_id": "TC-05",
        "file_name": "INV_2026_005_POMismatch.json",
        "invoice_number": "INV-2026-005",
        "vendor_name": "Acme Logistics Ltd",
        "po_number": "PO-2024-001",
        "currency": "KES",
        "subtotal": 2000.00,
        "tax": 500.00,
        "total": 2500.00,  # PO is 1250.00
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-04"
    },
    {
        "tc_id": "TC-06",
        "file_name": "INV_2026_006_CurrencyMismatch.json",
        "invoice_number": "INV-2026-006",
        "vendor_name": "Global Tech Supplies",
        "po_number": "PO-2024-002",
        "currency": "USD",  # PO is in KES
        "subtotal": 4000.00,
        "tax": 300.50,
        "total": 4300.50,
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-05"
    },
    {
        "tc_id": "TC-07",
        "file_name": "INV_2026_007_BatchDuplicate.json",
        "invoice_number": "INV-2026-007",
        "vendor_name": "Apex Stationers",
        "po_number": "PO-2024-003",
        "currency": "KES",
        "subtotal": 600.00,
        "tax": 80.00,
        "total": 680.00,
        "expected_status": "FAILED_VALIDATION",
        "expected_error": "BE-06"
    }
]

def generate_fixtures():
    # 1. Write JSON files for each invoice
    for tc in TEST_CASES:
        filepath = os.path.join(INVOICES_DIR, tc["file_name"])
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(tc, f, indent=4)
    print(f"Successfully generated {len(TEST_CASES)} mock invoice JSON fixtures in {INVOICES_DIR}")

    # 2. Write master Expected_Results.json
    expected_path = os.path.join(OUTPUT_DIR, "Expected_Results.json")
    with open(expected_path, "w", encoding="utf-8") as f:
        json.dump(TEST_CASES, f, indent=4)
    print(f"Successfully created expected baseline manifest at {expected_path}")

if __name__ == "__main__":
    generate_fixtures()
