transform firework_tint:
    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.8 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 1.2 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 0.6 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 1.0 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 1.6 matrixcolor TintMatrix("#ffffff") alpha 0.0  

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.7 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 1.5 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 0.9 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 0.5 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 1.3 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 0.8 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 1.0 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 1.9 matrixcolor TintMatrix("#ffffff") alpha 0.0  

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 0.7 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 1.4 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.6 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 1.1 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 0.9 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 1.2 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.5 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 1.3 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 0.8 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 2.0 matrixcolor TintMatrix("#ffffff") alpha 0.0  

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.8 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 1.2 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 0.6 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 1.0 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 1.6 matrixcolor TintMatrix("#ffffff") alpha 0.0  

    linear 0.1 matrixcolor TintMatrix("#3e8afc") alpha 1.0
    linear 0.7 matrixcolor TintMatrix("#3e8afc") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#d83cff") alpha 1.0
    linear 1.5 matrixcolor TintMatrix("#d83cff") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ff4c4c") alpha 1.0
    linear 0.9 matrixcolor TintMatrix("#ff4c4c") alpha 0.0

    linear 0.1 matrixcolor TintMatrix("#ffd13b") alpha 1.0
    linear 0.5 matrixcolor TintMatrix("#ffd13b") alpha 0.0

    repeat

image gazing_into_the_night:
    "images/cgs/fireworks/base_for.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/forward/b_pink.png" with Dissolve (0.1)
    pause 0.1
    "images/cgs/fireworks/base_for.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/forward/b_yellow.png" with Dissolve (0.1)
    pause 0.1
    "images/cgs/fireworks/base_for.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/forward/b_purple.png" with Dissolve (0.1)
    pause 0.1
    repeat

image gazing_at_you:
    "images/cgs/fireworks/base_turn.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/turn/t_pink.png" with Dissolve (0.1)
    pause 0.1
    "images/cgs/fireworks/base_turn.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/turn/t_yellow.png" with Dissolve (0.1)
    pause 0.1
    "images/cgs/fireworks/base_turn.png" with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/turn/t_purple.png" with Dissolve (0.1)
    pause 0.1
    repeat

image set_boom:
    Null() with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/boom/f_pink.png" with Dissolve (0.1)
    pause 0.1
    Null() with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/boom/f_yellow.png" with Dissolve (0.1)
    pause 0.1
    Null() with Dissolve (4.0)
    pause 4
    "images/cgs/fireworks/boom/f_purple.png" with Dissolve (0.1)
    pause 0.1
    repeat