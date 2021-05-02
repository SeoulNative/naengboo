from database.models import Ingredients


class IngredientsDao:

    def add_ingredients(self, data):
        new_ingredients = Ingredients()
        new_ingredients.category = data["category"]
        new_ingredients.name = data["name"]
        new_ingredients.icon_url = data["icon_url"]
        return new_ingredients.save()

    def get_ingredient_list(self, options):
        return Ingredients.objects(**options)

    def __call__(self):
        return Ingredients
        