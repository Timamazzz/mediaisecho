from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

from core.models.Base import Base


class Expert(Base):
    """Модель эксперта в БД"""

    __tablename__ = "experts"

    last_name = Column(String(100), nullable=False)
    """ Фамилия эксперта (обязательное поле, макс. 100 символов) """

    first_name = Column(String(100), nullable=False)
    """ Имя эксперта (обязательное поле, макс. 100 символов) """

    middle_name = Column(String(100), nullable=True)
    """ Отчество эксперта (необязательное поле, макс. 100 символов) """

    description = Column(String(500), nullable=False)
    """ Описание эксперта: должность, специализация и область знаний (макс. 500 символов) """

    # categories = relationship(
    #     "Category",
    #     back_populates="experts",
    # )
