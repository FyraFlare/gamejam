
AI_LEFT  = 1000
AI_RIGHT = 1001
AI_UP    = 1002
AI_DOWN  = 1003
AI_MOVE  = 1004
AI_SKIP  = 1005

class Event(object):

    _events = []

    @classmethod
    def get( cls ):
        events = cls._events
        cls._events = []

        return events

    def __init__( self, key, **kwargs ):
        self.key = key

        for k, v in kwargs.items():
            setattr(self, k, v )

        Event._events.append( self )

