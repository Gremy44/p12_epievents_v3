class Permissions:
    def __init__(self):
        pass

    def sales_required(fn):
        def wrapper(self, *args, **kwargs):
            if not (self.user.role_id == 1 or self.user.is_superuser != 0):
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper

    def support_required(fn):
        def wrapper(self, *args, **kwargs):
            if not (self.user.role_id == 2 or self.user.is_superuser != 0):
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper

    def gestion_required(fn):
        def wrapper(self, *args, **kwargs):
            if not (self.user.role_id == 3 or self.user.is_superuser != 0):
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper

    def admin_required(fn):
        def wrapper(self, *args, **kwargs):
            if not self.user.is_superuser == 1:
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper
    
    def support_or_gestion_required(fn):
        def wrapper(self, *args, **kwargs):
            if not (self.user.role_id == 2 or self.user.role_id == 3 or self.user.is_superuser != 0):
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper
    
    def sale_or_gestion_required(fn):
        def wrapper(self, *args, **kwargs):
            if not (self.user.role_id == 1 or self.user.role_id == 3 or self.user.is_superuser != 0):
                print(
                    "Vous n'avez pas l'autorisation "
                    "d'accéder à cette fonctionnalité."
                )
                input("Appuyez sur une touche pour continuer...")
                return
            return fn(self, *args, **kwargs)

        return wrapper
