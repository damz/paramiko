
import sys

if (sys.version_info[0] < 2) or ((sys.version_info[0] == 2) and (sys.version_info[1] < 3)):
    raise RuntimeError('You need python 2.3 for this module.')


__author__ = "Robey Pointer <robey@lag.net>"
__date__ = "10 Nov 2003"
__version__ = "0.1-charmander"
__credits__ = "Huzzah!"
__license__ = "Lesser GNU Public License (LGPL)"


import ssh_exception, transport, auth_transport, channel, rsakey, dsskey

class SSHException (ssh_exception.SSHException):
    """
    Exception thrown by failures in SSH2 protocol negotiation or logic errors.
    """
    pass

class Transport (auth_transport.Transport):
    """
    An SSH Transport attaches to a stream (usually a socket), negotiates an
    encrypted session, authenticates, and then creates stream tunnels, called
    L{Channel}s, across the session.  Multiple channels can be multiplexed
    across a single session (and often are, in the case of port forwardings).
    """
    pass

class Channel (channel.Channel):
    """
    A secure tunnel across an SSH L{Transport}.  A Channel is meant to behave
    like a socket, and has an API that should be indistinguishable from the
    python socket API.
    """
    pass

class RSAKey (rsakey.RSAKey):
    """
    Representation of an RSA key which can be used to sign and verify SSH2
    data.
    """
    pass

class DSSKey (dsskey.DSSKey):
    """
    Representation of a DSS key which can be used to sign an verify SSH2
    data.
    """
    pass


__all__ = [ 'Transport', 'Channel', 'RSAKey', 'DSSKey', 'transport',
            'auth_transport', 'channel', 'rsakey', 'dsskey', 'util',
            'SSHException' ]
