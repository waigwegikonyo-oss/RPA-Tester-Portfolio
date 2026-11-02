INSERT INTO vendors (vendor_id, vendor_name, country, is_active) VALUES
('VEND-101', 'Acme Logistics Ltd', 'Kenya', TRUE),
('VEND-102', 'Global Tech Supplies', 'Kenya', TRUE),
('VEND-103', 'Apex Stationers', 'Kenya', TRUE);

INSERT INTO purchase_orders (po_number, vendor_id, currency, total_amount, status) VALUES
('PO-2024-001', 'VEND-101', 'KES', 1250.00, 'OPEN'),
('PO-2024-002', 'VEND-102', 'KES', 4300.50, 'OPEN'),
('PO-2024-003', 'VEND-103', 'KES', 680.00, 'OPEN');
