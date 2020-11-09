##################
Websockets
##################

.. contents:: Table of Contents


.. note::
   More information about Django Channels and the ASGI interface can be found
   `here <https://channels.readthedocs.io/en/stable/introduction.html>`_

--------
Abstract
--------
 | `Here, the term "channel" is used to describe a one-to-one connection between a client and server`
 | `The term "room" will be used to talk about the different chat rooms`

 | When a client attempts to connect to a particular room, it is subscribed to 2 channels, the
   channel corresponding to the room, (``'chat_%s' % self.room_name``), it is also subscribed to a
   channel that is used by all clients which is used to communicate when a chat room is added/deleted


------------
Room Channel
------------
The room channel is used to broadcast the creation of a message. The message is passed to the channel like so:
TODO


--------------------
Notification Channel
--------------------
The notification channel is used to broadcast the creation or deletion of a chat room. The message is passed to the channel like so:
TODO
