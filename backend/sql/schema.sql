-- Creating the database
CREATE DATABASE ai_company;

-- Create table for projects
CREATE TABLE projects (
    project_id SERIAL PRIMARY KEY,
    idea TEXT,
    requirements TEXT
);

-- Create table for tasks within projects
CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    project_id INTEGER REFERENCES projects(project_id),
    title TEXT,
    description TEXT,
    status TEXT
);