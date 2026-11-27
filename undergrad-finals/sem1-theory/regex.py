import re

s = "meow"

# Level 1
re.findall(r"\d+", s)
re.findall(r"\b\d{4}\b", s)
re.fullmatch(r"\d{6}", s)
re.findall(r"\w+", s)
re.fullmatch(r"colou?r", s)
re.findall(r"\b[a-z]{3}\b", s)
re.sub(r"\d", "#", s)
re.search(r"\d", s)

# Level 2
re.fullmatch(r"[a-z]+", s)
re.findall(r"[aeiouAEIOU]", s)
re.sub(r"[aeiouAEIOU]", "*", s)
re.match(r"[A-Z]", s)
re.search(r"\.com$", s)
re.findall(r"\b[A-Z]\w*", s)
re.findall(r"[^A-Za-z ]", s)
re.sub(r"[^\w\s]", "", s)

# Level 3
re.fullmatch(r"[6-9]\d{9}", s)
re.fullmatch(r"\d{2}-\d{2}-\d{4}", s)
re.fullmatch(r"([01]\d|2[0-3]):[0-5]\d", s)
re.fullmatch(r"[A-Za-z_]\w*", s)
re.fullmatch(r"[\w.]+@[\w.]+\.[a-z]{2,4}", s)
re.fullmatch(r"[A-Z]{2}\d{2}[A-Z]{2}\d{4}", s)
re.fullmatch(r"(?=.*\d)(?=.*[A-Z]).{8,}", s)
re.fullmatch(r"#[0-9A-Fa-f]{6}", s)

# Level 4
m = re.search(r"(\d{2})-(\d{2})-(\d{4})", s)
re.sub(r"(\d{2})-(\d{2})-(\d{4})", r"\3-\2-\1", s)
re.split(r"\d+", s)            # ['a', 'b', 'c', 'd']
re.split(r"[,; ]+", s)
re.sub(r"\s+", " ", s)
re.findall(r"(\w+)=(\w+)", s)
re.findall(r"\b(\w+) \1\b", s)  # ['the', 'day']
re.sub(r"\d(?=\d{4})", "*", s)  # ************3456

# Level 5
re.findall(r"<.+?>", s)
re.findall(r'"(.*?)"', s)
re.findall(r"\bcat\b", s)
re.findall(r"#\w+", s)
re.findall(r"₹[\d,]+", s)
re.findall(r"\b\w+ing\b", s)
re.findall(r"[\w.]+@[\w.]+\.[a-z]{2,}", s)
re.findall(r"\d+(?:\.\d+)?", s)

# Using Regex101 for rest!

# QP 5a - Using Groups
record = "RegNo=26BE1001; Course=CSE1012; Attendance=36/45; CAT1=38/50; CAT2=42/50"
data = {}

data["RegNo"] = re.search(r"RegNo=(\w+)", record).group(1)
data["Course"] = re.search(r"Course=(\w+)", record).group(1)

m = re.search(r"Attendance=(\d+)/(\d+)", record)
data["Attended_Classes"] = m.group(1)
data["Total_Classes"] = m.group(2)

m = re.search(r"CAT1=(\d+)/(\d+)", record)
data["CAT1"] = int(m.group(1))
data["CAT1_Max"] = int(m.group(2))

m = re.search(r"CAT2=(\d+)/(\d+)", record)
data["CAT2"] = int(m.group(1))
data["CAT2_Max"] = int(m.group(2))

print(data)
