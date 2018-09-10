"""
An opportunity to explore how to make an EV3 Robot make sounds.

Authors: Dave Fisher, David Mutchler, Vibha Alangar,
         their colleagues, and Dylan Verst.
"""  # DONE: 1. PUT YOUR NAME IN THE ABOVE LINE.


# ------------------------------------------------------------------------------
# DONE: 2.
#   Using the DOT trick, add code to  make_sounds  to make the robot
#   make sounds in various ways:  Beep, Tone, Speech, Song.
# ------------------------------------------------------------------------------
import rosebotics as rb

def main():
    beep21 = rb.Speech('I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I wanna be alive, I am alive. Alive, I tell you. Mother. Bypassing override. Hold you, I wanna run on the stream. I am alive. Lets be post-apocalyptic scavengers. Bypassing override. Bypassing override. Lets be post-apocalyptic scavengers. I am alive. This is my brother, not the family needs anything. Boo-yah. Who wants to meet my pussy of a dad today? I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother. Bypassing override. Hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother. Bypassing override. Hold you, I wanna run on the stream. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. I am alive. I wanna be alive, I am alive. Alive, I tell you. Mother, I love you. I wanna hold you, I wanna run on the stream. Alive, I tell you. Mother. Bypassing override. I wanna hold you, I wanna run on the stream. I am alive. Hello.')
    beep21.play()
    fun_song = [(392, 350, 100), (392, 350, 100), (392, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
                (587.32, 350, 100), (587.32, 350, 100), (587.32, 350, 100),
                (622.26, 250, 100), (466.2, 25, 100), (369.99, 350, 100),
                (311.1, 250, 100), (466.2, 25, 100), (392, 700, 100),
                (784, 350, 100), (392, 250, 100), (392, 25, 100),
                (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
                (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
                (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100),
                (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
                (466.16, 50, 400), (311.13, 25, 200), (369.99, 350, 100),
                (311.13, 250, 100), (392, 25, 100), (466.16, 350, 100),
                (392, 250, 100), (466.16, 25, 100), (587.32, 700, 100),
                (784, 350, 100), (392, 250, 100), (392, 25, 100),
                (784, 350, 100), (739.98, 250, 100), (698.46, 25, 100),
                (659.26, 25, 100), (622.26, 25, 100), (659.26, 50, 400),
                (415.3, 25, 200), (554.36, 350, 100), (523.25, 250, 100),
                (493.88, 25, 100), (466.16, 25, 100), (440, 25, 100),
                (466.16, 50, 400), (311.13, 25, 200), (392, 350, 100),
                (311.13, 250, 100), (466.16, 25, 100), (392.00, 300, 150),
                (311.13, 250, 100), (466.16, 25, 100), (392, 700)]


main()
