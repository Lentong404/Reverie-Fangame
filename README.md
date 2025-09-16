# Reverie Fangame
Fangame created in Renpy, a python based engine to create visual novels


Code created that was not originally in use within the engine.

```python
screen choice(items):
    style_prefix "choice"
    
    vbox:
        for i in items:
            textbutton i.caption:
                action [i.action, Function(narrator.add_history, kind="adv",who=__("Choice:"),what=__(i.caption))]
                # adds choice text to history
                
                ##i.kwargs = Keyword arguments
                if "color" in i.kwargs:
                    idle_background Transform("gui/button/choice_white_idle.png")
                    hover_background Transform("gui/button/choice_" + i.kwargs["color"] + "_hover.png")
```
Renpy's engine only uses 1 idle and 1 hover button colors, to have different ones, I used kwargs to select different versions of the idle/hover state images. 