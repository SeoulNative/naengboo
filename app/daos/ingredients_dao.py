from app.daos.base_dao import BaseDao

class IngredientsDao(BaseDao):
    def __init__(self):
        BaseDao.__init__(self, "ingredients")

    def example_get_all_ingredients(self):
        return self.find_list_by_filter({})