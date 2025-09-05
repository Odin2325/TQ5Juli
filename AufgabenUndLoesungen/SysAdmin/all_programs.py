import subprocess
import os
import csv

def get_installed_programs():
    try:
        # PowerShell command to extract program details
        ps_command = (
            "Get-ItemProperty HKLM:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* ,"
            "HKCU:\\Software\\Microsoft\\Windows\\CurrentVersion\\Uninstall\\* | "
            "Select-Object DisplayName, DisplayVersion, Publisher, InstallLocation | "
            "Where-Object { $_.DisplayName -ne $null } | "
            "Sort-Object DisplayName | "
            "ForEach-Object { ($_.DisplayName + '`t' + $_.DisplayVersion + '`t' + $_.Publisher + '`t' + $_.InstallLocation) }"
        )

        result = subprocess.run(
            ["powershell", "-Command", ps_command],
            capture_output=True, check=True
        )

        # Decode as UTF-16 first, fallback to CP1252
        try:
            return result.stdout.decode("utf-16le")
        except UnicodeDecodeError:
            return result.stdout.decode("cp1252", errors="replace")

    except Exception as e:
        print(f"Error while fetching programs: {e}")
        return ""

def parse_programs(raw_output):
    programs = []
    for line in raw_output.splitlines():
        if "\t" in line:
            parts = line.split("\t")
            # Ensure exactly 4 fields
            while len(parts) < 4:
                parts.append("")
            name, version, publisher, location = [p.strip() for p in parts[:4]]
            programs.append((name, version, publisher, location))
        elif line.strip():
            programs.append((line.strip(), "", "", ""))
    return programs

def format_table(programs):
    if not programs:
        return "No programs found."

    # Compute max column widths
    max_name = max(len(name) for name, _, _, _ in programs)
    max_version = max(len(version) for _, version, _, _ in programs)
    max_publisher = max(len(publisher) for _, _, publisher, _ in programs)
    max_location = max(len(location) for _, _, _, location in programs)

    header = (
        f"{'Program Name'.ljust(max_name)} | "
        f"{'Version'.ljust(max_version)} | "
        f"{'Publisher'.ljust(max_publisher)} | "
        f"{'Install Location'.ljust(max_location)}"
    )
    table = [header, "-" * (max_name + max_version + max_publisher + max_location + 9)]

    for name, version, publisher, location in programs:
        table.append(
            f"{name.ljust(max_name)} | "
            f"{version.ljust(max_version)} | "
            f"{publisher.ljust(max_publisher)} | "
            f"{location.ljust(max_location)}"
        )

    return "\n".join(table)

def save_csv(programs, filename):
    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(["Program Name", "Version", "Publisher", "Install Location"])
        writer.writerows(programs)


if __name__ == "__main__":
    raw_output = get_installed_programs()
    programs = parse_programs(raw_output)

    # Save as aligned text
    formatted = format_table(programs)
    text_file = os.path.join(os.getcwd(), "installed_programs.txt")
    with open(text_file, "w", encoding="utf-8") as f:
        f.write(formatted)

    # Save as CSV
    csv_file = os.path.join(os.getcwd(), "installed_programs.csv")
    save_csv(programs, csv_file)

    print(f"Installed programs list saved to:\n- {text_file}\n- {csv_file}")