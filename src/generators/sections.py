from utils.ids import gid

SECTION_TEMPLATES = {
    "Sprint": ["Backlog", "To Do", "In Progress", "Review", "Done"],
    "Bug Tracking": ["Reported", "Triaged", "Fixing", "Testing", "Done"],
    "Marketing Campaign": ["Ideas", "Planned", "In Progress", "Launched"],
    "Operations": ["To Do", "In Progress", "Done"],
    "Roadmap": ["Planned", "In Progress", "Completed"],
    "Ongoing": ["Backlog", "Active"]
}

def generate_sections(conn, project_id, project_type):
    section_ids = []
    sections = SECTION_TEMPLATES.get(project_type, ["To Do", "Done"])

    for pos, name in enumerate(sections):
        section_id = gid()
        conn.execute(
            "INSERT INTO sections VALUES (?, ?, ?, ?)",
            (section_id, project_id, name, pos)
        )
        section_ids.append(section_id)

    return section_ids
