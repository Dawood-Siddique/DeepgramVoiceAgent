from apps.customer.models import CustomerModel


def handle_payment_confirmed(customer_id):
    try:
        customer = CustomerModel.objects.get(id=customer_id)
        customer.status = 'Paid'
        customer.save()
        return {
            "data_save": True,
            "message": "Payment Confirmed"
        }
    except CustomerModel.DoesNotExist:
        return {
            "data_save": False,
            "message": "Customer not found"
        }


def handle_extension_required(customer_id, extension_time: str):
    try:
        customer = CustomerModel.objects.get(id=customer_id)
        customer.status = 'Extended'
        customer.dueDate = extension_time
        customer.save()
        return {
            "data_save": True,
            "message": "Extension Required"
        }
    except CustomerModel.DoesNotExist:
        return {
            "data_save": False,
            "message": "Customer not found"
        }

def handle_payment_commitment(customer_id, commitment_time: str):
    try:
        customer = CustomerModel.objects.get(id=customer_id)
        customer.status = 'Active'
        customer.dueDate = commitment_time
        customer.save()
        return {
            "data_save": True,
            "message": "Payment Commitment"
        }
    except CustomerModel.DoesNotExist:
        return {
            "data_save": False,
            "message": "Customer not found"
        }
        
        
FUNCTION_MAP = {
    "handle_extension_required": handle_extension_required,
    "handle_payment_confirmed": handle_payment_confirmed,
    "handle_payment_commitment": handle_payment_commitment
}
