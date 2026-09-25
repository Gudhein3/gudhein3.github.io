from hashlib import sha1

with open("blogpost_format.html.in", "r") as inp:
    blogpost_format = inp.read()

posts = []

with open("posts.txt", "r") as inp:
    for post in inp.read().split("\n--------------------\n"):
        post = post.strip()
        id_title, date, body = post.split('\n', 2)
        id, title = id_title.split("|")
        date, body = date.strip(), body.strip()
        id, title = id.strip(), title.strip()
        body = body.replace("\n", "<br>\n")
        posts.append((title, id, date, body))

bloglist = ""
for title, id, date, body in posts[::-1]:
    # Hope that it won't cause collisions
    with open(f"blog/post_{id}.html", 'w') as out:
        out.write(blogpost_format.replace("%title%", title).replace("%body%", body).replace("%date%", date))
    bloglist += f"<a href=\"/blog/post_{id}.html\">{title}</a><br>\n"

with open("index.html.in", 'r') as inp:
    with open("index.html", 'w') as out:
        out.write(inp.read().replace("%%", bloglist))
