from IPython.display import display, Javascript
from ipywidgets import widgets

display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:hide-toolbar')"))
display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:hide-header')"))
display(Javascript("$('div.input').hide();"))

def hidecode():
    
    toggle=widgets.ToggleButtons(
    options=['Show Code', 'Hide Code'],
    disabled=False,
    )

    display(toggle)

    def on_value_change(change):
    
        if change['new'] == 'Hide Code':
            display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:hide-toolbar')"))
            display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:hide-header')"))
            display(Javascript("$('div.input').hide();"))
        elif change['new'] == 'Show Code':
            display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:show-toolbar')"))
            display(Javascript("Jupyter.toolbar.actions.call('jupyter-notebook:show-header')"))
            display(Javascript("$('div.input').show();"))

    toggle.observe(on_value_change, names='value')
    
hidecode()