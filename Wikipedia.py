# Keyword arguments:
        
#         * sentences - if set, return the first `sentences` sentences (can be no greater than 10).
#         * chars - if set, return only the first `chars` characters (actual text returned may be slightly longer).
#         * auto_suggest - let Wikipedia find a valid page title for the query
#         * redirect - allow redirection without raising RedirectError

import wikipedia
res=wikipedia.page("Mahatma Gandhi")
print(res.summary)
