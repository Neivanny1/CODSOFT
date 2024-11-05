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


@pytest.mark.parametrize("title, content, published", [
    ("awesome new title", "awesome new content", True),
    ("favorite pizza", "i love pepperoni", False),
    ("tallest skyscrapers", "wahoo", True),
])
def test_create_post(authorized_client, test_user, test_task, title, content, published):
    res = authorized_client.post(
        "/task/", json={"title": title, "content": content, "published": published})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == title
    assert created_post.content == content
    assert created_post.published == published
    assert created_post.owner_id == test_user['id']


def test_create_post_default_published_true(authorized_client, test_user, test_task):
    res = authorized_client.post(
        "/task/", json={"title": "arbitrary title", "content": "aasdfjasdf"})

    created_post = schemas.Post(**res.json())
    assert res.status_code == 201
    assert created_post.title == "arbitrary title"
    assert created_post.content == "aasdfjasdf"
    assert created_post.published == True
    assert created_post.owner_id == test_user['id']


def test_unauthorized_user_create_post(client, test_user, test_task):
    res = client.post(
        "/task/", json={"title": "arbitrary title", "content": "aasdfjasdf"})
    assert res.status_code == 401


def test_unauthorized_user_delete_Post(client, test_user, test_task):
    res = client.delete(
        f"/task/{test_task[0].id}")
    assert res.status_code == 401


def test_delete_post_success(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/{test_task[0].id}")

    assert res.status_code == 204


def test_delete_post_non_exist(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/8000000")

    assert res.status_code == 404


def test_delete_other_user_post(authorized_client, test_user, test_task):
    res = authorized_client.delete(
        f"/task/{test_task[3].id}")
    assert res.status_code == 403


def test_update_post(authorized_client, test_user, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[0].id

    }
    res = authorized_client.put(f"/task/{test_task[0].id}", json=data)
    updated_post = schemas.Post(**res.json())
    assert res.status_code == 200
    assert updated_post.title == data['title']
    assert updated_post.content == data['content']


def test_update_other_user_post(authorized_client, test_user, test_user2, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[3].id

    }
    res = authorized_client.put(f"/task/{test_task[3].id}", json=data)
    assert res.status_code == 403


def test_unauthorized_user_update_post(client, test_user, test_task):
    res = client.put(
        f"/task/{test_task[0].id}")
    assert res.status_code == 401


def test_update_post_non_exist(authorized_client, test_user, test_task):
    data = {
        "title": "updated title",
        "content": "updatd content",
        "id": test_task[3].id

    }
    res = authorized_client.put(
        f"/task/8000000", json=data)

    assert res.status_code == 404
