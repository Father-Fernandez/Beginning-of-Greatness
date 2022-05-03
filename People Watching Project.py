import random
import pygame

pygame.init()

#Characters and quotes theyve said
Candy = ["You meet these people over and over again or rather you don’t meet them\n because everyone is generically "
         "trying to appeal to the largest number of people", "A certain level of conventional beauty conventional "
                                                             "beauty mitigates\n that same level of craziness",
         "You just have to forget the possibility of failing.\n The system objectively doesn’t work so you have to "
         "change the system", "The universe is built on the law of energy conservation, meaning for every action "
                              "there is an equal and opposite reaction\n let’s say you’re hit by a car, the distance "
                              "you fly through the air is proportional to the speed of the car.\n Energy cannot be "
                              "destroyed else it lead to the creation of something else but death gives that the "
                              "finger.", "Think about a human life, think about the universe of thoughts and Ideas "
                                         "and experiences and memories contained in just one person\n think of all the "
                                         "infinite potential in just a single individual, think of all the social "
                                         "connections, family connections,\n the interdependence in a society, "
                                         "the about the power one person has to change the other people and the "
                                         "future in general.", "You’ve got to learn to be alive but not exist", "You can’t fucking tell me every action has an equal "
                                                               "and opposite reaction when in the moment of death,\n "
                                                               "the persons decades of experience and love and "
                                                               "abilities and interconnectedness just cease to "
                                                               "exist", "You look at me like you look at the world\n and all you see is wasted potential", "Religion is just what people used to explain "
                                                                        "things before we had the\n mechanical "
                                                                        "capability to explain it all properly",
         "To die means to ever figure out if humanity conquers death\n because if we do conquer death we will use that\n "
         "technology to save everyone who has ever died", "It’s so weird to think that other people\n would be in the same position as you", "It’s not if you’re thin or fat or ugly or beautiful\n it’s just that you’re different", "Maybe there’s constellation of similar views in here,\n only visible from a distance and burning bright\n in the silent darkness of the cosmos"]
Jeremy = ["Radical honesty maybe, I’m weird and funny and alone\n and I’d think I’d finally find someone who’d like "
          "those differences", "I can date someone and wish they were a certain way,\n or I can just say ‘hi I’m "
                               "looking for someone who thinks two people reading a book quietly counts as doing "
                               "something together\n and then find someone who actually thinks that.\n You only have to "
                               "be attractive to one person am I right?", "I’m sick of good people feeling bad\n and "
                                                                          "bad people feeling good\n that’s what’s on "
                                                                          "my mind", "Even if honesty doesn’t work "
                                                                                     "it’s about the Journey you "
                                                                                     "know.\n You put yourself out "
                                                                                     "there in a risky way and yes "
                                                                                     "there are a predictable number "
                                                                                     "of stares,\n but you learn a lot "
                                                                                     "about yourself just saying "
                                                                                     "stuff out loud and hearing them "
                                                                                     "out loud and realizing you "
                                                                                     "agree with yourself\n you "
                                                                                     "weren’t just thinking it.",
          "It’s like, is it the actual issue that is bothering you or that you its only you", "I totally get it, "
                                                                                              "like I’ve known "
                                                                                              "people,\n I’ve had my "
                                                                                              "moments, its just hard "
                                                                                              "to conceptualize what "
                                                                                              "its like for someone "
                                                                                              "who has it worse",
          "It’s just like an old ketchup bottle,\n at first nothing comes out but then everything comes out."]
Greg = [
    "if I can be honest, I can’t feel the right chemistry here\n but if I’m willing to tell you that then hopefully "
    "that means you’ll believe me when I say\n that I really respect your honesty and I genuinely wish you all the "
    "best in your search"]
Ted = [
    "There’s two things to know about F.R.I.E.N.D.S., everything funny you remember was from the first season\n when "
    "the actors were nobodies with average incomes playing nobodies with average incomes,\n instead of millionaires "
    "playing regular like aliens in human suits", "Yeah, its like guys saying women equal sex so if you’re not "
                                                  "having sex with him,\n he feels you’re ripping him off",
    "The idea of friend zones, infect the general discourse\n and then you’re feeling weird about things that are "
    "perfectly normal", "Not everything good,\n looks that way from the outside", "I have friends who don’t get it, "
                                                                                  "I mean they don’t say it out "
                                                                                  "right,\n but they say nothing "
                                                                                  "instead of stuff they’d normally "
                                                                                  "say", "Anyone looking at the world right now\n would conclude that this shit sucks", "We’re not going out mom, "
                                                                                         "we’re just in a situation "
                                                                                         "of permanent\n mutual "
                                                                                         "support and "
                                                                                         "understanding",
    "We’re just attracted to others because\n of the confidence we get by being accepted by another person", "We send out these various things that indicate that you’ve made it,\n so if someone has one of things, they will never again need assistance", "People can know the facts\n and never get past appearances", "Everything seems like a good idea at 3 am", "If anyone gets there\n its because of the examples other people set for us"]
