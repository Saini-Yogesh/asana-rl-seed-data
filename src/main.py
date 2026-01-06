from utils.db import get_connection
from config.settings import DATABASE_PATH, N_USERS, N_PROJECTS

from generators.organizations import generate_organization
from generators.teams import generate_teams
from generators.users import generate_users
from generators.team_memberships import generate_team_memberships
from generators.projects import generate_projects
from generators.sections import generate_sections
from generators.tasks import generate_tasks


def main():
    print("Starting Asana seed data generation...")
    print("Note: Running the script multiple times will regenerate the database from scratch.")

    conn = get_connection(DATABASE_PATH)

    with open("schema.sql") as f:
        conn.executescript(f.read())

    org_id = generate_organization(conn)
    team_ids = generate_teams(conn, org_id)
    user_ids = generate_users(conn, org_id, N_USERS)
    generate_team_memberships(conn, user_ids, team_ids)

    projects = generate_projects(conn, org_id, team_ids, N_PROJECTS)

    for project_id, project_type in projects:
        section_ids = generate_sections(conn, project_id, project_type)
        generate_tasks(conn, project_id, section_ids, user_ids, project_type)

    conn.commit()
    conn.close()
    print("Asana seed data generation completed.")


if __name__ == "__main__":
    main()
