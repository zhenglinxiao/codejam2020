# -*- coding: utf-8 -*-
"""Scoring.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1e60QrMguIyGyTUPoNMC7U9r8mkHJQgH5
"""

# import json
# file = r'./features.json'
# with open(file) as train_file:
#     features = json.load(train_file)
#
# print(features)

features = {"rocket leaves": 0, "file powder": 1, "salad greens": 2, "organic vegetable broth": 3, "bread slices": 4, "great northern beans": 5, "turbinado": 6, "fruit": 7, "thai green curry paste": 8, "capsicum": 9, "gari": 10, "nonstick spray": 11, "granulated garlic": 12, "California bay leaves": 13, "steamed rice": 14, "crushed ice": 15, "chicken bouillon granules": 16, "wild mushrooms": 17, "plain low-fat yogurt": 18, "ground almonds": 19, "sourdough bread": 20, "lobster": 21, "seedless cucumber": 22, "dried cranberries": 23, "yellow peppers": 24, "extra sharp cheddar cheese": 25, "chickpea flour": 26, "puff pastry": 27, "kasuri methi": 28, "bottled clam juice": 29, "rubbed sage": 30, "mustard greens": 31, "edamame": 32, "malt vinegar": 33, "shredded parmesan cheese": 34, "clarified butter": 35, "apple juice": 36, "lime slices": 37, "nonfat yogurt": 38, "Anaheim chile": 39, "artichok heart marin": 40, "spanish chorizo": 41, "pepperoni": 42, "mustard powder": 43, "celery salt": 44, "fresh herbs": 45, "pork chops": 46, "sambal ulek": 47, "anchovies": 48, "deveined shrimp": 49, "whole milk ricotta cheese": 50, "boneless chicken thighs": 51, "pork loin chops": 52, "chutney": 53, "chips": 54, "japanese eggplants": 55, "reduced fat sharp cheddar cheese": 56, "fusilli": 57, "salami": 58, "hamburger buns": 59, "haricots verts": 60, "tea bags": 61, "sage": 62, "anise seed": 63, "guajillo chiles": 64, "Italian turkey sausage": 65, "swiss cheese": 66, "condensed cream of mushroom soup": 67, "cheese tortellini": 68, "savoy cabbage": 69, "light sour cream": 70, "pecorino cheese": 71, "biscuits": 72, "teriyaki sauce": 73, "chicken meat": 74, "firmly packed light brown sugar": 75, "smoked salmon": 76, "salmon": 77, "fresh pineapple": 78, "picante sauce": 79, "shrimp paste": 80, "salad oil": 81, "thick-cut bacon": 82, "egg roll wrappers": 83, "lower sodium soy sauce": 84, "brown mustard seeds": 85, "fresh leav spinach": 86, "seaweed": 87, "roasted tomatoes": 88, "pepper flakes": 89, "wine": 90, "fresh oregano leaves": 91, "chopped green chilies": 92, "unsalted dry roast peanuts": 93, "radicchio": 94, "spring roll wrappers": 95, "navel oranges": 96, "beaten eggs": 97, "dates": 98, "mango chutney": 99, "rib": 100, "fenugreek leaves": 101, "potato starch": 102, "chinese cabbage": 103, "dipping sauces": 104, "sausage links": 105, "fish stock": 106, "semolina flour": 107, "manchego cheese": 108, "oysters": 109, "grated jack cheese": 110, "semolina": 111, "seasoned rice wine vinegar": 112, "liquid": 113, "parsley leaves": 114, "bird chile": 115, "cocoa powder": 116, "ramen noodles": 117, "white mushrooms": 118, "escarole": 119, "rotini": 120, "pie crust": 121, "orange liqueur": 122, "instant espresso powder": 123, "scallion greens": 124, "grated Gruy\u00e8re cheese": 125, "skinless chicken breasts": 126, "salad": 127, "beef brisket": 128, "parmigiano-reggiano cheese": 129, "light mayonnaise": 130, "pumpkin": 131, "prunes": 132, "sweet corn": 133, "roasting chickens": 134, "sweet pepper": 135, "low-fat sour cream": 136, "boneless pork loin": 137, "tahini": 138, "asparagus spears": 139, "condensed cream of chicken soup": 140, "short-grain rice": 141, "anise": 142, "lamb": 143, "cooking wine": 144, "smoked ham hocks": 145, "fresh marjoram": 146, "poultry seasoning": 147, "turkey": 148, "mashed potatoes": 149, "littleneck clams": 150, "preserved lemon": 151, "taco sauce": 152, "jumbo shrimp": 153, "corn syrup": 154, "dressing": 155, "mixed greens": 156, "shiitake mushroom caps": 157, "taco shells": 158, "dried sage": 159, "steak": 160, "pistachios": 161, "coarse kosher salt": 162, "crimini mushrooms": 163, "dry roasted peanuts": 164, "chicken livers": 165, "creole mustard": 166, "red enchilada sauce": 167, "rigatoni": 168, "ground sirloin": 169, "beef tenderloin": 170, "halibut fillets": 171, "herbes de provence": 172, "bacon drippings": 173, "chuck roast": 174, "konbu": 175, "rotisserie chicken": 176, "plums": 177, "italian salad dressing": 178, "celery seed": 179, "chuck": 180, "chipotle peppers": 181, "grating cheese": 182, "pork butt": 183, "curds": 184, "phyllo dough": 185, "anchovy paste": 186, "curry": 187, "urad dal": 188, "red beans": 189, "parsnips": 190, "chorizo": 191, "soba noodles": 192, "coarse sea salt": 193, "portabello mushroom": 194, "Mexican cheese": 195, "hot pepper": 196, "white hominy": 197, "rice paper": 198, "tomato ketchup": 199, "salad dressing": 200, "fresh curry leaves": 201, "coffee": 202, "masala": 203, "sirloin steak": 204, "chunky salsa": 205, "fat free yogurt": 206, "corn flour": 207, "lemon slices": 208, "cachaca": 209, "poppy seeds": 210, "pork loin": 211, "2% reduced-fat milk": 212, "refrigerated piecrusts": 213, "beef rib short": 214, "white miso": 215, "lower sodium chicken broth": 216, "red food coloring": 217, "cilantro stems": 218, "baby carrots": 219, "spinach leaves": 220, "prepared horseradish": 221, "egg substitute": 222, "lemon rind": 223, "skirt steak": 224, "ranch dressing": 225, "peeled tomatoes": 226, "miso paste": 227, "superfine sugar": 228, "fenugreek seeds": 229, "tilapia fillets": 230, "asafoetida": 231, "cooked ham": 232, "instant yeast": 233, "sweetened coconut flakes": 234, "grated coconut": 235, "condensed milk": 236, "dried shrimp": 237, "vodka": 238, "cauliflower florets": 239, "artichokes": 240, "canned tomatoes": 241, "white sesame seeds": 242, "reduced fat milk": 243, "whole cloves": 244, "chees fresh mozzarella": 245, "rum": 246, "hominy": 247, "chicken bouillon": 248, "semi-sweet chocolate morsels": 249, "salted butter": 250, "fennel": 251, "coconut cream": 252, "fish fillets": 253, "fat skimmed chicken broth": 254, "ancho powder": 255, "fillets": 256, "low-fat buttermilk": 257, "sweet italian sausage": 258, "lime rind": 259, "sherry": 260, "canned black beans": 261, "pico de gallo": 262, "small red potato": 263, "grapeseed oil": 264, "crabmeat": 265, "white beans": 266, "boneless pork shoulder": 267, "table salt": 268, "green cardamom pods": 269, "pizza sauce": 270, "raspberries": 271, "mace": 272, "skim milk": 273, "marinade": 274, "sushi rice": 275, "agave nectar": 276, "serrano chilies": 277, "pineapple juice": 278, "pepper jack": 279, "caraway seeds": 280, "golden brown sugar": 281, "cream of chicken soup": 282, "panko": 283, "tomato juice": 284, "cream style corn": 285, "tamarind paste": 286, "finely chopped fresh parsley": 287, "frozen whole kernel corn": 288, "vegetable oil spray": 289, "lamb shoulder": 290, "white cornmeal": 291, "asiago": 292, "galangal": 293, "mung bean sprouts": 294, "egg noodles": 295, "pearl onions": 296, "squid": 297, "quickcooking grits": 298, "baby bok choy": 299, "diced celery": 300, "green cardamom": 301, "tomatoes with juice": 302, "herbs": 303, "amchur": 304, "lentils": 305, "jicama": 306, "rolls": 307, "leg of lamb": 308, "stock": 309, "tamari soy sauce": 310, "fresh green bean": 311, "elbow macaroni": 312, "blackberries": 313, "orzo": 314, "fish": 315, "angel hair": 316, "fat": 317, "prawns": 318, "cooked shrimp": 319, "fresh raspberries": 320, "firmly packed brown sugar": 321, "chicken pieces": 322, "clam juice": 323, "ripe olives": 324, "orange bell pepper": 325, "leaves": 326, "rice vermicelli": 327, "whole wheat tortillas": 328, "blanched almonds": 329, "corn husks": 330, "vanilla ice cream": 331, "clams": 332, "adobo sauce": 333, "chicken drumsticks": 334, "cognac": 335, "dried currants": 336, "red kidney beans": 337, "grated orange peel": 338, "greens": 339, "canned low sodium chicken broth": 340, "dill": 341, "nori": 342, "fresh shiitake mushrooms": 343, "sunflower oil": 344, "pears": 345, "broth": 346, "fresh mozzarella": 347, "old bay seasoning": 348, "seasoned bread crumbs": 349, "gruyere cheese": 350, "boiling potatoes": 351, "hazelnuts": 352, "dried porcini mushrooms": 353, "lemon grass": 354, "beans": 355, "masa harina": 356, "Mexican oregano": 357, "cottage cheese": 358, "sliced carrots": 359, "pecan halves": 360, "ground chicken": 361, "cornflour": 362, "chorizo sausage": 363, "baby spinach leaves": 364, "swiss chard": 365, "dried red chile peppers": 366, "bow-tie pasta": 367, "whipped cream": 368, "marjoram": 369, "watercress": 370, "hard-boiled egg": 371, "serrano peppers": 372, "sugar pea": 373, "ricotta": 374, "dough": 375, "freshly grated parmesan": 376, "reduced-fat sour cream": 377, "molasses": 378, "frozen pastry puff sheets": 379, "curry paste": 380, "whole kernel corn, drain": 381, "cardamom": 382, "romano cheese": 383, "diced green chilies": 384, "beets": 385, "crushed garlic": 386, "fontina cheese": 387, "rosemary": 388, "green tomatoes": 389, "sausage casings": 390, "unflavored gelatin": 391, "Thai fish sauce": 392, "mustard": 393, "rosemary sprigs": 394, "catfish fillets": 395, "chili oil": 396, "yeast": 397, "red lentils": 398, "maple syrup": 399, "paneer": 400, "creamy peanut butter": 401, "shredded cabbage": 402, "ice": 403, "cooked chicken breasts": 404, "black mustard seeds": 405, "kimchi": 406, "sweet chili sauce": 407, "turnips": 408, "fresh chives": 409, "penne": 410, "walnuts": 411, "sage leaves": 412, "sea scallops": 413, "vidalia onion": 414, "pork sausages": 415, "yellow squash": 416, "quinoa": 417, "dark rum": 418, "chicken legs": 419, "lump crab meat": 420, "greek style plain yogurt": 421, "pizza doughs": 422, "crawfish": 423, "pesto": 424, "Italian bread": 425, "jack cheese": 426, "poblano peppers": 427, "granny smith apples": 428, "gingerroot": 429, "ginger paste": 430, "bok choy": 431, "chile powder": 432, "pineapple": 433, "corn oil": 434, "chillies": 435, "marsala wine": 436, "red curry paste": 437, "palm sugar": 438, "chili paste": 439, "peanut butter": 440, "chopped fresh sage": 441, "ginger root": 442, "dried shiitake mushrooms": 443, "pork belly": 444, "frozen corn kernels": 445, "Italian parsley leaves": 446, "part-skim ricotta cheese": 447, "chili pepper": 448, "barbecue sauce": 449, "dry yeast": 450, "whole peeled tomatoes": 451, "Thai red curry paste": 452, "chopped walnuts": 453, "dashi": 454, "allspice": 455, "garlic chili sauce": 456, "ice cubes": 457, "white bread": 458, "rice flour": 459, "caster sugar": 460, "seeds": 461, "seasoning salt": 462, "chinese rice wine": 463, "mint sprigs": 464, "fresh parsley leaves": 465, "chicken wings": 466, "tequila": 467, "kaffir lime leaves": 468, "non-fat sour cream": 469, "dried apricot": 470, "pimentos": 471, "fat free milk": 472, "sweet paprika": 473, "red cabbage": 474, "artichoke hearts": 475, "salsa verde": 476, "pork shoulder": 477, "ground lamb": 478, "tofu": 479, "seasoning": 480, "extra firm tofu": 481, "lime zest": 482, "italian sausage": 483, "bamboo shoots": 484, "meat": 485, "vegetable shortening": 486, "cremini mushrooms": 487, "ground cayenne pepper": 488, "smoked sausage": 489, "cotija": 490, "bittersweet chocolate": 491, "parsley sprigs": 492, "queso fresco": 493, "Gochujang base": 494, "fresh tarragon": 495, "szechwan peppercorns": 496, "cream cheese, soften": 497, "ancho chile pepper": 498, "panko breadcrumbs": 499, "pecans": 500, "peppercorns": 501, "cooked white rice": 502, "cr\u00e8me fra\u00eeche": 503, "boneless chicken breast": 504, "chili sauce": 505, "garbanzo beans": 506, "fresh tomatoes": 507, "polenta": 508, "mascarpone": 509, "grated orange": 510, "chipotle chile": 511, "daikon": 512, "dry mustard": 513, "chicken breast halves": 514, "jasmine rice": 515, "orange zest": 516, "plain flour": 517, "sharp cheddar cheese": 518, "cardamom pods": 519, "olives": 520, "poblano chiles": 521, "roasted peanuts": 522, "shredded carrots": 523, "light coconut milk": 524, "lard": 525, "pecorino romano cheese": 526, "reduced sodium soy sauce": 527, "shredded cheese": 528, "kale": 529, "asian fish sauce": 530, "chili flakes": 531, "wonton wrappers": 532, "salmon fillets": 533, "fettucine": 534, "cream of tartar": 535, "kidney beans": 536, "light corn syrup": 537, "sherry vinegar": 538, "beef stock": 539, "sliced black olives": 540, "sun-dried tomatoes": 541, "button mushrooms": 542, "mint": 543, "iceberg lettuce": 544, "semisweet chocolate": 545, "ice water": 546, "provolone cheese": 547, "apples": 548, "collard greens": 549, "slivered almonds": 550, "shredded sharp cheddar cheese": 551, "vanilla beans": 552, "ground turkey": 553, "goat cheese": 554, "dried parsley": 555, "pure vanilla extract": 556, "brandy": 557, "bread crumb fresh": 558, "hot red pepper flakes": 559, "spices": 560, "pinto beans": 561, "almond extract": 562, "dried rosemary": 563, "Mexican cheese blend": 564, "butternut squash": 565, "shredded lettuce": 566, "mussels": 567, "frozen corn": 568, "bread": 569, "stewed tomatoes": 570, "arugula": 571, "pancetta": 572, "green olives": 573, "thai basil": 574, "penne pasta": 575, "coconut": 576, "cake flour": 577, "whole wheat flour": 578, "all purpose unbleached flour": 579, "taco seasoning mix": 580, "grated lemon peel": 581, "snow peas": 582, "reduced sodium chicken broth": 583, "lettuce": 584, "grits": 585, "Tabasco Pepper Sauce": 586, "sausages": 587, "guacamole": 588, "chili": 589, "sliced almonds": 590, "lettuce leaves": 591, "couscous": 592, "minced onion": 593, "anchovy fillets": 594, "english cucumber": 595, "fresh thyme leaves": 596, "broccoli florets": 597, "unsweetened coconut milk": 598, "vegetable stock": 599, "french bread": 600, "1% low-fat milk": 601, "self rising flour": 602, "chipotles in adobo": 603, "bread flour": 604, "peas": 605, "almonds": 606, "water chestnuts": 607, "black-eyed peas": 608, "kalamata": 609, "vegetables": 610, "minced ginger": 611, "bourbon whiskey": 612, "dark sesame oil": 613, "beer": 614, "brown rice": 615, "cannellini beans": 616, "pitted kalamata olives": 617, "fennel bulb": 618, "red potato": 619, "chives": 620, "saffron": 621, "frozen chopped spinach": 622, "baking potatoes": 623, "firm tofu": 624, "evaporated milk": 625, "green cabbage": 626, "lasagna noodles": 627, "thyme sprigs": 628, "fresh orange juice": 629, "bacon slices": 630, "green peas": 631, "salt and ground black pepper": 632, "cilantro sprigs": 633, "heavy whipping cream": 634, "tomato pur\u00e9e": 635, "yukon gold potatoes": 636, "cashew nuts": 637, "strawberries": 638, "curry leaves": 639, "broccoli": 640, "margarine": 641, "red chili powder": 642, "cauliflower": 643, "coconut oil": 644, "rice wine": 645, "ham": 646, "tortillas": 647, "thai chile": 648, "bananas": 649, "noodles": 650, "lemon wedge": 651, "napa cabbage": 652, "chopped fresh chives": 653, "roma tomatoes": 654, "part-skim mozzarella cheese": 655, "grape tomatoes": 656, "pork tenderloin": 657, "black olives": 658, "marinara sauce": 659, "red wine": 660, "shortening": 661, "asparagus": 662, "fresh spinach": 663, "greek yogurt": 664, "grated nutmeg": 665, "monterey jack": 666, "ground cardamom": 667, "nutmeg": 668, "roasted red peppers": 669, "golden raisins": 670, "garlic salt": 671, "diced onions": 672, "fresh dill": 673, "sliced mushrooms": 674, "coriander powder": 675, "yoghurt": 676, "linguine": 677, "white rice": 678, "lemon zest": 679, "refried beans": 680, "chinese five-spice powder": 681, "dry sherry": 682, "baby spinach": 683, "flank steak": 684, "cream": 685, "star anise": 686, "vegetable oil cooking spray": 687, "rice noodles": 688, "mint leaves": 689, "peaches": 690, "Shaoxing wine": 691, "unsweetened cocoa powder": 692, "pasta sauce": 693, "russet potatoes": 694, "andouille sausage": 695, "basil leaves": 696, "mango": 697, "chopped green bell pepper": 698, "feta cheese": 699, "okra": 700, "apple cider vinegar": 701, "romaine lettuce": 702, "baguette": 703, "sweetened condensed milk": 704, "taco seasoning": 705, "fresh mushrooms": 706, "beef": 707, "creole seasoning": 708, "melted butter": 709, "saffron threads": 710, "long grain white rice": 711, "corn kernels": 712, "juice": 713, "garlic paste": 714, "basil": 715, "radishes": 716, "chopped pecans": 717, "prosciutto": 718, "fine sea salt": 719, "fresh coriander": 720, "fresh parmesan cheese": 721, "dry bread crumbs": 722, "yellow bell pepper": 723, "arborio rice": 724, "toasted sesame seeds": 725, "enchilada sauce": 726, "cooked chicken": 727, "chopped tomatoes": 728, "Sriracha": 729, "serrano chile": 730, "pork": 731, "tortilla chips": 732, "green chile": 733, "hot pepper sauce": 734, "bread crumbs": 735, "ghee": 736, "dry red wine": 737, "vanilla": 738, "dark soy sauce": 739, "mustard seeds": 740, "shredded Monterey Jack cheese": 741, "vinegar": 742, "chopped fresh mint": 743, "dark brown sugar": 744, "pasta": 745, "chiles": 746, "tomatillos": 747, "basmati rice": 748, "corn": 749, "shiitake": 750, "chopped parsley": 751, "chicken thighs": 752, "sweet onion": 753, "half & half": 754, "fresh ginger root": 755, "orange juice": 756, "low sodium chicken broth": 757, "chile pepper": 758, "yellow corn meal": 759, "green beans": 760, "spaghetti": 761, "grated lemon zest": 762, "boneless chicken skinless thigh": 763, "parsley": 764, "sake": 765, "fresh thyme": 766, "chopped garlic": 767, "smoked paprika": 768, "light soy sauce": 769, "pinenuts": 770, "ground white pepper": 771, "cider vinegar": 772, "boiling water": 773, "white wine vinegar": 774, "fennel seeds": 775, "ricotta cheese": 776, "long-grain rice": 777, "parmigiano reggiano cheese": 778, "orange": 779, "toasted sesame oil": 780, "hot water": 781, "feta cheese crumbles": 782, "thyme": 783, "lemongrass": 784, "ground allspice": 785, "plain yogurt": 786, "spinach": 787, "white wine": 788, "cornmeal": 789, "ground cloves": 790, "green pepper": 791, "chopped fresh thyme": 792, "cajun seasoning": 793, "active dry yeast": 794, "beef broth": 795, "frozen peas": 796, "ground pepper": 797, "low salt chicken broth": 798, "cooked rice": 799, "bell pepper": 800, "lean ground beef": 801, "fresh oregano": 802, "confectioners sugar": 803, "italian seasoning": 804, "coriander seeds": 805, "chickpeas": 806, "peanuts": 807, "spring onions": 808, "cracked black pepper": 809, "vegetable broth": 810, "large shrimp": 811, "cabbage": 812, "fresh mint": 813, "light brown sugar": 814, "cheddar cheese": 815, "low sodium soy sauce": 816, "chopped celery": 817, "hoisin sauce": 818, "ketchup": 819, "leeks": 820, "cherry tomatoes": 821, "white pepper": 822, "oregano": 823, "fresh rosemary": 824, "cheese": 825, "crushed tomatoes": 826, "black peppercorns": 827, "egg whites": 828, "beansprouts": 829, "sweet potatoes": 830, "oyster sauce": 831, "finely chopped onion": 832, "sauce": 833, "coriander": 834, "red pepper": 835, "raisins": 836, "medium shrimp": 837, "mozzarella cheese": 838, "cayenne": 839, "sliced green onions": 840, "fat free less sodium chicken broth": 841, "ground pork": 842, "shredded mozzarella cheese": 843, "lime wedges": 844, "cooking oil": 845, "large egg whites": 846, "powdered sugar": 847, "eggplant": 848, "fresh basil leaves": 849, "mirin": 850, "crushed red pepper flakes": 851, "cold water": 852, "rice": 853, "dijon mustard": 854, "onion powder": 855, "ground red pepper": 856, "capers": 857, "egg yolks": 858, "white vinegar": 859, "cream cheese": 860, "celery ribs": 861, "balsamic vinegar": 862, "large egg yolks": 863, "warm water": 864, "mushrooms": 865, "coarse salt": 866, "peeled fresh ginger": 867, "dried basil": 868, "parmesan cheese": 869, "clove": 870, "ground nutmeg": 871, "peanut oil": 872, "boneless skinless chicken breast halves": 873, "whipping cream": 874, "bacon": 875, "red chili peppers": 876, "cinnamon sticks": 877, "red pepper flakes": 878, "hot sauce": 879, "sesame seeds": 880, "ground ginger": 881, "white onion": 882, "worcestershire sauce": 883, "curry powder": 884, "cinnamon": 885, "tumeric": 886, "red wine vinegar": 887, "whole milk": 888, "green chilies": 889, "ground coriander": 890, "cucumber": 891, "shredded cheddar cheese": 892, "mayonaise": 893, "chicken breasts": 894, "chopped cilantro": 895, "crushed red pepper": 896, "celery": 897, "bay leaf": 898, "fresh cilantro": 899, "granulated sugar": 900, "coconut milk": 901, "plum tomatoes": 902, "buttermilk": 903, "flour tortillas": 904, "tomato sauce": 905, "large garlic cloves": 906, "dried thyme": 907, "ground beef": 908, "zucchini": 909, "black beans": 910, "shrimp": 911, "garam masala": 912, "cumin seed": 913, "sea salt": 914, "baking soda": 915, "freshly ground pepper": 916, "ground turmeric": 917, "cumin": 918, "salsa": 919, "corn tortillas": 920, "chicken": 921, "potatoes": 922, "bay leaves": 923, "chicken stock": 924, "lime juice": 925, "white sugar": 926, "flat leaf parsley": 927, "boneless skinless chicken breasts": 928, "fresh basil": 929, "cilantro": 930, "heavy cream": 931, "tomato paste": 932, "cilantro leaves": 933, "green bell pepper": 934, "yellow onion": 935, "rice vinegar": 936, "dry white wine": 937, "lemon": 938, "canola oil": 939, "avocado": 940, "ground cinnamon": 941, "fish sauce": 942, "chopped onion": 943, "paprika": 944, "vanilla extract": 945, "honey": 946, "flour": 947, "fresh lime juice": 948, "lemon juice": 949, "lime": 950, "garlic powder": 951, "shallots": 952, "cooking spray": 953, "fresh ginger": 954, "brown sugar": 955, "cayenne pepper": 956, "sour cream": 957, "chicken broth": 958, "minced garlic": 959, "fresh parsley": 960, "diced tomatoes": 961, "fresh lemon juice": 962, "chopped cilantro fresh": 963, "dried oregano": 964, "jalapeno chilies": 965, "baking powder": 966, "ginger": 967, "corn starch": 968, "sesame oil": 969, "grated parmesan cheese": 970, "scallions": 971, "purple onion": 972, "red bell pepper": 973, "oil": 974, "chili powder": 975, "milk": 976, "black pepper": 977, "ground cumin": 978, "extra-virgin olive oil": 979, "unsalted butter": 980, "carrots": 981, "large eggs": 982, "tomatoes": 983, "green onions": 984, "kosher salt": 985, "soy sauce": 986, "eggs": 987, "vegetable oil": 988, "pepper": 989, "all-purpose flour": 990, "ground black pepper": 991, "butter": 992, "garlic cloves": 993, "sugar": 994, "garlic": 995, "water": 996, "onions": 997, "olive oil": 998, "salt": 999}

