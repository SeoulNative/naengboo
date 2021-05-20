from database.__init__ import db


class Ingredients(db.Document):
    category = db.StringField(required=True)
    name = db.StringField(required=True)
    icon_url = db.URLField(required=True)
    

class Refrigerator(db.Document):
    rfg_name = db.StringField(required=True)
    rfg_img_url = db.URLField(required=True)
    rfg_memo = db.StringField(required=True)


class Recipes(db.Document):

    class RecipeIngredients(db.EmbeddedDocument):
        ingred_id = db.ObjectIdField(required=True)
        name = db.StringField(required=True)
        quantity = db.StringField(required=True)

    food_name = db.StringField(required=True)
    main_ingredients = db.EmbeddedDocumentListField(RecipeIngredients, required=True)
    sub_ingredients = db.EmbeddedDocumentListField(RecipeIngredients, required=True)
    recipe_steps = db.DictField(required=True)
    hash_tags = db.DictField(required=True)

