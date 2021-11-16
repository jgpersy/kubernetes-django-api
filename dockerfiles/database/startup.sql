CREATE TABLE meat_recipes (
    recipe_id int,
    PRIMARY KEY (recipe_id),
    recipe_title varchar(255),
    recipe_text varchar(255)
);

INSERT INTO meat_recipes VALUES (1, "Beef Stroganoff", "Beef Stroganoff recipe instructions blah blah");
INSERT INTO meat_recipes VALUES (2, "Steak", "Steak recipe instructions blah blah");
INSERT INTO meat_recipes VALUES (3, "Pepperoni Pizza", "Pepperoni Pizza recipe instructions blah blah");

CREATE TABLE vegetarian_recipes (
    recipe_id int,
    PRIMARY KEY (recipe_id),
    recipe_title varchar(255),
    recipe_text varchar(255)
);

INSERT INTO vegetarian_recipes VALUES (1, "Vegetarian wraps", "Vegetarian wraps recipe instructions blah blah");
INSERT INTO vegetarian_recipes VALUES (2, "Miso soup", "Miso soup recipe instructions blah blah");
INSERT INTO vegetarian_recipes VALUES (3, "Butternet quiche", "Butternet quiche recipe instructions blah blah");

