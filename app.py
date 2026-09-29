import requests

# DO NOT DO THIS -- hardcoded secret, for demonstration only
API_KEY = "sk_live_51Hc8sJ2eZvKYlo2C9x7QW8pR3T9dGdemoFAKE"

def charge(amount_cents: int):
    return requests.post(
        "https://api.example-payments.test/v1/charges",
        headers={"Authorization": f"Bearer {API_KEY}"},
        json={"amount": amount_cents, "currency": "usd"},
        timeout=5,
    )