# modules/config.py

from faker import Faker
from faker.providers import DynamicProvider
from .models import AgeClass, Size

faker = Faker()

# Uncomment for non-deterministic generation
# Leave commented to have some fun!
# faker.seed_instance(420)
# random.seed(69)

API_URLS = {
    'guilt': "http://34.136.198.50:8080",   # For Guilt Tripping
    # 'prod':   "http://35.208.60.16:8080",   # Production - Brendon's Runner
    'prod':   "http://woofadoption.homes:8080",
    'dev':    "http://35.224.27.57:8080",   # Remote Dev - ixiwoofrunner-001
    'backup': "http://34.57.220.165:8080",  # Backup - Icko's First Runner
    'local':  "http://localhost:8080"       # Local Development
}

# Cities and States for generation
city_state_map = {
    "New York City": "New York",
    "Los Angeles": "California",
    "Santa Clara": "California",
    "San Jose": "California",
    "San Diego": "California",
    "Chicago": "Illinois",
    "Houston": "Texas",
    "Dallas": "Texas",
    "Austin": "Texas",
    "Waco": "Texas",
    "Phoenix": "Arizona",
    "Springfield": "Illinois",
    "West Haven": "Connecticut"
}

# Sample center names
center_names_provider = DynamicProvider(
    provider_name="center_names",
    elements = [
        'Paws & Claws Rescue',
        'Furry Friends Sanctuary',
        'Whiskers & Tails Shelter',
        'Happy Tails Adoption Center',
        'Second Chance Pet Haven',
        'Loving Hearts Animal Rescue',
        'Forever Home Pet Adoption',
        'Rainbow Bridge Shelter',
        'Pawsitive Beginnings',
        'Tail Waggers Rescue Center',
        'Purr-fect Match Adoptions',
        'New Leash on Life Shelter',
        'Paw Prints Rescue',
        'Bark Avenue Adoption Center',
        'Cuddles & Kisses Pet Sanctuary',
        'Healing Paws Retreat',
        'Fur-ever Friends Shelter',
        'Compassionate Critter Haven',
        'Wildlife Wonders Sanctuary',
        'Pet Paradise Haven',
        'Safe Haven Pet Sanctuary',
        'Happy Paws Haven',
        'Kindred Creatures Sanctuary',
        'Angel Whiskers Shelter',
        'Four-Legged Friends Refuge',
        'Rescue Me Retreat',
        'Friendly Felines Sanctuary',
        'Whiskers and Wagging Tails Shelter',
        'Forever Homes Haven',
        'Animal Allies Sanctuary',
        'Loveable Creatures Shelter',
        'Pet Peaceful Place',
        'Whispers of Hope Sanctuary',
        'Zen Pet Haven',
        'Dreamland Critter Refuge',
        'Charming Creatures Cove',
        'Wondrous Wildlife Shelter',
        'Whispering Haven Sanctuary',
        'Moonlit Paws Refuge',
        'Ethereal Pets Paradise',
        'Sanctuary of Serenity',
        'Enchanted Tails Retreat',
        'Tails of Hope Sanctuary',
        'Fur-Ever Family Shelter',
        'Pawfect Harmony Refuge',
        'Furry Friends United',
        'Hopeful Homes Haven',
        'Critter Comfort Haven',
        'Warm Fuzzy Haven',
        'Gentle Souls Shelter'
    ]
)
faker.add_provider(center_names_provider)

pet_first_provider = DynamicProvider(
    provider_name="pet_first",
    elements=["Bongo","Flappy","Knobber","L-dog","Piggers",
              "Tinks","Biscuit","Judge","Warlock","Chunks",
              "Fluffles","Zoomers","Pickles","Thicken","Crunchwrap",
              "Professor","MF","Baron","Buff",
              "Clownish","Bonkers","Nutty","Silly","Sillier","Silliest",
              "Microscopic","Massive","Voodoo","Hunks","Princess",
              "Honored","Heavy","French Fry","Greg","Uncanny",
              "OoOo Ah Ah","Mini","Timmy","Buttermilk","Felony",
              "Misdemeanor","Skippy","Big Boy","Beef",
              "99 cent Arizona Ice Tea","Sausage","Bouncy",
              "\"Can I Get uhhhh\""],
)
faker.add_provider(pet_first_provider)

pet_last_provider = DynamicProvider(
    provider_name="pet_last",
    elements=["McGee","the Throngler","Muncher","Boi","Fluffernutter",
              "Horseface","Thunderbottom","Nugget","Supreme","DOOM",
              "Churro","Dillier of Dallies","von Buscuit","McSquishface",
              "Niblits","Wimdy","Chungus","King of Entropy","Mahoraga",
              "the Chosen One","the Fallen","Cabbage","Egg","Thrower of Ups",
              "McCollum","Not a Dog","Bouncers","Dipstick","McFish",
              "the Indomitable Spirit","the Disgraced One",
              "the Hurty of Tummies"],
)
faker.add_provider(pet_last_provider)

# Define weights for pet species generation
species_weights = {
    "Cat": 3,
    "Dog": 3,
    "Duck": 1,
    "Fox": 1,
    "Frog": 0.5,
    "Raccoon": 0.5
}

