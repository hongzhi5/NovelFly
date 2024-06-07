class AccountsRouter:
    def db_for_read(self, model, **hints):
        if model._meta.app_label == 'accounts' or model._meta.app_label == 'auth':
            return 'accounts_db'
        return 'default'

    def db_for_write(self, model, **hints):
        if model._meta.app_label == 'accounts' or model._meta.app_label == 'auth':
            return 'accounts_db'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        if obj1._meta.app_label == 'accounts' or obj2._meta.app_label == 'accounts' or \
           obj1._meta.app_label == 'auth' or obj2._meta.app_label == 'auth':
            return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        if app_label == 'accounts' or app_label == 'auth':
            return db == 'accounts_db'
        return db == 'default'
