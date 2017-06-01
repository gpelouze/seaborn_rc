Configure Seaborn through a RC file, similarly to how Matplotlib does it.

To load the configuration from the RC file, simply import this package after
seaborn:

~~~python
>>> import seaborn as sns
>>> import seaborn_rc
~~~

To reload the RC file:

~~~python
>>> seaborn_rc.load()
~~~

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


# License

Copyright (c) 2017 Gabriel Pelouze

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

Functions used to find the RC file (`_get_config_or_cache_dir`,
`_get_configdir`, and `get_fname`), were adapted from Matplotlib 2.0.2,
distributed with the following copyright notice: Copyright (c) 2012-2013
Matplotlib Development Team; All Rights Reserved.
