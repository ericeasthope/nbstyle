# nbstrux
Tweaks and hacks for Jupyter notebooks

In any code cell within a Jupyter notebook (Python 3),

```
!pip install --upgrade --force-reinstall --user git+git://github.com/ericeasthope/nbstrux.git#egg=nbstrux
!jupyter nbextension enable --py --user nbstyle
```

To disable `nbstyle`,

```
!jupyter nbextension disable --py --user nbstyle
```
