import random
from utils.time import random_past_datetime

def generate_team_memberships(conn, user_ids, team_ids):
    for user_id in user_ids:
        k = random.choices([1, 2, 3], [0.7, 0.25, 0.05])[0]
        for team_id in random.sample(team_ids, k):
            conn.execute(
                "INSERT OR IGNORE INTO team_memberships VALUES (?, ?, ?)",
                (team_id, user_id, random_past_datetime(5, 0))
            )
