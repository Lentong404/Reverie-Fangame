#Characters
define b = Character("Baxter")
define MC = "Jamie"

define h = "Hostess"
define s = "Employee"

#Cameos! 

define a = "Fox Enthusiast"
define r = "Lady in Purple"
define m = "Lady of Sunshine"

#Dunkers
define f = "Pale Young Man"
define d = "Stern Young Man"
define q = "Energetic Young Man"
define o = "Soft-Eyed Young Man"

#Story_traits
default mc_persona = 1    
default b_initiative = 1
default mc_height = 2

#Backgrounds
image matsuri = "images/background/matsuri.png"
image matsuri_food = "images/background/matsuri_food.png"
image innroom = "images/background/hotel.png"
image bamboo = "images/background/bamboo.png"
image change = "images/background/changeroom.png"
image lantern = "images/background/lantern.png"
image river = "images/background/river.png"
image maple = "images/background/maple.png"
image wisteria = "images/background/wisteria.png"

image yoyo = "images/background/water.png"


#Mini CG's 
image bax_at_yoyo = "images/mini_cgs/water_balloons.png"
image bax_at_shoot = "images/mini_cgs/shoot.png"
image bax_at_food = "images/mini_cgs/food.png"
image bax_at_kata = "images/mini_cgs/cookie.png"
image bax_at_string = "images/mini_cgs/laces.png"

#Still CG's

image your_side = "images/cgs/by_your_side/by_your_side_static.png"
image fw_forward = "images/cgs/firework/b_f_static.png"
image fw_turned = "images/cgs/firework/b_t_static.png"
image your_light = "images/cgs/lanterns/your_light.png"

#Animated CG's 



#'Global' Variables

#Clothing
default yukata = False
default jinbei = False
default normal_clothes = False
default flowers_p = False
default animals_p = False
default shapes_p = False 
default waves_p = False
default plants_pattern = False 
default solid_pattern = False 
#Accessories 
default hair_up = False
default bag = False
default sandals = False
default handfan = False
default acc_num = 0

#Festival Standard
default fest_food = False
default fest_games = False
default fest_fin = 0
default prizes_won = 0
default fox_mask_change = False
default b_opinion = False

#Vanishing Act 
default sep_early = False

#Food Section
default food_picked = 0
default yakisoba = False
default takoyaki = False 
default okonomiyaki = False
default karaage = False 
default kushiyaki = False 
default grilledmochi = False 

#Games Section 
default b_g_opinion = 0
default g_completed = 0

    #Yo-Yo Tsuri Flags
default yoyotsuri = False
default yoyo_win = 0
# 0 = Didn't play
# 1 = Win
# 2 = Lose

default baw_yoyo = 0
# 0 = Wanted to win it for yourself
# 1 = Told Baxter about it
# 2 = Didn't do anything
# 3 = Asked Baxter for it

default yoyo_owner = 0
# 0 = Baxter Only
# 1 = MC Only
# 2 = Both

    #Shateki Flags
default shateki = False
default shateki_win = 0
#0 - Didn't play
#1 - Win
#2 - Lost

default shots_left = 0
#0 - A lot left
#1 - Some left
#2 - none left
default sha_bax = False
default sha_yuzu = False
#Prizes
default sha_fox = False
default poke_plush = False
default large_plush = False
default yuzu_drink = False
default color_toy = False
default shiba_plush = False
default cove_plush = False

default drank_yuzu = False

    #Senbonbiki Flags
default senbonbiki = False 

default senbonbiki_play = False
#Prizes
default sen_fox = False
default tenugui = False
default ani_plush = False
default tissues = False
default acc_bracelet = False
default keychain = False

    #River Lantern Flags
default river_lanterns = False 

    #Katanuki Flags
default katanuki = False

default solo_cutting = False 

default kata_win = 0
#0 - Didn't play
#1 - win
#2 - Lose


#Shapes
default square_s = False
default rabbit_s = False
default tulip_s = False
default fish_s = False
default lant_s = False
default star_s = False

#CG Animated - Idk what for, but w/e I guess. Pop off or something.
image light_night = "images/cgs/fireworks/lit_night.png"
image bax_for = "images/cgs/fireworks/base_for.png"
image bax_turn = "images/cgs/fireworks/base_turn.png"

#turn hues
image bax_turn_yel = "images/cgs/fireworks/turn/t_yellow.png"
image bax_turn_pur = "images/cgs/fireworks/turn/t_purple.png"
image bax_turn_pin = "images/cgs/fireworks/turn/t_pink.png"
#forward hues
image bax_for_yel = "images/cgs/fireworks/forward/b_yellow.png"
image bax_for_pur = "images/cgs/fireworks/forward/b_purple.png"
image bax_for_pin = "images/cgs/fireworks/forward/b_pink.png"
#fireworks
image set_pink = "images/cgs/fireworks/boom/f_pink.png"
image set_purple = "images/cgs/fireworks/boom/f_purple.png"
image set_yellow = "images/cgs/fireworks/boom/f_yellow.png"

#Extending his hand cg 
image by_your_side = "images/cgs/by_your_side/base.png"
image fireworks_glow = "images/cgs/by_your_side/glow_1.png"




