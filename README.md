# speedapply
Package for automatically applying to relevant jobs on popular job boards.

This package is designed to crawl job boards like Monster, LinkedIn, and Indeed and automatically apply for jobs that you want. As of now only Monster is supported and only Speed Apply jobs are applied to. Further functionality needs to be added. `speedapply` uses selenium to traverse these web pages.

## Usage
1. Install using pip

```
$ pip install speedapply
```

In addition to the python package requirements, `speedapply` requires a `selenium`-compatible webdriver (e.g. chromedriver).

2. Create a new folder to house the apply bot

```
$ python -m speedapply new_bot
```

or

```
$ speedapply new_bot
```

3. Edit `new_bot/settings.py` to choose jobs and locations you want.

```python
# new_bot/settings.py
...
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
...
```

4. Set environment variables for your username and password that get accessed by the bot in `new_bot/bots.py`.
For example for `monster.com`:

```
$ export MONSTER_USERNAME="..." MONSTER_PASSWORD="..."
```

```python
# new_bot/bots.py
import os

from speedapply.bots import ApplyBot
from speedapply.sites import Monster


monster_bot = ApplyBot(
    site=Monster,
    auth=(
        os.environ['MONSTER_USERNAME'],
        os.environ['MONSTER_PASSWORD']
    )
)
```

5. Import the `bots` and `settings` and run the `start` function in `new_bot/run.py`.

```python
# new_bot/run.py
import bots
import settings
from speedapply import start

if __name__ == "__main__":
    start(bots, settings)
```

    $ python new_bot/run.py

This will begin applying to each job title in each location on each job board specified.

Leave it running and easily apply to hundreds of jobs per day!

## Development
There are many improvements that can be made:
- bots for more job boards
- faster loading and filtering of jobs (possibly from APIs instead of web-scraping)
- multiple drivers for quicker applying
- better logging of jobs applied to