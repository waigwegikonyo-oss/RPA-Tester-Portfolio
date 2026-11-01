-- Vendor Master Table
CREATE TABLE vendors (
    vendor_id VARCHAR(20) PRIMARY KEY,
    vendor_name VARCHAR(100) NOT NULL,
    country VARCHAR(50) DEFAULT 'Kenya',
    is_active BOOLEAN DEFAULT TRUE
);

-- Purchase Orders Table
CREATE TABLE purchase_orders (
    po_number VARCHAR(20) PRIMARY KEY,
    vendor_id VARCHAR(20) REFERENCES vendors(vendor_id),
    currency VARCHAR(3) DEFAULT 'KES',
    total_amount DECIMAL(10, 2) NOT NULL,
    status VARCHAR(20) DEFAULT 'OPEN'
);

-- Invoice Audit Log Table
CREATE TABLE invoice_audit_log (
    audit_id SERIAL PRIMARY KEY,
    invoice_number VARCHAR(50),
    vendor_name VARCHAR(100),
    currency VARCHAR(3),
    invoice_total DECIMAL(10, 2),
    processing_status VARCHAR(30),
    error_code VARCHAR(10),
    processed_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
