define([
    'require',
    'jquery',
    'base/js/namespace'
], function(
    requirejs,
    $,
    Jupyter
) {
    "use strict";

    // define default values for config parameters
    var params = {
        dummyConfig: undefined
    };

    var initialize = function () {
        // update params with any specified in the server's config file
        $.extend(true, params, Jupyter.notebook.config.thisextension);

        // find relative url path to custom style sheets, generate style tag
        var cssPath = Jupyter.notebook.base_url + "nbextensions/nbstyle/restyle.css",
            cssTag = "<link rel=\"stylesheet\" type=\"text/css\" href=\"" + cssPath + "\">";

        // append custom style sheets
        $("head").append(cssTag);
    };

    // called when nbextension is to be loaded
    var load_ipython_extension = function () {
        // once config loaded, do everything else
        // loaded object is a javascript Promise object
        return Jupyter.notebook.config.loaded.then(initialize);
    };

    // return object to export public methods
    return {
        load_ipython_extension: load_ipython_extension
    };
});
