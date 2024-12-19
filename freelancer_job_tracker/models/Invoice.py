class Invoice:
    def __init__(self, id, project_id, amount, status, issued_at, paid_at):
        self.id = id
        self.project_id = project_id
        self.amount = amount
        self.status = status
        self.issued_at = issued_at
        self.paid_at = paid_at

    def make_invoice_dict(self):
        return {
            "id": self.id,
            "project_id": self.project_id,
            "amount": self.amount,
            "status": self.status,
            "issued_at": self.issued_at,
            "paid_at": self.paid_at
        }