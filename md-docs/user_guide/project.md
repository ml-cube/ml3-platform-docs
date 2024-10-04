# Project

A Project is the secondary organizational entity in the ML cube Platform hierarchy.
A Project groups together a set of artificial intelligence algorithms that share a common goal expressed by a set of KPIs.
For this reason, it is composed of several [Tasks].

Users in the [Company] can have access to one or more Projects according to their roles.

When a Project is created, the [User] specifies its *name*, *description*, and selects the *default storage policy*.
Storage policy defines the default behavior the Platform follows to store data that are shared with it.
Indeed, data can be shared via direct upload or remote cloud data source.
In the first case, data are copied in the ML cube private cloud storage, while, for the second one there is the possibility to do not duplicate data keeping them only in the source cloud


[Company]: company.md
[Tasks]: task.md
[User]: user.md