import os
import sys
import urllib.parse

sys.path.append("C:/Users/User/Documents/A/Chatbot/Test")

if len(sys.argv) < 2:
    print("Usage: python search.py <search_query>")
    sys.exit()

query = ' '.join(sys.argv[1:])
encoded_query = urllib.parse.quote_plus(query)

# Open Google Chrome and search for the query
os.system(f'start chrome "https://www.google.com/search?q={encoded_query}"')
