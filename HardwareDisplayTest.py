#startup
import sys

import requests
print(sys)

# Configuration
GITHUB_REPO = 'Swift_Sand/ThumbyColorGames'  # Replace with your username/repository
FILE_PATH = '/workspaces/ThumbyColorGames/HDTInfo.txt'  # Replace with the path to your file

def fetch_first_line_as_int():
    """Fetch the first line of a GitHub file and convert it to an integer."""
    try:
        # Construct the URL to fetch the raw content of the file
        url = f'https://raw.githubusercontent.com/{GITHUB_REPO}/main/{FILE_PATH}'
        
        # Fetch the file content
        response = requests.get(url)
        
        if response.status_code == 200:
            # Get the first line and strip whitespace
            first_line = response.text.splitlines()[0].strip()
            
            # Convert to integer
            first_line_as_int = int(first_line)
            print(f'The first line as an integer: {first_line_as_int}')
            return first_line_as_int
        else:
            print(f'Error fetching file: {response.status_code} - {response.reason}')
            return None

    except ValueError:
        print('The first line is not a valid integer.')
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    fetch_first_line_as_int()

