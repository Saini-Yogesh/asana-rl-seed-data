from utils.ids import gid
from utils.time import random_past_datetime

def generate_organization(conn):
    org_id = gid()
    conn.execute(
        "INSERT INTO organizations VALUES (?, ?, ?, ?)",
        (org_id, "AcmeCloud", "acmecloud.com", random_past_datetime(8, 6))
    )
    return org_id
