import pyxel

## Bgm class has all the music of the game
class Bgm:
    ##constructor
    # @brief create all sound in all channels
    # @para self
    def __init__(self):
        pyxel.sound(0).set(
            "e2e2c2g1 g1g1c2e2 d2d2d2g2 g2g2rr" "c2c2a1e1 e1e1a1c2 b1b1b1e2 e2e2rr",
            "p",
            "6",
            "vffn fnff vffs vfnn",
            25,
        )
        pyxel.sound(1).set(
            "r a1b1c2 b1b1c2d2 g2g2g2g2 c2c2d2e2" "f2f2f2e2 f2e2d2c2 d2d2d2d2 g2g2r r ",
            "s",
            "6",
            "nnff vfff vvvv vfff svff vfff vvvv svnn",
            25,
        )
        pyxel.sound(2).set(
            "c1g1c1g1 c1g1c1g1 b0g1b0g1 b0g1b0g1" "a0e1a0e1 a0e1a0e1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
        pyxel.sound(3).set(
            "f0c1f0c1 g0d1g0d1 c1g1c1g1 a0e1a0e1" "f0c1f0c1 f0c1f0c1 g0d1g0d1 g0d1g0d1",
            "t",
            "7",
            "n",
            25,
        )
        pyxel.sound(4).set(
            "f0ra4r f0ra4r f0ra4r f0f0a4r", "n", "6622 6622 6622 6422", "f", 25
        )
        pyxel.sound(5).set(
            "c1d1f1g1a1b1", "t", "66", "n"*4 +"f", 7
        )
        pyxel.sound(6).set(
            note="c3e3g3c4c4", tone="s", volume="4", effect=("n" * 4 + "f"), speed=7
        )
        pyxel.sound(7).set(
            note="f3b2f2b1 f1f1f1f1", tone="n", volume="4", effect=("n" * 4 + "f"), speed=7
        )

    ##landpage music
    # @para self   
    def landpage_music(self):
        pyxel.play(0, [0, 1], loop=True)
        pyxel.play(1, [2, 3], loop=True)
        pyxel.play(2, 4, loop=True)

    ##game music
    # @para self  
    def game_music(self):
        pyxel.play(1, [2, 3], loop=True)

    ##end music
    # @para self 
    def end_music(self):
        pyxel.play(2, 4, loop=True)

    ##gift music
    # @para self 
    def gift_music(self):
        pyxel.play(2, 6, loop=False)
     
    ##shoot music
    # @para self    
    def shoot_music(self):
        pyxel.play(0, 5, loop=False)

    ##damage music
    # @para self 
    def damage_music(self):
        pyxel.play(1, 7, loop=False)
        
    ##stop music
    # @para self 
    def stop_music(self):
        for i in range(0,3):
            pyxel.stop(i)

