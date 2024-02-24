class EntityDoesNotExist(Exception):
    """Raised when entity was not found in database."""


class CPFAlreadyExists(Exception):
    """Raised when a CPF is already registered in the database."""


class ProductNameAlreadyExists(Exception):
    """Raised when a Product Name is already registered in the database."""
