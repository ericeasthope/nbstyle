#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
'''

def _jupyter_server_extension_paths():
    return [{
        'module':'nbstyle'
    }];

def _jupyter_nbextension_paths():
    return [
        dict(
            section='notebook',
            src='static',          # path is relative to `nbstyle` directory
            dest='nbstyle',        # directory in `nbextension/` namespace
            require='nbstyle/main' # _also_ in `nbextension/` namespace
        )
    ];

def load_jupyter_server_extension(nbapp):
    import restyle
    nbapp.log.info('Loaded nbstyle!');