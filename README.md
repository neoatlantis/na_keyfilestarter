NeoAtlantis Keyfile Starter
===========================

This is a derived project from [KeyfileFS](https://github.com/neoatlantis/keyfilefs)
and [Volatile Password Generator](https://github.com/neoatlantis/volatile-password-generator),
which represents the author's own policy on doing keyfiles.

The author intends to design this tool mainly for himself, therefore this will
include a number of paranoid & customized features. As hinted above, there
could be:

1. a keyfile choosen from filesystem
2. a passcode-protected key, retrieved from Google Cloud
3. a smartcard

simultaneously required to mount a KeyfileFS.

It's further designed to support launching an application subsequently when
the KeyfileFS is ready, e.g. KeepassXC.
