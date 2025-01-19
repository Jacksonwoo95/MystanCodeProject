"""
File:
Name:吳禹
----------------------
TODO:
"""

from campy.graphics.gobjects import GOval, GRect, GLine, GArc, GPolygon, GLabel
from campy.gui.events.timer import pause
from campy.graphics.gwindow import GWindow
import random

window = GWindow(400, 500, title="happy birthday,Daddy")

SIZE = 60  # sun size
VX = 4
DELAY = 18
GRAVITY = 1

CLOUD_SIZE = 25
cloud_x = 0
cloud_y = 0


def main():
    """
    Title: Happy birthday,Daddy
    This art work is for my dad
    親愛的爸爸，生日快樂：
        首先很感謝爸爸在我成長路上，一直當我精神的支柱
        在感到困惑時、低谷時、沮喪時，你總是鼓勵我不要放棄、保持耐心
        漸入佳境時，你也會提醒我，不能驕傲保持謙虛、有能力就幫助別人、常行佈施
        （以前覺得是嘮叨 XD）

        因為工作關係無法時常回家，沒辦法常常聽爸爸嘮叨
        即便如此，無論是遇到順境還是逆境，還是時常想起你告訴我的這些智慧

        爸，謝謝你，祝你生日快樂，健康長壽，歡喜自在
    """
    blue_sky()
    ground()  # with random leaf
    daddy()  # my dad
    baby_me()  # me
    tree()
    happy_birthday()
    moving_sun()


def tree():
    # tree
    tree_top = GOval(window.width*0.3, window.width*0.3)
    tree_top.x = window.width*0.7
    tree_top.y = window.height*0.3
    tree_top.filled = True
    tree_top.fill_color = 'forestgreen'
    window.add(tree_top)

    tree_trunk = GRect(window.width*0.1, window.height*0.2)
    tree_trunk.x = tree_top.x+(tree_top.width-tree_trunk.width)/2
    tree_trunk.y = tree_top.y+tree_top.height
    tree_trunk.filled = True
    tree_trunk.fill_color = 'saddlebrown'
    window.add(tree_trunk)


def blue_sky():
    global cloud_x, cloud_y
    sky = GRect(window.width, window.height*0.65)
    sky.color = "light blue"
    sky.filled = True
    sky.fill_color = "skyblue"
    window.add(sky)

    # make 3 cloud
    for i in range(3):
        for j in range(7):
            cloud = white_cloud()
            if j == 0:
                cloud_x = cloud.x
                cloud_y = cloud.y
            else:
                cloud.x = random.randint(cloud_x, cloud_x+cloud.width)
                cloud.y = random.randint(cloud_y, cloud_y+cloud.height)
            window.add(cloud)


def white_cloud():
    global cloud_x, cloud_y
    color = "white"

    cloud = GOval(CLOUD_SIZE*1.2, CLOUD_SIZE)
    cloud.color = color
    cloud.filled = True
    cloud.fill_color = color
    cloud.x = random.randint(0, window.width-cloud.width*2-1)
    cloud.y = random.randint(0, window.height*0.2)
    # window.add(cloud)
    return cloud


def moving_sun():
    sun = GOval(SIZE, SIZE)
    start_x = -SIZE
    start_y = window.height*0.12
    sun.color = "yellow"
    sun.filled = True
    sun.fill_color = "yellow"
    window.add(sun)

    # sun move 3 times
    for i in range(3):
        vy = -2
        sun.x = start_x
        sun.y = start_y
        while sun.x < window.width:
            sun.move(VX, vy)
            vy += 0.035
            pause(DELAY)
    window.add(sun, x=window.width*0.1, y=window.height*0.06)


def ground():
    green_ground = GRect(window.width, window.height*0.35)
    green_ground.y = window.height*0.65
    green_ground.color = "light green"
    green_ground.filled = True
    green_ground.fill_color = "light green"
    window.add(green_ground)

    # leaf
    for i in range(20):
        leaf = leaf_on_the_ground()
        leaf.x = random.randint(0, window.width - 1)
        leaf.y = random.randint(green_ground.y, window.height-1)
        window.add(leaf)


def leaf_on_the_ground():
    leaf = GOval(10, 4)
    leaf.filled = True
    leaf.fill_color = "yellowgreen"
    return leaf


