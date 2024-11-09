import os
import json
import shutil
import datetime
import filecmp
from difflib import unified_diff

CURRENT_FILES_FOLDER = "CurrentFiles"
VERSIONS_FOLDER = "Versions"
METADATA_FILE = "metadata.json"


class VersionControlCLI:
    def __init__(self, project_path):
        self.project_path = project_path
        self.current_files_path = os.path.join(self.project_path, CURRENT_FILES_FOLDER)
        self.versions_path = os.path.join(self.project_path, VERSIONS_FOLDER)
        self.metadata_path = os.path.join(self.project_path, METADATA_FILE)

    def initialize_repository(self):
        os.makedirs(self.current_files_path, exist_ok=True)
        os.makedirs(self.versions_path, exist_ok=True)
        with open(self.metadata_path, "w") as f:
            json.dump([], f)
        print("Repository initialized successfully!")

    def commit_changes(self, message):
        version_id = str(int(datetime.datetime.now().timestamp()))
        version_path = os.path.join(self.versions_path, version_id)
        os.makedirs(version_path, exist_ok=True)

        committed_files = []
        for file_name in os.listdir(self.current_files_path):
            src_file = os.path.join(self.current_files_path, file_name)
            dest_file = os.path.join(version_path, file_name)
            shutil.copy2(src_file, dest_file)
            committed_files.append(file_name)

        commit_metadata = {"id": version_id, "message": message, "date": datetime.datetime.now().isoformat(), "files": committed_files}
        metadata = self._get_metadata()
        metadata.append(commit_metadata)
        self._save_metadata(metadata)

        print(f"Commit '{message}' saved with version ID {version_id}.")

    def status(self):
        metadata = self._get_metadata()
        if not metadata:
            print("No commits found.")
            return

        last_commit_files = set(metadata[-1]["files"])
        print("Changed files since last commit:")
        for file_name in os.listdir(self.current_files_path):
            if file_name not in last_commit_files:
                print(f"Modified: {file_name}")

    def show_history(self):
        metadata = self._get_metadata()
        print("Version History:")
        for commit in metadata:
            print(f"ID: {commit['id']} | Message: {commit['message']} | Date: {commit['date']}")

    def show_commit_log(self, version_id):
        metadata = self._get_metadata()
        commit = next((c for c in metadata if c["id"] == version_id), None)
        if not commit:
            print("Commit not found.")
            return

        print(f"Commit ID: {commit['id']}")
        print(f"Message: {commit['message']}")
        print(f"Date: {commit['date']}")
        print("Files:")
        for file_name in commit["files"]:
            print(f" - {file_name}")

    def diff(self, file_name, version_id1, version_id2):
        file_path1 = os.path.join(self.versions_path, version_id1, file_name)
        file_path2 = os.path.join(self.versions_path, version_id2, file_name)

        if not os.path.exists(file_path1) or not os.path.exists(file_path2):
            print("One of the specified versions does not contain this file.")
            return

        with open(file_path1, "r") as f1, open(file_path2, "r") as f2:
            diff = unified_diff(
                f1.readlines(), f2.readlines(),
                fromfile=f"{file_name} (version {version_id1})",
                tofile=f"{file_name} (version {version_id2})"
            )
            for line in diff:
                print(line, end='')

    def delete_version(self, version_id):
        version_path = os.path.join(self.versions_path, version_id)
        if os.path.exists(version_path):
            shutil.rmtree(version_path)
            metadata = self._get_metadata()
            metadata = [commit for commit in metadata if commit["id"] != version_id]
            self._save_metadata(metadata)
            print(f"Version {version_id} deleted.")
        else:
            print("Version not found.")

    def _get_metadata(self):
        if os.path.exists(self.metadata_path):
            with open(self.metadata_path, "r") as f:
                return json.load(f)
        return []

    def _save_metadata(self, metadata):
        with open(self.metadata_path, "w") as f:
            json.dump(metadata, f, indent=4)


def main():
    import sys
    if len(sys.argv) < 2:
        print("Usage: python version_control.py <command> [<args>]")
        return

    project_path = "./MyRepo"  # Set this to the desired repository path
    vc = VersionControlCLI(project_path)

    command = sys.argv[1].lower()
    if command == "init":
        vc.initialize_repository()
    elif command == "commit":
        if len(sys.argv) < 3:
            print("Commit message required.")
            return
        message = sys.argv[2]
        vc.commit_changes(message)
    elif command == "status":
        vc.status()
    elif command == "history":
        vc.show_history()
    elif command == "log":
        if len(sys.argv) < 3:
            print("Version ID required.")
            return
        version_id = sys.argv[2]
        vc.show_commit_log(version_id)
    elif command == "diff":
        if len(sys.argv) < 5:
            print("Usage: diff <file_name> <version_id1> <version_id2>")
            return
        file_name, version_id1, version_id2 = sys.argv[2], sys.argv[3], sys.argv[4]
        vc.diff(file_name, version_id1, version_id2)
    elif command == "delete":
        if len(sys.argv) < 3:
            print("Version ID required.")
            return
        version_id = sys.argv[2]
        vc.delete_version(version_id)
    else:
        print("Unknown command.")


if __name__ == "__main__":
    main()
