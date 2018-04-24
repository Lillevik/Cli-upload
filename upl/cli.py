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


def main():
    """Main CLI entrypoint."""
    options = docopt(__doc__, version=VERSION)
    if '<file>' in options:
        import os, requests
        cwd = os.getcwd()
        in_file = open(os.path.join(cwd, options['<file>']), 'rb')
        print('Uploading ' + options['<file>'])
        try:
            r = requests.post('https://i.lillevik.pw/upload/file', files={'file': in_file})
            if r.status_code == 200:
                print('Done! url: ' + r.json()['location'])
            elif r.status_code == 413:
                print('Ups, file too large! Max 20mb.')
            else:
                print('An error occurred during upload.')
        except Exception as e:
            raise e
            print('An unexpected error occurred.')

