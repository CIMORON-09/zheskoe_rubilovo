import wrap

wrap.world.create_world(1000,800)
wrap.add_sprite_dir("kiberpank_file")
wrap.world.set_back_image("fion/foi/fon.jpg")

kiberpank=wrap.sprite.add("kiberpank_id",500,500, "kiberpank")
dom=wrap.sprite.add("kiberpank_id",50,50, "dombabeegi")



@wrap.on_key_always(wrap.K_w)
def dvizhenie(keys,pos_x,pos_y):

    if wrap.K_w in keys:
        wrap.sprite.move_at_angle_dir(kiberpank,15)


@wrap.always
def fswefw (pos_y,pos_x):
    wrap.sprite.set_angle_to_point(kiberpank,pos_x,pos_y)


#добавить обычный спрайт


import wrap_py
wrap_py.app.start()
