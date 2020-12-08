from ripper import get_pages

urls = [
    "https://wall.alphacoders.com/by_sub_category.php?id=174899&name=Bleach+Wallpapers",
    "https://mobile.alphacoders.com/by-sub-category/174899",
    "https://art.alphacoders.com/by_sub_category/174899",
    "https://pics.alphacoders.com/by_sub_category/174899",
    "https://avatars.alphacoders.com/by_sub_category/174899",
    "https://gifs.alphacoders.com/by_sub_category/174899",
    "https://covers.alphacoders.com/by_sub_category/174899"
]

for url in urls:
    for x in get_pages(url):
        print(x)
