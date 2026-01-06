PRAGMA foreign_keys = ON;

-- =========================
-- ORGANIZATION
-- =========================
CREATE TABLE IF NOT EXISTS organizations (
    organization_id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    domain TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL
);

-- =========================
-- USERS
-- =========================
CREATE TABLE IF NOT EXISTS users (
    user_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    full_name TEXT NOT NULL,
    email TEXT NOT NULL,
    role TEXT NOT NULL,
    title TEXT,
    is_active BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- =========================
-- TEAMS
-- =========================
CREATE TABLE IF NOT EXISTS teams (
    team_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    name TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id)
);

-- =========================
-- TEAM MEMBERSHIPS
-- =========================
CREATE TABLE IF NOT EXISTS team_memberships (
    team_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    joined_at TIMESTAMP NOT NULL,
    PRIMARY KEY (team_id, user_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- =========================
-- PROJECTS
-- =========================
CREATE TABLE IF NOT EXISTS projects (
    project_id TEXT PRIMARY KEY,
    organization_id TEXT NOT NULL,
    team_id TEXT,
    name TEXT NOT NULL,
    project_type TEXT NOT NULL,
    status TEXT NOT NULL,
    start_date DATE,
    due_date DATE,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (organization_id) REFERENCES organizations(organization_id),
    FOREIGN KEY (team_id) REFERENCES teams(team_id)
);

-- =========================
-- SECTIONS
-- =========================
CREATE TABLE IF NOT EXISTS sections (
    section_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    position INTEGER NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

-- =========================
-- TASKS & SUBTASKS
-- =========================
CREATE TABLE IF NOT EXISTS tasks (
    task_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    section_id TEXT,
    parent_task_id TEXT,
    assignee_id TEXT,
    name TEXT NOT NULL,
    description TEXT,
    due_date DATE,
    completed BOOLEAN NOT NULL,
    created_at TIMESTAMP NOT NULL,
    completed_at TIMESTAMP,
    FOREIGN KEY (project_id) REFERENCES projects(project_id),
    FOREIGN KEY (section_id) REFERENCES sections(section_id),
    FOREIGN KEY (parent_task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (assignee_id) REFERENCES users(user_id)
);

-- =========================
-- COMMENTS (STORIES)
-- =========================
CREATE TABLE IF NOT EXISTS comments (
    comment_id TEXT PRIMARY KEY,
    task_id TEXT NOT NULL,
    user_id TEXT NOT NULL,
    body TEXT NOT NULL,
    created_at TIMESTAMP NOT NULL,
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

-- =========================
-- CUSTOM FIELDS
-- =========================
CREATE TABLE IF NOT EXISTS custom_field_definitions (
    field_id TEXT PRIMARY KEY,
    project_id TEXT NOT NULL,
    name TEXT NOT NULL,
    field_type TEXT NOT NULL,
    FOREIGN KEY (project_id) REFERENCES projects(project_id)
);

CREATE TABLE IF NOT EXISTS custom_field_values (
    field_value_id TEXT PRIMARY KEY,
    field_id TEXT NOT NULL,
    task_id TEXT NOT NULL,
    value TEXT,
    FOREIGN KEY (field_id) REFERENCES custom_field_definitions(field_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id)
);

-- =========================
-- TAGS
-- =========================
CREATE TABLE IF NOT EXISTS tags (
    tag_id TEXT PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS task_tags (
    task_id TEXT NOT NULL,
    tag_id TEXT NOT NULL,
    PRIMARY KEY (task_id, tag_id),
    FOREIGN KEY (task_id) REFERENCES tasks(task_id),
    FOREIGN KEY (tag_id) REFERENCES tags(tag_id)
);