Module fedi_gatus.shared.db
===========================

Functions
---------

    
`setup_db_connection()`
:   

Classes
-------

`DataAccess(*args, **kwargs)`
:   

    ### Ancestors (in MRO)

    * fedi_gatus.shared.db.DataModel
    * fedi_gatus.shared.db.ModelBase
    * peewee.Model
    * peewee._metaclass_helper_
    * peewee.Node

    ### Class variables

    `id`
    :

    `some_data`
    :

    `timestamp`
    :

    ### Methods

    `get_single_record(self) ‑> dict`
    :

    `insert(self, some_data: str) ‑> None`
    :

`DataModel(*args, **kwargs)`
:   

    ### Ancestors (in MRO)

    * fedi_gatus.shared.db.ModelBase
    * peewee.Model
    * peewee._metaclass_helper_
    * peewee.Node

    ### Descendants

    * fedi_gatus.shared.db.DataAccess

    ### Class variables

    `id`
    :

    `some_data`
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

    * fedi_gatus.shared.db.DataModel

    ### Class variables

    `DoesNotExist`
    :   Common base class for all non-exit exceptions.

    `id`
    :