label start:

    call screen custom_input("Name:", "MC") with dissolve
    $ MC = MC.strip()
    if not MC:
        $ MC = "Jamie"
    
    #Changing Scene - Onsen Hotel Room
    play music sunset_landscape fadeout 1.0 fadein 1.0
    scene change:
        blur 25
    with dissolve
    "You and Baxter were currently in Kyoto, Japan and were staying at a popular onsen inn. There was a festival tonight, and the two of you had decided to go."
    "The hostess had asked if the two of you wanted to change into yukatas as part of the hotel package, and Baxter’s eyes lit up at the prospect."
    'He was charmed by the traditional outfits and wished to "truly immerse himself" as he had put it.'
    "He waved goodbye to you, excitement clear on his face as another host led him away to be changed."

    menu:
        "You shared your boyfriend's excitement!"(color = "yellow"):
            "On top of staying at a fancy hot spring inn, you were getting a one-of-a-kind experience with the package."
            "It was a great opportunity to explore a scenery that was different from where you lived. At the very least it was entirely unlike your hometown of Sunset Bird, and that alone had you feeling giddy."
        "You felt alright about everything."(color = "green"):
            "The experience was definitely something new, but you didn’t have any particular feelings either way."
            "{i}Whatever happens, happens,{/i} you thought. At the very least, you were glad to be here with Baxter."
        "You still felt nervous about being in another country."(color = "blue"):
            "But it was comforting knowing that Baxter was by your side. The two of you had already come so far together."
            "You did your best to alleviate your fears, after all this was a trip with your boyfriend! You would try to stay positive."
    
    show change:
        blur 0
    with dissolve
    "The clatter of the shoji door closing whisked you back from whatever thoughts you were having."
    "The attendant that had led you through the inn moved to the side so you had a good view of the room."
    "Rows of clothing hung on hangers, the delicate looking fabric a myriad of patterns and colors. Beside the mirror, beautiful accessories and bags sat waiting to be admired on the nearby table."
    "You turned your attention back to the hostess, who had a warm smile on her face as she caught your gaze."
    h "Honored guest, is there anything here that catches your eye?"
    "You decided on..."

    
    
    menu: 
        "A Yukata."(color = "yellow"):
            $ yukata = True
            "And the pattern was..."
            jump pattern_select
        "A Jinbei."(color = "green"):
            $ jinbei = True
            "And the pattern was..."
            jump pattern_select
        "Your normal clothes."(color = "blue"):
            $ normal_clothes = True
            h "Of course, right this way please."
            "As you passed the screen, you caught a glimpse of yourself in the mirror."
            jump height_choice
    
    menu pattern_select :
        "Flowers":
            $flowers_p = True
            jump change_scene
        "Animals":
            $animals_p = True
            jump change_scene
        "Geometric":
            $shapes_p = True
            jump change_scene
        "Waves":
            $waves_p = True
            jump change_scene
        "Plants":
            $plants_pattern = True
            jump change_scene
        "A solid color":
            $solid_pattern = True
            jump change_scene

    label change_scene:
        h "Please feel free to change here. I will assist you with the garment afterwards should you require it."
        "She welcomed you over to the partition, decorated with branches of a maple tree. There was a basket for your clothes in the corner."
        "As you moved behind the divider, you caught a glimpse of yourself in the mirror."
        jump height_choice
    
    menu height_choice: 
        "You were quite tall, and nearly went out of frame."(color = "yellow"):
            $ mc_height = 1
        "You were of average height, and it reflected in the mirror."(color = "green"):
            $ mc_height = 2
        "You were short, and had room in the mirror to spare."(color = "blue"):
            $ mc_height = 3
            
    if mc_persona == 1:
        "You made a funny face in the mirror before returning to the task at hand."
    elif mc_persona == 2:
        "Your gaze met your reflection's before you turned back to the task at hand."
    elif mc_persona == 3: 
        "You tilted your head and your reflection mimicked it before you returned to the task at hand."
    if normal_clothes:
        jump acc_select
    elif yukata:
        jump yukata_change
    elif jinbei:
        jump jinbei_change

    label yukata_change:
        "You removed your current clothes and slipped into the light fabric. Tying the yukata closed with a cord, you left a bit of the fabric hanging out."
        "After a few more adjustments, the yukata sat perfectly on your shoulders."
        "Stepping out from behind the screen, you were met with the hostess' beaming smile as she held the accompanying obi in her hands."
        "She had made sure the Yukata fit correctly, and assisted with the finishing touches."
        jump acc_select
    
    label jinbei_change:
        "Moving behind the screen you removed your current clothes and slipped into the light fabric. The Jinbei was easy to wear, consisting of shorts and a jacket-like top."
        "You tied the jacket closed with a simple knot and stepped out, meeting the hostess' beaming smile."
        "She had made sure the Jinbei fit comfortably, and that you were satisfied with your choice."
        jump acc_select
    
    label  acc_select:
        if normal_clothes == True:
            h " Would you like any accessories or styling?"
        else:
            h " Would you like any further accessories or styling?"
        "You looked over to the table lined with accessories and thought about what you wanted."
        menu acc_menu:
            "Putting up your hair."(color = "yellow") if hair_up == False:
                $hair_up = True
                $acc_num += 1
                "You sat down at the dressing table as the hostess helped tie your hair into a bun, held up neatly by a hair ornament."
                jump acc_menu

            "A matching bag."(color = "green") if bag == False:
                $bag = True
                $acc_num += 1
                "The extra storage space would come in handy. Its lovely pattern hung delicately by your side."
                jump acc_menu

            "Geta sandals."(color = "blue") if sandals == False:
                $sandals = True
                $acc_num += 1
                "You slipped into the wooden shoes and took a few steps to ensure they fit comfortably and wouldn’t slip off."
                jump acc_menu

            "A hand fan."(color = "yellow") if handfan == False:
                $handfan = True
                $acc_num += 1
                "It would do well to stave off the heat and humidity you were certain to meet out there."
                jump acc_menu

            "And that was all."(color = "green") if acc_num >= 1:
                jump meeting_baxter
 
            "You declined."(color = "blue") if acc_num < 1:
                jump meeting_baxter
    
    label meeting_baxter:
        "With a slight bow, the hostess led you back through the halls to the main entrance."
        play music autumn_scene fadeout 1.0 fadein 1.0
        scene maple 
        show b b_norm e_side m_norm
        with dissolve
        "You found Baxter sitting near the courtyard of the inn, his arms partly crossed as he fanned himself with a black fan."
        "He wore his yukata well, and seemed at ease. You noticed he had chosen to wear his favorite colors, as the fabric split down the middle with one half white and one half black."
        "He was gazing out at the yard, where maple trees bloomed with vivid red leaves, reminiscent of fall."
        "If you looked closely into his eyes, you could see gentle admiration for the colors matching the season he loved so much."
        show b e_norm
        "As you neared, Baxter shifted his gaze towards you, the adoration having never left those warm brown eyes of his."

        menu:
            '"Fancy meeting you here!"' (color = "yellow"):
                show b b_one_raised
                MC "Do you come here often?"
                show b b_norm e_closed m_norm
                "You waggled your eyebrows for emphasis, and Baxter brought a hand up to stifle his laughter."
                show b e_norm
                b "Not at all, I'm afraid."
                "He placed his hand over his chest, looking entirely too innocent despite that familiar smirk gracing his lips."
                show b e_closed m_grin
                b "I'm a {i}tourist{/i}, you see."
                show b b_soft e_norm m_norm
                "You laughed in response."
            '"You look great."' (color = "green"):
                show b e_closed m_grin
                b "Why, thank you."
                "Baxter grinned, happy to be sporting the familiar colors of his initials."
            '"That was fast."' (color = "blue"):
                show b b_one_raised
                MC "I guess choosing colors must have been easy."
                "You hummed, eyeing the color scheme."
                show b e_wide b_raised
                "Baxter looked down at his yukata in mock surprise, as if he hadn't been the one to choose his outfit."
                show b e_closed b_norm m_grin
                b"Now when did this happen? I'm shocked." 
            '"Are you going to survive without your dress shirt?"' (color = "yellow"):
                show b b_annoyed 
                "You snickered good-naturedly as Baxter rolled his eyes dramatically."
                show b b_norm e_side
                b "In truth, I considered wearing it underneath..."
                show b e_norm b_raised
                b"But to answer your question: yes, I will survive."
                show b b_annoyed m_grin
                b "After all, I'd like to enjoy your company for a very long time."
            "You gave a wave." (color = "green"):
                "Baxter returned it with an inclination of his head."
                show b b_soft
                "You could see him gazing at you fondly, his mouth opening and closing slightly as if he had something to say."
            "You blushed shyly." (color = "blue"):
                show b b_soft
                "You felt a bit of heat color your cheeks as your gaze drifted from his eyes. He cut a dashing figure in that outfit."
                show b b_one_raised e_squint
                "You heard him give a little hum, and as you lifted your eyes slightly to meet his gaze, you could see him enjoying your reaction."
                "Thankfully (or perhaps not), he made no further comments about your staring."
        
        show b e_norm m_norm b_soft
        "There was a gentle lull in the air as Baxter's eyes swept over your own choice of apparel for the evening. He sighed contentedly, like he was drinking in the sight of you."
        show b e_closed b_norm
        if flowers_p == True:
            b "I must say, the only thing that outshines the talent put into the delicate embroidery of the flowers, is how well you wear it, [MC]."
            show b e_norm b_soft
            b "You are truly radiant."
        elif animals_p == True:
            b "There's something truly incredible in seeing such a splendid design being worn by someone who can bring the art to life."
            show b e_norm b_soft
            b "You look positively endearing in that design."
        elif shapes_p == True:
            b "You look striking, [MC]. The purposeful design truly makes you quite eye-catching."
            show b e_norm b_soft
            b "You can see the incredible craftsmanship that has gone into that design."
        elif waves_p == True: 
            b "I should've surmised that you'd choose such a nostaglic-looking pattern."
            b "It does bring back lovely memories of our time together."
            show b e_norm b_soft
            b "You've been constantly breathtaking in each one."
        elif plants_pattern == True: 
            b "The botanical theme suits you quite well. The flow accentuates your form beautifully."
            show b e_norm b_soft
            b "You are as enchanting as ever."
        elif solid_pattern == True:
            b "Looks like we both couldn’t help ourselves. You look as stunning as ever in that shade."
            show b e_norm b_soft
            b "It brings out the color of your lovely eyes."
        elif normal_clothes == True: 
            b "You're always a sight for sore eyes, [MC]."
            show b e_norm b_soft
            b "I {i}do{/i} hope you aren't tired of me saying such words."
        
        show b m_grin
        if acc_num >= 2:
            b "And I love the accessories you've chosen. They really bring your ensemble together."
        else:
            b "And I love the accessory you've chosen. Simple, but effective in bringing your ensemble together."
        
        show b b_sad m_norm
        b "But forgive me, if I were to continue singing your praises we'd be here all evening. Shall we be off?"

        if mc_persona == 1:
            MC "Yeah, let's go!"
        elif mc_persona == 2:
            MC "Mhm."
        elif mc_persona == 3:
            "You gave a nod of affirmation."
        
        #Road to the Festival
        scene bamboo
        show b b_norm e_closed m_norm
        with dissolve
        "The road to the festival was quiet, and the sun had already begun to set. The buildings around you were dim and devoid of any signs of life."
        show b e_side_down
        "There wasn’t a soul to be seen along the path you walked."

        menu:
            "You and Baxter took a few dance steps down the street." (color = "yellow"):
                show b e_squint with dissolve:
                    zoom 1.25 yoffset 200
                "The two of you exchanged knowing glances as Baxter pantomimed a dance stance. You took his imaginary invitation as the two of you began to move in tandem."
                show b e_norm
                "You followed a few basic steps together, Baxter not wanting to accidentally loosen his obi."
                show b e_closed b_soft
                "Taking turns leading this impromptu ballroom waltz, Baxter glowed with happiness with each step and slight dip."
                show b b_one_raised e_norm with dissolve:
                    zoom 1 yoffset 0
                "As a pseudo finisher, he took a few steps forward, giving a small twirl to show you his two toned yukata in full."
                show b b_norm
                "You could see the fan he was using earlier tucked into the belt behind his back, with a little white koi fish swimming on its lonesome."
            "You asked Baxter how the change went." (color = "green"):
                show b e_norm b_one_raised m_grin
                b "Well, I'm positive you could imagine my surprise when they told me I could pick out anything I wanted."
                show b b_norm e_closed
                b "The choice was rather daunting,  since everything they had was utterly {i}marvelous.{/i}"
                show b e_side_down m_norm
                b "I was torn on this lovely shade of violet for a while...but then I kept thinking there {i}had{/i} to be another choice."
                show b e_closed
                b "And there it was, the perfect outfit for the evening."
                show b e_squint m_grin
                b "It had my name on it; {i}quite literally,{/i} in fact."
                show b e_closed m_norm
                b "He gave a small twirl to show you his two toned yukata in full."
                "You could see the fan he was using earlier tucked into the belt behind his back, with a little white koi fish swimming on its lonesome."
                show b e_closed m_norm 
                b "I hope your change was equally as pleasant, [MC]."
                show b b_one_raised e_norm
                "You told him about your own experience and he nodded along, enraptured by your retelling. He simply enjoyed sharing experiences with you, no matter how mundane."
                show b b_norm
                "You were certain he would be equally as interested even if you were telling him about paint drying."
            "You enjoyed the silent walk together." (color = "blue"):
                show b e_side
                "The streets of Kyoto were dimly lit by the setting sun, casting a brilliant shade of red and orange over the area."
                "Most of the shops around had closed up for the evening, no doubt in preparation for the festival."
                "You could feel the old capital’s tradition seeping from every step you took with Baxter, coupled with the sounds of his geta sandals hitting cobblestone."
                "Baxter was taking in the sights for himself like one would do at a museum, carefully admiring each building as if it were the next turn of century art."
                show b e_norm
                "You glanced at Baxter and, unsurprisingly, caught his gaze."
                show b e_squint m_grin
                "With your attention on him, he boldly went a few steps ahead of you, giving a small twirl to show off his two-toned yukata in full."
                show b m_norm
                "You could see the fan he was using earlier tucked into the belt behind his back, with a little white koi fish swimming on its lonesome."
                show b e_closed
                "He finished his twirl with a satisfied look on his face."
                show b e_norm m_norm
                "The two of you eventually fell back into a steady walk as more people began appearing around you."
        
        
        #Festival
        play music lets_build_a_secret_base_2 fadeout 1.0 fadein 1.0
        scene matsuri_food
        show b b_norm e_side m_norm
        with dissolve
        "The quiet sunset began giving way to a sea of colors, like vivid blooming flowers. Most in the crowd were also wearing yukatas, filling the atmosphere with liveliness and laughter."
        "A delicious scent accompanied it, bringing to mind a variety of grilled delicacies and desserts. There certainly seemed like there was a lot to do."
        "Baxter was glancing around like he had typically done, watching and waiting to see what he should do."
        show b e_norm b_one_raised
        b "I took the liberty of looking at the festival events earlier, and the fireworks will be a little later in the evening."
        show b e_side
        b "Until then, there are a number of activities available as well as food selections."
        show b e_norm
        b "Did you have any preferences, [MC]? I am ever willing to go anywhere as long as it's with you."
        show b b_norm
        "That last sentence had been delivered with the same honesty as he had continuously possessed, but you knew there was more to it now."
        "Baxter Ward had been a tourist in more than the literal sense, living every day to its fullest before moving on to the next."
        "He had resigned himself to being a part of the background; an extra that would soon be forgotten from everyone’s mind."
        "Yet this time, he'd kept pace with you. Walked alongside you, and he would continue to do. Forever and Always."
        "With that thought in mind, you answered Baxter."

        menu date_options:
            "You felt like getting some food first."(color = "yellow") if fest_food == False and fest_fin < 1:
                jump festival_food

            "You were content to get some food." (color = "yellow") if fest_food == False and fest_fin >= 1:
                jump festival_food

            "You wanted to try out the games first." (color = "green") if fest_games == False and fest_fin < 1: 
                jump festival_games

            "You wanted to try out the games now." (color = "green") if fest_games == False and fest_fin >= 1:
                jump festival_games

            "You suddenly felt under the weather."(color = "blue") if fest_fin < 1:
                jump separation_early

            "You were starting to feel a bit under the weather."(color = "blue") if fest_fin >= 1:
                jump separation_early

            "You asked Baxter what he wanted to do first." (color ="baxter") if fest_fin < 1 and b_opinion == False:
                $ b_opinion = True
                show b b_one_raised e_side_down
                "Baxter hummed thoughtfully, cupping his chin with his hand."  
                show b e_norm b_norm
                b "I think I would like to see the games first, and then we can have something to eat."
                show b e_closed
                b "There are a few booths that have piqued my interest, and there's nothing like working up an appetite."
                "Baxter was prepared with a plan no matter what the occasion was, it seemed."
                show b e_norm m_grin
                b "But of course, as you well know by now, I am quite flexible."
                "He delivered the line with a chuckle, bringing back his familiar ability to change gears at the drop of a hat."
                show b e_norm m_norm
                jump date_options

        label festival_food:
            $ fest_fin += 1
            $ fest_food = True
            play music hidamaritronica fadeout 1.0 fadein 1.0
            scene matsuri_food
            show b b_norm e_side_down m_norm
            with dissolve
            #CHECK
            "Heading in the direction of the food stalls, the delicious scent from earlier grew stronger with every passing step."
            "A line of standing tables stood off to the side for people to use, and across from several popular-looking booths."
            "Whether a person was hungry or just peckish, there seemed to be plenty to choose from."
            show b b_raised e_wide m_norm
            "Baxter himself seemed rather excited in particular. He was already reading several of the menus and posters around the stalls."
            b "I’m eager to try some of the local delicacies. A majority of the stalls seem to be selling vegetarian or pescatarian friendly meals."
            show b b_one_raised e_norm 
            b "Have you decided on what you’d like to have? I believe I’ll have the yakisoba and a few skewers."
            "Baxter had raised a good question: what to have?"

            menu food_selection: 
                "Yakisoba (Fried noodles)." (color = "yellow") if yakisoba == False:
                    $yakisoba = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "Takoyaki (Grilled octopus)."(color = "green") if takoyaki == False:
                    $takoyaki = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "Okonomiyaki (Japanese pancake)."(color = "blue") if okonomiyaki == False:
                    $okonomiyaki = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "Karaage (Fried chicken)."(color = "yellow") if karaage == False:
                    $karaage = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "Kushiyaki (Grilled Skewers)."(color = "green") if kushiyaki == False:
                    $kushiyaki = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "Grilled Mochi (Rice cake)."(color = "blue") if grilledmochi == False:
                    $grilledmochi = True 
                    $food_picked +=1
                    if food_picked >= 5:
                        jump eating_together
                    else:
                        jump food_selection
                "And that was all."(color = "yellow") if food_picked >= 1: 
                    jump eating_together
                "You had changed your mind and didn't want anything."(color = "green") if food_picked <= 0:
                    show b b_raised e_norm m_confused
                    b "Oh, are you certain?"
                    MC "Yeah, we can get what you'd like instead."
                    show b e_closed b_norm m_norm
                    b "Very well. If you change your mind, please don't hesitate to let me know."
                    show b e_side_down b_annoyed 
                    b "Or... you may feel free to, ah, 'commandeer', some of mine."
                    jump eating_together



            label eating_together:
                if food_picked > 0:
                    hide b
                    show bax_at_food
                    with dissolve
                    "After the decisions had been made, the two of you split up to order. It was easier to divide and conquer, as the lines seemed long even with their quick and efficient service."
                    "Then, with your food choices in hand, the two of you headed to one of the tables off to the side."
                    "Baxter had gotten a small portion of yakisoba, with three vegetarian skewers resting neatly on his other plate."
                    "The food was delicious, and you could feel the flavors melting on your tongue." 
                else: 
                    hide b
                    show bax_at_food
                    with dissolve
                    "Baxter waited in line while you made sure there was a table available. The lineup seemed long despite the quick and efficient service, so it had been easier to divide the tasks amongst the two of you."
                    "Not long after, he returned with two plates balanced in his hands perfectly, like a seasoned waiter."
                    "He had gotten a small portion of Yakisoba, with three vegetarian skewers resting neatly on his other plate."
                    
                hide bax_at_food
                with dissolve
                "Throughout the one-sided feast, the two of you talked about whatever struck your fancy."
                show b e_closed b_norm m_grin
                with dissolve
                "Baxter specifically was telling you about an interesting couple that had gotten married not too long ago."
                show b e_norm b_one_raised m_norm
                b "They had a very interesting story on how their proposal went. The husband, a lovely man, had hired a rather famous Oootuber famed for photographing strangers and their dogs."
                show b e_norm b_one_raised m_norm
                b "Feigning as if he had only bumped into them, he had begun with his usual greeting of asking if their dog was friendly, and offered them free photos on the nearby beach."
                show b e_closed b_norm m_norm
                b "The professional he was, he had the partner’s attention fully, allowing their husband to kneel behind them and propose."
                show b e_side_down b_raised
                b "I thought it was charming, and they had several photos of the moment displayed at their wedding. Their dog made an excellent ring bearer; very well mannered and courteous."
                show b e_squint b_annoyed m_norm
                b "I may have watched... a {i}few{/i} of his videos after that."
                show b e_norm b_norm
                menu: 
                    #CHECK
                    "Steal some of his food!" (color = "yellow"):
                        if food_picked == 0: 
                            "Looking at Baxter's food, you had the urge to steal a small bite. He did offer earlier, after all."
                            show b e_closed b_norm m_grin
                            "You glanced at the extra fork he had left on the side of his place and not-so-sneakily reached over."
                            show b e_squint_dl 
                            "Baxter watched amused as you snuck some of his fried noodles, and slid his plate closer with feigned innocence to assist your heist."
                        else: 
                            "Looking at Baxter's food, it suddenly seemed more appetizing than yours."
                            show b e_squint_dl  b_norm m_grin
                            "You not-so-sneakily slid your utensil to his plate of fried noodles, taking a small bite with you. Baxter chuckled, sliding his plate closer with feigned innocence to assist your heist."
                    "Share some of your food with Baxter." (color = "green") if food_picked >= 2 :
                        show b m_grin b_raised
                        "He took a small part of your dish and brightened at the taste. He nodded his approval, as expected of the food you had chosen."
                    "You went back for seconds." (color = "blue") if food_picked > 0:
                        show b e_side_down 
                        "The food was too delicious to pass up, and you wanted to try a bit more before moving on. Baxter went with you this time, and the two of you chatted in line while you waited."
                    "You had changed your mind and wanted some food now." (color = "blue")if food_picked == 0:
                        show b e_side_down
                        "Baxter waited at the table for your return, and thankfully the line up didn’t take too long this time. His food was still warm even after you’d gotten back, and you finished the meal together."
                    "You were enjoying his stories."(color = "green"):
                        show b e_closed b_soft
                        "Talking with Baxter had always been easy, whether it was just enjoying the quiet together or chatting about your respective jobs. Your ordinary mundane lives were something he cherished."

                show b e_norm b_soft m_norm
                "Not long after the conversation drifted towards the current events surrounding your mutual friends."
                show b e_closed
                "Everyone was moving forward in their lives, and the two of you were no exception."
                show b e_norm b_norm m_norm
                if food_picked > 0:
                    "With good food and good conversation, the meals vanished quickly."
                    "After you and Baxter threw away your plates, you moved onto something else."
                else: 
                    "With good food and good conversation, Baxter's meal vanished quickly."
                    "After he threw away his plates, the two of you moved onto something else."
                if fest_games == False: 
                    jump date_options
                else:
                    jump separation_last

                        
        label festival_games:
            play music lets_build_a_secret_base_2 fadeout 1.0 fadein 1.0 if_changed
            $ fest_fin += 1
            $ fest_games = True
            scene matsuri
            show b b_one_raised e_norm m_norm
            with dissolve
            "The game booths were in full swing as participants lined up to play and win prizes. You saw your potential future rewards hanging in every booth, ranging from snacks to toys both big and small."
            "Baxter had a relaxed stance, but you could see the excitement in his eyes as they swept over the area."
            "What to do first?"

            menu games_selection:
                
                "Yo-Yo Tsuri (Water Balloons)" (color = "yellow") if yoyotsuri == False:
                    jump yoyo_tsuri_booth
                
                "Shateki (Shooting Gallery)" (color = "green") if shateki == False:
                    jump shateki_booth
                
                "Senbonbiki (String Game)" (color = "blue") if senbonbiki == False:

                    jump senbonbiki_booth
                
                "Katanuki (Diecutting)" (color = "green")if katanuki == False:

                    jump  katanuki_booth
                
                "You asked Baxter what he wanted to do." (color = "baxter") if b_g_opinion <2:
                    if yoyotsuri == False:
                        show b b_raised
                        b "Earlier, I overheard some people say that a classic of the Summer Festival had to be the water balloons."
                        show b m_grin 
                        b "As a {i}seasoned tourist,{/i}  I {i}would{/i} like to try that out... if you wouldn’t mind, [MC]."
                        show b m_norm b_norm
                        if mc_persona == 1:
                            MC "Yeah, let's go!"
                        elif mc_persona == 2:
                            MC "Let's check it out!"
                        elif mc_persona == 3: 
                            MC "That sounds good."
                        jump yoyo_tsuri_booth
                    elif shateki == False:
                        show b b_one_raised e_side
                        b "I'm rather particular to the shooting gallery. Shall we take a look?"
                        show b e_norm
                        if mc_persona == 1:
                            MC "Yeah, let's go!"
                        elif mc_persona == 2:
                            MC "Let's check it out!"
                        elif mc_persona == 3: 
                            MC "That sounds good."
                        jump shateki_booth

                "That was all you were interested in."(color = "blue") if g_completed >= 1:
                        jump baxter_lanterns
                        
                



            label g_checkpoint:
                # play music lets_build_a_secret_base_2 fadeout 1.0 fadein 1.0 if_changed
                if g_completed != 4:
                    jump games_selection

                else:
                    if river_lanterns == False: 
                        jump baxter_lanterns
                    elif fest_food == False: 
                        jump date_options
                    else:
                        jump separation_last


            label baxter_lanterns: 
                $ river_lanterns = True 
                "Returning to the main street of the festival, you quickly glanced at a nearby map of the grounds."
                "There weren't anymore games that you were interested in or hadn't played already."
                show b b_one_raised e_squint
                MC "I think I’m done with the games for today."
                "As you finished your statement, you caught sight of the unmistakable gleam of interest in Baxter's eyes."
                show b b_raised e_closed m_grin
                b "Well then. In that case, there is a charming tradition that the festival is hosting today."
                "Reaching into his sleeve, Baxter pulled out his phone and checked the time."
                show b b_norm e_norm m_norm
                b "From what I gather, it would seem that it’s only running for a limited time. If we go there now, we may be able to see this illustrious event."
                show b b_soft
                b "I have heard that it is a sight to behold."     

                menu: 
                    "Your interest was piqued." (color = "yellow"):
                        MC "I think that would be nice to see."
                        show b b_raised e_squint
                        b "Shall we then?"
                        if b_initiative == 1:
                            if mc_persona == 1 or mc_persona == 2:
                                "Baxter offered his arm to you with an expectant look. Flashing him a smile, you wrap your arm onto his, resting a hand on his forearm."
                                if mc_persona == 1:
                                    show b b_soft m_norm
                                    "Placing his hand onto yours, he rubbed the back of your hand with a thumb as you both made your way through the throngs of people."
                                elif mc_persona == 2:
                                    show b b_soft m_norm
                                    "Resting a hand on yours, he guided you through the throng of people making their way to your destination."
                            if mc_persona == 3:
                                "Baxter offered his arm to you with an expectant look. You hesitated for a moment before steeling yourself and threading your arm with his, settling your hand gently on his arm."
                                show b b_soft e_closed m_norm
                                "Smiling softly, he rests a hand on yours before guiding you through the throng of people making their way to your destination."
                            jump lantern_booth
                        if b_initiative == 2 or b_initiative == 3:
                            "Baxter offered his arm to you with an expectant look."
                            menu:
                                "Take his arm." (color = "green"):
                                    if mc_persona == 1:
                                        show b b_soft m_norm
                                        "Flashing him a smile, you wrap your arm onto his, resting a hand on his forearm."
                                    elif mc_persona == 2:
                                        show b b_soft m_norm
                                        "Threading your arm with his, you lean against him as you give him a smile."
                                    elif mc_persona == 3:
                                        show b b_soft e_closed m_norm
                                        "You hesitated for a moment before steeling yourself and threading your arm with his, settling your hand gently on his arm."
                                    "Smiling softly, he rests a hand on yours before guiding you through the throng of people making their way to your destination."
                                "Refuse him." (color = "blue"):
                                    if mc_persona == 1:
                                        show b b_soft m_norm
                                        "With a warm smile, you shake your head. Without skipping a beat, Baxter drops his arm but not his smile."
                                    if mc_persona == 2:
                                        show b b_soft m_norm
                                        "With a soft smile, you shake your head. Without skipping a beat, Baxter drops his arm but not his smile."
                                    if mc_persona ==3:
                                        show b b_soft e_closed m_norm
                                        "With a nervous smile, you shake your head. Without skipping a beat, Baxter drops his arm but not his smile."
                                    show b b_norm e_norm m_norm
                                    "Inclining his head to you, he waves his hand forward as you both make your way towards the riverbed."
                            jump lantern_booth
                    
                    "You had exhausted your social battery." (color = "green"):
                        show b e_surprised m_confused b_raised
                        MC "Actually, I feel like I’m all ‘event-ed’ out."
                        show b m_sad
                        b "Baxter placed a hand over his heart in mock hurt."
                        show b e_closed 
                        b "You wound me so! Am I to find a new career now? I most certainly can’t have you becoming bored of {i}me{/i}."
                        show b e_norm b_one_raised m_norm
                        "You chuckled at his antics, shaking your head at him."
                        show b b_sad e_closed 
                        b "Well, if you are certain."
                        show b b_norm e_norm m_norm
                        if fest_food == False: 
                            jump date_options
                        else:
                            jump separation_last
                
                

            #Yo-Yo Tsuri/Water Balloons
            label yoyo_tsuri_booth:
                play music morning_cafe_au_lait fadeout 1.0 fadein 1.0
                scene matsuri
                show b b_norm e_norm m_norm at left
                show r e_norm at right
                with dissolve
                $g_completed += 1
                $b_g_opinion += 1
                $ yoyotsuri = True

                "The water balloons bobbed in a large wooden tub, a little ways away from the street. It seemed like quite the popular event, as many groups had their own little corner they were playing in."
                "A small group of kids seemed to be having a competition. Two of them were in the middle of a contest of speed, seeing which of them could fish out a yo-yo without the paper string breaking."
                "They had all but taken over one side of the playing field, and thus you and Baxter waited patiently for your turn."
                "Crouched in the other corner, there was a woman dressed in a purple yukata who had her eye on a black and green colored balloon."
                "With a careful pull, she had it sitting on the hook in no time."
                show r e_happy:
                    ease 0.3 xoffset -75
                pause 0.05
                show r:
                    ease 0.03 xoffset 0
                r "Yay!"
                hide r
                with dissolve
                "Slipping it over her wrist, she left the booth, giving you and Baxter room to play undisturbed."
                show b e_norm b_norm m_norm at default:
                    ease 0.5
                with dissolve
                "The two of you stepped up to the booth."
                show b b_one_raised 
                b "I can't remember the last time I played with a yo-yo; certainly not the kind they're offering here."
                show b b_soft e_closed
                b "I suppose it's merely another ‘first’ that we’ll be having together."
                show b b_norm e_norm
                "Noticing the both of you, the stall owner turned in your directions, holding out paper hooks with a grin."
                s "Are you two in?"

                menu:
                    "You wanted to play."(color = "yellow"):
                        jump yoyo_tsuri_together
                    "You didn't want to play."(color = "blue"):
                        jump yoyo_tsuri_baxter


                label yoyo_tsuri_together:
                    show b e_side_down
                    "The booth owner handed over the hook attached to a paper string before needing to help another group that arrived."
                    "Your eyes explored the playing field, looking for a yo-yo that suited you, but a different one caught your attention instead."
                    "{i}A black and white one,{/i} featuring a design of tiny white koi fish swimming in a night pond, with little white flecks that looked like stars."
                    show b e_squint_dl b_one_raised
                    "It matched Baxter to a T."

                    menu:
                        "You wanted to win it!" (color = "yellow"):
                            $ baw_yoyo = 0
                            "You moved towards the yo-yo, now that you had a goal set in your mind. Baxter gave a half acknowledgment to your departure, oddly focused on his own prize."
                            show b b_soft e_norm 
                            b "Best of luck to you, [MC]."
                            hide b
                            show bax_at_yoyo with dissolve
                            "You watched as he crouched down to fish for his own yo-yo, having apparently decided which one he wanted."
                            "He was testing to see how the paper string and hook worked, gently skimming the water surface as he experimented with hooking one."
                            "It seemed to be a mystery as to which he was actually aiming for, but you had your own prize to catch."
                            hide bax_at_yoyo with dissolve
                            "Taking a more comfortable position, you began fishing for it."
                        
                        "You pointed out the BAW to Mr.BAW."(color = "green"):
                            $ baw_yoyo = 1
                            if mc_persona == 1:
                                show b b_one_raised e_norm
                                MC "Look, same outfit."
                                show b b_one_raised e_closed m_grin
                                "He smirked at your little jab as you pointed at the yo-yo for emphasis."
                            if mc_persona == 2:
                                show b b_one_raised e_norm m_norm
                                MC "Baxter, there's a black and white yo-yo."
                                show b e_squint
                                "At the sound of his name, Baxter turned towards you. You pointed in the direction of the yo-yo in question."
                            if mc_persona == 3:
                                show b b_soft e_norm m_norm
                                MC "Umm, Baxter."
                                "At the sound of his name, he turned towards you as you stretched out your finger to the yo-yo."
                            
                            show b b_one_raised e_squint 
                            "Following your gaze, he finally spotted the yo-yo that matched his namesake, and he shuffled to the other side to get to it."
                            show b b_norm e_closed 
                            "He nodded his approval, as well as his thanks."
                            show b b_annoyed m_grin
                            b "I'm so lucky to have such a considerate partner. Thank you, [MC]. Best of luck to you as well."
                            hide b
                            show bax_at_yoyo 
                            with dissolve
                            "You watched as he crouched down to fish for his namesake, oddly focused on the task."
                            "Baxter was testing to see how the paper string and hook worked, gently skimming the water surface as he experimented with hooking one."
                            "He seemed to be well on the road to succeeding."
                            hide bax_at_yoyo with dissolve
                            "But you had your own prize to catch, so you crouched down to find one for yourself."
                            "After eyeing all the available balloons, you focused on one with your favorite color and got comfortable."
                        
                        "You ignored it and looked for a different yo-yo to catch."(color = "blue"):
                            $ baw_yoyo = 2
                            b "Best of luck to you, [MC]."
                            hide b
                            show bax_at_yoyo
                            with dissolve
                            "You watched as he crouched down to fish for his own yo-yo, oddly focused on the task."
                            "He was testing to see how the paper string and hook worked, gently skimming the water surface as he experimented with hooking one."
                            "It seemed to be a mystery as to which one he wanted, but you had your own prize to catch."
                            hide bax_at_yoyo with dissolve
                            "You peered over the pond of floating balloons and focused on one with your favorite color."
                            "Taking a more comfortable position, you began fishing for it."

                    
                    menu: 
                        "You played to win." (color = "yellow"):
                            $ yoyo_win = 1
                            "Mindful of the paper string, you played cautiously."
                            "If it was too wet, it might break due to the weight of the balloon."
                            "Your first try slid across the water surface, barely grazing the loop of the yo-yo. {i}Almost!{/i}"
                            "The paper was still holding strong as you tried again. This time, the hook went through the loop and you pulled the balloon upwards."
                            "You waited with bated breath as the string held, the yo-yo bouncing slightly. You had gotten it!"
                        "You played casually" (color = "green"):
                            $ yoyo_win = renpy.random.randint(1,2)
                            "Aiming for the small circle, you skimmed the surface of the water, hoping to get lucky."
                            "The first few tries you came up with nothing, and you were certain the string would not hold up much longer."
                            "With one more try, you felt the water beneath your fingers as the hook found the loop and you pulled!"
                            if yoyo_win == 1:
                                "As if you had reeled in a big catch, the yoyo bounced on the line. Once setttled, it sat firm."
                            if yoyo_win == 2:
                                "The string itself had already felt weak, and your fears were confirmed as it broke under the weight."
                        "You weren’t really that into it." (color = "blue"):
                            $ yoyo_win = 2
                            "The paper string broke after a few tries, with the weight of the balloon dragging the hook back into the watery depths with a ‘plop’."
                    #MC Won
                    if yoyo_win == 1:
                        $ yoyo_owner = 2
                        "Your trophy hung on your line as you turned to Baxter. He had also been successful in hooking a prize as the two of you showed them off to each other."
                        
                    #MC Lost
                    if yoyo_win == 2:
                        "You looked at your fallen prize bobbing sadly in the water before turning to Baxter, who had been successful in winning his."
                        "He held it up triumphantly, grinning like he'd won the lottery."
                        
                    jump yoyo_trade

                label yoyo_tsuri_baxter:
                    show b e_side_down
                    "The booth owner handed Baxter a hook attached to a paper string before needing to help another group that arrived."
                    "Your eyes roamed the playing field, where a black and white yo-yo caught your eye, but seemed to be hiding itself from Baxter."
                    show b e_squint_dl b_one_raised
                    "It fit him to a T. You were {i}certain{/i} that he'd like that one."
                    "Although, you were {i}equally certain{/i} that, if you asked, he'd would be happy to win one for you."
                    
                    menu:
                        "You asked him to fish you one." (color = "yellow"):
                            if mc_persona <3:
                                show b e_norm b_one_raised
                                MC "Baxter, could you get me one?"
                            elif mc_persona == 3: 
                                show b b_soft e_norm
                                MC "Umm, Baxter? I'd like one."
                            show b e_wide b_raised1
                            "His eyes lit up as you asked, eager to fulfill your wishes."
                            show b e_closed m_grin 
                            b "Of course."
                            show b b_norm e_norm m_norm
                            b "Which one?"

                            menu:
                                "You wanted one matching your current outfit." (color = "yellow"):
                                    show b e_wide b_raised1
                                    "A flicker of surprise crossed his face as if you had caught him in flagrante delicto."
                                    show b e_closed b_norm m_grin
                                    b "It appears great minds think alike."
                                    show b e_side b_sad m_norm
                                    b "In truth, I had already wanted one in your colors."
                                    show b e_squint b_norm m_norm
                                    b "It would look charming alongside your apparel, not that you aren't enchanting enough already."
                                    "With the final word his, he crouched down and began fishing for the yoyo."
                                "You wanted the one matching Baxter’s colors." (color = "green"):
                                    $ baw_yoyo = 2
                                    show b e_surprised b_raised1 m_norm blush
                                    "You pointed out the black and white yo-yo as recognition and a light blush dawned on Baxter's face."
                                    show b e_squint b_one_raised m_norm
                                    "He smiled, awfully pleased with himself as he crouched down near it."
                                    show b m_grin -blush
                                    b "It's an honor to be in your thoughts even at times like this."
                                    if mc_persona == 1:
                                        show b m_norm
                                        "You grinned right back, matching his smug little smile."
                                    if mc_persona == 2:
                                        show b b_raised e_squint_dl m_norm
                                        "You remained impassive, and Baxter let out a small 'tsk'."
                                        show b b_annoyed e_squint
                                        b "So cruel to have me surmise your affections for me."
                                        "With the final word his, he crouched down and began fishing for the yoyo."
                                    if mc_persona == 3:
                                        show b b_soft e_norm m_norm
                                        "You fidgeted with the edge of your clothing a little. Baxter's honesty never failed to make you happy."
                                        "He tilted his head, charmed by your expression before crouching down and starting the game."
                                "You changed your mind."(color = "blue"):
                                    show b b_norm e_norm m_norm
                                    "Baxter nodded his head, flashing you an understanding smile."
                                    b "It's no trouble at all, [MC]. Let me know if you'd like one in the end."
                        "You pointed out the BAW to Mr.BAW."(color = "green"):
                            $ baw_yoyo = 1
                            if mc_persona == 1:
                                show b b_one_raised e_norm
                                MC "Look, same outfit."
                                show b b_one_raised e_closed m_grin
                                "He smirked at your little jab as you pointed at the yo-yo for emphasis."
                            if mc_persona == 2:
                                show b b_one_raised e_norm m_norm
                                MC "Baxter, there's a black and white yo-yo."
                                show b e_squint
                                "At the sound of his name, Baxter turned towards you. You pointed in the direction of the yo-yo in question."
                            if mc_persona == 3:
                                show b b_soft e_norm m_norm
                                MC "Umm, Baxter."
                                "At the sound of his name, he turned towards you as you stretched out your finger to the yo-yo."
                            "Baxter followed your gaze, finally spotting the yo-yo that matched his namesake, and he shuffled to the other side to get to it."
                            show b b_norm e_closed 
                            b "Thank you, [MC]."
                            show b b_annoyed m_grin
                            b "I’m so lucky to have such a caring and attentive partner."
                            "His eyes gleamed with warmth before he turned his undivided attention towards his goal."
                        "You didn't say anything." (color = "blue"):
                            $ baw_yoyo = 2
                            show b b_annoyed e_squint_dl m_norm
                            "You were content to watch him play. It seemed he didn't notice the balloon after all, as he began fishing for a closer one."
                            "What {i}you{/i} noticed was that the color of the balloon suspiciously matched the color of the clothes you were currently wearing."
                            "Knowing your partner it most likely wasn’t a coincidence. It was further solidified by the oddly determined look he had in his eyes."
                            "The only thing you couldn’t be certain of was if he was doing it for you, or if he wanted to carry around something that reminded him of you."
                    show bax_at_yoyo 
                    hide b
                    with dissolve
                    "Baxter was a patient player, testing the method of hooking first before he aimed for the chosen yo-yo."
                    "The hook gracefully skimmed the surface before catching the loop of the string. He lifted it gingerly, seemingly afraid of it falling."
                    "There was a quiet pause, and Baxter sucked in a gasp until it was apparent that the yo-yo held on the string."
                    hide bax_at_yoyo with dissolve
                    show b b_raised1 e_wide m_grin
                    "He triumphantly lifted up his prize, looking proud as the yo-yo dangled from the string."
                    

                label yoyo_trade:
                    show b e_norm m_grin
                    with dissolve
                    b "I confess: this was much easier than fixing a chocolate fountain."
                    "He chuckled, having come to terms with his teenaged nemesis."
                    #If MC Won the Black and White one
                    if baw_yoyo == 0 and yoyo_win == 1:
                        show b e_surprised b_raised1 m_norm blush
                        "You could see Baxter's eyes widen with recognition as you held up the black and white balloon."
                        show b e_squint_dl
                        "Similarly, the balloon he held up had colors matching your current outfit."
                        show b e_squint
                        "He smirked, and you could see a blush creeping onto his face. He was clearly happy he was in your thoughts."
                        b "I can see someone was thinking of me."
                        menu: 
                            "Seems like you were also thinking about me." (color = "yellow"):
                                show b e_norm b_norm m_norm 
                                "Baxter tilted his head, face aglow with happiness."
                                b "{b}Always{/b}, [MC]."
                                show b b_soft
                                b "I am {i}always{/i} thinking about you."
                            "Always." (color = "green"):
                                show b b_one_raised e_squint
                                MC "I'm always thinking about you, Baxter."
                                show b m_grin
                                b "I do believe that's {i}my{/i} line."
                                show b b_norm e_closed
                                "Baxter laughed, looking partly scandalized that you’d beaten him to it."
                            "You blushed." (color = "blue"):
                                show b e_closed b_raised m_grin
                                "Baxter laughed, warm eyes looking at you."
                                show b e_norm b_soft m_norm
                                b "Thank you."
                                b "I’m happy to know I’m in your thoughts."
                            "I just think these colors are nice." (color = "yellow"):
                                show b b_one_raised e_squint m_norm
                                "Baxter arched his eyebrow, not buying your answer."
                                b "Is that so?"
                                show b b_norm e_closed 
                                b "Very well. Who am I to judge your tastes?"
                                MC "I have very good taste."
                            "You gave him a pointed stare." (color = "blue"):
                                show b b_one_raised e_squint m_norm
                                "Baxter tilted his head innocently."
                                b "Was I incorrect in my hasty judgment?"
                                show b e_closed b_raised m_grin
                                b "My apologies."
                                "He didn’t seem at all apologetic."
                        show b e_norm b_norm m_norm -blush
                        jump trade_menu
                    #CHeck
                    #If MC played and didn't tell Baxter about it then Baxter is fishing for one in MC's colors.
                    if yoyo_win != 0 and baw_yoyo != 1:
                        show b e_squint b_one_raised m_norm
                        "You glanced at the yo-yo he held in his hands. It was a direct match to your current outfit, down to the complementary color."
                        show b e_side b_annoyed m_norm
                        "He had been fishing something that reminded him of you all this time."
                        menu:
                            '"You were thinking about me all this time?"'(color = "yellow"):
                                show b b_raised e_closed m_grin
                                "Baxter smiled, no doubt in response to you catching onto his little scheme."
                                show b b_norm e_squint m_norm
                                b "{i}Always{/i}, [MC]."
                                show b e_norm b_soft
                                b "I am {i}always{/i} thinking about you."
                            '"Thank you for always thinking about me."'(color = "green"):
                                show b b_raised e_closed m_grin
                                "You knew that Baxter had fished one with your colors on purpose."
                                show b b_norm e_squint m_norm
                                "Whether it was just to remind himself of you, or to find something to match your outfit–"
                                show b e_norm b_soft
                                "You knew you were at the forefront of his mind."
                            "You blushed with realization of his goal."(color = "blue"):
                                show b b_raised e_closed m_grin
                                "He had been fishing for you this whole time, and the thought brought the red to your face."
                                show b e_squint m_norm b_norm
                                "Baxter smiled in response to you catching onto his little scheme."
                                "There was a mischievous little twinkle in his eye as he enjoyed making you blush."
                            '"Nice colors."' (color = "yellow"):
                                show b b_raised e_closed m_grin
                                "You smiled at the yo-yo, acting oblivious about it."
                                show b e_squint m_norm 
                                "Baxter gave a little hum, playing along as if his affections for you wasn't immediately obvious."
                                b "'Nice', indeed."
                            "You stared at the yo-yo."(color = "blue"):
                                show b b_raised e_closed m_grin
                                "It was just like him to be thinking about you."
                                show b e_norm b_soft m_norm
                                "You didn't think you'd ever tire of how much his affections for you were on full display."
                        #if MC lost, Baxter will offer his to them.
                        if yoyo_win == 2:
                            jump offer_prize
                        else:
                            pass
        
                    # Otherwise if MC didn't play or lost, Baxter will give his yoyo to MC
                    if yoyo_win == 0 or yoyo_win == 2:
                        label offer_prize:
                            show b m_norm e_norm b_norm
                            "Baxter then held out his yo-yo to you."
                            show b b_raised e_closed 
                            b "I'd like to officially offer my lovely partner this prize for the evening."
                            if yoyo_win == 2:
                                "He may have wanted you have his, since your string had broken part of the way through."
                            if baw_yoyo == 1:
                                show b b_norm e_norm
                                b "I'd love it if you were to carry something that reminds you of me around."
                            else: 
                                show b b_norm e_norm
                                b "I hope the yo-yo complements you as much as I do, [MC]."

                            menu offer_menu:
                                '"Just the one?"' (color = "yellow"):
                                    $ yoyo_owner = 1
                                    show b b_raised e_closed m_grin
                                    "You raised your eyebrow inquisitively as Baxter snorted, covering his mouth with his hand. Satisfied with his reaction, you took the prize with a grin."
                                    show b b_norm e_closed m_norm
                                    "The warmth of his hand brushing past lingered for a more moments longer."
                                    show b b_norm e_squint m_grin
                                    b "Of course not. Give me some more time, I’ll be sure to have you leaving this place with no hands left."
                                "You thanked him."(color = "green"):
                                    $ yoyo_owner = 1
                                    show b b_norm e_closed m_norm
                                    b "It's my pleasure, [MC]."
                                    show b b_norm e_squint m_norm
                                    b "Truth be told, it was my intention from the beginning to give you my prize."
                                    show b e_norm
                                    "He beamed as you took the yo-yo from him, the warmth of his hand brushing past lingered for a moment."
                                    "You could tell he was happy to make {i}you{/i} happy, and that was worth any prize."
                                "You blushed and nodded your thanks." (color = "blue"):
                                    $ yoyo_owner = 1
                                    show b b_norm e_closed m_norm
                                    b "It’s my pleasure, [MC]."
                                    show b b_soft e_norm
                                    b "Nothing would make me happier."
                                    "Baxter smiled as you took the prize from him, the warmth of his hand brushing past lingered for a moment."
                                    show b b_one_raised e_squint m_norm
                                    "He was enjoying your reaction, almost as if he’d been trying to win for that and not the yo-yo all along."
                                '"{i}You{/i} keep it, Baxter."' (color = "green"):
                                    $ yoyo_owner = 0
                                    show b b_soft e_norm
                                    b "Are you certain?"
                                    show b b_sad e_side
                                    b "Truth be told, it was always my intention to give you my prize."
                                    if baw_yoyo == 1:
                                        show b b_sad e_norm
                                        MC "It matches you better."
                                    elif baw_yoyo == 3:
                                        show b b_sad e_norm
                                        MC "I want you to have it instead."
                                    else:
                                        show b b_sad e_norm
                                        MC "You won it fair and square."
                                    show b b_sad e_side_down
                                    "Baxter hesitated briefly, before accepting your decision. He had a sentimental look on his face, almost as if you were gifting it to him."
                                    show b b_norm e_norm m_norm
                                    b "Very well."


                    #Menu for if MC and Baxter have a yoyo.                           
                    if yoyo_win == 1:
                        
                        menu trade_menu: 
                            #Only available if you won the B/W one
                            '"I won this one for you, Baxter."' (color = "yellow") if baw_yoyo == 0 and yoyo_win == 1:
                                show b b_soft
                                "Baxter gave you a gentle look. It was rare that he was speechless, but it seemed to be the case this time as he took a few seconds to recompose himself."
                                "Knowing that you thought of him never failed to catch him off guard, no matter how many times you showed it."
                                show b m_grin e_closed
                                b "Thank you. How about a trade? I couldn't in good conscience walk around with {i}two{/i} prizes."
                                "He snickered and you thought it was a sound idea. His hand brushed past yours as he reached for the string."
                                show b b_soft e_side_down m_norm
                                "Baxter held it in his hand for a few seconds to admire the pattern on the balloon. His fingers ran across the tiny white koi fish."
                                "He held the prize with a sentimental look, a soft smile on his features."
                            #Only available if you told Baxter about the B/W and you won one.
                            '"Can I have your yo-yo?"' (color = "yellow") if baw_yoyo == 1 and yoyo_win == 1:
                                if mc_persona == 1 or mc_persona == 2:
                                    show b e_surprised b_raised1 m_confused
                                    MC "I like your colors better."
                                    "Baxter seemed mortified at first, holding the balloon closer to him as if you'd steal it."
                                    show b e_squint_dl b_annoyed m_s_smile
                                    b "{i}Greedy one, aren't you?{/i}"
                                    "His words were muttered under his breath, but still audible enough for you to hear. You were certain that was his intention, as he sported a grin soon enough."
                                    show b e_squint_dl b_one_raised m_grin
                                    b "Did you point this one out to me so I would do the legwork in your stead?"
                                    MC "That's not a no to my question..."
                                    show b e_closed b_norm m_norm
                                    b "How cheeky. {i}very well,{/i}, but only if I may have yours in return."
                                    MC "That's fair."
                                    show b e_norm
                                    "With the 'deal' struck, the two of you exchanged prizes. The warmth of his hand lingering as it brushed past yours."
                                elif mc_persona == 3: 
                                    show b b_soft e_norm m_norm
                                    MC "If that's okay..."
                                    if b_initiative == 1 or b_initiative == 2:
                                        "Baxter reached for your hand, placing his yo-yo in your palm, and the warmth of his hand lingered as he let go."
                                    elif b_initiative == 3:
                                        "Baxter nodded, a reassuring look on his face."
                                    b "Of course it is."
                                    show b e_side_down b_one_raised
                                    "His eyes fell on the one you had."
                                    b "And if I may have yours in return?"
                                    show b e_norm b_norm
                                    "You nodded your head in agreement, handing over your yoyo."
                            #Always available if you win a yoyo.
                            '"Would you like to trade yo-yos?"' (color = "green") if yoyo_win == 1:
                                show b b_soft
                                "Baxter gave you a gentle look. It was rare that he was speechless, but it seemed to be the case this time as he took a few seconds to recompose himself."
                                show b e_side_down b_sad
                                "Knowing that you thought of him never failed to catch him off guard, no matter how many times you showed it."
                                show b e_norm b_soft
                                b "I'd like that a great deal. Thank you."
                                "As the two of you exchanged yoyos, Baxter's hand brushed past your own. The warmth from him lingered on the back of your hand."
                            #Baxter will always propose trading yoyos if MC has one
                            # "Baxter proposed trading yoyos."(color = "baxter"):
                            #     #CHECK
                            #     show b e_closed m_grin b_raised
                            #     b "In the spirit of cooperation, how would you like to trade, [MC]?"
                            #     #if MC won the B/W one
                            #     #if he won something in their color
                            #Option to leave the booth as is- without trading.
                            "You were content with how things were." (color = "blue"):
                                jump leaving_yoyo
                
                label leaving_yoyo:
                    show b e_norm b_norm m_norm
                    "Remembering that there was a line forming for the game, you and Baxter moved away to make room for them."
                    if yoyo_owner == 0:
                        show b e_squint b_one_raised m_norm
                        "Baxter slipped the water balloon's string around his wrist as the two of you were leaving, bouncing it up and down with curiosity."
                        "He flashed you a smile when he saw you were looking at him."
                    if yoyo_owner == 2:
                        show b e_squint b_one_raised m_norm
                        "You both slipped your respective string around your wrists, where it bobbed slightly with each movement. After securing his, Baxter poked your yo-yo, sending it wobbling away."
                    if yoyo_owner == 1:
                        show b e_squint b_one_raised m_norm
                        "You slipped the string around your wrist, securing it as it bobbed slightly with each movement."
                        "Baxter was admiring it, giving it a gentle poke that sent it swaying."
                    show b e_closed b_sad m_norm
                    "After ruminating to himself for a moment though, he let out a little sigh."
                    show b e_norm b_sad m_norm
                    if yoyo_owner == 2: 
                        b "It's a shame we won’t be able to keep them for our return home. They would make wonderful souvenirs."
                        show b e_squint_dl b_one_raised m_norm
                        b "Not that they would be allowed onto the plane, or last that long in the first place."
                    else: 
                        b "It's a shame we won’t be able to keep it for our return home. It would make a wonderful souvenir."
                        show b e_squint_dl b_one_raised m_norm
                        b "Not that it would be allowed onto the plane, or last that long in the first place."
                    
                    show b e_closed b_norm m_norm
                    "Baxter chuckled to himself."
                    show b e_norm
                    b "But I’m certain we’ll find other wonderful souvenirs to bring back, if not equally delightful memories."
                    "The promise of more memories was enticing enough on it's own. Thus the two of you left in search of other things to do."
                    
                
                jump g_checkpoint
            
            #Shatkei/Shooting Gallery
            label shateki_booth:
                $ shateki = True
                $g_completed += 1
                $b_g_opinion += 1
                play music glassworks fadeout 1.0 fadein 1.0 
                scene matsuri
                with dissolve

                "You approached a booth that had a counter in-between you and the shelves that the prizes were stacked up on. There were various stuffed dolls, unique toys, and accessories both small and large."
                "The most curious decorations were the several extremely large plushies. They sat on tarps, welcoming guests into the shooting gallery."
                "A group of boys had taken up the space already, but were on their last try from the looks of it. You saw them load up the toy gun with corks that were set out in front of them."
                "Two of them seemed to be engrossed in the game, aiming carefully at the row of prizes."
                "The other two were more relaxed, with one of them looking like he wasn’t interested at all."
                "In unison, the final shots popped out. Two flew straight, knocking over a plush toy and a snack. The third shot had missed entirely."
                "The last shot thudded against the opposing counter before flying back towards the group, hitting one of them square in the head."
                f "{i}Oww...{/i} why does that keep happening?"
                "He rubbed his forehead as the one next to him looked over the bump."
                o "Ah, let’s get you an ice pack for that..."
                "The employee placed the prizes onto the table, to which the one in red picked them up rather gleefully."
                q "I think they’re going to like these ones!"
                "The man who seemed uninterested caught sight of you and Baxter waiting patiently, and waved his friends onwards."
                d "Let’s go, there’s already a line."
                show b b_norm e_norm m_norm
                with dissolve
                "The employee waved as they all departed, leaving you and Baxter a lot of space to play."
                "Turning to the two of you, the employee lifted their gaze in tandem with the brim of their hat, revealing a smirk underneath."
                s "Dear customers, would you like to try the shooting gallery?"
                show b b_one_raised e_squint m_norm
                "Next to you, Baxter was sizing up the different prizes already. His eyes were full of elation and curiosity."

                menu:
                    "You wanted to play."(color = "yellow"):
                        jump shateki_together
                    "You didn't want to play." (color = "green"):
                        jump shateki_baxter
                
                #MC plays with Baxter
                label shateki_together:
                    show b e_norm b_norm 
                    s "Alrighty, please shoot down any prize you’d like!"
                    "They handed over a toy rifle and some extra corks, standing aside out of harm's way. One of the corks had already been preloaded for you. The rest sat neatly in a dish."
                    if mc_persona == 1 or mc_persona == 2:
                        show b b_one_raised
                        MC "Do you want to go first?"
                        show b m_grin e_closed b_norm
                        b "No, please, after you."
                        "Baxter gestured you forwards with a flourish of his hand."
                    elif mc_persona == 3:
                        show b b_soft
                        "You glanced at Baxter and he gave you a nod in return, motioning you to take your turn first."
                    
                    show b e_squint b_raised m_grin
                    b "Knock 'em dead, darling."
                    if mc_persona == 1:
                        MC "You know I will. "
                        "You replied with confidence, mirroring his own."
                    if mc_persona == 2:
                        "You gave him a smile in return, happy for the bit of encouragement."
                    if mc_persona == 3:
                        "You gave a resolute nod in response, focusing on Baxter’s encouragement."
                    hide b 
                    with dissolve
                    "You looked at the line up of prizes and decided to focus on..."
                    menu prize_neck:
                        "A fox mask."(color = "yellow"):
                            $sha_fox = True 
                        "A starter Poketure plushie."(color = "green"):
                            $poke_plush = True
                        "A blank-looking card folded into two."(color = "blue"):
                            $large_plush = True
                        "A colorful toy package."(color = "yellow"):
                            $color_toy = True
                        "A juice bottle."(color = "green"):
                            $yuzu_drink = True
                        "A Shiba plush."(color = "blue"):
                            $shiba_plush = True
                        "A plush that looks like Cove."(color = "green"):
                            $cove_plush = True
                        "You didn't want anything." (color = "yellow") if sha_bax and shateki_win == 0:
                            show b m_grin e_closed b_raised1
                            b "As you wish."
                            "He gave a small chuckle, readying himself once more."
                            jump large_plush_dialogue
                    
                    if sha_bax:
                        jump sha_prize_line

                    "Baxter watched from the sidelines, peering over the prizes with elation before his attention flicked back to you."
                    "You squared up the target ahead of you, taking aim."

                    menu:
                        "You hit your prize with the first shot!"(color = "yellow"):
                            $ shateki_win = 1
                            "The cork flew straight at your intended target! The prize toppled over without much more of a fight."
                            "You heard Baxter's polite clapping behind you."
                            show b e_closed m_grin b_raised
                            with dissolve
                            b "A hidden talent, [MC]? We might just walk away with all the prizes today."
                            show b e_side m_norm 
                            b "However, remind me not to get in-between you and what you want."
                            show b e_side_down b_sad
                            b "...I feel like I knew that already though."
                        "It took a few tries, but you landed the target."(color = "green"):
                            $ shateki_win = 1
                            $ shots_left = 1
                            "With every shot you took, you got closer and closer, until finally one landed square in the middle of the item."
                            "It easily pushed over the target, toppling it over."
                            show b e_closed m_grin b_raised
                            with dissolve
                            b "{i}Very{/i} nice shooting, [MC]."
                            show b e_squint_dl m_norm b_norm
                            b "Let’s hope I fare equally as well."
                        "You managed to hit it on the last shot!"(color = "blue"):
                            $ shateki_win = 1
                            $ shots_left = 2
                            "Much to your dismay, most of your shots whizzed by your target. Some outright flew nowhere close."
                            "Before you knew it, there was only one cork left. It {i}had{/i} to hit!"
                            "You took a deep breath as the final cork popped from the gun. It flew straight and true, hitting your intended target dead center!"
                            show b b_one_raised e_norm m_norm
                            with dissolve
                            b "I think I’ve heard that it’s the last shot that matters, yes?"
                            show b e_closed m_grin b_raised
                            b "Well done."
                        "You missed all your shots!"(color = "yellow"):
                            $ shateki_win = 2
                            $ shots_left = 2
                            "Each cork flew past your intended prize, one even barely grazing past."
                            "It seemed like your skills, or lady luck, wasn't with you today, as the prize continued to sit on the stand."
                            show b e_squint b_raised1 m_norm
                            with dissolve
                            "Baxter gave a little hum, eyes flicking over to the item that sat mockingly on its perch."
                    
                    if shateki_win == 1:
                        show b e_norm b_one_raised m_norm
                        "Baxter joined you at the counter as you went about inspecting your prize." 
                        label sha_prize_line: 
                            if sha_bax and not large_plush:
                                show b b_annoyed e_squint m_norm
                                "Baxter leaned against the counter, lining up for his goal quickly and decisively."
                                "With a single shot, the cork flew over to the unsuspecting prize, knocking it clean off the countertop."
                            if sha_fox:
                                "The mask had been knocked cleanly off its perch and fallen onto the table below."
                                "It was beautifully crafted, with purple markings detailed around the mask."
                                s "The masks are pretty popular this year."
                                "The owner remarked with that as they placed the mask on the table. Baxter picked it up, inspecting it closely."
                                show b e_wide b_raised 
                                b "The detail put into the markings is lovely."
                                if sen_fox:
                                    show b m_confused
                                    "Baxter had a sudden flash of recognition as he peered closer at the details."
                                    show b b_one_raised e_norm m_norm
                                    b "You won something similar at the lottery earlier, did you not?" 
                                    show b b_one_raised e_side m_confused
                                    b "This couldn’t possibly be the same one." 
                                elif sen_fox and fox_mask_change:
                                    show b b_one_raised e_norm m_norm
                                    "Baxter had a sudden flash of recognition while he was peering closer at the details. A smile spread across his face as he placed the mask back down."
                                    show b b_norm e_closed 
                                    b "It’s lovely that we have a matching set now."
                                else:
                                    show b b_one_raised e_squint_dl m_norm
                                    b "I’ve seen a few around with similar designs, but all seem to be unique in some shape or form."
                                    show b e_squint 
                                    "His eyes flitted from the mask to you, placing it in your hands."
                                    if shateki_win == 1:
                                        b "As unique as their winner."
                                    else:
                                        b "As unique as their new owner."
                            elif poke_plush:
                                show b e_side_down m_confused
                                "The plush had fallen over on its side, and the owner scooped it up."
                                "Once they placed it onto the table, they gave it a few approving head pats."
                                s "Take good care of your partner. I hope you can catch 'em all."
                                "The owner snickered as Baxter pondered over its appearance."
                                show b e_side m_norm
                                b "Was this that cartoon show you were telling me about earlier?"
                                show b e_closed m_grin
                                b "I had a feeling that this curious creature would catch your attention."
                                show b e_norm m_norm
                                if shateki_win == 1:
                                    b "It’s as endearing as its winner."
                                else:
                                    b "It’s as endearing as its new owner."
                            elif large_plush:
                                jump large_plush_dialogue
                            elif yuzu_drink: 
                                show b b_raised e_squint m_grin
                                "Despite its weight, the glass bottle had been knocked over onto its side without a crack."
                                "The owner caught just as it began rolling off the ledge. They placed it onto the counter with a bit of flourish and a small clink."
                                "On the bottle's face was a picture of two yuzu fruits sitting in a basket; a sweet refreshing drink that certainly fit the summer theme."
                                if shateki_win == 1: 
                                    show b b_one_raised e_squint_dl m_grin
                                    b "I {i}do{/i} hope you'll share some with me. Watching you has made me {i}quite parched{/i} indeed."
                                else:
                                    show b b_one_raised e_squint_dl m_grin
                                    b "I {i}do{/i} hope you'll share some with me. Something about being around you makes me {i}quite parched{/i} indeed."
                            elif color_toy:
                                "The toy package flew off the ledge cleanly, its odd weight distribution likely serving as the deciding factor."
                                "The owner gave an impressed whistle, placing the toy onto the counter for a closer examination."
                                "It was a bubble blower toy set, complete with a tiny jar of bubble formula."
                                show b b_raised e_wide m_confused
                                b "Oh, these are rather popular lately with wedding showers."
                                show b b_angry e_side_down m_grin
                                b "It's certainly a step up from using items that are such a mess to clean up..."
                                "The remark was dry, Baxter no doubt remembering some less than pleasant experiences from his work."
                            elif shiba_plush:
                                "The brown dog plush was a rather popular mascot of Japan, a cartoon version of the Shiba Inu."
                                show b b_norm 
                                b "We certainly have seen a few of them around, haven’t we?"
                                show b b_raised e_closed m_grin
                                b "Splendid decision to bring one home with us."
                            elif cove_plush:
                                show b b_raised e_wide m_confused
                                "You had thought the plush looked familiar even before it sat on the counter, and Baxter’s face had the same stunned realization; neither of you believed it was real."
                                "The owner had begun reading the small tag attached to the plush."
                                s '"Your childhood friend that loves the sea and sweets..."'
                                s "Huh. Did I have a plush like that?"
                                "Incredibly perplexed and muttering something about copyright issues, they handed over the plush that bared a striking resemblance to your longtime neighbour."
                                "Baxter continued staring in surprise at the miniature lookalike, mouth slightly agape."
                                show b b_sad e_norm m_sad
                                "His features soon shifted to dismay. One hand lifted to cover his mouth as he gasped."
                                show b m_confused e_wide
                                b "[MC], I'm hurt. Am I not good enough for you?"
                                "You could tell from his tone that he was teasing you."
                                
                                menu:
                                    '"It’s not what it looks like!"'(color = "yellow"):
                                        MC "I only have eyes for you, I swear!"
                                        show b e_squint b_annoyed m_norm
                                        b "But you're keeping the plush."
                                        MC "I’m keeping the plush."
                                        show b e_squint_dl b_sad
                                        "Baxter sighed defeatedly, shoulders dropping as his eyes looked away from yours. But you saw his smile, the one that mirrored yours in the moment."
                                    '"Baxter, we’re in Japan."'(color = "green"):
                                        show b e_squint b_raised m_norm
                                        MC "Together, {i}with no one else.{/i}"
                                        show b e_squint_dl
                                        b "{i}Not anymore, in a manner of speaking,{/i}"
                                        show b e_closed m_grin b_raised
                                        b "But I appreciate the thought."
                                    "You did feel a little homesick." (color = "blue"):
                                        show b e_surprised b_raised
                                        "You frowned, remembering that this was an unfamiliar place far away from your cherished friends and family."
                                        show b e_norm b_soft
                                        "Baxter dropped the act immediately, giving you a caring look."
                                        if b_initiative == 1:
                                            "Reaching over, he gave your hand a small squeeze."
                                        if b_initiative == 2:
                                            "He lightly patted your shoulder."
                                        if b_initiative == 3:
                                            "He stepped a little closer, hoping his presence would help your mood improve."
                                        show b e_closed m_grin 
                                        b "You should show the others later. I'm certain they would be ecstatic to see our new friend."
                                        "He gave you a comforting smile and you felt yourself smiling in return. He was constantly looking out for you after all, and his kindness eased your nerves."
                        
                        # Baxter shoots and wins the prize MC wanted.
                        if shateki_win == 2 and sha_bax:
                            show b e_squint b_annoyed m_norm
                            "Baxter gave you an innocent smile to meet your look of surprise. Did he want you to go first in case something like this was going to happen?"
                            show b e_closed m_grin b_raised
                            b "Merely trying to earn a few brownie points."
                            "The unmistakable gleam of playfullness twinkled in his eyes, confirming your guess."
                            if mc_persona == 1:
                                show b e_norm b_soft 
                                "You gave a laugh in response to his cheekiness, mirroring his grin."
                                MC "Consider them earned."
                            if mc_persona == 2:
                                show b e_norm b_soft
                                MC "Thanks, Baxter."
                                "Even despite his little 'trick', his intentions had been wanting to make you happy all along."
                            if mc_persona == 3:
                                show b e_norm b_soft
                                "With a small shake of your head in response to his smug little grin, you then smiled your thanks."
                                "You knew he was always looking out for you, in his own way. Pardoning his mischievous methods was {i}your{/i} method of reciprocating."

                        if sha_bax:
                            jump leave_shateki
                
                #Baxter plays
                label shateki_baxter:
                    $sha_bax = True
                    # if MC didn't want to play
                    if shateki_win == 0:
                        "You decided against playing, but Baxter seemed interested, so he smoothly stepped up to the counter."
                        "They handed over a toy gun with a grin, a cork already preloaded. The rest of them sat neatly in the dish in front of him."
                        hide b
                        show bax_at_shoot
                        with dissolve
                        "Baxter examined it carefully, figuring out where to best position himself. He had a gleam in his eyes like he was about to clean out the booth."
                        "You looked over the lineup of prizes. There was quite a spread!"
                        show b e_norm b_norm m_norm
                        hide bax_at_shoot 
                        with dissolve
                        "Baxter glanced back at you."
                        show b b_soft
                        b "Was there anything that caught your eye?"
                        "If you wanted a prize, he'd be more than happy to win one for you."
                        jump prize_neck
                    if shateki_win != 0:
                        if shots_left < 2:
                            "Since there were still corks remaining; you left them to baxter, which he acknowledged with a slight tilt of his head as thanks."
                        if shots_left == 2:
                            "The stall owner had replaced the corks for Baxter's turn, setting the now refilled dish down as he tilted his head in thanks."
                        
                        hide b
                        show bax_at_shoot 
                        with dissolve
                        "With your turn completed, you placed the toy rifle onto the counter, which Baxter picked up."
                        s "Alrighty, go right on ahe–"
                        "The stall owner froze after seeing Baxter step up to the counter."
                        "He had a gleam in his eyes like he was about to clean out the booth."
                        s "{w=0.5}{i}{size=-8}Please have mercy on my prizes...{/size}{/i}{w=0.5}"
                        hide bax_at_shoot 
                        show b e_norm b_norm m_norm
                        with dissolve
                        
                    #If MC didnt win the prize they wanted.
                    if shateki_win == 2:
                        "Baxter leaned against the counter, lining up for his goal quickly and decisively."
                        "...He was aiming for the prize you wanted!"
                        "With a single shot, the cork flew over to the unsuspecting prize, knocking it clean off the countertop."
                        jump sha_prize_line
                    #if mc won but not the large plush
                    if shateki_win == 1 and large_plush == False:
                        jump large_plush_dialogue
                    #If MC shot and won the large plush
                    if shateki_win == 1 and large_plush:
                        $sha_yuzu = True
                        show b e_squint b_one_raised m_norm
                        "Having satisfied his curiosity over the mysterious piece of paper, Baxter was now mulling over the other prizes."
                        "He finally settled on aiming for the drink, taking his time to line up the shot."
                        show b e_surprised m_grin b_raised
                        "With one swift pull of the trigger, the cork soared across the booth, knocking the drink over instantly!"
                        show b e_norm b_norm
                        "The employee caught it just as it rolled off the ledge, placing it onto the counter with a bit of flourish."
                        MC "Nice shooting."
                        show b e_closed b_raised m_grin
                        "Baxter flashed you one of his dazzling smiles as he picked up the bottle."
                        b "Why, thank you."
                        jump leave_shateki

                
                label large_plush_dialogue:
                    #if MC won the large plush
                    if shateki_win == 1 and large_plush: 
                        
                        b "Oh. I {i}was{/i} rather curious about that one."
                        "The stall owner began snickering as they handed over the card."
                        show b e_surprised b_raised m_confused
                        "Opening it, the words 'A Giant Plush' was printed neatly on the page."
                        show b e_side_down 
                        "Baxter looked caught off guard, a rare shocked look on his face before he cleared his throat."
                        show b e_side b_raised m_grin
                        b "I wasn't expecting this. That said, I could help you carry it back if you'd like."
                    #if MC didn't play or won a different prize.
                    if shateki_win == 0 or large_plush == False:
                        if shateki_win != 0: 
                            show b e_squint_dl m_norm b_norm
                            "Baxter took his turn, eyeing the row of prizes and eventually seeming to settle on the blank-looking card."
                        show b b_annoyed e_squint m_norm
                        "He leaned against the countertop, lining up the prize into his sight." 
                        show b e_surprised m_grin b_raised
                        "With a loud pop, the cork flew across the booth, easily knocking over the piece of paper."
                        show b e_norm m_norm b_norm
                        "The stall owner was holding back laughter as they handed over the card. Baxter unfolded it and read it aloud."
                        show b b_one_raised
                        b "A giant plush."
                        show b e_wide b_raised m_confused
                        "You looked around at the large plushies that the owner had around the stall. They had several regular-sized plushies available and ones that were {i}definitely{/i} on the larger side."
                        "But a {i}giant{/i} plush?"
                        show b e_side_down b_sad m_grin
                        "It could only mean that the ones you thought were decorations were actually large, huggable plushies, the size of a person!"
                        show b e_side
                        "Baxter looked caught off guard, a rare shocked look on his face before he cleared his throat."
                        show b e_norm m_norm b_sad
                        b "I admit I was wondering what the prize might be, but now that my curiosity is sated I would like to politely decline."
                        show b e_closed b_raised
                        b "Unless, of course, {i}you'd{/i} like it, [MC]? I will gladly help you carry it back."
                    if shateki_win == 2 and large_plush:
                        "The card was knocked over easily as the cork caught the corner of the page before floating helplessly down onto the counter."
                        show b b_raised e_squint m_norm
                        "Baxter gave you an innocent looking smile as he looked away slightly."
                        show b e_squint_dl
                        b "I {i}was{/i} rather curious about this prize, you know."
                        "As if he wasn't aiming for that because {i}you{/i} were..."
                        if mc_persona == 1:
                            show b b_raised e_squint m_grin
                            "You gave a laugh at his sudden show of passivity, meeting his 'innocent' little smile.."
                            MC "Sure you were."
                        if mc_persona == 2:
                            show b b_soft e_squint m_grin
                            MC "Thanks, Baxter."
                            "Despite his pretend passivity, Baxter's eyes shone with happiness."
                        if mc_persona == 3:
                            show b e_norm b_soft m_norm
                            "Even you couldn't help a wry smile at his sudden passivity, before you nodded your thanks to him."
                            "Baxter glowed with happiness in response."
                        show b e_wide b_raised m_confused
                        "Though his smile was quickly replaced with surprise as he read the words aloud."
                        b "A giant plush."
                        show b e_surprised b_one_raised m_norm
                        "You looked around at the large plushies that the owner had around the stall. They had several regular-sized plushies available and ones that were {i}definitely{/i} on the larger side."
                        "But a {i}giant{/i} plush?"
                        show b e_side m_grin
                        b "Are you perhaps still interested, [MC]? I will gladly help you carry it back..."

                    menu:
                        "You wanted to keep the plush. "(color = "yellow"):
                            show b e_squint b_norm m_grin
                            "Upon seeing that you wanted to keep it, Baxter took on a more serious tone and pulled out his phone from his sleeve."
                            b "I understand."
                            show b e_closed b_raised
                            b "Shall we purchase a return flight for it then?"
                            show b e_norm b_soft m_norm
                            "You laughed. Whether he was serious or not really depended on you."
                            "At the end of the day, you knew Baxter was readily prepared to help with your crazy ideas, especially if it meant planning a party where you’d stay up all night baking."
                            show b b_one_raised e_side_down
                            b "In truth, how about we come back for it later?"
                            show b e_squint_dl
                            b "It would be... rather difficult to carry around..."
                            "Planning for the large plush {i}did{/i} seem to be a hard task, since you weren’t leaving right away."
                            show b e_norm b_norm m_norm
                            "Unexpectedly, the owner spoke before you or Baxter could."
                            s "You two look like you're going to be around for a while. Are you staying for the fireworks?"
                            s "Just leave your winnings here and come back for them later."
                            "It {i}would{/i} be a hassle to go on without your hands free. You thought it was a sensible solution and Baxter agreed with a nod."
                            show b m_grin
                            b "Thank you for the offer. We'll return as soon as we can."

                        "You wanted to hug it at least once." (color = "green"):
                            "At least it would dampen the sting of not being able to bring it back."
                            show b b_sad e_side_down m_norm
                            "With the stall owner's go ahead, you wrapped your arms around the plush you liked the most and gave it a great big hug!"
                            "Its fuzzy material rubbed against your cheek and seemed to envelop you in fluffiness."
                            "When you were satisfied to leave the plush behind, you pulled back."
                            show b e_squint b_raised m_grin
                            b "If you ever feel lonely about leaving our friend here, you can always hug {i}me{/i}."
                            if mc_persona == 1 or mc_persona == 2:
                                MC "Maybe I'll take you up on that."
                                show b m_norm
                                b "Please do."
                            elif mc_persona == 3:
                                "That {i}did{/i} sound nice."
                                show b m_norm
                                "Baxter smiled knowingly."
                            b "The offer will be eternally available to you."
                        
                        "You declined taking it."(color ="blue"):
                            show b e_norm m_norm 
                            "It wouldn't be feasible to return with it."
                            "You and Baxter were on vacation to boot. You would not be subjecting him or yourself to that logistical nightmare."
                    
                    # If MC didn't play or Baxter has had his turn after MC, they leave.
                    if sha_bax:
                        jump leave_shateki
                    else:
                        jump shateki_baxter

                label leave_shateki:
                    show b e_norm m_norm b_norm
                    "The stall owner pinched the brim of their hat, their eyes sparkling underneath the shadow."
                    if shateki_win != 0:
                        s "Well, it was a very fine showing from the both of you!"
                    else: 
                        s "Well, it was a very fine showing from you, sir!"
                    show b m_grin e_closed b_raised
                    b "Thank you for the exciting opportunity."
                    show b m_norm e_norm b_norm
                    s "No, Thank {i}you{/i} for your patronage, dear customers!"
                    show b e_side_down
                    "The owner tipped their hat to the two of you, sporting the same grin."
                    if shateki_win != 0:
                        "As you left, you could catch a glimpse of the owner wiping sweat from their brow, clearly relieved that the two of you hadn't truly cleaned them out."
                    else: 
                        "As you left, you could catch a glimpse of the owner wiping sweat from their brow, clearly relieved that Baxter hadn't truly cleaned them out."

                    if sha_yuzu:
                        show b b_one_raised
                        "Baxter was examining the bottle of juice he'd won, eyeing the neatly printed label with interest."
                        show b e_closed b_raised m_grin
                        b "This was fortuitous timing, considering that I was feeling rather parched."
                        show b e_side_down b_norm m_norm
                        "With a twist of the lid, the drink opened with a 'crack'."
                        show b e_closed b_annoyed
                        b "It smells refreshing as well."
                        show b e_norm b_raised
                        b "Would you like some, [MC]?"
                        jump yuzu_menu
                    if yuzu_drink:
                        show b e_norm b_one_raised
                        "You eyed the bottle in your hands and considered Baxter's earlier comment about sharing with him."

                        menu yuzu_menu:
                            "Have a sip." (color = "blue")if sha_yuzu:
                                $drank_yuzu = True
                                "Baxter passed you the open bottle, the scent of citrus wafting to your nose."
                                "The sweet flavors of the drink tingled on your tongue as you passed it back to Baxter."
                                show b e_wide b_raised
                                "His eyes lit up with delight as he had the same reaction."
                                show b e_closed b_norm
                                "Passing it back and forth between the two of you, the bottle was quickly emptied."
                            "You declined a sip." (color = "yellow")if sha_yuzu:
                                $drank_yuzu = True
                                b "Alright." 
                                show b e_wide b_raised
                                "He took a small sip, a delighted smile coming onto his face."
                                b "It tastes a bit like lemonade, but less sharp. It's delicious."
                            "You shared some with Baxter." (color = "green")if yuzu_drink:
                                $drank_yuzu = True
                                b "Why, thank you."
                                "You handed the bottle over to Baxter and he cracked open the lid."
                                show b e_wide b_raised
                                "He took a small sip, a delighted smile coming onto his face."
                                show b e_closed b_norm m_grin
                                b "It tastes a bit like lemonade, but less sharp. It's delicious."
                                "Passing it back and forth between the two of you, the bottle was quickly emptied."
                            "You drank it yourself." (color = "blue")if yuzu_drink: 
                                $drank_yuzu = True
                                show b e_squint_dl b_one_raised
                                "Twisting open the lid, the scent of citrus greeted your nose. You took a sip to taste test."
                                "It tasted a bit like lemonade, but less sharp. It was delicious."
                                
                            "You saved it for later."(color = "yellow") if yuzu_drink:
                                "You didn't feel thirsty right now, but perhaps later."
                    if drank_yuzu:
                        show b b_norm e_norm m_norm
                        "After finishing the drink, it was thrown in the nearest recycling bin before you both continued onwards."
                    
                    show b b_norm e_norm m_norm
                jump g_checkpoint
            
            #Senbonbiki/String Game
            label senbonbiki_booth:
                $ senbonbiki = True
                $g_completed += 1
                play music lets_build_a_secret_base_2 fadeout 1.0 fadein 1.0 if_changed
                scene matsuri
                show b b_norm e_norm m_norm at left
                with dissolve

                "You passed by a booth with a myriad of strings hanging from the top of the booth. Each one was tied to a prize hidden in the pile."
                "If you tried to follow any to their destination, you’d find yourself lost in a maze of colorful items and the same colored strings."
                "The game itself was rather simple: pulling on a string would give you whatever prize was attached to its end."
                "It was essentially a lottery played with strings."
                "Each string stood tensed from whatever item they were attached to, but none gave any hints to which item that was."
                "It usually ranged from toys to snacks. There was a rumor that you could get a gaming console, but maybe that was only meant to attract the bold and eager."
                show b b_one_raised e_squint 
                "Baxter’s hand cupped his chin as he looked around, amused. It seemed like he wanted to play."
                show a e_norm b_angry m_norm glasses at right
                with dissolve
                "The two festivalgoers before you were still taking their turn. Glancing at the table, there were already at least a dozen fish plushies stacked high, all abandoned by those who {i}won{/i} them but didn't {i}want{/i} them."


                menu:
                    "You wanted to play."(color = "yellow"):
                        $ senbonbiki_play = True
                        jump senbonbiki_together
                    "You didn't want to play."(color = "blue"):
                        show b b_one_raised e_wide m_confused at default
                        hide a
                        with dissolve
                        "The group ahead of you was close to finishing, but their insistence on winning the prize they wanted gave you time to pause."
                        "It was as if Baxter had caught onto your hesitation, or disinterest, as he called out to you."
                        show b b_raised e_norm m_norm
                        b "[MC]?"
                        b "Shall we find something else to occupy our time? I'm certain we can find other activities."
                        "As he spoke, the participating players had wrapped up their game. One walked off in defeat, while the other had a brisk skip in their step as they cradled their bouquet of piscine plushies."
                        
                        menu: 
                            '"I want to watch you play!"'(color = "yellow"):
                                show b b_one_raised e_squint m_grin
                                b "Mm, are you that eager to watch me pull a dud?"
                                show b e_closed
                                "He smiled teasingly, and went despite his little protest."

                            '"Go ahead, Baxter."' (color = "green"):
                                show b b_raised e_squint_dl m_norm
                                b "Very well, but knowing how my luck {i}usually{/i} is... well..."
                                show b e_closed
                                "Despite his protest, he walked forwards towards the strings."

                            "You pantomimed pushing him forward." (color = "blue"):
                                show b b_one_raised e_squint m_grin
                                b "Very well, since you're so eager to see me pull a dud..."
                                show b e_closed
                                "He mock sighed as he walked towards the strings."
                                
                            '"I’d rather find something else."' (color = "yellow"):
                                show b b_soft e_closed m_norm
                                b "Of course."
                                jump g_checkpoint
                            "You left the booth together." (color = "blue"):
                                show b b_soft e_closed m_norm
                                "You didn't need to exchange words with Baxter as the two of you left to find something else to do."
                                show b b_norm e_norm m_norm
                                jump g_checkpoint

                        jump senbonbiki_baxter
                        
                label senbonbiki_together:
                    show b b_norm e_norm m_norm
                    "As you waited for the current players to be finished, the person in green had resolutely grabbed one of the strings, tensing from the anticipation."
                    show a:
                        ease 0.3 xoffset -75
                    pause 0.05
                    show a:
                        ease 0.03 xoffset 0
                    a "{i}Please.{/i} for the love of everything, I just want that fox."
                    "They took a deep breath before pulling the string."
                    show a m_sad b_sad shock:
                        ease 0.3 xoffset -75
                    pause 0.05
                    show a:
                        ease 0.03 xoffset 0
                    show b b_one_raised e_surprised m_confused
                    "You watched as yet another of Cove's friends in plush form laid dangling on the string, much to the chagrin of the player."
                    show b e_squint_dl b_raised m_grin
                    show a e_closed b_sad m_norm tear -shock
                    "They crouched on the ground despondently, while the almost identical-looking person next to them clapped their hands in joy."
                    hide a 
                    show b e_closed at default
                    with dissolve
                    "Done with the game, the pair walked off, one seemingly extremely crestfallen and the other elated with their new bouquet of piscine plushies."
                    show b b_norm e_norm m_norm
                    "The stall owner then nodded to you, signalling for your turn."
                    "Walking up to the counter, you pulled on the..."

                    menu:
                        "First String."(color = "yellow"):
                            $ tenugui = True
                            "The string felt light to pull as your prize came up. A towel cloth with an intricate pattern dangled on the other end."
                            show b b_raised e_squint 
                            "It was soft to touch and felt more handmade than store-bought."
                            b "Oh, what {i}wonderful{/i} craftsmanship. I {i}do{/i} enjoy seeing the work of artisans."
                        "Second String."(color = "green"):
                            $ ani_plush = True
                            "The string felt moderately heavy as you tugged on it. A plush of an animal greeted you, and its body squished pleasantly under your touch when you grabbed it."
                            show b b_raised e_closed m_grin
                            b "What an adorable new friend we've made, and very soft as well."
                            if shiba_plush:
                                show b b_raised e_squint m_grin
                                b "Perhaps it would like to get to know the other little one from the shooting booth as well."
                        "Third String."(color = "blue"):
                            $ tissues = True
                            show b b_raised e_surprised m_confused
                            "The string felt light to tug as your prize was fished up. A small packet of colorful tissues dangled in front of your eyes."
                            show b m_grin
                            "Baxter’s smile broke as a laugh escaped him. He hurriedly tried stifling it."
                            show b e_wide b_raised
                            b "Is this... one of those consolation prizes I've heard a great deal about?"
                            show b e_closed
                            b "At least... it's a rather useful prize, no?"
                        "Fourth String."(color = "yellow"):
                            $ acc_bracelet = True
                            show b b_soft e_squint
                            "The string felt incredibly light as you pulled up a colorful bracelet. Each piece glittered under the light of the booth."
                            show b e_squint_dl
                            b "How marvelous. It reminds me of that one summer, when we crafted those charming little accessories by the shore."
                        "Fifth String."(color = "green"):
                            $ keychain = True
                            "The string felt incredibly light as you pulled up a small keychain with a popular anime character on it."
                            show b b_one_raised 
                            "As it swayed, you saw the holographic flakes making it shine."
                            show b e_closed b_raised
                            b "Aha. I believe this is the same character I saw in Tokyo on that large television screen."
                            show b e_norm b_norm
                            b "They must be quite popular indeed."
                        "Sixth String."(color = "blue"):
                            $ sen_fox = True
                            show b b_one_raised 
                            "The string was moderately weighty as you pulled up an intricate-looking fox mask, its details painted in purple. It was beautifully crafted and made out of paper."
                            "There was a string attached on the back so it was wearable."
                            if shateki == False:
                                show b e_squint_dl 
                                b "That is quite the intricate design, I always enjoy seeing detailing such as this."
                            elif shateki:
                                show b e_squint_dl b_norm
                                b "I believe we saw a similar mask at the shooting gallery earlier. What a delightful coincidence."
                            elif shateki and fox_mask_change:
                                b "Oh, have we found the missing half of this pair?"
                                "Baxter tapped the side of his mask."
                    
                    show b b_norm e_norm m_norm
                    "As you held the prize in your hands, you thought..."

                    menu: 
                        "You were elated to have won." (color = "yellow"):
                            $senbonbiki_prize = True
                            "Winning was a good thing. Winning what you wanted was even better."
                        "You felt neutral about your prize." (color = "green"):
                            $senbonbiki_prize = True
                            "You supposed that winning was better than losing, but you didn't really feel anything in particular this time."
                        "You didn't really like the prize, and gave it back." (color = "blue"):
                            "It was a tad underwhelming to you. You placed the prize back onto the counter as the stall owner nodded in understanding."
                        "At least it wasn't fish."(color = "yellow"):
                            $senbonbiki_prize = True
                            "You took comfort in knowing it wasn't another of Cove's friends that you had fished up."
                            "{i}Unlike that other poor soul...{/i}"
                        "You declined the prize." (color = "green"):
                            "With a resolute nod, you placed the item back onto the counter. The owner nodded in understanding."
                    
                    if mc_persona == 1:
                        "Assured of your decision, you turned to look at your partner."
                        MC "It's your turn, Baxter."
                    if mc_persona > 1: 
                        "Satisfied with the outcome, you gestured for Baxter to take his turn."

                label senbonbiki_baxter:
                    if senbonbiki_play:
                        show b b_one_raised e_closed m_grin
                        b "Very well. What's life without a little surprise in it?"
                        show b b_norm e_squint 
                        "Baxter confidently strolled up to the booth, the stall owner giving him a nod as Baxter returned it."
                    hide b
                    show bax_at_string 
                    with dissolve
                    "He looked thoughtful, almost as if he was silently calculating which string would bring him to victory."
                    "He grasped a seemingly random string, giving a sharp tug as his prize emerged from below the countertop."
                    show b e_wide b_raised1 m_grin
                    hide bax_at_string 
                    with dissolve
                    "A fuzzy zebra keychain hung on the end of it in all its black and white glory and incredibly cute beady eyes."
                    "Baxter looked positively thrilled, basking in all the lovely coincidences of his favorite colors."
                    show b e_closed
                    "He held the zebra charm lovingly, like it was gold in his hands."

                    menu:
                        '"It looks just like you!"'(color = "yellow"):
                            show b e_squint 
                            "Between his outfit and the keychain, you could see a resemblance... granted, a {i}distant{/i} resemblance."
                            "Baxter dangled the charm next to his face, facing the zebra towards you. He put on his best professional smile."
                            show b b_one_raised
                            b "Twins perhaps? Fraternal twins?"
                            show b e_closed
                            b "I’ll even accept distant cousins."
                            "Baxter chuckled at each absurd comment he made, but you nodded in seriousness."
                            MC "Absolutely, you’re identical."
                            show b e_squint 
                            b "Excellent."
                        '"I’m happy for you."'(color = "green"):
                            show b b_norm 
                            b "As am I. Thank you, [MC]."
                        "You clapped politely."(color = "blue"):
                            show b e_squint m_norm
                            "Baxter took a slight bow, dipping the small keychain to mirror him."
                            show b b_norm e_squint_dl m_grin
                            b "You're too kind."
                        '"It matches your slippers!"'(color = "yellow"):
                            show b e_wide b_one_raised
                            b "So it does."
                            show b e_squint_dl 
                            b "Though I don't believe our new friend here would be keen on becoming the next pair."
                        '"What are the chances..."'(color = "green"):
                            show b e_wide b_one_raised m_norm
                            "Baxter grinned, turning the keychain over to make sure it wasn’t his imagination."
                            show b e_closed b_norm m_grin
                            b "Apparently, much higher than I would like to think."
                    
                    show b e_squint_dl b_annoyed m_norm
                    "Baxter took another look at the charm, contemplating on whether or not to keep this new companion. Finally, he responded:"
                    show b e_closed b_raised
                    b "I believe I'll keep it. It'll be a nice little reminder of this evening."
                    show b e_squint b_one_raised
                    "Baxter tucked the charm away in his sleeve. Where he was keeping his things was certainly a mystery. He chuckled to himself, as if he knew what you were thinking."
                    show b e_squint_dl b_norm m_grin
                    b "Had I won any larger prize, I doubt I could hide it away as efficiently."
                    if mc_persona == 1:
                        show b e_squint b_annoyed
                        MC "Is that one of your mysterious planner abilities?"
                        
                        "You were teasing, but Baxter played along with this new identity you had given him."
                        show b b_raised1 e_closed 
                        b "Along with being able to scrounge up a plan for an extremely last minute party or two, yes."
                    elif mc_persona == 2:
                        show b e_squint_dl b_raised
                        MC "You would've figured something out."
                        show b b_raised1 e_closed 
                        b "I appreciate the vote of confidence."
                        show b b_norm e_norm m_grin
                        b "I suppose improvisation helps when you need to plan or help with a last minute party or two."
                    elif mc_persona == 3: 
                        show b e_squint b_one_raised
                        "You briefly wondered how he was doing that, but chalked it up to Baxter being his usual enigmatic self."
                        show b m_grin e_closed b_norm
                        "Baxter seemed to know what you were thinking there as well, but left it there with a quiet laugh."
                    show b e_norm b_norm m_norm
                    b "Now then, shall we be off? Please lead the way. [MC]."
                    b "I'm looking forward to whatever comes next."

                jump g_checkpoint
            
            #River Lanterns
            label lantern_booth:
                play music sunset_on_the_beach fadeout 1.0 fadein 1.0 
                scene river
                show b b_soft e_norm m_norm
                with dissolve
                "After a short walk, you found yourself approaching the riverside that you were searching for."
                "It was a small ways away from the festival itself, the sound of the bustling streets and tents fading into the background as you neared it."
                "The sight was truly something to behold."
                show b b_raised e_surprised 
                "You could have easily mistaken the river to have been the night sky brought down to earth."
                "The lanterns scattered across the water's surface, gently flickering against the dark background and reminding you of stars against the dark void of space."
                "Turning to look at Baxter, you could see the awe on his face as he took in the scene as well."
                "Feeling your gaze on him, he turned to you, excitement apparent in his expression."
                MC "Isn’t it a beautiful view?"
                show b b_soft e_side_down
                b "It really is. I wonder if we might be able to put a lantern out?"
                show b e_norm
                b "Only one way to find out. Shall we?"
                "As you approached, you saw a group of people listening in on the overseer of the event, who was explaining the traditions behind the lanterns."
                show b e_squint_dl b_norm
                "Baxter listened with curiosity, head tilted much like a kitten intrigued by a toy that was presented to them."
                hide b 
                with dissolve
                menu:
                    "You listened as well."(color = "green"):
                        s "Traditionally, lanterns are released during the O-Bon festival, when the spirits of our ancestors are said to visit the living."
                        s "These flowing lanterns, or 'Toro Nagashi', are said to guide them back to the afterlife once their visits have concluded."
                        s "You'll find that people typically write personal thoughts and messages on the paper."
                        s "Though, these days, a lot of visitors like this tradition even outside O-Bon."
                        s "Please feel free to write your hopes, your wishes, or even your concerns onto them, and watch as the river carries them all away."
                        
                    "You tuned it out." (color = "yellow"):
                        scene river:
                            blur 25
                        with dissolve
                        "You turned to look out at the dark river, where tiny specks of light could be seen at the very end of how far you could see."
                        "The surrounding area itself was dimly lit, no doubt to give more attention to the beauty of the lanterns."
                        "You listened to the sounds of the river until the end of the attendents speech brought back to reality."
                        scene river
                        with dissolve

                s "Ah, and please don't worry about the impact to the environment!" 
                s "Though it's not seen from here, we have a net in place to catch the lanterns- and more staff in the area to ensure none of these harm nature."
                show b b_norm e_norm m_norm at left 
                show m at right
                with dissolve
                "The employee began handing out pens to pseudo groups that had formed."
                s "Now, if everyone would please release their lanterns in groups of three or less to avoid traffic-"
                s "And I do apologize, but we have a limited number of pens at the moment, so please wait for other people to finish using theirs!"
                "Now that they were seemingly at the end of their talk, Baxter spoke quietly to you."
                show b b_raised e_closed m_grin
                b "What a beautiful tradition. I would very much like to send my wish out to the universe."
                show b b_norm e_side_down m_norm
                "Looking around, your attention was caught by a woman with hair the color of sunflowers. She had on a secretive smile as she twirled a pen in her hand and considered what to write."
                "After a moment of thought, she scribbled down on the lantern before picking it up."
                "Since she was done, she looked to you and handed over the pen."
                m "Here you go."
                hide m
                with dissolve
                "With that, she sashayed away."
                show b e_norm at default with dissolve
                "While you stood there, lanternless but at least having a pen now, the overseer of the event came up to you and Baxter with a wave."
                s "Hello, I hope you two are enjoying yourselves! Did you need me to explain what the tradition is about?"
                show b b_raised e_closed m_grin
                b "Oh, no. We were listening as you spoke with the previous group. The tradition seems truly lovely and we would like to participate."
                show b b_norm e_norm m_norm
                s "That's great! Let me get you set up with the lanterns, and another staff member will help you light them by the river bank."
                s "Please ensure that you write gently with the pen, as the paper can be broken if too much force is used."
                "With a small laugh, they handed over two unlit lanterns. After making sure you and Baxter were comfortable with the assignment, they moved on to help the others that showed up."
                show b b_one_raised e_squint_dl
                "Lanterns in hand, the two of you went out to pick a spot to release the pair of them."
                "Placing his own down momentarily, Baxter began penning something onto it immediately. After listening to the overseer, it seemed he knew {i}precisely{/i} what he wanted to wish for."

                menu:
                    "You wanted to sneak a peek at what Baxter was writing." (color = "yellow"):
                        show b e_squint b_annoyed
                        b "Ah, no peeking."
                        "He hugged his lantern close to himself, giving you a teasingly chastising look."
                        show b e_closed b_raised1 m_grin
                        b "You know the secret to having a wish come true - you {i}cannot{/i} tell anyone. All the fairy tales say so."
                        show b e_squint b_one_raised m_norm
                        MC "What if we both wish for the same thing by accident?"
                        show b e_squint_dl m_grin
                        "Giving you his cheshire grin, Baxter couldn’t help the chuckle that left him."
                        show b e_squint
                        b "Well then, all the better chances for it coming true."

                        if b_initiative == 1:
                            show b b_annoyed m_norm e_squint
                            "Eyes sparkling with mirth, Baxter brought you close and left a soft kiss on your temple, his warm breath scattering across the side of your face."
                            show b b_one_raised e_squint_dl blush
                            "As he pulled back, you could see the slight pinkness of his cheeks before he returned to writing his wish."
                            "Taking in his profile, you could feel your own cheeks warm at his blatant adoration. No matter how much time has passed, you felt like you would never get over his darling ways to show how much he cared for you."
                            show b b_norm e_side_down m_norm -blush
                            "Clearing your throat, you turned back to your lantern."
                        elif b_initiative == 2:
                            show b b_annoyed m_norm e_squint
                            "Eyes sparkling with mirth, Baxter went closer to you and waited for your reaction. When you didn’t pull away, he left a soft kiss on your temple, his warm breath scattering across the side of your face."
                            "As he pulled back, you could see the slight pinkness of his cheeks before he returned to writing his wish."
                            show b b_one_raised e_squint_dl blush
                            "Taking in his profile, you could feel your own cheeks warm at his blatant adoration. Baxter had a talent for being able to fluster you, and his public displays of affection certainly brought it out of you."
                            show b b_norm e_side_down m_norm -blush
                            "Clearing your throat, you turned back to your lantern."
                    "You focused on your own." (color = "green"):
                        "You considered what the overseer had said: that whatever you wrote could be your personal thoughts, a wish, or even a hope."

                    
                menu:
                    "You already had a good idea of what to write." (color = "yellow"):
                        "Using the pen you received earlier, you started to write on the paper. All your hopes and wants, you manifested in written form onto the lantern."
                        "It didn’t take long, and you were done by the time Baxter had approached you, lantern in tow."
                        show b e_norm b_norm 
                        b "All finished, [MC]?"
                        MC "Yep! I knew exactly what I wanted to put down for as soon as we learned what this was about."
                        "With a soft chuckle, he looked over your lantern with interest."
                        show b e_squint_dl m_norm
                        b "I must admit I {i}am{/i} a touch curious to know what you had written, but that would ruin all the fun."
                    "But you needed to think about it for a bit." (color = "green"):
                        "You were uncertain what to write. There were so many things that you {i}could{/i} write, and yet none came to mind as the one you wanted to write down on your lantern."
                        "It wasn’t until Baxter had finished writing his secret wish and came to check on you that you had finally figured out what to go with."
                        show b e_norm b_sad
                        b "Having trouble deciding?"
                        MC "I was, but not anymore. Give me a second."
                        show b b_raised e_squint m_grin
                        b "Of course. I’ll make sure not to look over your shoulder and take a peek."
                        MC "Much appreciated."
                        show b e_side_down b_norm m_norm
                        "It didn’t take you long to write what you had wanted to, your words flowing earnestly from your heart to your pen."
                    "You didn’t feel like writing anything."(color = "blue"):
                        "Though you thought it was a lovely tradition, you found yourself being unable to find anything you would want to write."
                        "Patiently, you waited as Baxter finished writing on his and approached you, lantern in tow."
                        show b e_norm b_sad
                        b "Did you not wish to write a wish down?"
                        MC "Not really. I don’t have any wishes that I can think of that need to come true."
                        show b e_closed b_raised
                        b "You have always taken life by the reins and brought your wants and dreams to life, so it doesn’t surprise me that you couldn’t think of one."
                        show b e_norm b_soft
                        b "Shall we then?"

                    
                hide b
                with dissolve
                "You passed the pen to the new group of people that had arrived, and together you and Baxter went to the waterside."
                "Others had already begun releasing their lanterns onto the water and letting them float gently down the stream."
                "A passing staff member helped light the lanterns, and reminded the two of you to be careful with the open flame."
                show rl e_norm
                with dissolve
                "Baxter held his lantern gently, gazing into the flickering light that shone through the paper walls."
                "It was mesmerizing to see that very light flicker off his hazel eyes - it further brought out the warmth of them."
                "You could swear at times that you could heat yourself up with just those eyes, like one would at the hearth of a fireplace."
                "Baxter turned to look at you, a smile playing at his lips as he silently stepped up to the riverbank. Crouching down, he took care in how he placed the lantern onto the water's surface, wanting to make sure it didn’t tip."
                "Following his lead, you crouched next to him and set your lantern beside his."
                hide rl
                scene lantern
                with dissolve
                "Together, you both let go of the lanterns and watched as they floated down the river. Side by side, the lanterns bumped into one another, pushing each other further along the stream but never drifting far apart."
                "{i}Much like their owners.{/i}"
                "You saw as they joined the rest of the lanterns floating in the water, grouping together like constellations in the night sky. The vision was magical in every way."
                "Quietly, you stood with Baxter, taking in the scene before you and thinking about everything that brought you here today."
                "The exciting summer of 2016 where you had a whirlwind romance with him that ended in you parting ways."
                "That fateful summer of 2021 where you reconnected with him after five years of emptiness without him."
                "The time after where you both wanted to make this work - took the time to understand each other, build your relationship, and look towards a future hand in hand."
                "There was once a time you didn’t think that was going to be possible. You were grateful that Lady Fate had played her games with you to give you the chance to try at least one more time."
                "Now, you stood with him, watching the night sky descend into the river."
                "Life was full of wonderful coincidences."
                show b b_norm e_squint m_norm
                with dissolve
                b "[MC], I have something for you."
                "Baxter’s voice drew you out from your thoughts."
                show b b_sad e_norm 
                "Turning to face him, he regarded you warmly as he silently asked for your hand."
                show b e_closed
                "Slipping his own hand into the sleeve of his yukata, he pulled out a small object that you couldn’t make out just yet."
                if b_initiative == 1 or b_initiative == 2: 
                    "Grasping your hand gently, he pressed the small object into your palm."
                elif b_initiative == 3:
                    "Hovering lightly above your hand, he pressed the small object into your palm."
                
                show b e_norm
                "In the middle of your hand sat a small black and white charm, still warm from his body heat."
                "You recognized the design - plenty of stalls were selling them in a variety of colours and patterns, all having something different embroidered into it. ‘Omamori’ came to mind when you tried to remember the name."
                "You couldn’t make out what the embroidered design was - though it was clear that it was kanji, you didn’t know what it stood for."
                show b e_squint_dl
                b "I was waiting for a good time to give this to you."
                show b e_side_down
                "He paused. His next words sounded hesitant."
                show b b_annoyed 
                b "That summer... You had given me so much. A {i}wonderful{/i} summer, a charming partner, and gifts to help me remember my time at Sunset Bird... with you."
                show b b_angry e_squint_dl
                b "Despite that, I never got anything {i}for{/i} you, most likely due to not wanting to leave anything to tie you to me. If you had something to remember me by... it would’ve been harder to forget me."
                show b b_sad e_norm
                b "{i}But,{/i} well... I’ll spare you the pity party that you know all too well."
                show b b_soft
                "He looked downcast for a moment as he stared at the charm you still held in your hands, but when you made eye contact, he softened."
                show b b_annoyed
                b "This time, I want us both to have something to take home after this. A reminder of our time together; the excitement, the fun, and more importantly, {i}us{/i}."
                show b b_soft e_side
                "Baxter’s gaze warmed you to your core. Though you knew he had many regrets of those five years that he kept you at a distance, everything in his eyes told you that he was coming to terms with that."
                "That he wanted to move forward into a future with you, leaving the regrets behind and taking life by the reins, forging into a life that he could be proud of."
                "With {i}you{/i} by his side."
                show b b_raised e_surprised m_confused blush
                "Closing your hand around the gift, you pressed it to your heart as you leaned towards him."
                if mc_persona == 1:
                    "You were close enough that you could see the deviation of the warm browns in his eyes, and how wide his pupils had become at seeing you so close."
                    show b b_one_raised e_wide
                    MC "Can I expect a present every summer then?"
                    "Cupping his face, you could hear his quiet intake of breath at the contact before he could respond."
                    show b b_sad e_norm m_grin
                    b "{i}Every summer,{/i} for as long as you'll have me. I’ll mark each one with a new gift."
                    MC "I might need to get more shelving to store it all."
                    show b e_closed -blush
                    "The ever adorable ‘Baxter Snort’ made its debut - as you continued to take him in adoringly, he couldn’t help but chuckle at your comment."
                    show b b_annoyed m_norm e_squint
                    "Nuzzling into your hand as he covered it with one of his own, Baxter regarded you with sparkling eyes,"
                    show b b_one_raised 
                    b "I’ll help you choose a fitting one then. I'll need to make sure they are displayed appropriately."
                    MC "I can't wait."
                    hide b
                    with dissolve
                elif mc_persona == 2:
                    show b b_sad e_wide m_confused
                    MC "You’ve already given me a lot, Baxter."
                    "He regarded you with a soft look."
                    show b b_sad e_side m_norm
                    b "Yet, I feel like it’s never enough. I truly don’t believe that I’ll ever be able to give you all that you deserve."
                    show b b_raised e_wide m_confused
                    "Reaching up to cup his face, you could hear his quiet intake of breath at the contact."
                    show b b_sad e_norm m_grin
                    MC "All I ever need is {i}you.{/i} While I won’t say no to you showering me with gifts, all I could ever ask for is to have you by my side."
                    show b b_sad e_closed m_norm
                    "Leaning into your hand, Baxter’s eyes fluttered closed before he made a hushed promise to you."
                    b "For as long as you’ll have me, I’ll stay by your side. {i}I swear.{/i}"
                    hide b
                    with dissolve
                    "You matched his soft look with your own as you both took each other in, the rest of the world seeming to disappear around you."
                elif mc_persona == 3:
                    "Though you could feel your cheeks warming in your flustered state, you wanted to speak your heart's desires to him."
                    show b b_raised e_wide m_confused
                    MC "You’re all the souvenir that I’ll ever need, Baxter."
                    "Reaching up to cup his face, you could hear his quiet intake of breath at the contact."
                    show b b_sad e_norm m_grin
                    MC "Thank you. I... will treasure this gift, like how I treasure you."
                    show b m_norm
                    "If your words didn’t make you blush even further, then his intense stare of adoration surely did. You didn’t think his already warm brown eyes could get brighter, but you were wrong."
                    show b b_sad e_closed m_norm
                    "Covering your hand with his own, Baxter leaned into the touch,"
                    b "You never cease to make me realise how lucky I am to know you, {i}to be with you.{/i}"
                    hide b
                    with dissolve
                    "You matched his soft look with your own as you both took each other in, the rest of the world seeming to disappear around you."

                #CHECK
                "Rubbing the charm between your fingers, you were reminded of the embroidery that had caught your attention - the kanji that you couldn’t read." 
                show b e_norm b_norm m_norm
                with dissolve
                MC "Hey, Baxter?"
                show b b_one_raised
                b "Yes, darling?"
                MC "Do you know what's embroidered on the charm?"
                show b b_sad e_side_down blush with dissolve
                "The flush of pink on his cheeks was endearing. It was like he was caught out on a secret he wasn’t supposed to share."
                show b e_squint_dl
                "Shuffling on the spot, Baxter’s eyes darted from yours to your hand, before darting back, almost as if he was flustered at the question."
                show b e_squint b_annoyed
                "He was very rarely like that, so it made you even more curious as to what was on the charm."
                show b b_sad e_norm 
                b "{i}It means love.{/i}"
                "His voice was hushed, but there was no hesitation."
                show b e_wide b_sad 
                "Well, {i}that certainly made sense.{/i} As your heart beat so hard that you could hear it in your ears, you placed a hand over his and felt the hummingbird pattern his own heart fluttered at."
                "If only you were not out in public, at a festival where people rushed past you to see the entertainment themselves, you might’ve considered pulling him in for a kiss."
                show b b_raised m_confused -blush
                "Alas, before you got the chance to even make such a decision, a group of people excitedly brushed past you, jostling you and breaking the intimate moment you had with Baxter."
                "He held you close, making sure that you didn’t get hurt by stumbling too far."
                show b b_angry e_squint_dl m_grin blush
                "Then, clearing his throat, he pointedly avoided your eyes as the blush grew on his cheeks."
                show b b_raised e_squint -blush
                b "Perhaps we should move on from here. It seems to be getting a touch busier."
                MC "Yeah, let’s head on back."
                scene matsuri
                show b b_norm e_norm m_norm
                with dissolve
                if fest_food == False: 
                    jump date_options
                else:
                    jump separation_last
            
            #Katanuki/Die Cutting
            label katanuki_booth:
                play music a_relaxed_afternoon fadeout 1.0 fadein 1.0 
                scene matsuri
                show b b_norm e_norm m_norm
                with dissolve
                $g_completed += 1
                $ katanuki = True
                "Under the shade of a tent, a gaggle of people were hovering around the entrance, seemingly watching other patrons enjoying a game."
                show b b_one_raised
                "Curious, you wanted to see what all the fuss was about."
                if mc_persona == 1:
                    show b e_norm
                    "You threaded your fingers with Baxter's and gave him a slight tug."
                    MC "Hey, why don’t we go see what’s happening over there?"
                    show b e_closed b_norm
                    "Baxter squeezed your hand in return as he turned to eye the spot you were looking at."
                    show b e_squint m_grin
                    b "Oh. Well, that {i}certainly{/i} has people excited."
                    MC "My thoughts exactly."
                    show b b_norm e_norm m_norm
                    b "Very well. Let us see what the commotion is then, hmm?"
                    "Hand in hand, you both made your way towards the tent."
                elif mc_persona == 2:
                    show b e_norm
                    MC "That looks interesting." 
                    "Baxter turned to look as you pointed at the tent."
                    show b b_one_raised squint m_grin
                    b "It certainly {i}has{/i} attracted a crowd, hasn’t it?"
                    show b b_norm e_closed
                    b "Let us have a gander, hm?"
                    show b b_norm e_norm m_norm
                    "Offering him a smile, you took a step towards the commotion, Baxter following eagerly behind."
                elif mc_persona == 3: 
                    show b e_norm b_soft 
                    "Pulling gently at his yukata sleeve, you caught Baxter’s attention."
                    "Turning to you, his soft eyes questioned you before you wordlessly urged them in the direction of the tent."
                    show b b_one_raised e_squint m_grin
                    b "Ah, that certainly seems to have people excited."
                    show b b_one_raised m_norm e_norm
                    b "Shall we see what the fuss is about?"
                    show b b_norm e_norm m_norm
                    "Nodding shyly, you both made your way towards the tent."

                "As you approached, some of the crowd dispersed, giving you a chance to take a peek past those remaining."
                "Peering inside, you watched an activity that would very well test the extent of Baxter’s artistic abilities today."
                show b e_squint_dl b_annoyed
                "Displayed on the tables was an assortment of molded candies, each featuring a distinct shape embedded within them. Next to the candy was a needle."
                
                "Sitting at tables, patrons were huddled over their respective candy and were trying to carve out a shape from the mold with a needle."
                show b e_surprised b_raised1 m_confused
                "Your attention was drawn to an individual who was meticulously carving a flower from their molded candy - one which seamlessly complemented the floral theme of their yukata."
                "Verdant eyes focused on their task as they pressed the needle carefully into the candy and, with a few precise movements, the flower popped out cleanly from the mold."
                show b e_side_down b_sad m_norm
                "With a satisfied smile, they took their flower and left the tent, leaving a table ready to be tidied up and available for the next willing contestant."
                
                "Turning to Baxter, you noticed the apprehension on his face as he watched the other patrons, proving your earlier suspicions."
                if mc_persona == 1:
                    show b e_squint b_annoyed 
                    MC "Like staring down an old opponent, right?"
                    show b m_grin
                    b "Very much so."
                elif mc_persona == 2:
                    MC "What's wrong?"
                    show b e_squint b_annoyed 
                    b "Ah. Well..."
                elif mc_persona == 3: 
                    "You didn’t say anything, but he could feel you observing him and his dread over what this game was about."
                    show b e_squint b_annoyed m_grin
                    b "I never thought that the past would come back to haunt me so."
                show b b_sad e_side_down m_norm
                "Though he was staring at the candy as if it was a sworn enemy of his - not unlike a certain chocolate fountain - you could see a soft smile playing at the edge of his lips."
                show b e_norm
                "His deep brown eyes found yours as he tried to explain himself."
                b "While reminiscing is something of a pastime of mine, I {i}do{/i} recall a particular game controller that had given me a run for my money... {i}and possibly some of my sanity.{/i}"

                menu:
                    '"It was a group effort!"'(color = "yellow"):
                        show b e_squint b_raised1 
                        b "I {i}do{/i} also recall someone single-handedly swooping in to save me."
                        MC "I believe I used two hands."
                        if b_initiative == 1:
                            show b e_squint b_annoyed m_grin
                            "Baxter clasped your hands in his before bringing it to his lips, leaving a soft kiss on your knuckles."
                            b "{i}Semantics.{/i} Naturally, you remain my gallant savior of that evening."
                        if b_initiative == 2: 
                            show b e_squint b_raised1 
                            "Baxter extended a hand out to you in a wordless request, waiting for your response."
                            show b e_squint b_annoyed m_grin
                            "As you placed your hand in his, he clasped your hand in his before bringing it to his lips, leaving a soft kiss on your knuckles."
                            b "{i}Semantics.{/i} Naturally, you remain my gallant savior of that evening."
                        if b_initiative == 3:
                            show b b_soft e_norm m_norm
                            b "If I may?"
                            "Baxter extended a hand out to you - a request to hold your hand written on his face, as well as in his words."
                            menu:
                                "You placed your hand in his." (color = "yellow"):
                                    show b b_soft e_closed 
                                    "Placing your hand in his, he clasped your hand in his before bringing it to his lips, leaving a soft kiss on your knuckles."
                                    show b m_grin b_raised e_norm
                                    b "You remain my gallant savior of that evening to this day."
                                "You abstained." (color = "green"):
                                    "You gave him a soft smile as you shook your head. He was unphased by it, pocketing his hand back into his yukata and giving you a brilliant smile."
                                    show b m_grin b_raised e_norm
                                    b "You remain my gallant savior of that evening to this day."
                    '"You got it eventually."'(color = "green"):
                        show b e_side_down b_angry m_norm
                        b "True, though it {i}has{/i} remained a stern reminder of why I remain an {i}appreciator{/i} of the arts rather than a {i}participant.{/i}"
                        show b e_squint 
                        b "Speaking of which..."
                        show b b_raised 
                        "He directed his attention towards you - a look of that certain appreciation in his eyes."
                        show b b_raised1 m_grin e_closed
                        b "I consider myself rather fortunate that I am able to view such an {i}exquisite{/i} example of art on the regular."
                        if mc_persona == 1:
                            show b b_one_raised e_wide m_confused
                            "You gave him a sparkling smile as you leaned in and left a soft kiss on his cheek."
                            b "{i}Ah.{/i}"
                            show b m_norm e_squint
                            b "Not that I’m complaining, but {i}what was that for,{/i} my dear?"
                            MC "For your flattering words."
                            show b b_soft e_side_down blush
                            "A soft blush colored Baxter’s cheeks as his eyes cast aside, unable to keep eye contact with you after flustering him so."
                            show b b_norm e_closed -blush
                            "Clearing his throat, he tried to set the conversation back on track."
                        elif mc_persona == 2:
                            "You rolled your eyes at his flirtations."
                            show b b_one_raised e_wide m_confused
                            MC "Flatterer."
                            "Baxter placed a hand on his chest in mock offense."
                            show b m_sad
                            b "I would never speak a lie."
                            "You snickered at his antics, which made him drop his act to chuckle along with you."
                        elif mc_persona == 3: 
                            "You blushed furiously at his blatant flirtations, unable to keep eye contact with him."
                            show b b_soft e_closed m_grin
                            "Seeing how he flustered you, Baxter chuckled lightly,"
                            show b e_norm m_norm
                            b "Apologies, [MC]. I didn’t mean to fluster you so."
                            "He offered you a soft smile, his apology evident in the furrow of his brow."
                            "You returned his smile with your own, though the blush on your cheeks wasn’t going anywhere anytime soon."
                    "You snickered good-naturedly."(color = "blue"):
                        show b b_raised1 e_squint_dl
                        "You could see him roll his eyes in mock indignation."
                        show b m_grin e_closed
                        b "So lovely of you to break the news to me that I wont be the next Da Vinci."
                        show b e_squint
                        b "I suppose I shall console myself by appreciating the masterpieces instead."
                        "His gaze fell on you with the last line."
                        if mc_persona == 1:
                            show b b_one_raised e_wide m_confused
                            "You gave him a sparkling smile as you leaned in and left a soft kiss on his cheek."
                            b "{i}Ah.{/i}"
                            show b m_norm e_squint
                            b "Not that I’m complaining, but {i}what was that for,{/i} my dear?"
                            MC "For your flattering words."
                            show b b_soft e_side_down blush
                            "A soft blush colored Baxter’s cheeks as his eyes cast aside, unable to keep eye contact with you after flustering him so."
                            show b b_norm e_closed -blush
                            "Clearing his throat, he tried to set the conversation back on track."
                        elif mc_persona == 2:
                            "You rolled your eyes at his flirtations."
                            show b b_one_raised e_wide m_confused
                            MC "Flatterer."
                            "Baxter placed a hand on his chest in mock offense."
                            show b m_sad
                            b "I would never speak a lie."
                            "You snickered at his antics, which made him drop his act to chuckle along with you."
                        elif mc_persona == 3: 
                            "You blushed furiously at his blatant flirtations, unable to keep eye contact with him."
                            show b b_soft e_closed m_grin
                            "Seeing how he flustered you, Baxter chuckled lightly,"
                            show b e_norm m_norm
                            b "Apologies, [MC]. I didn’t mean to fluster you so."
                            "He offered you a soft smile, his apology evident in the furrow of his brow."
                            "You returned his smile with your own, though the blush on your cheeks wasn’t going anywhere anytime soon."
                    "You shivered from the horror of the memory."(color = "yellow"):
                        show b e_wide b_raised m_sad
                        b "Don’t worry, [MC], the cake cannot hurt us anymore."
                        show b e_closed b_annoyed m_grin
                        b "It may not have been a masterpiece, but one doesn’t have to look far for a true wonder."
                        show b e_squint
                        "His gaze fell on you with his last words."
                        if mc_persona == 1:
                            show b b_one_raised e_wide m_confused
                            "You gave him a sparkling smile as you leaned in and left a soft kiss on his cheek."
                            b "{i}Ah.{/i}"
                            show b m_norm e_squint
                            b "Not that I’m complaining, but {i}what was that for,{/i} my dear?"
                            MC "For your flattering words."
                            show b b_soft e_side_down blush
                            "A soft blush colored Baxter’s cheeks as his eyes cast aside, unable to keep eye contact with you after flustering him so."
                            show b b_norm e_closed -blush
                            "Clearing his throat, he tried to set the conversation back on track."
                        elif mc_persona == 2:
                            "You rolled your eyes at his flirtations."
                            show b b_one_raised e_wide m_confused
                            MC "Flatterer."
                            "Baxter placed a hand on his chest in mock offense."
                            show b m_sad
                            b "I would never speak a lie."
                            "You snickered at his antics, which made him drop his act to chuckle along with you."
                        elif mc_persona == 3: 
                            "You blushed furiously at his blatant flirtations, unable to keep eye contact with him."
                            show b b_soft e_closed m_grin
                            "Seeing how he flustered you, Baxter chuckled lightly,"
                            show b e_norm m_norm
                            b "Apologies, [MC]. I didn’t mean to fluster you so."
                            "He offered you a soft smile, his apology evident in the furrow of his brow."
                            "You returned his smile with your own, though the blush on your cheeks wasn’t going anywhere anytime soon."
                
                show b b_norm e_norm m_norm
                "A shout from another contestant caught Baxter’s attention - begrudgingly, he tore his gaze away from you to observe the others once again."
                show b b_sad e_side_down
                "Brows furrowed, he seemed torn between wanting to play and not making a fool of himself."
                show b e_side
                "Finally, he spoke up with a distinctly defeated tone."
                show b e_closed m_grin
                b "...I believe I’ll abstain from this one."
                ##CHECK
                show b e_norm
                if senbonbiki:
                    b "I'm certain my luck at the lottery was merely a fluke. I would rather not push it any further."
                else:
                    b "Knowing how my luck holds up, I would rather not take my chances." 
                menu: #
                    '"Baxter, pretty please~"' (color = "yellow"):
                        show b e_surprised b_raised1 m_confused
                        "You batted your eyelashes at him."
                        show b e_squint_dl b_angry m_grin
                        "Baxter's eyes briefly flitted to the heavens as he let out a humoured sigh,"
                        b "{i}What am I going to do with you?{/i}"
                        show b e_squint b_annoyed m_grin
                        "You heard him mumble that under his breath as he stepped up to the tent."
                    '"I’d like to see you play though."'(color = "green"):
                        show b e_closed b_sad 
                        "Baxter sighed good-naturedly,"
                        show b e_squint b_annoyed m_grin
                        b "Very well."
                        "Plastering on his cheshire smile as a shield, he approached the tent."
                    "You nudged his shoulder playfully." (color = "blue"):
                        show b e_closed b_sad 
                        "Baxter sighed."
                        show b e_squint_dl b_angry m_grin
                        b "{i}The things I do for you...{/i}"
                        show b e_squint b_annoyed m_grin
                        "You heard him mumble that under his breath as he stepped up to the booth."
                        
                    ## I could see another option here where the MC doesn't plead with/nudge him towards playing, but he sees their disappointment and gives in anyway; his version of Hang has something similar
                    
                    # "You gave him a soft smile"(color = "yellow"):
                    #     MC "I get that. I would still like to try though. Do you want to watch?"
                    #     b "You should know without a shadow of a doubt, that I would love to observe you take on this task."
                    '"Let’s go find something else."' (color = "green"):
                        show b b_norm e_norm m_norm
                        b "Let's. I'm certain we can find something else to occupy our time together." 
                        jump g_checkpoint
                
                label katanuki_together:
                    show b b_norm e_norm m_norm
                    "You went up behind Baxter, ready to try your hand at the game."
                    s "Hello! Are you wanting to have a try at diecutting?"
                    show b m_grin
                    b "We most certainly are. If possible, could you please explain the rules for us?"
                    show b m_norm
                    s "Of course! It's really simple. After deciding on a shape that you wish to work with, you use the needle to try releasing the shape from the candy mold without breaking it."
                    s "The more detail there is in the shape, the more difficult it becomes and the larger the risk of you walking away with broken candy."
                    show b b_one_raised
                    b "Sounds simple enough. [MC], do you have a preference for what you would like?"
                    ##CHECK
                    menu: 
                        "A Square." (color = "yellow"):
                            $ square_s = True
                            MC "I think I’ll keep it simple for today. I’ll pick the square."
                            show b e_closed m_grin
                            b "A prudent choice."
                        "A Rabbit." (color = "green"):
                            $ rabbit_s = True
                            MC "The rabbit looks too cute to pass up. I’ll try my hand at that."
                            show b e_side b_one_raised 
                            b "It {i}is{/i} indeed an adorable rabbit, isn’t it? A lovely choice."
                        "A Tulip." (color = "blue"):
                            $ tulip_s = True
                            MC "What’s life without a little challenge? I want to try the tulip."
                            show b e_squint_dl b_one_raised m_grin
                            b "You are a far braver soul than I. Though, it {i}does{/i} look quite lovely."
                        "A Fish." (color = "yellow"):
                            $ fish_s = True
                            MC "There’s just something about the fish that’s calling to me. I’ll choose that."
                            show b e_squint_dl b_one_raised
                            b "Perhaps you're longing for the familiarity of that lovely beach of yours."
                        "A Lantern." (color = "green"):
                            $ lant_s = True
                            MC "With all the lanterns decorating the festival, I feel like it would be rude to not at least {i}try{/i} the lantern shape."
                            show b b_soft e_closed m_grin
                            b "Keeping within the theme of the festival, quite prudent."
                        "A Star." (color = "blue"):
                            $ star_s = True
                            MC "I know it's a risk, but I think I'd like to do the star."
                            show b b_one_raised e_wide 
                            b "What a coincidence, I was thinking the same. However, I rather think that the straight lines will give me the {i}edge{/i} I’ll need to succeed in this task."
                            show b b_norm e_norm 
                            "He turned back to the stall owner."
                            b "Do you by any chance have two stars?"
                            
                    
                    if star_s:
                        "You thought Baxter’s logic was sound - straight lines should mean for an easier time to carve the shape out of the mold."
                        "{i}Right?{/i}"
                    else:
                        show b b_norm e_closed m_grin
                        b "I rather feel like I will try my hand at the star. Hopefully the straight lines will give me the chance I need to not fail this task."
                    hide b
                    with dissolve
                    s "Certainly! Here you go. Take a seat at one of the empty tables, and good luck."
                    "Retrieving your chosen candy mold from the stall owner, both yourself and Baxter made your way to a free table."
                    "Taking a seat, you turned the candy mold in your hands - though it was light, it was {b}hard.{/b} You wondered how the needle was going to be able to pierce the candy."
                    show b e_squint_dl b_norm m_norm
                    with dissolve
                    b "It would seem that you are to carve into the shape in small increments."
                    show b b_annoyed
                    b "Too much pressure and you risk creating a crack in the whole mold and destroying the integrity of the candy."
                    show b e_surprised m_confused b_raised1
                    "Before you could get started on your mission, an echo of awe resounded from a table a few spaces away from you."
                    "Subtly, you craned your neck to the side to see what the commotion was about, Baxter following your lead."
                    show b b_raised
                    "A few tables away, someone held aloft their final product: the face of an anime character carved perfectly out of the mold."
                    "You looked back to Baxter, whose face you were sure reflected your own awed expression."
                    show b m_grin e_squint
                    "Hazel eyes finding your own, he quickly recovered with a sly smile curling his lips."
                    b "It’s not too late to change your mind, [MC] - why not see if the owner has another one of those character molds?"
                    if mc_persona == 1:
                        show b e_squint_dl b_annoyed
                        MC "Why, Baxter, I’m wounded. It’s as if you {i}want me{/i} to fail."
                        show b e_squint b_annoyed
                        b "Not at all. I am simply advising you of an alternate option."
                        show b e_closed b_raised
                        MC "Not in this lifetime."
                        b "That is fair. "
                    elif mc_persona == 2:
                        MC "I don’t think so."
                        show b e_squint_dl b_annoyed
                        b "No? Ah, what a shame. We shall have to be content with our simple shapes."
                        show b e_closed b_raised
                        MC "I mean, you are {i}more{/i} than welcome to try, Baxter."
                        b "Perish the thought."
                    elif mc_persona == 3: 
                        show b e_squint b_annoyed
                        "You raised a brow at Baxter, wordlessly getting your point across to him of how much you would {i}not{/i} be doing that."
                        show b e_closed b_raised
                        b "Understandable."

                    hide b with dissolve
                    "Focusing back on your candy mold, you considered how you would go about carving the shape out."
                    if star_s:
                            jump starry_night

                    menu:
                        "You were precise with your movements." (color = "yellow"):
                            $kata_win = 1
                            "Avoiding putting too much pressure onto the candy with your needle, you slowly but surely carved your way into the shape."
                            "Before long, you heard a small crack. Lifting the mold, you saw the shape you had been diligently working away at fall out, all whilst still holding its shape."
                            "{i}You had succeeded!{/i}"
                            
                        # "You were uncertain, but you did your best."(color = "green"): 
                        #     "Making your way around the shape of your mold, you tried your best to keep a consistent pressure on the candy to carve it out of its mold."
                        #     "It was unfortunate, but soon you heard an audible crack and saw your precious candy snap in half."
                        #     "You had done your best, but alas, the candy won this round."
                        
                        "You were just here for fun."(color = "blue"):
                            $kata_win = 2
                            "Working your way around the mold, you didn’t take much care in the pressure that you were applying to the candy."
                            "In that way, perhaps what followed was inevitable." #Pacing
                            "Soon enough, you could hear the audible crack as the candy broke under your needle, leaving you with two pieces snapped right down the middle."
                            "The candy had bested you - your weak attempt at removing it from its form having failed."
                    
                    if kata_win == 1:
                        "Turning to Baxter, you wanted to show off your success and see how he was doing."
                    elif kata_win == 2:
                        "Turning to Baxter, you hoped he was faring better than you were."
                    
                    show b e_side_down b_angry m_pout
                    with dissolve
                    "With him being so deep in thought, you couldn’t help but adore the furrow of his brows as he concentrated on his task."
                    "He would regularly test the structure of the mold with the needle, pressing into the crevice and listening for creaks in the mold that might warn that the candy could crack under his pressure."
                    show b e_squint_dl b_annoyed m_norm
                    "Feeling your eyes on him, he paused, eyes flicking towards you as he gave you a small smile."
                    show b e_norm b_norm
                    b "Have you already finished your herculean task, my dear?"
                    
                    if kata_win == 1:
                        if mc_persona == 1:
                            show b e_wide b_one_raised m_confused
                            MC "Yep! I wanted to show you, but then I was distracted by your pretty face."
                            show b e_closed b_norm m_grin
                            "Baxter snorted at your comment, visibly relaxing at the lightness of the conversation."
                            show b e_squint_dl b_angry m_grin
                            b "I’m glad to see that you have succeeded so wonderfully. Let us hope I can be so lucky."
                            "He turned back to his task, determination burning in his eyes."
                        elif mc_persona == 2:
                            MC "Yeah. No issues on my end. How is yours going?"
                            show b e_closed b_norm m_grin
                            "Baxter visibly relaxed, but let out a sigh."
                            show b e_squint_dl b_angry m_grin
                            b "This is turning out to be as difficult as I imagined it to be. Still, I am confident that I will at least get {i}somewhere{/i} with this."
                            MC "Good luck!"
                            show b e_closed b_sad m_grin
                            b "I am {i}certain{/i} I will need it."
                            show b e_side_down b_annoyed m_norm
                            "Giving you a soft smile, he turned back to his task, a sparkle twinkling in his eyes. "
                        elif mc_persona == 3: 
                            show b e_norm b_soft m_norm
                            "Nodding, you gave him a soft smile."
                            MC "Yeah, I think I got lucky."
                            show b e_squint
                            "Baxter returned your smile, eyes crinkling with delight."
                            b "I am glad to hear it. Let us see if I am just as lucky, hmm?"
                            show b e_squint_dl b_angry m_grin
                            "He turned back to his task, determination burning in his eyes."
                    
                    elif kata_win == 2:
                        if mc_persona == 1:
                            show b e_squint
                            "You pouted at Baxter despondently."
                            show b b_one_raised 
                            MC "Yeah, but I didn’t luck out. Look, I only got half a... {i}shape?{/i}"
                            show b e_squint_dl
                            "Baxter looked over at your poor candy sitting sadly broken on the table."
                            b "Oh my, it certainly {i}has{/i} seen better days, hasn’t it?"
                            show b b_raised e_closed m_grin
                            b "Perhaps I shall fare better? Let us find out."
                            "He turned back to his task, determination burning in his eyes."
                        elif mc_persona == 2:
                            show b b_one_raised
                            "You frowned, gesturing at your tragically bisected work."
                            MC "I tried, but it still cracked."
                            show b b_sad e_side_down
                            "Baxter smiled sympathetically as he gazed upon your broken candy."
                            show b b_raised e_norm m_grin
                            b "Perhaps it was the {i}candy{/i} that cracked under the pressure then, mm? The evidence is right there."
                            show b b_norm e_closed m_norm
                            b "Let us see if my candy will survive the same treatment."
                            show b b_soft e_norm
                            "Giving you a soft smile, he turned back to his task, a sparkle twinkling in his eyes."
                        elif mc_persona == 3: 
                            "You gestured with your hand at the broken candy, not uttering a word over the poor attempt."
                            show b b_one_raised e_norm m_norm
                            "Baxter smiled at you softly,"
                            show b b_norm e_closed
                            b "Ah, sometimes we get bested by sleep. Other times, we get bested by some melted sugar. I’m certain you tried your best."
                            show b b_soft e_norm
                            "His ever-optimistic attitude when it came to you brightened your spirits."
                            show b b_raised e_closed m_grin
                            "He then turned back to his task, determination burning in his eyes."
                            
                    show b m_pout b_angry e_squint_dl
                    "Since you'd finished your own attempt, you decided to turn your attention wholly onto Baxter."
                    show b b_annoyed m_confused e_closed
                    "You watched as he returned to pressing the needle into the crevice of the mold, edging his way around the shape of the star."
                    show b e_side_down
                    "It didn’t take too long after he'd approached the halfway point for..."
                    show b b_raised e_surprised m_confused
                    "{size=+15}{i}Crack.{/i}{/size}"
                    hide b
                    show bax_at_kata 
                    with dissolve
                    "The star that Baxter was working on had cracked directly down the middle."
                    "He held the broken half of the star with a dejected sigh."
                    b "Alas, it looks like I have suffered yet another defeat at a confectionary item."
                    hide bax_at_kata 
                    show b e_closed b_sad m_norm
                    with dissolve
                    MC "I'm pretty sure you won that first fight with the chocolate fountain."
                    show b e_side 
                    b "Just barely. I fear that battle has left its scar on me."
                    show b e_closed m_grin b_norm
                    "You could barely contain your giggle at his dramatic shudder, knowing that he was just exaggerating."
                    jump katanuki_leave

                    label starry_night:
                        "Starting from the top most point, you pressed the needle into the mold, slowly carving into the shape - stroke after determined stroke."
                        show b e_side_down b_angry m_pout
                        with dissolve
                        "After a few minutes of focus, you turned to Baxter to see how he was doing."
                        
                        "You couldn’t help but adore the furrow of his brows as he concentrated on his task."
                        "He would regularly test the structure of the mold with the needle, pressing into the crevice and listening to a creak in the mold that would possibly signal that the candy could crack under his pressure."
                        show b e_squint_dl b_annoyed m_norm
                        "Feeling your eyes on him, he paused, eyes flicking towards you as he gave you a small smile."
                        show b e_norm b_norm
                        b "Have you already finished your herculean task, my dear?"
                        if mc_persona == 1:
                            show b e_wide b_one_raised m_confused
                            MC "No, I was simply distracted by your pretty face."
                            show b e_closed b_norm m_grin
                            "He snorted at your comment, visibly relaxing at the lightness of the conversation."
                            show b e_squint_dl b_angry m_grin
                            b "Well, don’t let it distract you for long - you still have your own candy to carve out."
                            "Giggling, you nodded and turned back to your task."
                        elif mc_persona == 2:
                            MC "No, I was just curious how you were doing. You seemed really deep in thought."
                            show b e_closed b_norm 
                            "He visibly relaxed, letting out a sigh."
                            show b m_grin e_squint_dl
                            b "{i}Deep{/i} would be correct; {i}thought,{/i} however, may not be the correct word to use. "
                            b "This is turning out to be as hard as I imagined it to be. Still, we forge on forward, don’t we?"
                            "Nodding, you turned back to your task. "
                        elif mc_persona == 3: 
                            show b e_norm b_soft m_norm
                            MC "Oh, no. I should’ve... but I.. ah..."
                            "Being caught out staring at him had flustered you, unable to string a sentence together without stumbling."
                            show b e_squint
                            "He regarded you warmly, a soft smile playing at the corner of his lips."
                            b "It’s quite alright. I’m certain that we can both get through this together, yes?"
                            "Nodding sheepishly, you turned back to your task."
                        hide b
                        with dissolve
                        "You looked down at the poor candy in front of you, clearly waging a war against you and the needle."
                        "Picking it up with a renewed vigor, you started to press the needle back into the mold. For a while, you felt like you were doing well, even approaching the halfway point before..."
                        "{size=+15}{i}Crack.{/i}{/size}"
                        "You gazed at the poor broken star staring pitifully back up at you."
                        show bax_at_kata with dissolve
                        "A moment later, you heard another audible crack accompanied with a dejected sigh."
                        "Looking to your side, you saw Baxter holding two pieces of his own star and smiling in defeat."
                        hide bax_at_kata with dissolve
                        show b e_squint_dl b_angry m_norm
                        "Eyes flicking from his dismal attempt to yours, he chuckledy wryly,"
                        show b e_squint b_raised1 m_grin
                        b "Ah, looks like we both suffered the same fate."
                        "You were about to comment something similar, but then he set his broken pieces down and you noticed that your stars broke in an almost identical way."
                        show b e_surprised b_raised m_confused
                        "Picking up your half, you scooched over in your seat to get closer to Baxter."
                        MC "Look, our halves match perfectly though."
                        show b e_wide b_raised m_norm
                        "Placing your half next to one of his pieces, you flashed him a smile."
                        MC "Just like us."
                        show b b_sad e_side_down
                        "Baxter couldn’t take his eyes away from the two perfectly broken pieces of candy star pressed together."
                        show b e_closed blush
                        "Tracing a finger over the joined candies, a small blush formed on his cheeks as he turned to you."
                        show b e_norm b_soft 
                        b "{i}Just like us.{/i} You never fail to surprise me, [MC]."
                        "His voice softened as he looked down at the star."
                        show b e_closed m_grin -blush
                        b "It {i}is{/i} a shame that we cannot bring this back home with us. Nevertheless, I am certain there will be many tokens that we will be able to steal away to remind us of our time here."

                    label katanuki_leave:
                        show b e_norm m_grin b_soft
                        "Smiling, you took in his profile as he admired your attempt to brighten his mood."
                        show b e_side_down m_norm
                        "You could remember a time where moments like this would break Baxter’s spirit, with him believing that any sort of failure - no matter how large or minute - spelled disaster for him."
                        "This time, he took it in stride. Rather than wallowing in his mistakes, he delighted in seeing the outcome in a different light - one that allowed him to accept that not everything bad was a failure."
                        show b e_norm
                        if star_s:
                            "Leaving the broken pieces where they were, Baxter turned in his seat to fully face you."
                        else:
                            "Placing the broken pieces back down, Baxter turned in his seat to fully face you."
                        show b e_norm b_one_raised m_grin
                        b "Now then, shall we be off? Please lead the way, [MC]."
                        "Together, you and Baxter left the booth."
                        show b e_norm b_norm m_norm 
                        jump g_checkpoint

        label separation_early:
            $ sep_early = True
            stop music fadeout 1.0
            scene matsuri_food
            show b b_sad e_norm m_confused
            with dissolve
            b "[MC], are you feeling alright? You look a bit pale."
            show b e_side m_norm
            b "Let's not push ourselves too hard now. Shall we find a place to rest?"
            "He was right to ask; you weren't feeling too well at all, and were in no position to argue as Baxter led you away."
            scene matsuri_food:
                blur 25
            with dissolve
            "Though, the crowds seemed to be against you, as you soon became surrounded by other people."
            "It felt awfully claustrophic trying to pull free from the masses."
            "You thought you heard Baxter call your name, but as you craned your head to look at him..."
            "{i}He was nowhere to be found.{/i}"
            "Countless unknown faces filled your view, and not a single one was familiar."
            "You and Baxter had gotten separated!"
            "Whatever had you feeling down was suddenly blown away from Baxter's sudden disapperance."
            "At the very least you needed to find him first."
            jump meetings

        label separation_last:
            stop music fadeout 1.0
            scene matsuri_food
            show b e_side_down m_norm b_norm
            with dissolve
            "Baxter had taken his phone from out of his sleeve, glancing at the time before putting it away again."
            show b b_one_raised e_norm
            b "I believe we still have a bit of time before the fireworks. Shall we find a place to rest?"
            "You thought it was a good idea, so the two of you began moving again."
            scene matsuri_food:
                blur 25
            with dissolve
            "Though, it seemed everyone else had the same idea, as the crowd began to thicken with people."
            "It felt awfully claustrophic trying to pull free from the crowd."
            "You thought you heard Baxter call your name, but as you craned your head to look at him..."
            "{i}He was nowhere to be found.{/i}"
            "Countless unknown faces filled your view, and not a single one was familiar."
            "You and Baxter had gotten separated!"
    
    label meetings:
        play music child_dreams fadeout 1.0 fadein 1.0
        scene matsuri_food
        with dissolve
        menu: 
            "Your anxiety spiked." (color = "blue"):
                "Being a stranger in a new place, and being separated from your boyfriend was terrifying."
                if mc_height == 1:
                    "Looking over the tops of the heads around you, you searched for Baxter amongst the crowd."
                if mc_height == 2:
                    "You could barely see over the people around you as you searched for Baxter amongst the crowd."
                if mc_height == 3:
                    "Trying your best, you raised yourself up onto your toes to try and see past the crowd around you to look for Baxter."
                "Unable to find him, and the crowd further pushing you further away, you decided that it was best to get out of the clamour."
                "Following the flow of the crowd, you eventually found an open area that was raised from the crowd."
                "You made your way through the throng of people, climbing onto the open area to search for your missing boyfriend."
                show b e_wide b_angry m_confused sweat
                with dissolve
                "A few moments later, you could see Baxter making his way through the crowd with haste."
                show b b_raised1 m_confused e_surprised 
                "Your body flooded with relief when you noticed him, and when he caught sight of you, the smile on his face further assisted in reducing your anxiety."
                show b b_sad m_norm e_wide
                "Though he wore a smile, you could see the concern that marred his features - the furrow of his brow and the worry in his eyes."
                show b b_angry e_closed m_sad
                b "[MC] I’m so sorry. The crowd took me nearly halfway through the festival, I swear."
                show b e_squint_dl m_confused
                "Baxter’s chest rose and fell quickly, and you could see the shine of sweat beading on his neck."
                "It seemed that he was worried for you and wanted to get back as soon as he could."
                "That brought a smile to your face."
                show b e_wide b_raised -sweat
                MC "That’s okay. I’m glad you were able to find me."
                show b b_soft e_norm 
                "His expression softened as his confidence slowly returned."
                show b b_sad e_norm m_norm
                b "Always, my dear. You’ll find that I will always come searching for you."
                menu: 
                    "You threw your arms around him."(color = "yellow"): 
                        show b b_sad e_closed blush
                        "You heard a soft ‘ooft’ as you squeezed, catching him off guard. A moment later you could feel as he wrapped his arms around, squeezing you back in equal measure."
                    "You took his hand."(color = "green"): 
                        show b b_raised e_surprised blush
                        "Threading your fingers with Baxters, you could feel his warm hand squeeze yours gratefully."
                        show b b_sad e_closed blush
                        "All the worry having evaporated from his body."
                jump and_remeetings
            "You weren’t too stressed." (color = "green"):
                "It wouldn’t be too far-fetched to say that this was almost anticipated."
                if mc_height == 1:
                    "Looking over the tops of the heads around you, you searched for Baxter amongst the crowd."
                if mc_height == 2:
                    "You could barely see over the people around you as you searched for Baxter amongst the crowd."
                if mc_height == 3:
                    "Trying your best, you raised yourself up onto your toes to try and see past the crowd around you to look for Baxter."
                "Unable to find him, and the crowd further pushing you further away, you decided that it was best to get out of the clamour."
                "Following the flow of the crowd, you eventually found an open area that was raised from the crowd."
                "You made your way through the throng of people, climbing onto the open area to search for your missing boyfriend."
                show b e_norm b_norm m_norm
                with dissolve
                "A few moments later, you could see Baxter making his way through the crowd, weaving between people with ease."
                show b e_surprised b_raised m_grin
                "You waited to see if he would catch sight of you, and it wasn’t long before your eyes met across the crowd and Baxter gave you a dazzling smile."
                show b e_closed sweat
                "Baxter approached you, shoulders relaxed and a content smile on his face, but you could see that his breathing was faster than usual."
                show b e_squint
                b "I thought you’d be alright [MC]. I swear, the crowd took me nearly halfway through the festival."
                show b e_squint_dl
                "Though he trusted that you would be okay, he was still worried for you. "
                "That brought a smile to your face."
                show b e_wide m_confused b_raised
                MC "That’s okay. I’m glad you were able to find me."
                "Baxter eyes widened as if in shock, before he relaxed and shot you a winning smile."
                show b e_norm b_raised m_grin -sweat
                b "Always, my dear. You’ll find that I will always come searching for you."
                menu: 
                    "You threw your arms around him."(color = "yellow"): 
                        show b b_sad e_closed blush
                        "You heard a soft ‘ooft’ as you squeezed, catching him off guard. A moment later you could feel as he wrapped his arms around, squeezing you back in equal measure."
                    "You took his hand."(color = "green"): 
                        show b b_raised e_surprised blush
                        "Threading your fingers with Baxters, you could feel his warm hand squeeze yours gratefully."
                        show b b_sad e_closed blush
                        "All the worry having evaporated from his body."

    label and_remeetings:
        play music child_dreams fadeout 1.0 fadein 1.0 if_changed
        show b b_sad e_side_down m_norm -blush
        "Though reluctantly, Baxter released his grip on you as he reached into the sleeve of his coat and produced a plastic water bottle."
        show b b_norm
        "{i}Where does he keep storing this stuff?{/i}"
        
        if sep_early: 
            show b b_sad e_side_down
            b "I was concerned you may still be feeling unwell. I managed to grab a free one from one of the stalls on the way here..."
            show b e_norm
        else:
            show b e_squint b_raised 
            b "I thought you might have been thirsty. I managed to grab a free one from one of the stalls on the way here..."
        "There was a barely hidden look of pride as he offered the bottle to you."
        show b b_raised m_grin
        "With a chuckle you accepted the bottle from him, having found yourself parched, now that you had thought about it."
        if sep_early: 
            show b b_sad m_norm
            MC "I'm feeling better, now that you mention it."
            b "A most fortuitous recovery, I'm glad."
        show b m_norm
        "As you drank your fill, you couldn’t believe that even in the midst of the chaos you both had found yourself in, he thought of you."
        show b b_one_raised
        MC "Honestly, where are you keeping all that stuff?"
        show b e_squint b_annoyed m_grin
        "Baxter stood a little straighter as he gave you a wolfish grin."
        b "A good planner never reveals his secrets."
        show b e_wide b_raised m_norm
        "Before he could continue, an announcement rang through the festival, first in Japanese and then in English."
        "Baxter looked to you with an eyebrow quirked in question."
        show b b_one_raised e_norm 
        b "Would you like to go see the fireworks?"
        menu: 
            "You didn’t feel up to seeing the fireworks today." (color = "yellow"):
                show b b_soft 
                "Giving Baxter a soft smile, you shook your head gently."
                MC "I’m sure it would be lovely to see, but I don’t think I’m up for it today"
                show b e_closed m_grin
                "Without missing a beat, Baxter returned your smile. Your decline doing nothing to dampen his mood. Offering an arm to you, he aims his charm at you once again."
                b "That is perfectly fine. Why don’t we take a walk to somewhere a bit more quiet, hmm?"
                show b e_norm m_norm
                "Without hesitation, you took the proffered arm, leaning into him as you both made your way away from where the fireworks were set to display."
                if mc_height == 1:
                    "You propped your head onto his gently, eliciting a giggle from him before he nuzzled back."
                    "Leaning against each other, you both made your way forward towards your new destination."
                if mc_height == 2:
                    "You propped your head onto his shoulder as you walked."
                    "Baxter hummed at the added contact, allowing you to feel his happiness vibrating through his body as you held on."
                if mc_height == 3:
                    "You propped your head onto his arm, hugging him closer whilst doing so."
                    "Baxter hummed at the added contact, allowing you to feel his happiness vibrating through his body as you held on."
                jump bamboo_nights
            "It sounded like a wonderful way to end the evening." (color = "green"):
                MC "How could I say no?"
                if b_initiative == 1:
                    "With a brilliant smile, Baxter reached out to grasp your hand again, entwining your fingers together."
                    b "This way, I won’t lose you again."
                    MC "Lead the way."
                if b_initiative == 2:
                    "You felt his hand bump into yours, a silent request to hold hands once again as Baxter gave you a questioning look."
                    menu: 
                        "You took his hand." (color = "yellow"):
                            "Baxter smiled brilliantly at you as he entwined his fingers with yours."
                            b "This way, I won’t lose you again."
                        "You shook your head" (color = "green"):
                            "Grinning at you, Baxter pockets his hand back into his yukata, not flustered one bit."
                            b "Very well, but I {i}will{/i} be keeping a closer eye on you."
                            b "Can’t go losing you again in this crowd."
                if b_initiative == 3:
                    b "[MC], would you like to hold hands? So that we won’t get separated anymore?"
                    menu: 
                        "You took his hand." (color = "yellow"):
                            "Baxter smiled brilliantly at you as he entwined his fingers with yours."
                            b "This way, I won’t lose you again."
                        "You shook your head" (color = "green"):
                            "Grinning at you, Baxter pockets his hand back into his yukata, not flustered one bit."
                            b "Very well, but I {i}will{/i} be keeping a closer eye on you."
                            b "Can’t go losing you again in this crowd."
                "Side by side, you both made your way with the crowd to where the fireworks presentation was going to be held."
                jump under_wisteria

    
    #MC Chose not to go see Fireworks
    label bamboo_nights:
        play music one_love fadeout 1.0 fadein 1.0
        scene bamboo 
        with dissolve
        "As you left the bustling crowd behind, walking further away from the festival, the air around you became more quiet and peaceful."
        "The colors changed from warm festival lights to the calm shades of the bamboo garden the two of you had found yourselves in."
        "Embracing this moment, you basked in the fact that you got to have Baxter all to yourself."
        show b b_soft e_side m_norm
        with dissolve
        "You had enjoyed the festivities whilst you were here, more so because you got to experience them with Baxter."
        "Now that the night was coming to an end, there was a certain bittersweetness to it all coming to a close."
        "Not that Baxter would let it end on any note but sweet."
        show b b_sad e_closed
        b "I am grateful that we have been able to enjoy this trip together."
        show b b_raised m_grin
        b "It is not often that I get to enjoy some time away from work, away from the responsibilities of adult life."
        show b b_soft e_norm m_norm
        b "But being able to do so, and by your side, has made it all worthwhile."
        show b b_raised1 e_surprised m_confused
        "Pulling you to a stop, he turned to face you directly. As he was about to say something, the sound of fireworks in the distance caught his attention."
        show b e_wide 
        "Somehow, along your walk, you had memerged from the bamboo garden to find yourself in an almost perfect location to watch the night sky erupt in a myriad of colours."
        "All the while being able to avoid the worst of the noise. It was quite the happy coincidence."
        hide b with dissolve

        scene light_night
        show set_boom as set_boomturn
        show gazing_at_you
        show light_night as light_nightfor
        show set_boom
        show gazing_into_the_night
        with dissolve
        "As if entranced, Baxter turned to observe the fireworks - the bright lights reflecting in his eyes as he watched the colours flicker in and out of existence."
        b "How lovely."
        "His voice was hushed, but you were close enough to hear him regardless."
        hide light_nightfor
        hide set_boom
        hide gazing_into_the_night
        with dissolve
        "Stepping closer to him, you caught his attention, diverting his gaze from the lights back to you."
        "Baxter’s gaze settled on you, the light of the fireworks having seemingly been caught in his eyes as he took you in."
        show handout
        show fireworks_glow at firework_tint
        with dissolve
        b "[MC], darling."
        "His hand extended towards you, ghosting just above your cheek as he spoke."
        b "If theres only one thing, {i}merely{/i} one thing, that I want you know: is that I wouldn't choose to be anywhere else."
        b "No matter where we are, so long as I am with you, I know I will be the happiest man alive."
        b "{i}This{/i} is where I want to be every summer from now on:"
        b "By your side."
        "His hand dropped slightly, changing from a gentle caress to a quiet and solemn question."
        "As the world around you fell silent, your eyes flickered between Baxter and his proffered hand."
        "Will you take his hand and continue experiencing all that you can with him, hand in hand?"
        "The question wasn't anything that you thought needed mulling over, and with an assured smile you slipped your hand into his."
        "You were about to make your way into the future with the knowledge that Baxter would spend every possible moment of it with you."
        "Always."
        return

    #MC Wanted to go see the fireworks
    label under_wisteria:
        play music one_love fadeout 1.0 fadein 1.0
        scene wisteria
        with dissolve
        "The walk was a pleasant one, the colours changing as you moved from the warm lights of the festival, to the cool hue of the wisteria blossoms."
        "You noted that there was an absence of people going towards the wisteria trees - perhaps there could be a nice place to view the fireworks there."
        show b b_soft e_closed m_norm
        with dissolve
        MC "Hey Baxter, why don’t we see if we can find a clearing in the wisteria?"
        show b e_wide b_raised
        "Baxter turned towards the sea of purple flowers, his eyes widening in excitement."
        show b e_norm b_soft
        b "That sounds like a splendid idea."
        hide b
        with dissolve
        "Separating yourselves from the sea of people, you both sneaked away into the seemingly magical forest."
        "The further you made your way through the forest, the quieter it became - the noise of the festival all but becoming a distant memory."
        "As luck would have it, you soon found a clearing that gave you a clear view of the sky."
        "After the hustle and bustle of the day, it was nice to find a spot that was clear of other people."
        show b e_side_down b_norm m_norm
        with dissolve
        "The quiet, intimate location allowed you to bask in Baxter’s presence, relishing the fact that you got to have him all to yourself."
        show b e_squint b_one_raised
        "Baxter seemed to be of the same mind as he turned to you, his hazel eyes regarding you a warmth that you could feel down to your core."
        show b e_side_down b_sad
        "His mouth popped open and closed several times, as if trying to find the words he wished to convey, but failing in doing so."
        show b b_raised e_wide m_confused
        "Before he got the chance to speak his mind, the first of the fireworks erupted in the air, showering the dark sky in brilliant colours."
        scene light_night
        show set_boom as set_boomturn
        show gazing_at_you
        show light_night as light_nightfor
        show set_boom
        show gazing_into_the_night
        with dissolve
        "As if entranced, Baxter turned to observe the fireworks - the bright lights reflecting in his eyes as he watched the colours flicker in and out of existence."
        "You were brought back to a similar day like today - a spontaneous trip to watch the sky be painted with bright colours in the embrace of the man that you stand beside today."
        "It truly only felt like it happened a few weeks ago, rather than several years now."
        "Baxter having more than kept his promise of making up for the lost years where he kept you at arm's length."
        b "Thank you, [MC]."
        "You could almost miss what he said, his voice hushed against the sound of the fireworks lighting up the sky. But when it came to Baxter, you always made sure to pay attention."
        hide light_nightfor
        hide set_boom
        hide gazing_into_the_night
        with dissolve
        "Turning away from the dizzying display, Baxter’s gaze settled on you, the light of the fireworks having seemingly been caught in his eyes as he took you in."
        MC "What for?"
        "His eyes crinkled ever so slightly, as if out of shyness of the situation he had found himself in."
        b "For coming with me to experience this festival. For being your ever charming and darling self."
        "A rosy hue spread across his cheeks, dark enough that you could see it even in the dim light."
        b "For choosing me. I... Well, there is no need to rehash everything that happened."
        b "I wanted to let you know how grateful I am that you decided to take my hand in this life and learn the steps of this unknown dance together."
        b "Everything seems less daunting when you have someone to share these experiences with."
        b "Even more so when it is with someone you adore and love."
        "The only way you knew that the fireworks were still happening was from how it illuminated Baxter profile. They could have all but fizzled into nothing as far as you were concerned."
        "All your focus was on the man in front of you."
        "How was it that all these years later, he has kept finding new ways to surprise you."
        show handout
        show fireworks_glow at firework_tint
        with dissolve
        "You almost missed as he reached out to cup your face, so softly that the gentle caress of his fingertips felt like they could burn."
        "As he leaned in closer, you could feel his warm breath scatter across your cheeks."
        "With how close Baxter was, you could smell his floral cologne as it enveloped you."
        "It wouldn’t take much at all, to lean in and kiss him."
        "Which is precisely what you did."
        if mc_height ==1:
            "Baxter tilted his head upwards, warm brown eyes gazing at you from beneath his lashes as your lips met."
            "He readily reciprocated the kiss as you wrapped your arms around him."
            "Sliding his hand upwards, he cupped your face, reluctant to let go."
        if mc_height ==2:
            "Closing the distance, you pressed your lips into his, relishing in how Baxter readily reciprocated."
            "Lips falling against each other, you wrapped your arms around him as he cupped your face, reluctant to let go."
        if mc_height ==3: 
            "You stood on the tips of your toes as Baxter tilted his head downwards, eagerly meeting your lips."
            "His hand slid upwards to cup your cheek as you wrapped your arms around him, both reluctant to let go."
        "Only once you both needed to come up for air did the kiss end, with you both trying to catch a breath."
        "He once again regarded you with an emotion that could only be described as 'love'."
        b "If theres only one thing, {i}merely{/i} one thing, that I want you know; is that I wouldn't choose to be anywhere else."
        b "No matter where we are, so long as I am with you, I know I will be the happiest man alive."
        b "{i}This{/i} is where I want to be every summer from now on:"
        b "By your side."
        "This moment couldn’t compare to all the memories you have collected over the years."
        "As the fireworks continued to scatter across the sky, your focus didn’t shift from Baxter."
        "You made a promise to yourself all those years ago to hold onto your memories, the feelings that came with them for as long as you possibly could."
        "Deep within your heart, you knew that this was a day that would stick with you for many years to come."
        "A memory to call back on when you reminisced on all the excitement you have had with Baxter."
        "As you gazed into his warm hazelnut eyes, you knew that this was just another step in the dance that you had recommended, and will continue many years into the future."
        "Forever and Always."
        

    return
