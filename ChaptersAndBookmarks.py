def group_bookmarks(bookmarks, chapters):
    chapters_index = -1

    chapter_buckets = {}

    for bookmark_index in range(len(bookmarks) - 1, -1, -1) :
        # We know that bookmarks[0] will never be earlier than chapters[0],
        # so we don't need to do any checking for that here.
        while bookmarks[bookmark_index] < chapters[chapters_index]:
            chapters_index -= 1

        if chapters[chapters_index] not in chapter_buckets:
            chapter_buckets[chapters[chapters_index]] = []

        chapter_buckets[chapters[chapters_index]].append(bookmarks[bookmark_index])

    return chapter_buckets

##########################

# b = [6, 7, 9, 10, 11, 16, 19, 21, 22]
# c = [5, 10, 15, 20]


# b = [1]
# c = range(1, 100000)

b = [274, 19928]
c = range(1, 100000, 43)

result = group_bookmarks(b, c)
print(result)