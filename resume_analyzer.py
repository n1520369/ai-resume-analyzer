skills_database = [
    "python",
    "sql",
    "machine learning",
    "data analysis",
    "excel",
    "java",
    "javascript",
    "git",
    "github",
    "communication"
]

resume_text = input("Paste resume text:\n").lower()

found_skills = []

for skill in skills_database:
    if skill in resume_text:
        found_skills.append(skill)

print("\nDetected Skills:")
for skill in found_skills:
    print("-", skill)

print(f"\nTotal Skills Found: {len(found_skills)}")
