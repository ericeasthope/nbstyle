# nbstrux
Tweaks and hacks for Jupyter notebooks

In any code cell within a Jupyter notebook (Python 3),

```
!pip install --upgrade --force-reinstall --user git+git://github.com/ericeasthope/nbstrux.git#egg=nbstrux
!jupyter nbextension install --py --user nbstyle
!jupyter nbextension enable --py --user nbstyle
```

Refresh the notebook to see changes take effect.

To disable and uninstall`nbstyle`,

```
!jupyter nbextension disable --py --user nbstyle
!jupyter nbextension uninstall --py --user nbstyle
```
