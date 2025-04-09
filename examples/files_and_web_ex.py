from EasyPyTools.web import fetch_url, scrape_links
from EasyPyTools.files import write_json

# Getting url
links = scrape_links("https://python.org")
write_json({"links": links}, "python_links.json")
