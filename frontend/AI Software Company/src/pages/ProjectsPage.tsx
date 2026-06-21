type Project = {
    id: number;
    name: string;
    requirements: string;
};

import { useState, useEffect } from "react";

export default function ProjectsPage() {
    const [projects, setProjects] = useState<Project[]>([]);

    useEffect(() => {
        fetch("http://localhost:8000/projects")
        .then(res => res.json())
        .then(data => {
            setProjects(data);
        });
    }, [])

    return (
        <div>
            <h1>Projects</h1>

            {projects.map((project) => (
                <div key={project.id}>
                    {project.name}
                    </div>
            ))}
        </div>
    );
}