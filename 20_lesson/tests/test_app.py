import re
import pytest

from fastapi import status
from conftest import async_session_maker

from sqlalchemy import select
from app.user_models import User


async def test_user_registration_success(async_client, get_user_by_field):
    payload = {
        "email": "test@example.com",
        "password": "password123",
    }
    response = await async_client.post("/auth/register", json=payload)
    assert response.status_code == status.HTTP_201_CREATED, f"Registration failed: {response.text}"
    
    user = await get_user_by_field("email", payload["email"])
    assert user, "User not found"


async def test_user_registration_wrong_email(async_client):
    payload = {
        "email": "test",
        "password": "password123",
    }
    response = await async_client.post("/auth/register", json=payload)
    assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY, f"Registration failed: {response.text}"


async def test_user_registration_wrong_password(async_client):
    payload = {
        "email": "test@example.com",
        "password": "p",
    }
    response = await async_client.post("/auth/register", json=payload)
    assert response.status_code == status.HTTP_400_BAD_REQUEST, f"Registration failed: {response.text}"


async def test_login(async_client, token_storage):
    login_response = await async_client.post(
        "/auth/jwt/login",
        data={"username": "test@example.com", "password": "password123"}
    )
    assert login_response.status_code == status.HTTP_200_OK, "Login failed: " + login_response.text
    token = login_response.json().get("access_token")
    assert token is not None
    token_storage["token"] = token


async def test_get_user(async_client, get_token):
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    get_user_response = await async_client.get("users/me", headers=headers)
    assert get_user_response.status_code == status.HTTP_200_OK, "Get user failed: " + get_user_response.text


async def test_change_user_data(async_client, get_token, get_user_by_field):
    email = "test@example.com"
    new_password = "newpass123"
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    change_user_response = await async_client.patch("users/me", headers=headers, json={"password": new_password})

    assert change_user_response.status_code == status.HTTP_200_OK, "Change user failed: " + change_user_response.text

    async with async_session_maker() as session:
        async with session.begin():
            result = await session.execute(select(User).filter_by(email=email))
            user = result.scalar_one_or_none()
            assert user, "User not found"

            user.is_superuser = True
        
        await session.commit()
        
        user = await get_user_by_field("email", email)
        assert user.is_superuser, "User was not set as superuser"


async def test_registration_another_user(async_client, user_id_storage, get_user_by_field):
    registration_response = await async_client.post("/auth/register", json={
        "email": "fastapi@example.com",
        "password": "password123",
    })
    assert registration_response.status_code == status.HTTP_201_CREATED, "Registration failed: " + registration_response.text
    user_id = registration_response.json().get("id")

    assert user_id is not None
    user_id_storage["id"] = user_id

    user = await get_user_by_field("email", "fastapi@example.com")
    assert user, "Another user was not created in the database"


async def test_get_another_user_data(async_client, get_token, get_user_id):
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    get_user_response = await async_client.get(f"users/{get_user_id}", headers=headers)
    assert get_user_response.status_code == status.HTTP_200_OK, "Get user failed: " + get_user_response.text


async def test_change_another_user_data(async_client, get_token, get_user_id, get_user_by_field):
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    change_user_response = await async_client.patch(f"users/{get_user_id}", headers=headers, json={"is_superuser": "true"})

    assert change_user_response.status_code == status.HTTP_200_OK, "Change user failed: " + change_user_response.text

    user = await get_user_by_field("id", get_user_id)
    assert user.is_superuser, "User was not set as superuser"


async def test_delete_another_user_data(async_client, get_token, get_user_id, get_user_by_field):
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    delete_user_response = await async_client.delete(f"users/{get_user_id}", headers=headers)

    assert delete_user_response.status_code == status.HTTP_204_NO_CONTENT, "Delete user failed: " + delete_user_response.text
    user = await get_user_by_field("id", get_user_id)

    assert not user, "User was not deleted from the database"


async def test_upload_file(async_client, get_token):
    with open('src/python.png', 'rb') as f:
        files = {'file': ('python.png', f, 'image/png')}
        data = {'resize': '500x500'}
        
        headers = {"Authorization": f"Bearer {get_token}"}
        image_upload_response = await async_client.post("/files/upload/", files=files, data=data, headers=headers)

    assert image_upload_response.status_code == status.HTTP_200_OK, "Upload file failed: " + image_upload_response.text


async def test_logout(async_client, get_token):
    headers = {"Authorization": f"Bearer {get_token}", "Content-Type": "application/json"}
    logout_response = await async_client.post("/auth/jwt/logout", headers=headers)
    assert logout_response.status_code == status.HTTP_204_NO_CONTENT, "Logout failed: " + logout_response.text
