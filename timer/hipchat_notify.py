import sys
import hipchat

from random import randint

if __name__ == '__main__':
    args = sys.argv
    
    if sys.argv[1] == '0':
        messages = [
            'POMO-STARTO-SHUTUP-O',
            'POMO-SHUT-YOUR-FACEO',
            'POMO-It started y\'all',
            'POMO DON\'T STOPO!',
            'TALK NOT, POMO INTERRUPTER!',
            'DIE THEE, WHO INTERRUPTITH THE POMO!',
            'AND SO WE POMO AGAIN, FOR THE FIRST TIME, FOR THE LAST TIME.',
            'IN 25 MINUTES, YOU CAN OPEN YOUR FACE AGAIN. UNTIL THEN, POMO!'
       ]
    elif sys.argv[1] == '1':
        messages = [
            'POMO-SO-DONEO.',
            'POMO-OVERO!',
            'POMO-BE-FINITO!',
            'POMO-TALK-AGAIN-YO!',
            'NOT-THE-POMO!',
            'I ate the POMO sandwhich and NOW IT IS DONE.',
            'I was just sitting there and BAM! POMO OVER!',
            'You may emerge from you dark lonliness of the POMODORO.',
            'Thus endeth the journey of the ONE TRUE POMO.',
            'Yo, that one guy said you\'re a sissy. POMO OVER!'
        ]
    else:
        exit(1)

    index = randint(0, len(messages)-1)
    
    hipster = hipchat.HipChat(token='d825fb1f1e773daef30d3187716715')
    hipster.method(
        'rooms/message', 
        method='POST', 
        parameters={
          'room_id': 146757, # 287655, 
          'from': 'POMODORO', 
          'message': '@all %s' % messages[index], 
          'color': 'red' if sys.argv[1] == '0' else 'green',
          'notify': 1
        }
    )
