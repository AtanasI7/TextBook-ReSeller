from django.urls import reverse
from rest_framework.test import APIClient


def test_schema_contains_health_endpoint():
    client = APIClient()

    response = client.get(reverse("schema"), {"format": "json"})

    assert response.status_code == 200
    assert "/api/health/" in response.json()["paths"]


def test_docs_page_opens():
    client = APIClient()

    response = client.get(reverse("docs"))

    assert response.status_code == 200
