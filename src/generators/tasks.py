import random
from utils.ids import gid
from utils.time import random_past_datetime, after

ENGINEERING_TASKS = [
    "Refactor authentication flow",
    "Optimize database queries",
    "Fix payment webhook bug",
    "Improve API error handling",
    "Add caching layer"
]

MARKETING_TASKS = [
    "Prepare campaign landing page",
    "Design ad creatives",
    "Launch email campaign",
    "Analyze campaign performance"
]

def generate_tasks(conn, project_id, section_ids, user_ids, project_type, n_tasks=120):
    task_ids = []

    for _ in range(n_tasks):
        task_id = gid()
        created_at = random_past_datetime(1, 0)
        completed = random.random() < 0.6
        completed_at = after(created_at, 1, 14) if completed else None

        name_pool = ENGINEERING_TASKS if project_type in ["Sprint", "Bug Tracking"] else MARKETING_TASKS
        name = random.choice(name_pool)

        assignee = random.choice(user_ids) if random.random() > 0.15 else None
        section = random.choice(section_ids) if random.random() > 0.1 else None

        conn.execute(
            "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                task_id,
                project_id,
                section,
                None,
                assignee,
                name,
                None,
                None,
                completed,
                created_at,
                completed_at
            )
        )

        task_ids.append(task_id)

        # SUBTASKS (30%)
        if random.random() < 0.3:
            for _ in range(random.randint(1, 3)):
                sub_id = gid()
                conn.execute(
                    "INSERT INTO tasks VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                    (
                        sub_id,
                        project_id,
                        section,
                        task_id,
                        assignee,
                        f"Subtask: {name}",
                        None,
                        None,
                        completed,
                        created_at,
                        completed_at
                    )
                )

    return task_ids
