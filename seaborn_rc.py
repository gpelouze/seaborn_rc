import os
import six
import sys
import warnings

import matplotlib as mpl
import seaborn as sns

def _get_config_or_cache_dir(xdg_base):
    from matplotlib.cbook import mkdirs

    configdir = os.environ.get('SNSCONFIGDIR')
    if configdir is not None:
        configdir = os.path.abspath(configdir)
        if not os.path.exists(configdir):
            mkdirs(configdir)

        return configdir

    p = None
    h = mpl.get_home()
    if h is not None:
        p = os.path.join(h, '.seaborn')
    if sys.platform.startswith(('linux', 'freebsd')) and xdg_base:
        p = os.path.join(xdg_base, 'seaborn')

    if p is not None:
        if os.path.exists(p):
            return p
        else:
            try:
                mkdirs(p)
            except OSError:
                pass
            else:
                return p

def _get_configdir():
    ''' Return the string representing the configuration directory.

    The directory is chosen as follows:

    1. If the SNSCONFIGDIR environment variable is supplied, choose that.

    2a. On Linux, if `$HOME/.seaborn` exists, choose that, but warn that
        that is the old location.  Barring that, follow the XDG specification
        and look first in `$XDG_CONFIG_HOME`, if defined, or `$HOME/.config`.

    2b. On other platforms, choose `$HOME/.seaborn`.

    3. If the chosen directory exists and is writable, use that as the
       configuration directory.
    4. If possible, create a temporary directory, and use it as the
       configuration directory.
    5. A writable directory could not be found or created; return None.
    '''
    return _get_config_or_cache_dir(mpl._get_xdg_config_dir())

def get_fname():
    ''' Get the location of the Seaborn RC file.

    The file location is determined in the following order

    - `$PWD/seabornrc`

    - `$SEABORNRC/seabornrc`

    - `$SNSCONFIGDIR/seabornrc`

    - On Linux,

          - `$HOME/.seaborn/seabornrc`, if it exists

          - or `$XDG_CONFIG_HOME/seaborn/seabornrc` (if
            $XDG_CONFIG_HOME is defined)

          - or `$HOME/.config/seaborn/seabornrc` (if
            $XDG_CONFIG_HOME is not defined)

    - On other platforms,

         - `$HOME/.seaborn/seabornrc` if `$HOME` is defined.

    - Lastly, it looks in `$SEABORNDATA/seabornrc` for a
      system-defined copy.

    This function is copied from `matplotlib.matplotlib_fname`.
    '''
    if six.PY2:
        cwd = os.getcwdu()
    else:
        cwd = os.getcwd()
    fname = os.path.join(cwd, 'seabornrc')
    if os.path.exists(fname):
        return fname

    if 'SEABORNRC' in os.environ:
        path = os.environ['SEABORNRC']
        if os.path.exists(path):
            fname = os.path.join(path, 'seabornrc')
            if os.path.exists(fname):
                return fname

    configdir = _get_configdir()
    if configdir is not None:
        fname = os.path.join(configdir, 'seabornrc')
        if os.path.exists(fname):
            home = mpl.get_home()
            if (sys.platform.startswith('linux') and
                home is not None and
                os.path.exists(os.path.join(
                    home, '.seaborn', 'seabornrc'))):
                warnings.warn(
                    "Found seaborn configuration in ~/.seaborn/. "
                    "To conform with the XDG base directory standard, "
                    "this configuration location has been deprecated "
                    "on Linux, and the new location is now %s/seaborn/. "
                    "Please move your configuration there to ensure that "
                    "seaborn will continue to find it in the future." %
                    mpl._get_xdg_config_dir())
                return os.path.join(
                    home, '.seaborn', 'seabornrc')
            return fname

def load(fname=None):
    ''' Load Seaborn RC file.

    Parameters
    ==========
    fname : str or None
        The path to the RC file. If None, use the RC file returned by
        `get_fname()`.
    '''

    if fname is None:
        fname = get_fname()

    if fname:
        rc = mpl.rc_params_from_file(
            fname,
            use_default_template=False,
            )
        sns.set(rc=rc)

    else:
        warnings.warn('No Seaborn configuration file found.')