def daddy():
    # daddy's head
    head = GOval(72, 96, x=0, y=0)
    head.x = window.width/2-head.width
    head.y = window.height/5
    head.filled = True
    head.fill_color = "tan"
    window.add(head)

    # daddy's mouth
    mouth = GArc(30, 10, 0, -180)
    mouth.x = head.x+(head.width-mouth.width)//2
    mouth.y = head.y+(head.height-mouth.height)//1.3
    window.add(mouth)

    # daddy's eyes
    l_eye = GArc(10, 5, 0, 180)
    l_eye.x = head.x+head.width/2-l_eye.width*1.5
    l_eye.y = head.y+head.height/3.5
    window.add(l_eye)

    r_eye = GArc(l_eye.width, l_eye.height, 0, 180)
    r_eye.x = l_eye.x + l_eye.width*2
    r_eye.y = l_eye.y
    window.add(r_eye)

    # daddy's hair
    hair = GPolygon()
    hair.add_vertex((head.x+head.width*0.05, head.y+head.height/5))  # left
    hair.add_vertex((head.x+head.width*0.95, head.y+head.height/5))  # right
    hair.add_vertex((head.x+head.width*0.95, head.y+head.height*0.1))
    hair.add_vertex((head.x+head.width*3/4, head.y-5))
    hair.add_vertex((head.x+head.width/2, head.y-7))
    hair.add_vertex((head.x+head.width/4, head.y-5))
    hair.add_vertex((head.x+head.width*0.05, head.y+head.height*0.1))
    hair.filled = True
    hair.fill_color = "black"
    window.add(hair)

    # daddy's nose
    nose = GPolygon()
    nose.add_vertex((mouth.x+mouth.width/2, l_eye.y+l_eye.height*1.1))
    nose.add_vertex((mouth.x+mouth.width/4, mouth.y*0.9))
    nose.add_vertex((mouth.x + mouth.width / 2, mouth.y * 0.95))
    nose.add_vertex((mouth.x + mouth.width*3/4, mouth.y * 0.9))
    nose.filled = True
    nose.fill_color = "pink"
    window.add(nose)

    # daddy's shirt
    shirt = GPolygon()
    shirt.add_vertex((head.x-head.width*0.15, head.y+head.height))  # Left-top
    shirt.add_vertex((head.x+head.width*1.3, head.y+head.height))  # R-t
    shirt.add_vertex((head.x+head.width, head.y+head.height*2))  # R-bottom
    shirt.add_vertex((head.x, head.y+head.height*2))  # L-b
    shirt.filled = True
    shirt.fill_color = "yellow green"
    window.add(shirt)

    # daddy's jeans
    jeans = GPolygon()
    jeans.add_vertex((head.x, head.y+head.height*2))  # left-top
    jeans.add_vertex((head.x+head.width, head.y+head.height*2))  # r-t
    jeans.add_vertex((head.x + head.width*7/8, head.y + head.height * 4))  # r-b_r
    jeans.add_vertex((head.x + head.width*4/6, head.y + head.height * 4))  # r-b_l
    jeans.add_vertex((head.x + head.width/2, head.y + head.height * 2.5))  # middle-bottom
    jeans.add_vertex((head.x + head.width*2/6, head.y + head.height * 4))  # l-b_r
    jeans.add_vertex((head.x + head.width/8, head.y + head.height * 4))  # l-b_l
    jeans.filled = True
    jeans.fill_color = "cadetblue"
    window.add(jeans)

    # daddy's shoes
    shoes1 = GRect(SIZE*1.1, SIZE*0.5)  # L
    shoes1.filled = True
    shoes1.fill_color = "purple"
    window.add(shoes1, x=head.x + head.width*2/6-shoes1.width, y=head.y + head.height * 4)
    shoes2 = GRect(SIZE * 1.1, SIZE * 0.5)  # R
    shoes2.filled = True
    shoes2.fill_color = "purple"
    window.add(shoes2, x=head.x + head.width*4/6, y=head.y + head.height * 4)

    # daddy's left arm is in baby_me()
    arm1 = GArc(head.width/2, head.height*1.3, 90, 180)  # L
    arm1.x = head.x-head.width/2.5
    arm1.y = head.y+head.height
    # window.add(arm1)
    arm2 = GArc(head.width / 2, head.height * 1.3, 90, -180)  # R
    arm2.x = head.x+head.width*1.15
    arm2.y = head.y + head.height
    # window.add(arm2)


