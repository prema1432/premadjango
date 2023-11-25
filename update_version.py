# your_package/update_version.py

import subprocess
from setuptools_scm import get_version


def get_changed_files():
    # Use git to get the list of changed files
    changed_files_command = "git diff --name-only --diff-filter=AM HEAD^ HEAD"
    result = subprocess.run(changed_files_command, shell=True, check=True, capture_output=True, text=True)
    return result.stdout.strip().split("\n")


def count_changed_pages(changed_files):
    # Count all changed files, including added ones
    return len(changed_files)


def update_version():
    current_version = get_version()
    major, minor, patch = map(int, current_version.split('.')[:3])

    changed_files = get_changed_files()
    changed_page_count = count_changed_pages(changed_files)

    if changed_page_count <= 2:
        patch += 1
    else:
        major = 0
        minor += 1
        patch = 0

    new_version = f"{major}.{minor}.{patch}"

    return new_version


if __name__ == "__main__":
    new_version = update_version()
    print("Updated Version:", new_version)
