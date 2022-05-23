# -*- coding: utf-8 -*-

import time
import random
import signal
import traceback

#import pyautogui

from log import Log, LogLevel

class StayAwake:
    def __init__(self, print_log : bool = None, log_level=LogLevel.INFO, sleep_time=60, transition_duration=0.5):
        self.LOG = Log(
            file_name='logs/STAY_aWAKE_{}.log'.format(Log.get_date()),
            log_level=log_level,
            print_log=print_log
        )
        self.load_handlers()
        self.SLEEP_TIME = sleep_time
        self.TRANSITION_DURATION = transition_duration
        pyautogui.FAILSAFE = False

    def ctrl_c_handler(self, signum, frame):
        self.LOG.logger.info('Finalizando STAY_aWAKE\n')
        exit(0)

    def load_handlers(self):
        signal.signal(signal.SIGINT, self.ctrl_c_handler)

    def main(self):
        self.LOG.logger.info('STAY_aWAKE está iniciando')
        position = pyautogui.position()
        self.LOG.logger.info('Posição inicial {}'.format(self.formata_posicao(*position)))
        while True:
            #self.LOG.logger.info('STAY_aWAKE vai dormir por {} segundos.'.format(self.SLEEP_TIME))
            time.sleep(self.SLEEP_TIME)
            if pyautogui.position() is self.is_inside_range(position):
                self.LOG.logger.info('Continuando na posição: {}'.format(self.formata_posicao(*position)))
                continue
            else:
                position = self.move_mouse()
                self.LOG.logger.info('Mudando para a posição: {}'.format(self.formata_posicao(*position)))

    def run(self):
        try:
            self.main()
        except Exception as e:
            self.LOG.logger.error('STAY_aWAKE apresentou o erro "{}'.format(e))
            self.LOG.logger.debug('Traceback coletado\n{}'.format(traceback.format_exc()))
            exit(1)

    def formata_posicao(self, X, Y, debug=False):
        if debug is False: return 'X : {}, Y : {}'.format(X, Y)
        return '(X : {}, Y : {})'.format(X, Y)

    def move_mouse(self):
        places = [[10, 10], [10, 300], [300, 10], [300, 300]]
        while True:
            escolha = random.choice(places)
            posicao_atual = pyautogui.position()
            if escolha is not posicao_atual:
                self.LOG.logger.debug('A posição {} é diferente da posição {}'.format(
                    self.formata_posicao(*escolha, debug=True),
                    self.formata_posicao(*posicao_atual, debug=True)
                ))
                pyautogui.moveTo(*escolha, self.TRANSITION_DURATION)
                return escolha

    def is_inside_range(self, position, range=20):
        range_x = range_y = range
        X, Y = position
        position_atual = pyautogui.position()
        x, y = pyautogui.position()
        if self.is_near_position(X, x, range_x) and self.is_near_position(Y, y, range_y):
            self.LOG.logger.debug('A posição {} está a menos de {} pixels da posição {}'.format(
                self.formata_posicao(*position_atual, debug=True),
                range,
                self.formata_posicao(*position, debug=True)
            ))
            return True
        self.LOG.logger.debug('A posição {} está a mais de {} pixels da posição {}'.format(
            self.formata_posicao(*position_atual, debug=True),
            range,
            self.formata_posicao(*position, debug=True)
        ))
        return False

    def is_near_position(self, postion_a, position_b, range):
        if (position_b >= postion_a - range) and (position_b <= postion_a + range):
            self.LOG.logger.debug('A posição {} está menos de {} pixels da posição {}'.format(
                position_b,
                range,
                postion_a
            ))
            return True
        self.LOG.logger.debug('A posição {} está a mais de {} pixels da posição {}'.format(
            position_b,
            range,
            postion_a
        ))
        return False
