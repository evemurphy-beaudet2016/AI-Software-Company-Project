// Frontend equivalent of the backend services.py

export async function getProjects() {
    const response = await fetch(
        "http://localhost:8000/projects"
    );
    return response.json();
}

export async function createProject(name: string) {
    await fetch(
        "http://localhost:8000/projects",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                name
            })
        }
    );
}