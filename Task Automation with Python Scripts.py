import os
import requests

def download_file(url, save_path):
    try:
        # Send a HTTP request to the URL
        response = requests.get(url, stream=True)
        response.raise_for_status()  # Check if the request was successful

        # Write the content to a file
        with open(save_path, 'wb') as file:
            for chunk in response.iter_content(chunk_size=8192):
                file.write(chunk)

        print(f"File successfully downloaded and saved to {save_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading file: {e}")

def main():
    url = input("Enter the URL of the file to download: ")
    save_path = input("Enter the path where the file should be saved: ")

    # Create the directory if it doesn't exist
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    
    download_file(url, save_path)

if __name__ == "__main__":
    main()
