#!/usr/bin/env python
# -*- coding: utf-8 -*-

def _jupyter_server_extension_paths():
    return [{
        "module": "nbstyle"
    }]

# Jupyter Extension points
def _jupyter_nbextension_paths():
    return [
        dict(
            section="notebook",
            src="static",          # path is relative to `nbstyle` directory
            dest="nbstyle",        # directory in the `nbextension/` namespace
            require="nbstyle/main" # _also_ in the `nbextension/` namespace
        )
    ]

def load_jupyter_server_extension(nbapp):
    nbapp.log.info("nbstyle enabled!")
