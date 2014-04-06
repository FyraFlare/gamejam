
import pygame

import flower
import manager
from terrain import Terrain
import unit

class Action( unit.Unit ):

    def __init__( self, terrain, executor ):
        unit.Unit.__init__( self, terrain )

        self.active_listeners = {
            pygame.K_s:         self.action_seed,
            pygame.K_t:         self.action_thorns,
            pygame.K_p:         self.action_poison,
            pygame.K_BACKSPACE: self.action_cancel
        }

        self.executor = executor

        manager.restore_default()
        manager.update_current( unit.Unit.active().active_listeners )

    def action_seed( self, event ):
        if self.executor.growth < 2:
            return False
        else:
            self.executor.growth -= 2
            flower.Flower( self.terrain )
        self.delete()
        return True

    def action_thorns( self, event ):
        if self.executor.growth < 3:
            return False
        else:
            self.executor.growth -= 3
            flower.Obstical( self.terrain )
            #create rabit senerio
        self.delete()
        return True

    def action_poison( self, event ):
        if self.executor.growth < 3:
            return False
        else:
            self.executor.growth -= 3
            flower.Obstical( self.terrain )
            self.terrain.multiplier = 0
            #add effects here
        self.delete()
        return True

    def action_cancel( self, event ):
        self.delete()

        manager.restore_default()
        manager.update_current( unit.Unit.active().active_listeners )

        return False