#Define encoding process
import numpy as np
def encode (list_of_ingredients):
  encoding = np.zeros(1000)
  for x in list_of_ingredients:
    if x in features:
      encoding[features[x]] = 1
    else:
      encoding[999] = 1
  return encoding

# #create sample user history
# sample_user_history = {}
# sample_user_history[1001] = [['tomatoes', 'eggs', 'pepper', 'shellfish'], 5]
# sample_user_history[1004] = [['tomatoes', 'chicken', 'fresh ginger', 'cayenne pepper'], 4]
# sample_user_history[1006] = [['carrots', 'milk', 'lime', 'zucchini'], 2]

# sample_user_history

#construct user preference representation
def encode_preference(sample_user_history):
  encoding = np.zeros(1000)
  for order in sample_user_history:
    rating = sample_user_history[order][1]
    if rating >= 3:
      encoding = encoding + (rating * encode(sample_user_history[order][0]))
    else:
      encoding = encoding - ((5-rating) * encode(sample_user_history[order][0]))
  return (encoding)

def score(offer, user_preference):
  offer_encoding = encode(offer)
  score_matrix = np.multiply(offer_encoding, user_preference)
  score = np.sum(score_matrix)
  return score
#
# offer = ['carrots', 'chicken', 'fresh ginger', 'cayenne pepper']
# score(offer)