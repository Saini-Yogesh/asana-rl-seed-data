from utils.ids import gid
from utils.time import random_past_datetime

TEAM_NAMES = [
    "Core Platform Engineering",
    "Mobile Engineering",
    "Growth Marketing",
    "Product Operations",
    "Customer Support",
    "Data & ML",
    "Sales Operations"
]

def generate_teams(conn, org_id):
    team_ids = []
    for name in TEAM_NAMES:
        team_id = gid()
        conn.execute(
            "INSERT INTO teams VALUES (?, ?, ?, ?)",
            (team_id, org_id, name, random_past_datetime(6, 1))
        )
        team_ids.append(team_id)
    return team_ids
