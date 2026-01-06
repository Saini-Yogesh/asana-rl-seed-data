import random
from faker import Faker
from utils.ids import gid
from utils.time import random_past_datetime

fake = Faker()

ROLES = ["admin", "member", "guest"]
ROLE_WEIGHTS = [0.05, 0.85, 0.10]

TITLES = [
    "Software Engineer", "Senior Software Engineer",
    "Product Manager", "Designer",
    "Marketing Manager", "Data Scientist"
]

def generate_users(conn, org_id, n_users):
    """
    Generates users for the organization.
    - Realistic names via Faker
    - Role distribution: admin / member / guest
    """
    user_ids = []
    for _ in range(n_users):
        user_id = gid()
        name = fake.name()
        email = name.lower().replace(" ", ".") + "@acmecloud.com"
        role = random.choices(ROLES, ROLE_WEIGHTS)[0]
        title = random.choice(TITLES)
        is_active = random.random() < 0.95

        conn.execute(
            "INSERT INTO users VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
            (user_id, org_id, name, email, role, title, is_active,
             random_past_datetime(6, 0))
        )
        user_ids.append(user_id)
    return user_ids
