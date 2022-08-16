from otree.api import *
import random


class Constants(BaseConstants):
    name_in_url = 'task'
    players_per_group = None
    num_rounds = 3
    contact = 'Amsterdam/contact.html'
    papercups_template = 'Amsterdam/papercups.html'
    task1= __name__ + '/task1.html'
    task2 = __name__ + '/task2.html'
    task3 = __name__ + '/task3.html'



class Subsession(BaseSubsession):
    pass

def creating_session(subsession, partipant=None):
    if subsession.round_number == 1:
        for player in subsession.get_players():
            player.participant.seed = random.random()
            if player.id_in_group % 2 == 0:
                player.participant.payment="they received 1 Pound"
            else:
                player.participant.payment="they received 0.50 pounds and 0.50 pounds was donated to a charity of their choice"


    for player in subsession.get_players():
        random.seed(player.participant.seed)
        list = random.sample([1, 2, 3], 3)
        index=(player.round_number)-1
        case=list[index]
        player.case = case


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    case = models.StringField()
    b1 = models.StringField()
    b2 = models.StringField()
    skill=models.StringField(label="In your opinion: What is the main skill required for this task?")
    payment = models.StringField()




class task(Page):
    form_model = 'player'
    form_fields = ['b1', 'b2','skill']
    @staticmethod
    def vars_for_template(player: Player):
        case = player.case
        return dict(case=case)


class end(Page):
    @staticmethod
    def is_displayed(player):
        return player.round_number == 3



page_sequence = [task, end]
