import os
import sys
import subprocess
from datetime import datetime

class ProjectCLI:
    def __init__(self, base_path):
        self.base_path = base_path
        self.log_file = os.path.join(base_path, "cli_log.txt")

    def create_project(self, project_name, project_type):
        project_path = os.path.join(self.base_path, project_name)
        if os.path.exists(project_path):
            print(f"Project '{project_name}' already exists.")
            return

        os.makedirs(project_path)
        self.log_action(f"Creating {project_type} project: {project_name}")

        if project_type == "python":
            self._create_python_project(project_path)
        elif project_type == "web":
            self._create_web_project(project_path)
        elif project_type == "csharp":
            self._create_csharp_project(project_path)
        else:
            print(f"Unknown project type: {project_type}")
            return

        print(f"{project_type.capitalize()} project '{project_name}' created successfully!")

    def _create_python_project(self, project_path):
        os.makedirs(os.path.join(project_path, "src"))
        os.makedirs(os.path.join(project_path, "tests"))
        os.makedirs(os.path.join(project_path, "docs"))
        with open(os.path.join(project_path, "src", "main.py"), "w") as f:
            f.write("def main():\n    print('Hello, Python Project!')\n\nif __name__ == '__main__':\n    main()\n")
        with open(os.path.join(project_path, "README.md"), "w") as f:
            f.write("# Python Project\n\nDescription of the Python project.")
        with open(os.path.join(project_path, "requirements.txt"), "w") as f:
            f.write("# Add your project dependencies here")

    def _create_web_project(self, project_path):
        os.makedirs(os.path.join(project_path, "assets", "css"))
        os.makedirs(os.path.join(project_path, "assets", "js"))
        os.makedirs(os.path.join(project_path, "assets", "images"))
        with open(os.path.join(project_path, "index.html"), "w") as f:
            f.write("<!DOCTYPE html><html><head><title>Web Project</title><link rel='stylesheet' href='assets/css/style.css'></head><body><h1>Hello, Web Project!</h1><script src='assets/js/app.js'></script></body></html>")
        with open(os.path.join(project_path, "assets", "css", "style.css"), "w") as f:
            f.write("/* Add your CSS styles here */")
        with open(os.path.join(project_path, "assets", "js", "app.js"), "w") as f:
            f.write("// Add your JavaScript code here")

    def _create_csharp_project(self, project_path):
        os.makedirs(os.path.join(project_path, "src"))
        os.makedirs(os.path.join(project_path, "tests"))
        with open(os.path.join(project_path, "src", "Program.cs"), "w") as f:
            f.write("using System;\nnamespace CSharpProject\n{\n    class Program\n    {\n        static void Main(string[] args)\n        {\n            Console.WriteLine('Hello, C# Project!');\n        }\n    }\n}")
        with open(os.path.join(project_path, "README.md"), "w") as f:
            f.write("# C# Project\n\nDescription of the C# project.")
        with open(os.path.join(project_path, "CSharpProject.sln"), "w") as f:
            f.write("# Solution file for the C# project")

    def run_project(self, project_name, project_type):
        project_path = os.path.join(self.base_path, project_name, "src")
        self.log_action(f"Running {project_type} project: {project_name}")
        
        if project_type == "python":
            subprocess.run(["python", os.path.join(project_path, "main.py")])
        elif project_type == "web":
            print("Web projects can't be 'run' directly. Open 'index.html' in a browser.")
        elif project_type == "csharp":
            subprocess.run(["dotnet", "run"], cwd=project_path)
        else:
            print(f"Unknown project type: {project_type}")

    def git_init(self, project_name):
        project_path = os.path.join(self.base_path, project_name)
        if not os.path.exists(project_path):
            print(f"Project '{project_name}' does not exist.")
            return
        
        self.log_action(f"Initializing Git repository for {project_name}")
        subprocess.run(["git", "init"], cwd=project_path)
        with open(os.path.join(project_path, ".gitignore"), "w") as f:
            f.write("# Ignore Python\n*.pyc\n__pycache__/\n\n# Ignore web assets\nassets/css/\nassets/js/\n\n# Ignore C# binaries\nbin/\nobj/")
        print(f"Git repository initialized for project '{project_name}'.")

    def log_action(self, action):
        with open(self.log_file, "a") as log:
            log.write(f"[{datetime.now()}] {action}\n")
        print(f"Action logged: {action}")

    def show_logs(self):
        if not os.path.exists(self.log_file):
            print("No logs found.")
            return
        with open(self.log_file, "r") as log:
            print(log.read())

    def list_templates(self):
        print("Available project templates:")
        print("1. python - Basic Python project structure")
        print("2. web - Basic web project with HTML, CSS, and JS folders")
        print("3. csharp - Basic C# project structure")

    def add_log(self, log_message):
        """Add a custom log entry."""
        self.log_action(log_message)
        print(f"Custom log entry added: {log_message}")

    def setup_version_control(self, project_name):
        """Setup version control with Python-specific .gitignore and environment setup."""
        project_path = os.path.join(self.base_path, project_name)
        if not os.path.exists(project_path):
            print(f"Project '{project_name}' does not exist.")
            return
        
        self.log_action(f"Setting up version control for Python project: {project_name}")
        
        subprocess.run(["git", "init"], cwd=project_path)
        with open(os.path.join(project_path, ".gitignore"), "w") as f:
            f.write(
                "*.pyc\n"
                "__pycache__/\n"
                ".env\n"
                "venv/\n"
                ".vscode/\n"
            )
        print(f"Version control setup with Python-specific .gitignore for project '{project_name}'.")

def main():
    if len(sys.argv) < 3:
        print("Usage: python project_cli.py <command> <project_name> [project_type]")
        return

    command = sys.argv[1].lower()
    project_name = sys.argv[2]
    project_type = sys.argv[3].lower() if len(sys.argv) > 3 else None
    base_path = "./Projects"
    cli = ProjectCLI(base_path)

    if command == "create":
        if not project_type:
            print("Please specify a project type (e.g., python, web, csharp).")
            return
        cli.create_project(project_name, project_type)
    elif command == "run":
        if not project_type:
            print("Please specify the project type.")
            return
        cli.run_project(project_name, project_type)
    elif command == "git":
        cli.git_init(project_name)
    elif command == "log":
        cli.show_logs()
    elif command == "addlog":
        if len(sys.argv) < 4:
            print("Usage: python project_cli.py addlog <log_message>")
            return
        cli.add_log(sys.argv[3])
    elif command == "versioncontrol":
        cli.setup_version_control(project_name)
    elif command == "list":
        cli.list_templates()
    else:
        print(f"Unknown command: {command}")

if __name__ == "__main__":
    main()
