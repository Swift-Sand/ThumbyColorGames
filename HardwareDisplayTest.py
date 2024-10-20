import sys
import requests

# Configuration
GITHUB_REPO = 'Swift-Sand/ThumbyColorGames'  # Replace with your username/repository
FILE_PATH = 'HDTInfo.txt'  # Replace with the path to your file
Version = 1.0

def fetch_first_line_as_float():
    """Fetch the first line of a GitHub file and convert it to a float."""
    try:
        # Construct the URL to fetch the raw content of the file
        url = f'https://raw.githubusercontent.com/{GITHUB_REPO}/main/{FILE_PATH}'
        
        # Fetch the file content
        response = requests.get(url)
        
        if response.status_code == 200:
            # Get the first line and strip whitespace
            first_line = response.text.splitlines()[0].strip()
            
            # Convert to float
            first_line_as_float = float(first_line)
            print(f'Latest Software Version: {first_line_as_float}')
            return first_line_as_float
        else:
            print(f'Error fetching file: {response.status_code} - {response.reason}')
            return None

    except ValueError:
        print('The first line is not a valid float.')
        return None
    except Exception as e:
        print(f'Error: {e}')
        return None

if __name__ == '__main__':
    first_line_as_float = fetch_first_line_as_float()
    version = float(1.0)
    print('Current version:', version)
    
    # Check if the fetched version is greater than the current version
    if first_line_as_float is not None and first_line_as_float > version:
        print('Error, outdated software version')
#HIPSSN-q791288254S