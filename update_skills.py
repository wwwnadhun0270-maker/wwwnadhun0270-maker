import re

# Define skill percentages (update manually or from external data)
skills = {
    "Python": 85,
    "Arduino": 75,
    "HTML/CSS": 70,
    "OpenCV": 70,
    "MATLAB": 50,
    "Circuit Analysis": 60
}

# Read README.md
with open("README.md", "r", encoding="utf-8") as f:
    content = f.read()

# Update Shields.io badges in README
for skill, percent in skills.items():
    pattern = rf"!\[{skill}\]\(https://img\.shields\.io/badge/{skill}-\d+%25-[a-z]+\)"
    replacement = f"![{skill}](https://img.shields.io/badge/{skill}-{percent}%25-brightgreen)"
    content = re.sub(pattern, replacement, content)

# Write updated README.md
with open("README.md", "w", encoding="utf-8") as f:
    f.write(content)

print("README.md skill badges updated!")
