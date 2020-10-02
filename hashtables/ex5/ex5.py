# Your code here



def finder(files, queries):
    """
    Given a list of full paths to files, and a list of filenames to query,
    report all the full paths that match that filename.
    """
    cache = {}
    result = []

    for path in files:
        #file comes before last backslash
        file = path.split('/')[-1]

        if file in cache:
            #append path of file
            cache[file].append(path)
        else:
            cache[file] = [path]

    for i in queries:
        if i in cache:
            results = cache[i]
            for path in results:
                result.append(path)
  

    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
