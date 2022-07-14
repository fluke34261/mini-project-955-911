# Read HAR File

## What is HAR File
[HAR file](https://en.wikipedia.org/wiki/HAR_(file_format))

## How HAR file store image
HAR file store image as base64 data in field `mimeType`

```JSON
...
...
"content": {
            "size": 50347,
            "mimeType": "image/jpeg",
            "compression": -126,
            "text": "/9j/4AAQSkZJRgABAQAAAQABAAD/2wBDAAgGBgcGBQgHBwcJCQgKDBQNDAsLDBkSEw8UHRofHh0aHBwgJC4nIII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZna...."
},
...
...
```
