# UShorten - 🔗 URL Shortening Service

UShorten is a simple URL shortening service built using Flask, a micro web framework for Python. This service allows users to create short and easy-to-share links for long URLs. It provides a web interface to shorten URLs and also offers a JSON API for programmatic access.

## Features 🚀

- Shorten long URLs into shorter, more manageable links.
- Access short links and get redirected to the original long URLs.
- API support for integrating URL shortening into your applications.
- Cross-origin resource sharing (CORS) enabled for easy integration with different domains.

## Web Interface 🌐

[UShorten](https://ushorten.xyz) offers a user-friendly web interface where users can input a long URL and get a shortened link in return. The generated shortened link can then be easily shared with others. This web interface is open source & included with this repo !

## API Documentation 📚

UShorten provides a simple JSON API for programmatically interacting with the service. Below are the available API endpoints:

### Shorten a URL

Shortens a long URL and returns a JSON response containing the shortened link.

**Endpoint**: `/short/<link>`  
**Method**: GET

#### Example 📝

```python
import requests

url_to_shorten = "https://www.example.com/very/long/url"
response = requests.get(f"https://ushorten.xyz/short/{url_to_shorten}")

data = response.json()
if data["success"]:
    shortened_link = data["data"]["link"]
    print("Shortened link:", shortened_link)
else:
    print("Error:", data["error"])
```

### Access Shortened URL

Redirects to the original long URL associated with the given short ID.<br>
*Note: if opened in browser, you'll be redirected*

**Endpoint**: `/<id>`  
**Method**: GET

#### Example 📝

```python
# Make a request to the short link
response = requests.get("https://ushorten.xyz/abc123")

# If the status code is 200, it means the short link was found and redirected
if response.status_code == 200:
    print("Redirected URL:", response.url)
else:
    print("Short link not found.")
```

## Usage 🛠️

1. Clone this repository to your local machine.
2. Install the required packages using `pip install -r requirements.txt`.
3. Run the Flask app using `python api.py`.

The app will start running locally, and you can access the web interface by opening your browser and navigating to `http://localhost:6969`.

## Contributions 🤝

Contributions to UShorten are welcome! If you find any issues or want to add new features, please feel free to open a pull request.

## License 📜

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

UShorten is a project created by [vodkarm](https://github.com/vodkarm). It aims to simplify URL sharing by providing a convenient way to generate short links. If you have any questions or feedback, please open an issue on the GitHub repository.
