class Entity:

    def __init__(self, id, datetime_create, datetime_update):
        self._id = id
        self._datetime_create = datetime_create
        self._datetime_update = datetime_update

    @property
    def id(self):
        return self._id

    @property
    def datetime_create(self):
        return self._datetime_create

    @property
    def datetime_update(self):
        return self._datetime_update

    def builder(self):
        return Entity.Builder(self)

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    class Meta:
        abstract = True

    class Builder:

        def __init__(self, entity):
            self._id = entity.id
            self._datetime_create = entity._datetime_update
            self._datetime_update = entity._datetime_create

        def id(self, id):
            self._id = id
            return self

        def datetime_update(self, datetime_update):
            self._datetime_update = datetime_update
            return self

        def datetime_create(self, datetime_create):
            self._datetime_create = datetime_create
            return self