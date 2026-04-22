-- Creates a trigger that decreases the quantity of an item after adding a new order.
CREATE TRIGGER decrease_quantity
AFTER INSERT ON items
FOR EACH ROW
UPDATE items
SET quantity = quantity - NEW.number
WHERE name = NEW.item_name