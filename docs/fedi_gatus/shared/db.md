Module fedi_gatus.shared.db
===========================

Functions
---------

    
`get_connection()`
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

    `banner_url`
    :

    `description`
    :

    `domain`
    :

    `first_seen_at`
    :

    `id`
    :

    `last_seen_at`
    :

    `location_city`
    :

    `location_country`
    :

    `open_registration`
    :

    `software_name`
    :

    `software_version`
    :

    `stats_monthly_active_users`
    :

    `stats_status_count`
    :

    `stats_user_count`
    :

    ### Methods

    `get_single_record(self) ‑> dict`
    :

    `get_top_lemmy_instances(self, count=25) ‑> dict`
    :

    `insert_data(self, data_in: object) ‑> None`
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

    `banner_url`
    :

    `description`
    :

    `domain`
    :

    `first_seen_at`
    :

    `id`
    :

    `last_seen_at`
    :

    `location_city`
    :

    `location_country`
    :

    `open_registration`
    :

    `software_name`
    :

    `software_version`
    :

    `stats_monthly_active_users`
    :

    `stats_status_count`
    :

    `stats_user_count`
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