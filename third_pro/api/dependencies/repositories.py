from fastapi import Depends
from sqlalchemy.orm import Session

from third_pro.configs.session import get_session


def get_db() -> Session:
    return next(get_session())


def get_repository(repository):
    def _get_repository(session: Session = Depends(get_db)):
        return repository(session)

    return _get_repository
