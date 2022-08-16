from otree.api import *
c = Currency  # old name for currency; you can delete this.


class Constants(BaseConstants):
    name_in_url = 'intro'
    duration = 15
    players_per_group = None
    num_rounds = 1
    instructions_template = __name__ + '/instructions.html'
    contact = __name__ + '/contact.html'
    papercups_template = __name__ + '/papercups.html'



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass



class Player(BasePlayer):
  pass



class Introduction(Page):
   pass



class begin(Page):
    pass


page_sequence = [begin,Introduction]
