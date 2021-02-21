import mercadopago
import json

mp = mercadopago.MP("TEST-4756010857771638-021907-ba0c2dc608c738d07ed034b1dcadbf03-292499614")


def buy(name, price, cant, id):
    preference = {
        "items": [{"title": name, "quantity": cant, "currency_id": "ARS", "unit_price": price}],
        "back_urls": {
            "success": "http://127.0.0.1:8000/api/payment/success",
        },
        "external_reference": id,
    }
    url = mp.create_preference(preference)

    return url
