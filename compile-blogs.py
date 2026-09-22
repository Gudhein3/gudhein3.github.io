from hashlib import sha1

with open("blogpost_format.html.in", "r") as inp:
    blogpost_format = inp.read()

with open("posts.txt", "r") as inp:
    posts = []
    for post in inp.read().split("\n--------------------\n"):
        title, date, body = post.split('\n', 2)
        body = body.replace("\n", "<br>")
        posts.append((title, date, body))

bloglist = ""
for title, date, body in posts[::-1]:
    # Pray that it won't cause collision
    hash = sha1(title.encode()).hexdigest()[:10]
    with open(f"blog/post_{hash}.html", 'w') as out:
        out.write(blogpost_format.replace("%title%", title).replace("%body%", body).replace("%date%", date))
    bloglist += f"<a href=\"/blog/post_{hash}.html\">{title}</a><br>\n"

with open("index.html.in", 'r') as inp:
    with open("index.html", 'w') as out:
        out.write(inp.read().replace("%%", bloglist))
