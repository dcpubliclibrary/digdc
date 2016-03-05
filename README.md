# DigDC API Documentation

DigDC is the online home for the DC Public Library's Special Collections. If you visit it, you can find historical DC cartoons, photographs, maps, oral histories, postcards, and other ephemera, as well as extensive metadata about each item. Cool, right? The site uses a platform called ContentDM. It's used by many, many libraries across the country. But ContentDM's API documentation is bad. This page covers what you need to know to see what collections are on DigDC, view what they contain, and download collection files.

The `dump.py` script provides an example use case. It creates a JSON array of collections and adds in the full metadata for all records in each collection.
