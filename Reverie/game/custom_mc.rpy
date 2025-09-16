



screen custom_input(label_text=Null, variable_name=Null):
    # add "custom/mc_creator_notext.png"
    add "custom/mc_creator.png"
    style_prefix "custom_input"
    modal True
    zorder 100

    # hbox:
        
    #     text "Comfort":
    #         pos(0, 0)

    #     fixed:
    #         text "My Relationship \nwith Baxter":
    #             text_align 0.5
    #             color "#000000"
    #             font "fonts/lemonada-regular.ttf"
                
    #             xalign 0.5
    #             ypos 50


    #     text "Iniatitve":
    #         pos(0, 0)
    
    vbox:
        
        hbox:
            spacing 650
            pos (60,250)
            vbox:
                xysize (200, 500)
                # Direct
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/direct_inactive.png"
                    selected_idle "custom/direct.png"
                    hover "custom/direct.png"
                    action SetVariable("mc_persona", 1)
                # Relaxed
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/relaxed_inactive.png"
                    selected_idle "custom/relaxed.png"
                    hover "custom/relaxed.png"
                    action SetVariable("mc_persona", 2)
                # Nervous
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/nervous_inactive.png"
                    selected_idle "custom/nervous.png"
                    hover "custom/nervous.png"
                    action SetVariable("mc_persona", 3)
            vbox:
                xysize (200, 500)
                # High
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/high_inactive.png"
                    selected_idle "custom/high.png"
                    hover "custom/high.png"
                    action SetVariable("b_initiative", 1)
                # Medium
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/medium_inactive.png"
                    selected_idle "custom/medium.png"
                    hover "custom/medium.png"
                    action SetVariable("b_initiative", 2)
                # Low
                imagebutton:
                    xalign 0.5
                    yalign 0.5
                    idle "custom/low_inactive.png"
                    selected_idle "custom/low.png"
                    hover "custom/low.png"
                    action SetVariable("b_initiative", 3)
        vbox:
            xalign 0.5
            ypos 200
            vbox:
                label label_text:
                    text_color gui.text_color
                    xalign 0.5
                null height 2
                input size 60 color "#ffffff" default globals()[variable_name] value VariableInputValue(variable_name, returnable=True) length 25:
                    yalign 1.0
                    xalign 0.5
                    xysize (450, 30)

        fixed:
            pos(875, 250)
            textbutton _("Ready!"):
                style_prefix "custom"
                action If(renpy.get_screen("statistics"), true=Hide("custom_input"), false=Return())


style custom_button_text is text:
    size 40
    font "fonts/lemonada-regular.ttf"
    hover_color "#d474d4"