# Define age and size classifications for different species
species_classifications = {
    "Cat": {
        "age": [(0, 1, AgeClass.BABY),
                (1, 2, AgeClass.ADOLESCENT),
                (2, 10, AgeClass.ADULT),
                (10, 20, AgeClass.OLD)],
        "size": [(0, 5, Size.EXTRA_SMALL),
                 (5, 10, Size.SMALL),
                 (10, 15, Size.MEDIUM),
                 (15, 20, Size.LARGE),
                 (20, 50, Size.EXTRA_LARGE)]
    },
    "Dog": {
        "age": [(0, 1, AgeClass.BABY),
                (1, 3, AgeClass.ADOLESCENT),
                (3, 8, AgeClass.ADULT),
                (8, 20, AgeClass.OLD)],
        "size": [(0, 10, Size.EXTRA_SMALL),
                 (10, 25, Size.SMALL),
                 (25, 50, Size.MEDIUM),
                 (50, 90, Size.LARGE),
                 (90, 200, Size.EXTRA_LARGE)]
    },
    "Duck": {
        "age": [(0, 0.17, AgeClass.BABY),  # 0-2 months
                (0.17, 0.5, AgeClass.ADOLESCENT),  # 2-6 months
                (0.5, 5, AgeClass.ADULT),
                (5, 12, AgeClass.OLD)],
        "size": [(0, 0.5, Size.EXTRA_SMALL),
                 (0.5, 1, Size.SMALL),
                 (1, 2, Size.MEDIUM),
                 (2, 3, Size.LARGE),
                 (3, 6, Size.EXTRA_LARGE)]
    },
    "Fox": {
        "age": [(0, 0.5, AgeClass.BABY),
                (0.5, 1, AgeClass.ADOLESCENT),
                (1, 5, AgeClass.ADULT),
                (5, 14, AgeClass.OLD)],
        "size": [(0, 2, Size.EXTRA_SMALL),
                 (2, 4, Size.SMALL),
                 (4, 6, Size.MEDIUM),
                 (6, 10, Size.LARGE),
                 (10, 20, Size.EXTRA_LARGE)]
    },
    "Frog": {
        "age": [(0, 0.5, AgeClass.BABY),
                (0.5, 1, AgeClass.ADOLESCENT),
                (1, 4, AgeClass.ADULT),
                (4, 10, AgeClass.OLD)],
        "size": [(0, 1, Size.EXTRA_SMALL),
                 (1, 2, Size.SMALL),
                 (2, 4, Size.MEDIUM),
                 (4, 6, Size.LARGE),
                 (6, 30, Size.EXTRA_LARGE)]
    },
    "Raccoon": {
        "age": [(0, 0.5, AgeClass.BABY),
                (0.5, 1, AgeClass.ADOLESCENT),
                (1, 3, AgeClass.ADULT),
                (3, 20, AgeClass.OLD)],
        "size": [(0, 1, Size.EXTRA_SMALL),
                 (1, 3, Size.SMALL),
                 (3, 7, Size.MEDIUM),
                 (7, 10, Size.LARGE),
                 (10, 15, Size.EXTRA_LARGE)]
    },
}

# Define breeds for each species
species_breeds = {
    "Cat": [
        "Siamese",
        "Persian",
        "Maine Coon",
        "Ragdoll",
        "Bengal",
        "Sphynx",
        "British Shorthair",
        "Scottish Fold",
        "Russian Blue",
        "American Shorthair",
    ],
    "Dog": [
        "Affenpinscher",
        "Beagle",
        "Boxer",
        "Bulldog",
        "Chihuahua",
        "Corgi",
        "Dachshund",
        "Doberman",
        "German Shepherd",
        "Bulldog",
        "Poodle",
        "Rottweiler",
        "Husky",
        "Samoyed",
        "Retriever",
        "Shiba",
        "Shihtzu",
    ],
    "Duck": [
        "Pekin Duck",
        "Muscovy Duck",
        "Moulard Duck",
        "Welsh Harleuin",
        "Silver Appleyard",
        "Aylesbury Duck",
        "Ancona Duck",
        "Rouen Duck",
        "Magpie Duck",
        "Buff Duck",
        "Golden 300 Hybrid Layer Duck",
    ],
    "Fox": [
        "Red Fox",
        "Fennec Fox",
        "Arctic Fox",
        "Cape Fox",
        "Bengal Fox",
        "Blanford's Fox",
        "Corsac Fox",
        "Kit Fox",
        "Tibetan Sand Fox",
        "Pale Fox",
        "Rüppell’s Fox",
        "Swift Fox",
        "Darwin’s Fox",
        "Culpeo Fox",
    ],
    "Frog": [
        "Horned Frog",
        "Gray Tree Frog",
        "Dart Frog",
        "Red-eyed Tree Frog",
        "American Bullfrog"
    ],
    "Raccoon": [
        "North American Raccoon",
        "Cozumel Raccoon",
        "Crab-Eating Raccoon",
    ],
}

# Event providers
species_names_provider = DynamicProvider(
    provider_name = "species_names",
    elements = list(species_classifications.keys())
)
faker.add_provider(species_names_provider)

event_actions_provider = DynamicProvider(
    provider_name = "event_actions",
    elements = ["Adoption", "Rescue", "Care", "Love", "Cuddle", "Training"]
)
faker.add_provider(event_actions_provider)

event_types_provider = DynamicProvider(
    provider_name = "event_types",
    elements = ["Day", "Festival", "Fair", "Extravaganza", "Celebration", "Gala", "BOGO"]
)
faker.add_provider(event_types_provider)

event_themes_provider = DynamicProvider(
    provider_name = "event_themes",
    elements = ["Superhero", "Pirate", "Space", "Tropical", "Vintage", "Magical", "Guilt-Trip"]
)
faker.add_provider(event_themes_provider)
