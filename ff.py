from ripper import singular_post, get_pages

url = "https://pics.alphacoders.com/pictures/view/371223"
# print(singular_post(url))

blrc = "https://pics.alphacoders.com/by_sub_category/174899?page=1"
for x in get_pages(blrc):
    print(x)
