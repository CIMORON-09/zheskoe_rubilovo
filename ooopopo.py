import random

import wrap

wrap.world.create_world(1000,800)

wrap.add_sprite_dir("kiberpank_file")

kiberpank = wrap.sprite.add("kiberpank_id", 0, 0, "kiberpank")
i=2
o=2


@wrap.on_key_down(wrap.K_5,wrap.K_6)
def pop(keys):
    global i,o
    if wrap.K_5 in keys:
        i=30
        o=30
    if wrap.K_6 in keys:
        i=0
        o=0

@wrap.always()
def r(keys):


    # if wrap.K_6 in keys:
    #     i=None
    #     o=None
    wrap.sprite.move(kiberpank, +i, +o)


import wrap_py
wrap_py.app.start()
