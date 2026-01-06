import random
from utils.ids import gid
from utils.time import random_past_datetime

PROJECT_TYPES = [
    "Sprint",
    "Roadmap",
    "Marketing Campaign",
    "Operations",
    "Bug Tracking",
    "Ongoing"
]

STATUSES = ["active", "completed", "archived"]

def generate_projects(conn, org_id, team_ids, n_projects=300):
    project_ids = []

    for _ in range(n_projects):
        project_id = gid()
        team_id = random.choice(team_ids) if random.random() > 0.15 else None
        project_type = random.choice(PROJECT_TYPES)
        status = random.choices(
            STATUSES, weights=[0.6, 0.25, 0.15]
        )[0]

        name = f"{project_type} - {random.randint(2024, 2026)} Initiative"

        conn.execute(
            "INSERT INTO projects VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (
                project_id,
                org_id,
                team_id,
                name,
                project_type,
                status,
                None,
                None,
                random_past_datetime(2, 0),
            ),
        )

        project_ids.append((project_id, project_type))

    return project_ids
