'''
Configure Seaborn through a RC file, similarly to how Matplotlib does it.

To load the configuration from the RC file, simply import this package after
seaborn:

>>> import seaborn as sns
>>> import seaborn_rc

To reload the rc:
>>> seaborn_rc.load()

The RC file used is the first found in the following list:

- `$PWD/seabornrc`
- `$SEABORNRC/seabornrc`
- `$SNSCONFIGDIR/seabornrc`
- On Linux,
      - `$HOME/.seaborn/seabornrc`
      - `$XDG_CONFIG_HOME/seaborn/seabornrc` (if
        $XDG_CONFIG_HOME is defined)
      - `$HOME/.config/seaborn/seabornrc` (if
        $XDG_CONFIG_HOME is not defined)
- On other platforms,
     - `$HOME/.seaborn/seabornrc` if `$HOME` is defined.

'''

from .seaborn_rc import load, get_fname

load()
