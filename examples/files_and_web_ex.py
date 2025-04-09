from easy_python.web import fetch_url, scrape_links
from easy_python.files import write_json

# Получить ссылки с сайта
links = scrape_links("https://python.org")
write_json({"links": links}, "python_links.json")