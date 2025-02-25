
# POST /albums Route Design Recipe

_Copy this design recipe template to test-drive a plain-text Flask route._

## 1. Design the Route Signature

_Include the HTTP method, the path, and any query or body parameters._

```
# Create new album
POST /albums
  Body args:
    title: string
    release_year: int
    artist_id: int
```

## 2. Create Examples as Tests

_Go through each route and write down one or more example responses._

_Remember to try out different parameter values._

_Include the status code and the response body._

```python
# POST /albums
#  Params: None or any of title, release_year, artist_id missing
#   Expected repsonse (400 BAD REQUEST)
"""
Must include album title, release_year and artist id.
"""

# POST /albums
#   Params: 
#     title: "Voyage"
#     release_year: 2022
#     artist_id: 2
#   Expected response (200 OK)


```

## 3. Test-drive the Route

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
"""
POST /albums
  Parameters:
    None
  Expected response (400 BAD REQUEST)
  "Must include album title, release_year and artist id."
"""
def test_post_albums_all_fields_missing(web_client):
  response = web_client.post('/albums')
  assert response.status_code == 400
  assert response.data.decone('utf-8') == "Must include album title, release_year and artist id."

"""
POST /albums
  Parameters:
    title: Voyage
    release_year: 2022
    artist_id: 2
  Expected response (200 OK)
"""
def test_post_albums_valid_entry(web_client):
  response = web_client.post('/albums', data={"title": "Voyage", "release_year": 2022, "artist_id": 2})
  assert response.status_code == 200
  albums = web_client.get('/albums')
  assert albums = [
    Album('Doolittle', 1989, 1),
    Album('Surfer Rosa', 1988, 1),
    Album('Waterloo', 1974, 2),
    Album('Super Trouper', 1980, 2),
    Album('Bossanova', 1990, 1),
    Album('Lover', 2019, 3),
    Album('I Put a Spell on You', 1965, 4),
    Album('Baltimore', 1978, 4),
    Album('Here Comes the Sun', 1971, 4),
    Album('Fodder on My Wings', 1982, 4),
    Album('Ring Ring', 1973, 2)
  ]

```

