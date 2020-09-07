import pytest
from django.urls import reverse

from pypro.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


def test_status_code(resp):
    resp.status_code == 200


def test_title(resp):
    assert_contains(resp, '<title>Curso Django Pro</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Python Pró</a>')
