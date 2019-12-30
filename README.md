NeoAtlantis Keyfile Starter
===========================

This is a derived project from [KeyfileFS][KF] and [Volatile Password
Generator][VPG], which represents the author's own policy on doing keyfiles.

The author intends to design this tool mainly for himself, therefore this will
include a number of paranoid & customized features. As hinted above, there
could be:

1. a keyfile choosen from filesystem
2. a passcode-protected key, retrieved from Google Cloud
3. a smartcard

simultaneously required to mount a KeyfileFS.

It's further designed to support launching an application subsequently when
the KeyfileFS is ready, e.g. KeepassXC.

## Multiple Factor Decryption

The idea behind this project is my consideration of good password managements.
Good management of passwords, shall not only provide secrecy, as most
applications have solved, by encrypting daily passwords with a master one, but
also a feature that **allows you to destroy the whole password storage in no
time, permanently, and with exactly one attempt**.

Say that you have all your passwords in a Keepass database. And since you value
that database much, you have set both a keyfile and a password to be entered
for decryption.

However both factors here may be forced to be given out, if someone threatens
you. If you cannot deny (e.g. someone is certain to find something interest
from your computer), then at least you can nullify their efforts at the time
they attempt a decryption. Setting a game rule like this, they might think once
again.

By replacing an ordinary keyfile with a temporarily generated one from
[KeyfileFS][KF], you can set additional requirements for a successful
decryption:

1. A google cloud function, as in project [Volatile Password Generator][VPG].
   The cloud function runs on an isolated (meaning that you cannot access it
   without huge effort or cooperation from Google) account of firebase. Its
   API allows retrival for a secret key in exchange of a passcode, the latter
   however must remain the same upon each access. Otherwise, the secret key
   is destroyed.
2. A smartcard, currently from ZeitControl, and programmed with similar logic
   as the cloud function. 
3. A single file stored on a portable medium, e.g. the previous keyfile that
   would be used directly with Keepass.

Should one of these protections work, e.g. one of them being activated and
destroys the secret holded, the whole storage is destroyed as no keyfiles will
ever be resumed for decrypting anything encrypted with them. There's no easy
way to tell if your passcode handed out for (1) or (2) will retrieve the
_correct_ key (it will always give out a key).





[KF]: https://github.com/neoatlantis/keyfilefs
[VPG]: https://github.com/neoatlantis/volatile-password-generator
