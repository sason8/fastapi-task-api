def test_register_user(client):
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "securepassword123"}
    )
    assert response.status_code == 201
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data

def test_register_duplicate_user(client):
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "password"}
    )
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "password"}
    )
    assert response.status_code == 400
    assert response.json()["detail"] == "Email already registered"

def test_login_user(client):
    # Register first
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "securepassword"}
    )
    # Login
    response = client.post(
        "/auth/login",
        data={"username": "test@example.com", "password": "securepassword"}
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_invalid_credentials(client):
    response = client.post(
        "/auth/login",
        data={"username": "wrong@example.com", "password": "badpassword"}
    )
    assert response.status_code == 401

def test_get_tasks_unauthorized(client):
    response = client.get("/tasks/")
    assert response.status_code == 401

def test_create_and_read_tasks(client):
    # 1. Register and Login
    client.post(
        "/auth/register",
        json={"email": "user@example.com", "password": "password"}
    )
    login_resp = client.post(
        "/auth/login",
        data={"username": "user@example.com", "password": "password"}
    )
    token = login_resp.json()["access_token"]
    headers = {"Authorization": f"Bearer {token}"}

    # 2. Create Task
    task_payload = {"title": "Test Task", "description": "Verify testing pipeline", "is_completed": False}
    create_resp = client.post("/tasks/", json=task_payload, headers=headers)
    assert create_resp.status_code == 201
    created_task = create_resp.json()
    assert created_task["title"] == "Test Task"

    # 3. Read Tasks
    read_resp = client.get("/tasks/", headers=headers)
    assert read_resp.status_code == 200
    tasks_list = read_resp.json()
    assert len(tasks_list) == 1
    assert tasks_list[0]["id"] == created_task["id"]

def test_tasks_isolation(client):
    # Register and login user A
    client.post("/auth/register", json={"email": "a@example.com", "password": "pwd"})
    token_a = client.post("/auth/login", data={"username": "a@example.com", "password": "pwd"}).json()["access_token"]
    
    # Register and login user B
    client.post("/auth/register", json={"email": "b@example.com", "password": "pwd"})
    token_b = client.post("/auth/login", data={"username": "b@example.com", "password": "pwd"}).json()["access_token"]

    # User A creates a task
    client.post(
        "/tasks/",
        json={"title": "A's Task"},
        headers={"Authorization": f"Bearer {token_a}"}
    )

    # User B reads tasks (should be empty)
    resp_b = client.get("/tasks/", headers={"Authorization": f"Bearer {token_b}"})
    assert len(resp_b.json()) == 0
