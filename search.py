from fuzzywuzzy import process

# Finds the best matches for the search term
def findBestMatch(searchTerm, options, limit=10):
    if not options:
        # When there are no options for searching
        print("No options available for searching.")
        return []

    """Normalises/Lowercases the search term so that it can be string easier with article titles that are also lowercased, 
    then with the extraction of searchTerms and options with the possible articles possible"""
    searchTerm = searchTerm.lower()

    try:
        results = process.extract(searchTerm, options, limit=limit)
    except Exception as e:
        print(f"An error occurred while finding the best match: {e}")
        return []
    
    return results

# Wrapper for fuzzy search to return matches, which allows for the instance to be valid for return of results
def fuzzySearch(searchTerm, options, limit=10):
    # Validates the input for when the instance is called upon when the fuzzy search is utlised
    if not isinstance(searchTerm, str) or not isinstance(options, list):
        print("Invalid input types.")
        # Reurns nothing as there is no valid input types that was inputted for it
        return []

    # Results speaks for itself, it returns the results, which makes results equal to the best match with its question, articles, and limit
    results = findBestMatch(searchTerm, options, limit)
    return results
