from pathlib import Path

ORDER = [
  "01_part.py",
  "02_part.py",
  "03_part.py",
  "04_part.py",
  "05_part.py",
  "06_part.py",
  "07_part.py",
  "08_part.py",
  "09_part.py",
  "10_part.py",
]

root = Path("app_parts_split")
out = Path("app.py")

with out.open("w", encoding="utf-8") as f_out:
    for name in ORDER:
        f_out.write((root / name).read_text(encoding="utf-8"))
print("✅ app.py reconstruido sin cambios adicionales.")
