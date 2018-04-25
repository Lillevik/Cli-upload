"""
upl

Usage:
  upl <file>
  upl -h | --help
  upl --version

Options:
  -h --help                         Show this screen.
  --version                         Show version.

Examples:
  upl <file>
"""


from docopt import docopt
from upl import __version__ as VERSION
import os, requests


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)
    if '<file>' in options:
        cwd = os.getcwd()
        filepath = os.path.join(cwd, options['<file>'])
        try:
            in_file = open(filepath, 'rb')
            print('Uploading ' + options['<file>'])
            r = requests.post('https://i.lillevik.pw/upload/file', files={'file': in_file})
            if r.status_code == 200:
                print('Done! url: ' + r.json()['location'])
            elif r.status_code == 413:
                print('Error: file too large. Max 100mb.')
            else:
                print('Error: An error occurred during upload.')
        except FileNotFoundError:
            print('Error: Could not find the file.')
        except PermissionError:
            print('Error: Insufficient permissions.')
        except IsADirectoryError:
            print('Error: File is a directory.')
        except Exception:
            print('Error: An unexpected error occurred. Please create an issue on github. ')