Safra = [
    "I just tend to assume I’m 100 times worse than everyone else,\n its kind of a depression/anxiety thing I guess.", "You can be attractive and independent with a decent job\n and live in an apartment and you’ll still feel\n like a total fucking failure half the time",
    "When you’re talking depression, it’s just the whole thing of not seeing a point to doing anything\n because "
    "you’re so shitty or the world is so shitty\n and you can’t stop telling yourself that even though you know it’s "
    "not true",
    "That’s basically the basis of my depression metaphor,\n it’s like this thing where you keep slipping into\n another "
    "reality and you don’t notice until it’s too late", "You’ve had to learn how to imitate humans\n so you can pass for one of them\n but you still worry about being discovered",
    "Depression is like a hipster mustache villain,\n he blends in so you don’t see it coming and then he just,\n "
    "annihilates your self-esteem before you can remember that this keeps happening",
    "I have to think of depression as this outside entity\n which tricks you into forgetting reality because\n "
    "intellectually, I do know I’m alright, that I’m good and nice to everyone"]
Martha = ["Friendzone. That’s where little dickless losers hang around the chick they wanna screw\n but she obviously "
          "doesn’t return their feeling or something right?", "You gotta learn to bury the anger\n or else all there would be is anger", "You keep getting dressed up for the ball\n but it keeps getting differed"]
Jackson = ["There is no such thing as normal\n but there is definitely a common experience", "They keep telling you to learn so relevant skills and go outside\n go meet someone but they never tell you how", "what if you had to spend so much time and emotion trying to figure out who you are\n that when you look around it looks like you begun 100 feet back from the start", "What if you have decades left to go\n but it always feels like you have no time left"]
Flossy = ["what if your carefully crafted persona\n came at the expense of developing practical skills", "You’ve had to learn to live with the knowledge\n that all this will over and all you can do is desperately\n try to make ripples in the water"]

# various attributes
Black = (0, 0, 0)
White = (255, 255, 255)
Blue = (0, 0, 255)
window = pygame.display.set_mode((1000, 700))
Red = (255, 0, 0)
Dark_Red = (185, 0, 0)
name = ['Candy', 'Jeremy', 'Greg', 'Safra', 'Martha', 'Ted', 'Jackson', 'Flossy']
x = 800
y = 250
Width = 175
Height = 125
pygame.display.set_caption("I am the best")
Clicked = pygame.MOUSEBUTTONDOWN
Button = pygame.draw.rect(window, Red, (x, y, Width, Height))
Position = pygame.MOUSEMOTION
random_message = pygame.font.SysFont('Comic sans', 25)
clock = pygame.time.Clock()


#to randomly choose the different names and quotes theyve said
def random_phrase_generation():
    Character = random.choice(name)
    Character_name = (Character + ": ")
    if Character_name == 'Candy: ':
        print(Character_name + random.choice(Candy))
    elif Character_name == 'Jeremy: ':
        print(Character_name + random.choice(Jeremy))
    elif Character_name == 'Greg: ':
        print(Character_name + random.choice(Greg))
    elif Character_name == 'Ted: ':
        print(Character_name + random.choice(Ted))
    elif Character_name == 'Martha: ':
        print(Character_name + random.choice(Martha))
    elif Character_name == 'Jackson: ':
        print(Character_name + random.choice(Jackson))
    elif Character_name == 'Flossy: ':
        print(Character_name + random.choice(Flossy))
    else:
        print(Character_name + random.choice(Safra))


class DrawTheButton():
    def __init__(self, Colour, x, y, Width, Height, Text='',):
        self.Colour = Colour
        self.x = x
        self.y = y
        self.Width = Width
        self.Height = Height
        self.Text = Text

#draw the button on the screen
    def drawing(self, window, outline=True):
        if outline:
            pygame.draw.rect(window, White, (self.x - 4, self.y - 4, self.Width + 8, self.Height + 8), 0)
        pygame.draw.rect(window, self.Colour, (self.x, self.y, self.Width, self.Height,))

#putting a text in the center of the box
        if self.Text != '':
            font = pygame.font.SysFont('Comic sans', 25)
            text = font.render(self.Text, True, (0, 0, 0))
            window.blit(text, (self.x + (self.Width / 2 - 150 / 2), self.y + (self.Height / 2 - 30 / 2)))
#getting the position of the mouse on the screen to change the colour of the box
    def mouse_position(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.Width:
            if pos[1] > self.y and pos[1] < self.y + self.Height:
                return True

        return False

running = True
RedButton = DrawTheButton(Red, x, y, Width, Height, 'CLICK ME')

#operation to get everything running
while running:
    window.fill(Black)
    RedButton.drawing(window)
    for event in pygame.event.get():
        pos = pygame.mouse.get_pos()
        if event.type == Clicked:
            if RedButton.mouse_position(pos):
                random_phrase_generation()
                RedButton.Colour = Dark_Red
            else:
                RedButton.Colour = Red
        if event.type == Position:
            if RedButton.mouse_position(pos):
                RedButton.Colour = Blue
            else:
                RedButton.Colour = Red
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()

