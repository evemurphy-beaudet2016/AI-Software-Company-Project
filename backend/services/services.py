# Business logic

from database import get_connection
from fastapi import HTTPException

# PROJECT FUNCTIONALITIES
def save_project(project_name, requirements):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        # ID automatically gets allocated
        """
        INSERT INTO projects (idea, requirements)
        VALUES (%s, %s)
        """,
        (project_name, requirements)
    )

    conn.commit()
    cur.close()
    conn.close()

    print(f"Saving project: {project_name}")

def get_projects():
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, idea, requirements
        FROM projects
        """
    )

    projects = cur.fetchall()

    cur.close()
    conn.close()

    if projects is None:
        raise HTTPException(status_code=404, detail="Projects not found")

    return [
        {
            "id":p[0],
            "name":p[1],
            "requirements":p[2]
        }
        for p in projects
    ]

def get_project(project_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, idea, requirements
        FROM projects
        WHERE id = %s
        """,
        (project_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Project not found")


    return {
        "id":row[0],
        "name":row[1],
        "requirements":row[2]
    }

def update_project(project_id, project_name, requirements):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE projects
        SET idea = %s, requirements = %s
        WHERE id = %s
        """,
        (project_name, requirements, project_id)
    )

    conn.commit()

    cur.close()
    conn.close()

def delete_project(project_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM projects
        WHERE id = %s
        """,
        (project_id,)
    )

    conn.commit()
    cur.close()
    conn.close()



# TASK FUNCTIONALITIES
def save_task(project_id, title, description, status):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        # ID automatically gets allocated
        """
        INSERT INTO tasks (project_id, title, description, status)
        VALUES (%s, %s, %s, %s)
        WHERE id = project_id
        """,
        (project_id, title, description, status)
    )

    conn.commit()
    cur.close()
    conn.close()

    print(f"Saving project: {title}")

def get_tasks(project_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, title, description, status
        FROM tasks
        WHERE project_id = %s
        """,
        (project_id,)
    )

    tasks = cur.fetchall()

    cur.close()
    conn.close()

    if tasks is None:
        raise HTTPException(status_code=404, detail="Tasks not found")

    return [
        {
            "id":t[0],
            "title":t[1],
            "description":t[2],
            "status":t[3]
        }
        for t in tasks
    ]

def get_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        SELECT id, title, description, status
        FROM tasks
        WHERE id = %s
        """,
        (task_id,)
    )

    row = cur.fetchone()

    cur.close()
    conn.close()

    if row is None:
        raise HTTPException(status_code=404, detail="Task not found")


    return {
        "id":row[0],
        "title":row[1],
        "description":row[2],
        "status":row[3]
    }

def update_task(task_id, title, description, status):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        UPDATE tasks
        SET title = %s, description = %s, status = %s
        WHERE id = %s
        """,
        (title, description, status, task_id)
    )

    conn.commit()

    cur.close()
    conn.close()

def delete_task(task_id):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute(
        """
        DELETE FROM tasks
        WHERE id = %s
        """,
        (task_id,)
    )

    conn.commit()
    cur.close()
    conn.close()
