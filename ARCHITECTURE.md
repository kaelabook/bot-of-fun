# Architecture

## Root Directory

### `bot.py`

The core file. Used to initialize the bot. Provides on-ready functionality and error handling.

### `utils.py`

Contains a bunch of nice utilities. Most files

```py
from utils import *
```

## Cogs

### `CogManagement.py`

Cog used to load, unload, and reload other cogs. Cannot be unloaded

### `Listeners.py`

Any generic event handles or listeners that don't belong in any other cog

