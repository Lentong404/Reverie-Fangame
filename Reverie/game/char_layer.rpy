##Baxter
    #animations
image b_normal_blink:
    "characters/baxter/expressions/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_side_blink:
    "characters/baxter/expressions/e_side.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_wide_blink:
    "characters/baxter/expressions/e_wide.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_surprised_blink:
    "characters/baxter/expressions/e_surprised.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_side_down_blink:
    "characters/baxter/expressions/e_side_down.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_squint_blink:
    "characters/baxter/expressions/e_squint.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

image b_squint_dl_blink:
    "characters/baxter/expressions/e_squint_d_l.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/baxter/expressions/e_closed.png"
    pause 0.05
    repeat

##Atributions

layeredimage b:

    always:
        "characters/baxter/base.png"

    #Special
    group face-lower:
        attribute sweat:
            "characters/baxter/expressions/sweat.png"
        attribute sweat_two:
            "characters/baxter/expressions/sweat_two.png"

    group face-middle:
        attribute blush:
            "characters/baxter/expressions/blush.png"
    
    group other:
        attribute star:
            "characters/baxter/expressions/star.png"

    #Mouth
    group mouth:
        attribute m_norm:
            "characters/baxter/expressions/m_smile.png"
        attribute m_sad:
            "characters/baxter/expressions/m_sad.png"
        attribute m_confused:
            "characters/baxter/expressions/m_confused.png"
        attribute m_grin:
            "characters/baxter/expressions/m_grin.png"
        attribute m_pout:
            "characters/baxter/expressions/m_frown.png"
        attribute m_vmouth:
            "characters/baxter/expressions/m_s_smile.png"
        attribute m_smug:
            "characters/baxter/expressions/m_smug.png"
        
    #Eyes
    group eyes:
        attribute e_norm default:
            "b_normal_blink"
        attribute e_norm-still:
            "characters/baxter/expressions/e_norm.png"
        attribute e_closed:
            "characters/baxter/expressions/e_closed.png"
        attribute e_side:
            "b_side_blink"
        attribute e_side-still:
            "characters/baxter/expressions/e_side.png"
        attribute e_wide:
            "b_wide_blink"
        attribute e_surprised-still:
            "characters/baxter/expressions/e_surprised.png"
        attribute e_surprised:
            "b_surprised_blink"
        attribute e_wide-still:
            "characters/baxter/expressions/e_wide.png"
        attribute e_side_down:
            "b_side_down_blink"
        attribute e_side_down-still:
            "characters/baxter/expressions/e_side_down.png"
        attribute e_squint-still:
            "characters/baxter/expressions/e_squint.png"
        attribute e_squint:
            "b_squint_blink"
        attribute e_squint_dl-still:
            "characters/baxter/expressions/e_squint_d_l.png"
        attribute e_squint_dl:
            "b_squint_dl_blink"
        
    
    #Brows
    group brows:
        attribute b_norm default:
            "characters/baxter/expressions/b_norm.png"
        attribute b_annoyed:
            "characters/baxter/expressions/b_annoyed.png"
        attribute b_angry:
            "characters/baxter/expressions/b_angry.png"
        attribute b_one_raised:
            "characters/baxter/expressions/b_one_raised.png"
        attribute b_raised:
            "characters/baxter/expressions/b_raised.png"
        attribute b_raised1:
            "characters/baxter/expressions/b_raised_1.png"
        attribute b_sad:
            "characters/baxter/expressions/b_sad.png"
        attribute b_soft:
            "characters/baxter/expressions/b_soft.png"


#River Lanterns CG
image rl_blink:
    "cgs/lanterns/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "cgs/lanterns/e_closed.png"
    pause 0.05
    repeat

layeredimage rl:
    
    always:
        "cgs/lanterns/base.png"

    group eyes:
        attribute e_norm default:
            "rl_blink"
        attribute e_norm-still:
            "cgs/lanterns/e_norm.png"
        attribute e_closed:
            "cgs/lanterns/e_closed.png"


#Final CG
image handout_blink:
    "cgs/by_your_side/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "cgs/by_your_side/e_closed.png"
    pause 0.05
    repeat

layeredimage handout:
    
    always:
        "cgs/by_your_side/base.png"

    group eyes:
        attribute e_norm default:
            "handout_blink"
        attribute e_norm-still:
            "cgs/by_your_side/e_norm.png"
        attribute e_closed:
            "cgs/by_your_side/e_closed.png"


##August
image a_blink:
    "characters/august/expressions/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/august/expressions/e_closed.png"
    pause 0.05
    repeat



layeredimage a: 
    always:
        "characters/august/base.png"

    group face-middle:
        attribute glasses:
            "characters/august/expressions/glasses.png"
    
    group other:
        attribute shock:
            "characters/august/expressions/shock.png"
        attribute tear:
            "characters/august/expressions/tear.png"

    #Mouth
    group mouth:
        attribute m_norm:
            "characters/august/expressions/m_frown.png"
        attribute m_sad:
            "characters/august/expressions/m_sad.png"
    #Brows
    group brows:
        attribute b_norm default:
            "characters/august/expressions/b_angry.png"
        attribute b_angry:
            "characters/august/expressions/b_angry.png"
        attribute b_sad:
            "characters/august/expressions/b_sad.png"
    #Eyes
    group eyes:
        attribute e_norm default:
            "a_blink"
        attribute e_norm-still:
            "characters/august/expressions/e_norm.png"
        attribute e_closed:
            "characters/august/expressions/e_closed.png"


#Ruri
image r_blink:
    "characters/ruri/expressions/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/ruri/expressions/e_closed.png"
    pause 0.05
    repeat


layeredimage r: 
    always:
        "characters/ruri/base.png"
    #Eyes
    group eyes:
        attribute e_norm default:
            "r_blink"
        attribute e_norm-still:
            "characters/ruri/expressions/e_norm.png"
        attribute e_closed:
            "characters/ruri/expressions/e_closed.png"
        attribute e_happy:
            "characters/ruri/expressions/e_happy.png"

##Maggie


image m_blink:
    "characters/maggie/expressions/e_norm.png"
    choice:
        pause 0.1
    choice:
        pause 2
    choice:
        pause 5
    choice:
        pause 8
    "characters/maggie/expressions/e_closed.png"
    pause 0.05
    repeat


layeredimage m: 
    always:
        "characters/maggie/base.png"
    #Eyes
    group eyes:
        attribute e_norm default:
            "m_blink"
        attribute e_norm-still:
            "characters/maggie/expressions/e_norm.png"
        attribute e_closed:
            "characters/maggie/expressions/e_closed.png"
    
##Zelenka


##Felix

##Dalton

##Quinn

##Ollie

