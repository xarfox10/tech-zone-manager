from database.database import Database
from repositories.id_repository import IdRepository


class IdEngine:

    def __init__(self):
        self.repository = IdRepository()

    def generate(self, prefix):

        next_number = self.repository.get_next_number(prefix)

        item_id = f"{prefix}-{next_number:06d}"

        self.repository.update_next_number(
            prefix,
            next_number + 1,
        )

        return item_id