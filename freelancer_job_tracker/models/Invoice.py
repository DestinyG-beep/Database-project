from datetime import datetime

class Invoice:
    VALID_STATUSES = ["unpaid", "paid"]
    def __init__(self, id, project_id, amount, status="unpaid", issued_at=None, paid_at=None):
        self.id = id
        self.project_id = project_id
        self.amount = amount
        self.status = status
        self.issued_at = issued_at or datetime.now()
        self.paid_at = paid_at

    def make_invoice_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "amount": self.amount,
            "status": self.status,
            "issued_at": self.issued_at,
            "paid_at": self.paid_at,
        }
    
    def payment_status(self):
        return self.status == "paid" and self.paid_at is not None
    
    def marking_payment(self):
        if self.status == "paid":
            print("already paid👍👍")
    
        else:
            self.status = "paid"
            self.paid_at = datetime.now()
            
    @staticmethod
    def create_invoice(project_id, amount):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO invoices (project_id, amount) VALUES (?, ?)", (project_id, amount))
        conn.commit()
        invoice_id = cursor.lastrowid
        conn.close()
        return Invoice(invoice_id, project_id, amount)
    
    @staticmethod
    def delete_invoice(invoice_id):
        conn = create_connection()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM invoices WHERE id = ?", (invoice_id,))
        conn.commit()
        deleted_rows = cursor.rowcount
        conn.close()
        return deleted_rows > 0