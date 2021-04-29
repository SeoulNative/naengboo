from database.models import Ingredients


class IngredientsDao:
    model = Ingredients

    def add_ingredients(self, data):
        new_ingredients = self.model()
        new_ingredients.category = data["category"]
        new_ingredients.name = data["name"]
        new_ingredients.icon_url = data["icon_url"]
        return new_ingredients.save()
        