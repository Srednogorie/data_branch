class DataTablesRouter:
    """
    A router to control all database operations on models in the
    data_core application.
    """

    def db_for_read(self, model, **hints):
        """
        Attempts to read data models go to data_tables.
        """
        if model._meta.app_label == 'data_core':
            return 'data_core'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write data models go to data_tables.
        """
        if model._meta.app_label == 'data_core':
            return 'data_core'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the data app is involved.
        """
        if obj1._meta.app_label == 'data_core' or obj2._meta.app_label == 'data_core':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the data app only appears in the 'data_tables' database.
        """
        if db == 'data_core':
            return app_label == 'data_core'
        elif app_label == 'data_core':
            return False
        return None
