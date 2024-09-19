def group_bookmarks(bookmarks, chapters):
    bookmark_index = len(bookmarks) - 1
    chapters_index = len(chapters) - 1

    chapter_buckets = {}

    while bookmark_index >= 0:
        # We know that bookmark[0] will never be earlier than chapters[0],
        # so we don't need to do any checking for that here.
        while bookmarks[bookmark_index] < chapters[chapters_index]:
            chapters_index -= 1

        if chapters[chapters_index] not in chapter_buckets:
            chapter_buckets[chapters[chapters_index]] = []

        chapter_buckets[chapters[chapters_index]].append(bookmarks[bookmark_index])
        bookmark_index -= 1

    return chapter_buckets

##########################

# b = [6, 7, 9, 10, 11, 16, 19, 21, 22]
# c = [5, 10, 15, 20]


# b = [1]
# c = range(1, 100000)

b = [274]
c = range(1, 100000, 50)

result = group_bookmarks(b, c)
print(result)