def baby_me():
    # my head
    head = GOval(48, 43)
    head.x = window.width / 2 + head.width/4
    head.y = window.height / 3.2
    head.filled = True
    head.fill_color = "pink"
    window.add(head)

    # my mouth
    mouth = GArc(head.width*0.2, head.height*0.1, 0, 180)
    mouth.x = head.x + (head.width - mouth.width) // 2
    mouth.y = head.y + (head.height - mouth.height) // 1.2
    window.add(mouth)

    # my eyes
    l_eye = GArc(head.width*0.25, head.height*0.1, 340, 160)
    l_eye.x = head.x + head.width / 2 - l_eye.width * 1.5
    l_eye.y = head.y + head.height / 2.2
    window.add(l_eye)

    r_eye = GArc(head.width*0.25, head.height*0.1, 20, 190)
    r_eye.x = l_eye.x + l_eye.width * 2
    r_eye.y = l_eye.y
    window.add(r_eye)

    # my hair
    hair = GPolygon()
    hair.add_vertex((head.x+head.width*0.05, head.y + head.height / 5))  # L-bottom
    hair.add_vertex((head.x + head.width*0.95, head.y + head.height / 5))  # R-bottom
    hair.add_vertex((head.x+head.width*0.95, head.y+head.height*0.1))
    hair.add_vertex((head.x + head.width * 3 / 4, head.y - 5))
    hair.add_vertex((head.x + head.width / 2, head.y - 7))
    hair.add_vertex((head.x + head.width / 4, head.y - 5))
    hair.add_vertex((head.x+head.width*0.05, head.y+head.height*0.1))
    hair.filled = True
    hair.fill_color = "black"
    window.add(hair)

    # my nose
    nose = GArc(6, 6, 80, 240)
    nose.x = head.x+head.width*0.4
    nose.y = head.y+head.height*0.55
    window.add(nose)

    # my shirt
    shirt = GPolygon()
    shirt.add_vertex((head.x+head.width*0.95, head.y+head.height))  # R-top
    shirt.add_vertex((head.x+head.width*0.05, head.y+head.height))  # L-top
    shirt.add_vertex((head.x-head.width*0.1, head.y+head.height*1.5))
    shirt.add_vertex((head.x-head.width*0.05, head.y+head.height*2))
    shirt.add_vertex((head.x+head.width, head.y+head.height*2))
    shirt.filled = True
    shirt.fill_color = "tomato"
    window.add(shirt)

    # my pant
    pant = GPolygon()
    pant.add_vertex((head.x + head.width, head.y + head.height * 2))  # L-t
    pant.add_vertex((head.x-head.width*0.05, head.y + head.height * 2))  # R-t
    pant.add_vertex((head.x - head.width * 0.05, head.y + head.height * 2.7))
    pant.add_vertex((head.x + head.width * 0.5, head.y + head.height * 2.7))
    pant.add_vertex((head.x + head.width * 0.5, head.y + head.height * 2.4))  # middle
    pant.add_vertex((head.x + head.width * 0.6, head.y + head.height * 2.7))
    pant.add_vertex((head.x + head.width, head.y + head.height * 2.7))
    pant.filled = True
    pant.fill_color = "darkslateblue"
    window.add(pant)

    # my hand
    hand = GArc(head.width*1.1, head.height*2.1, 0, -100)
    hand.x = head.x+head.width*0.
    hand.y = head.y+head.height*0.6
    window.add(hand)

    fist = GOval(8, 8)
    fist.x = hand.x+head.width*0.1
    fist.y = hand.y+hand.height*0.9
    fist.filled = True
    fist.fill_color = "pink"
    window.add(fist)

    # daddy's left arm
    arm_x0 = head.x - head.width*1.9
    arm_y0 = head.y + head.height
    arm_x1 = arm_x0+head.width
    arm_y1 = arm_y0+head.height*0.7
    arm1 = GLine(x0=arm_x0, y0=arm_y0, x1=arm_x1, y1=arm_y1)
    arm2 = GLine(x0=arm1.end.x, y0=arm1.end.y, x1=head.x*1.01, y1=head.y + head.height*1.9)
    window.add(arm1)
    window.add(arm2)

    dad_l_fist = GOval(15, 15)
    dad_l_fist.x = arm2.end.x-dad_l_fist.width*0.5
    dad_l_fist.y = arm2.end.y-dad_l_fist.height*0.5
    dad_l_fist.filled = True
    dad_l_fist.fill_color = "tan"
    window.add(dad_l_fist)

    #  my leg
    l_leg = GArc(head.width*0.2, head.height*0.6, 100, 190)
    l_leg.x = head.x+head.width*0.2
    l_leg.y = head.y+head.height*2.5
    window.add(l_leg)

    r_leg = GArc(head.width*0.2, head.height*0.6, 100, 190)
    r_leg.x = l_leg.x+head.width*0.6
    r_leg.y = l_leg.y
    window.add(r_leg)

    # my shoes
    l_shoes = GRect(12, 8)
    l_shoes.x = l_leg.x-l_shoes.width*0.5
    l_shoes.y = l_leg.y+l_leg.height
    l_shoes.filled = True
    l_shoes.fill_color = "darkred"
    window.add(l_shoes)

    r_shoes = GRect(l_shoes.width, l_shoes.height)
    r_shoes.x = r_leg.x-r_shoes.width*0.5
    r_shoes.y = l_shoes.y
    r_shoes.filled = True
    r_shoes.fill_color = "darkred"
    window.add(r_shoes)


def happy_birthday():
    hbd = GLabel("Happy Birthday Daddy")
    hbd.font = '-10'
    hbd.y = window.height-hbd.height*3
    hbd.x = window.width*0.02
    window.add(hbd)

    my_name = GLabel("by 扛轎少年團.吳禹")
    my_name.font = hbd.font
    my_name.y = hbd.y+my_name.height
    my_name.x = hbd.x
    window.add(my_name)


if __name__ == '__main__':
    main()
