from fuzzywuzzy import process

"""Finds the best matches for the search term using the fuzzy search algorithm.
In simple terms, it uses a score based on displacement and changes in letters and position to give a score,
which is then used for ranking the results."""

def findBestMatch(searchTerm, options, limit=10):
    if not options:
        # When there are no options for searching, which occurs when there are no articles to present
        print("No options available for searching.")
        return []

    """Normalises (lowercases) the search term so that it can be compared more easily with article titles
    that are also lowercased, then performs the search using the search term and options."""
    searchTerm = searchTerm.lower()

    # Extraction of the searchTerm which is the entry used, options in the articles and the limit
    try:
        results = process.extract(searchTerm, options, limit=limit)
    except Exception as e:
        print(f"An error occurred while finding the best match: {e}")
        return []
    
    return results

# Wrapper for fuzzy search to return matches, which allows for the instance to be valid for return of results
def fuzzySearch(searchTerm, options, limit=10):
    # Validates the input types when the fuzzy search is utilised
    if not isinstance(searchTerm, str) or not isinstance(options, list):
        print("Invalid input types.")
        # Returns nothing as the input types are not valid
        return []

    # Results contains the matches with their relevance scores
    results = findBestMatch(searchTerm, options, limit)
    return results
