from IPython.display import HTML
import os

module_dir = os.path.dirname(os.path.abspath(__file__))
style_filepath = os.path.join(module_dir, 'signature.css')

def restyle():
    with open(style_filepath, 'r') as f:
        display(HTML('<style>' + f.read() + '</style>'))