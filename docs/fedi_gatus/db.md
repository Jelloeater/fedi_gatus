Module fedi_gatus.db
====================

Functions
---------

    
`setup_db_connection()`
:   

Classes
-------

`Data(*args, **kwargs)`
:   

    ### Ancestors (in MRO)

    * fedi_gatus.db.DataModel
    * fedi_gatus.db.ModelBase
    * peewee.Model
    * peewee._metaclass_helper_
    * peewee.Node

    ### Class variables

    `id`
    :

    `timestamp`
    :

    ### Methods

    `get(self, num_minutes_to_get: int) ‑> list`
    :   Takes time range of past mins, and returns list of db rows w/ temp data

    `insert(self) ‑> None`
    :

`DataModel(*args, **kwargs)`
:   

    ### Ancestors (in MRO)

    * fedi_gatus.db.ModelBase
    * peewee.Model
    * peewee._metaclass_helper_
    * peewee.Node

    ### Descendants

    * fedi_gatus.db.Data

    ### Class variables

    `id`
    :

    `timestamp`
    :

`ModelBase(*args, **kwargs)`
:   

    ### Ancestors (in MRO)

    * peewee.Model
    * peewee._metaclass_helper_
    * peewee.Node

    ### Descendants

    * fedi_gatus.db.DataModel

    ### Class variables

    `DoesNotExist`
    :   Common base class for all non-exit exceptions.

    `id`
    :