
import pygame

import ai
import colors
import unit
import terrain as t

import event

class Rabbit( unit.Unit ):

    def __init__( self, terrain ):
        unit.Unit.__init__( self, terrain )
        self.growth = 5

        self.active_listeners = {
            event.AI_SKIP:  self.action_skip,
            event.AI_LEFT:  self.action_left,
            event.AI_RIGHT: self.action_right,
            event.AI_UP:    self.action_up,
            event.AI_DOWN:  self.action_down
        }

        self.wait_time = 1

        self.target = None

    def _action_direction( self, action_terrain ):
        ai.Action( action_terrain, self )
        return False

    def action_up( self, event ):
        action_terrain = self.terrain.up_terrain()
        return self._action_direction( action_terrain )

    def action_down( self, event ):
        action_terrain = self.terrain.down_terrain()
        return self._action_direction( action_terrain )

    def action_left( self, event ):
        action_terrain = self.terrain.left_terrain()
        return self._action_direction( action_terrain )

    def action_right( self, event ):
        action_terrain = self.terrain.right_terrain()
        return self._action_direction( action_terrain )
    
    def action_skip( self, event):
        return True

    def distance( self, terrain ):
        row_diff = abs(self.terrain.row - terrain.row)
        col_diff = abs(self.terrain.col - terrain.col)
        return row_diff + col_diff

    def closer( self, terrain1, terrain2 ):
        if self.distance( terrain1 ) <= self.distance( terrain2 ):
            return terrain1
        return terrain2

    def find_target( self ):
        for terrain in t.all():
            if terrain is not self.terrain and terrain.contains_unit():
                if self.target is None:
                    self.target = terrain
                self.target = self.closer( terrain, self.target )
                    

    def update( self, dt ):
        if self is not unit.Unit.active(): return
        self.wait_time -= dt

        if self.wait_time < 0:
            self.wait_time = 1
            if self.target:
                row_diff = self.target.row - self.terrain.row
                col_diff = self.target.col - self.terrain.col

                if abs( row_diff ) > abs( col_diff ):
                    if row_diff < 0:
                        event.Event( event.AI_UP )
                    else:
                        event.Event( event.AI_DOWN )
                else:
                    if col_diff < 0:
                        event.Event( event.AI_LEFT )
                    else:
                        event.Event( event.AI_RIGHT )
            else:
                event.Event( event.AI_SKIP )

        elif self.target is None:
            self.find_target()

    def draw( self, screen ):
        pygame.draw.rect( screen, colors.GREY, self.terrain )#old, restore?
        self.draw_number( screen )
        #screen.blit(screen,colors.RABBIT)#DELETE????
        unit.Unit.draw( self, screen )#Old, restore?

