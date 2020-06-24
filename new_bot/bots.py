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
