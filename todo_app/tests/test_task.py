import pytest
from app import schemas


def test_get_all_task(authorized_client, test_task):
    res = authorized_client.get("/task/")

    def validate(task):
        return schemas.TaskOut(**task)
    task_map = map(validate, res.json())
    task_list = list(task_map)

    assert len(res.json()) == len(test_task)
    assert res.status_code == 200


def test_unauthorized_user_get_all_task(client, test_task):
    res = client.get("/task/")
    assert res.status_code == 401


def test_unauthorized_user_get_one_task(client, test_task):
    res = client.get(f"/task/{test_task[0].id}")
    assert res.status_code == 401


def test_get_one_task_not_exist(authorized_client, test_task):
    res = authorized_client.get(f"/task/88888")
    assert res.status_code == 404


def test_get_one_task(authorized_client, test_task):
    res = authorized_client.get(f"/task/{test_task[0].id}")
    task = schemas.TaskOut(**res.json())
    assert task.Task.content == test_task[0].content
    assert task.Task.title == test_task[0].title


@pytest.mark.parametrize("title, content, accomplished", [
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_create_task(authorized_client, test_user, test_task, title, content, accomplished):
    res = authorized_client.post(
        "/task/", json={"title": title, "content": content, "accomplished": accomplished})

    created_task = schemas.Task(**res.json())
    assert res.status_code == 201
    assert created_task.title == title
    assert created_task.content == content
    assert created_task.accomplished == accomplished
    assert created_task.owner_id == test_user['id']


def test_create_task_default_accomplished_true(authorized_client, test_user, test_task):
    res = authorized_client.post(
        "/task/", json={"title": "arbitrary title", "content": "aasdfjasdf"})

    created_task = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_task.title == "arbitrary title"
    assert created_task.content == "aasdfjasdf"
    assert created_task.accomplished == True
    assert created_task.owner_id == test_user['id']


def test_unauthorized_user_create_task(client, test_user, test_task):
    res = client.post(
        "/task/", json={"title": "arbitrary title", "content": "aasdfjasdf"})
    assert res.status_code == 401


def test_unauthorized_user_delete_task(client, test_user, test_task):
    res = client.delete(
        f"/task/{test_task[0].id}")
    assert res.status_code == 401


def test_delete_task_success(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/{test_task[0].id}")

    assert res.status_code == 204


def test_delete_task_non_exist(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/8000000")

    assert res.status_code == 404


def test_delete_other_user_task(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/{test_task[3].id}")
    assert res.status_code == 403


def test_update_task(authorized_client, test_user, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[0].id

    }
    res = authorized_client.put(f"/task/{test_task[0].id}", json=data)
    updated_task = schemas.task(**res.json())
    assert res.status_code == 200
    assert updated_task.title == data['title']
    assert updated_task.content == data['content']


def test_update_other_user_task(authorized_client, test_user, test_user2, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[3].id

    }
    res = authorized_client.put(f"/task/{test_task[3].id}", json=data)
    assert res.status_code == 403


def test_unauthorized_user_update_task(client, test_user, test_task):
    res = client.put(
        f"/task/{test_task[0].id}")
    assert res.status_code == 401


def test_update_task_non_exist(authorized_client, test_user, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[3].id

    }
    res = authorized_client.put(
        f"/task/8000000", json=data)

    assert res.status_code == 404
