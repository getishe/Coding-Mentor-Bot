import wikipedia

# Set language (optional)
wikipedia.set_lang("en")

# Define pages to download
pages = [
    "Python (programming language)",
    "NumPy",
    "Pandas (software)",
    "Flask (web framework)",
    "Python syntax and semantics",
    "History of Python"
]

# Download and save each page
for title in pages:
    content = wikipedia.page("Python (programming language)").content
    filename = title.replace(" ", "_").replace("(", "").replace(")", "") + ".txt"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(content)


# Wikipedia Bot
# https://copilot.microsoft.com/shares/2sNqERu8taDVRj6YGWa5o

# https://copilot.microsoft.com/shares/S39TLsUx1BLMVKfsAAh5y
