# your_package/update_version.py

import subprocess
from setuptools_scm import get_version

def get_version_without_dev():
    # Use a version scheme that excludes the development version
    return get_version(version_scheme="guess-next-dev")

def get_changed_files():
    try:
        # Use git to get the list of changed files
        changed_files_command = "git diff --name-only --diff-filter=AM $(git rev-parse HEAD^) HEAD"
        result = subprocess.run(changed_files_command, shell=True, check=True, capture_output=True, text=True)
        return result.stdout.strip().split("\n")
    except subprocess.CalledProcessError as e:
        print(f"Error getting changed files: {e}")
        return []

def count_changed_pages(changed_files):
    # Count all changed files, including added ones
    return len(changed_files)

def update_version():
    # Get the version from setuptools_scm without the development version
    current_version = get_version_without_dev()

    print("current_versioncurrent_version",current_version)

    # Extract only major, minor, and patch
    version_parts = current_version.split('.')
    if len(version_parts) >= 3:
        major, minor, patch = map(int, version_parts[:3])
    else:
        # Handle the case where the version string doesn't have major, minor, and patch
        raise ValueError("Invalid version format")

    changed_files = get_changed_files()
    changed_page_count = count_changed_pages(changed_files)

    if changed_page_count <= 2:
        patch += 1
    else:
        major += 1
        minor = 0
        patch = 0

    new_version = f"{major}.{minor}.{patch}"

    return new_version

if __name__ == "__main__":
    try:
        new_version = update_version()
        print("Updated Version:", new_version)
    except ValueError as e:
        print(f"Error: {e}")
