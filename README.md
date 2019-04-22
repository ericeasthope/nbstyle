# nbstyle
Personal UI styling for Jupyter notebooks

In any code cell within a Jupyter notebook (Python 3),

```
!pip install --user git+git://github.com/ericeasthope/nbstyle.git#egg=nbstyle
!jupyter nbextension install --py --user nbstyle
!jupyter nbextension enable --py --user nbstyle
```

Refresh the notebook to see changes take effect.

To disable and uninstall`nbstyle`,

```
!jupyter nbextension disable --py --user nbstyle
!jupyter nbextension uninstall --py --user nbstyle
```
