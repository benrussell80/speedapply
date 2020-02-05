import os
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('name', help='Name of folder to create in order to house apply bot.')
    
    args = parser.parse_args()

    name = args.name

    dirpath = os.path.join(os.getcwd(), name)
    try:
        os.mkdir(dirpath)
    except FileExistsError:
        pass

    with open(os.path.join(dirpath, '__init__.py'), 'w') as fh:
        pass

    with open(os.path.join(dirpath, 'settings.py'), 'w') as fh:
        fh.write("""# driver
DRIVER = 'chrome'
DRIVER_OPTIONS = ['--headless']

# job titles
TITLES = [
    'Entry Level Software Engineer',
    'Data Engineer',
    'Machine Learning Engineer'
]

# job locations
LOCATIONS = [
    'New York, Ny',
    'Atlanta, GA',
    'Los Angeles, CA'
]
""")
    
    with open(os.path.join(dirpath, 'bots.py'), 'w') as fh:
        fh.write("""import os

from speedapply.bots import ApplyBot
from speedapply.sites import Monster


monster_bot = ApplyBot(
    site=Monster,
    auth=(
        os.environ['MONSTER_USERNAME'],
        os.environ['MONSTER_PASSWORD']
    )
)
""")

    with open(os.path.join(dirpath, 'run.py'), 'w') as fh:
        fh.write(f"""import bots
import settings
from speedapply import start

if __name__ == "__main__":
    start(bots, settings)
""")

if __name__ == "__main__":
    main()