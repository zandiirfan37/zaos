# ZAOS migrations

Migration scripts are ordered, executable shell files named
`NNN-description.sh`.  They receive the installed ZAOS root as `$1`, must be
idempotent, and must fail before changing an incompatible user configuration.
There are no migrations in the initial 2.0.0 public layout.  The updater runs
only migrations whose number is newer than the recorded installed version.
