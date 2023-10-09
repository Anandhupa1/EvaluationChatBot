members =[
  {"name":"Alice","preferred_genre":"Romance"},
  {"name":"Bob","preferred_genre":"History"},
]
books =[
  {"title":"Love in the rain","genre":"Romance"},
  {"title":"Historical Times","genre":"History"},
]

out =[]
for x in members:
  genre = x["preferred_genre"];
  for y in books:
    if y["genre"]==genre:
      out.append({
        "name":x["name"],
        "book":y["title"]
      })
print(out)