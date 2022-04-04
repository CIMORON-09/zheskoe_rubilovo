import random

import wrap

wrap.world.create_world(1000,800)
wrap.add_sprite_dir("kiberpank_file")
wrap.world.set_back_image("fion/foi/fon.jpg")

kiberpank=wrap.sprite.add("kiberpank_id",500,500, "kiberpank")
dom=wrap.sprite.add("kiberpank_id",100,100, "dombabeegi")
patron = wrap.sprite.add("kiberpank_id",500,500, "patron")
wrap.sprite.hide(patron)
limon = []
@wrap.on_key_always(wrap.K_w)
def dvizhenie(keys,pos_x,pos_y):


    if wrap.K_w in keys:
        wrap.sprite.move_at_angle_dir(kiberpank,15)
    sdvin_Eart()


@wrap.on_mouse_move()
def fswefw (pos_y,pos_x):
    wrap.sprite.set_angle_to_point(kiberpank,pos_x,pos_y)




def sdvin_Eart():
    global kiberpank
    print("0000")
    x_kiberpanka_do_sdviga=wrap.sprite.get_x(kiberpank)
    y_kiberpanka_do_sdviga=wrap.sprite.get_y(kiberpank)

    wrap.sprite.move_to(kiberpank,500,500)
    wrap.sprite.move(dom,500-x_kiberpanka_do_sdviga,500-y_kiberpanka_do_sdviga)

@wrap.always(delay=100)
def delaem_polet(mouse_buttons):
    kol = 0
    if  wrap.BUTTON_LEFT  in mouse_buttons  :
        kol=1
        l=mouse_buttons[0]

        limon.append(l)


        lol=limon[0]
        pol=limon[-1]
        poi=random.randint(lol,pol)
        if poi==1 :
            wrap.sprite.move(patron,0,0-10)
#нужн0 что бы мир двигался во крук героя


@wrap.on_mouse_down(wrap.BUTTON_LEFT)
def delaem_strelbu():
    wrap.sprite.show(patron)

    ypatrona=wrap.sprite.get_y(patron)
    if ypatrona==500:
        kiberpnk_gradus = wrap.sprite.get_angle(kiberpank)
        wrap.sprite.set_angle(patron, kiberpnk_gradus)
        wrap.sprite.show(patron)

import wrap_py
wrap_py.app.start()
