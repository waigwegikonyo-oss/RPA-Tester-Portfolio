-- Seed Active Vendors
INSERT INTO vendors (vendor_id, vendor_name, is_active) VALUES
('VEND-101', 'Acme Logistics Ltd', TRUE),
('VEND-102', 'Global Tech Supplies', TRUE),
('VEND-103', 'Apex Stationers', TRUE);

-- Seed Purchase Orders (Ground Truth for Validation)
INSERT INTO purchase_orders (po_number, vendor_id, total_amount, status) VALUES
('PO-2024-001', 'VEND-101', 1250.00, 'OPEN'),
('PO-2024-002', 'VEND-102', 4300.50, 'OPEN'),
('PO-2024-003', 'VEND-103', 680.00, 'OPEN');
