# Flask File Lister and Content Retriever

This Flask application provides an API to recursively list files in a directory and retrieve the content of specific files. It includes two main routes: one for listing files and directories and another for fetching the content of a file.

## Features
- Recursively list files and directories starting from a root directory.
- Retrieve the content of a file through an API request.

## Requirements
- Python 3.x
- Flask

## Installation

1. Clone the repository or download the files.
2. Make sure you have Flask installed. You can install it using pip:

    ```bash
    pip install Flask
    ```

3. Run the Flask application:

    ```bash
    python app.py
    ```

## API Endpoints

### 1. `GET /`

Lists all files and directories recursively starting from `/home/ubuntu/`.

#### Response:
- Success: Returns a list of dictionaries, each containing the `filetype` (either `dir` or `file`) and `path`.
  
    Example:
    ```json
    [
        {"filetype": "dir", "path": "/home/ubuntu/some_folder"},
        {"filetype": "file", "path": "/home/ubuntu/some_folder/file.txt"}
    ]
    ```

### 2. `POST /getfilecontent`

Fetches the content of a specific file based on the provided file path.

#### Request:
- Content-Type: `application/json`
- JSON Body:
    ```json
    {
        "path": "/path/to/file"
    }
    ```

#### Response:
- Success: Sends the file as a response for download.
- Error: If the file path is a directory or the file path is invalid, it returns an error message.

    Example error response:
    ```json
    {
        "error": "filetype is directory"
    }
    ```

    ```json
    {
        "error": "Invalid file Path"
    }
    ```

## Running the Application

Once the server is running, you can use tools like `curl`, `Postman`, or any HTTP client to interact with the API:

### Example request to list files:
```bash
curl http://localhost:4000/
