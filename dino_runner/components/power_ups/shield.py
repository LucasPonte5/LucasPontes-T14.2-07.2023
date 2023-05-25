from dino_runner.components.power_ups.power_up import PowerUp
from dino_runner.utils.constants import SHIELD

class Shield(PowerUp):
    def __init__(self):
        #enviado imagem do shield
        super().__init__(SHIELD)