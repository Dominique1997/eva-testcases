import json
import pytest
from generator import Generator
from requests import get, post, put, patch, delete


generated_username = Generator.generate_username()
generated_password = Generator.generate_password()
generated_password_new = Generator.generate_password()
userID = 0

scheme = "http"
server_address = "localhost"
server_port = 9998


def check_api_status():
    api_response = get(f"{scheme}://{server_address}:{server_port}/api/status").json()
    api_status = api_response["api_state"]
    return api_status


def test_user_create():
    if not check_api_status():
        pytest.skip("API is not available")

    api_data = {"username": generated_username, "password": generated_password}
    api_reponse = post(f"{scheme}://{server_address}:{server_port}/api/user/create", data=json.dumps(api_data))
    assert api_reponse.json()["User creation"], api_reponse.content


def test_user_read():
    if not check_api_status():
        pytest.skip("API is not available")

    global userID
    api_data = {"username": generated_username, "password": generated_password}
    api_reponse = post(f"{scheme}://{server_address}:{server_port}/api/user/read", data=json.dumps(api_data))
    userID = api_reponse.json()["UserId"]
    assert userID != -1, api_reponse.content


def test_user_update():
    if not check_api_status():
        pytest.skip("API is not available")

    api_data = {"userID": str(userID), "username": generated_username, "password": generated_password_new}
    api_reponse = patch(f"{scheme}://{server_address}:{server_port}/api/user/update", data=json.dumps(api_data))
    assert api_reponse.json()["User update"] is True, api_reponse


def test_user_delete():
    if not check_api_status():
        pytest.skip("API is not available")

    global userID
    api_data = {"userID": str(userID), "username": generated_username, "password": generated_password_new}
    api_reponse = put(f"{scheme}://{server_address}:{server_port}/api/user/delete", data=json.dumps(api_data))
    assert api_reponse.json()["User delete"] is True, api_reponse.content
