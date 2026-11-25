import os

LINE = "I did not eat the homework. I filed it — in my stomach, where no teacher can ever find it again. Case closed."

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(LINE)
