# Task: Add rsync Exclude Patterns to Blog Post

## Objective
Update the iMac Disk Recovery blog post to include recommendations for excluding specific directories (`Library/Containers` and `Library/Mobile Documents`) to improve reliability and speed.

## Details
- **Directories to Exclude**:
    - `Library/Containers`: High volume of small, volatile app state files.
    - `Library/Mobile Documents`: iCloud data that can cause sync issues during manual transfer.
- **Goal**: Document the use of the `--exclude` flag for these specific paths.
