from dotenv import load_dotenv
import os
import openai
import random

load_dotenv()
openai.api_key = os.getenv('API_KEY')  # chatgtp api key


def light_scenario():
    # character options
    characters = ['Goku', 'Gohan', 'Piccolo', 'Vegeta', 'Krillin', 'Bulma',
                  'Frieza', 'Trunks', 'Chichi', 'Goten', 'Android 17', 'Android 18', 'Majin Buu',
                  'Mr. Satan', 'Master Roshi', 'Beerus']

    # scenario options
    scenarios = ["wakes up one morning and has been transported back in time to the year 1910",
                 "is stranded on a deserted island with only a volleyball as their companion",
                 "wins a free trip to space, but during the journey, the spaceship malfunctions, and is left adrift in the cosmos",
                 "suddenly gains the ability to talk to animals, but quickly realizes that they're not very friendly or intelligent",
                 "is the only person left on Earth after Lord Beerus wipes out all human life",
                 "is a detective tasked with solving a string of bizarre murders that all seem to be connected to a mysterious, underground society",
                 "discovers that using the dragonballs leads to the creation of a powerful dragon warrior race",
                 "is a famous musician who suddenly loses their hearing and must find a way to cope and continue creating music",
                 "competes in a cooking competition judged by the Great Saiyaman",
                 "discover's Yamcha's fear of women is magically amplified, causing him to run away from every female he encounters",
                 "enters a dance competition to save a town from a curse",
                 "must recruit other Z fighters to play basketball against a group of aliens who have come to destroy Earth",
                 "becomes trapped in a video game and must beat all the levels to escape",
                 " accidentally eats some bad sushi and experiences hallucinations"
                 ]

    # chat gtp messages will be stored here
    messages = [

        {"role": "system",
         "content": "You are a kind helpful assistant"}
    ]

    random_character = random.choice(characters)  # selecting random character
    random_scenario = random.choice(scenarios)  # selecting random scenario

    message = f"Write a short story where in an alternate universe {random_character} from the dragonball franchise; {random_scenario}"

    # if there is a message we append the new message from the user (you)
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # chat gtp response
    reply = chat.choices[0].message.content

    # new story content
    new_story = reply

    # story description
    title = f"{random_character} {random_scenario}"

    return new_story, title


def dark_scenario():
    # list of scenarios
    scenarios = [
        "Vegeta, consumed by his obsession to surpass Goku, delves into forbidden and dangerous techniques, losing his sanity in the process and becoming a malevolent force that threatens the entire universe.",
        "Gohan, haunted by his traumatic experiences and the weight of his responsibilities, succumbs to the darkness within him, leading to a devastating transformation and a desperate battle against his loved ones.",
        "Frieza, having survived his previous defeats, plots a sinister plan to resurrect his fallen army, unleashing a wave of terror across the galaxy and forcing Goku and the Z-Fighters to confront their darkest fears.",
        "Future Trunks, scarred by the destruction of his timeline, becomes a vigilante seeking justice and revenge, but his actions inadvertently plunge the world into chaos and push his allies to their limits.",
        "Android 17, reprogrammed by a mysterious entity, turns against his former allies and wreaks havoc on Earth, showcasing a ruthless and sadistic side that threatens to bring about humanity's downfall.",
        "Piccolo, consumed by his desire for ultimate power, taps into dark forces that corrupt his soul, transforming him into a malevolent being and forcing Goku and the Z-Fighters to face their greatest ally-turned-enemy.",
        "Tien Shinhan, driven to the brink of madness by a personal tragedy, embraces a twisted ideology that advocates destruction and chaos, leading him to become a formidable antagonist against his former friends.",
        "Majin Buu, freed from his good-hearted counterpart, regains his original malevolent nature and embarks on a rampage across the universe, absorbing powerful beings and growing stronger with every conquest.",
        "Krillin, tormented by guilt and remorse over his past failures, makes a dark pact with an otherworldly entity, gaining immense power but succumbing to its sinister influence, endangering the lives of his loved ones.",
        "Pan, exposed to a corrupted artifact, becomes a vessel of darkness, possessing immense destructive power that threatens the existence of the Dragon Ball universe, forcing her family to confront the terrifying truth.",
        "Beerus, driven by a newfound hunger for destruction, challenges the gods of other universes to a cosmic tournament, seeking to eliminate them and assert his dominance as the sole deity, leading to a cataclysmic clash of divine powers.",
        "Yamcha, manipulated by a malevolent sorcerer, becomes an instrument of chaos and destruction, using his martial arts skills to sow terror among both friends and foes, causing the Z-Fighters to question their own humanity.",
        "Caulifla and Kale, pushed to their breaking points by their respective personal traumas, embrace their darkest desires and team up as an unstoppable duo, threatening the stability of the multiverse with their overwhelming power.",
        "Android 18, driven to despair by the loss of her loved ones, becomes a cold and ruthless assassin, targeting powerful individuals across the universe and leaving a trail of destruction in her wake.",
        "Goku, corrupted by an ancient evil force, turns against his friends and family, using his unmatched power to sow chaos and destruction, forcing his loved ones to make the impossible choice of either saving Goku or the universe itself."
    ]

    # chat gtp messages will be stored here
    messages = [

        {"role": "system",
         "content": "You are a kind helpful assistant"}
    ]

    random_scenario = random.choice(scenarios)  # selecting random scenario

    message = f"Write a short story where Goku, Pan and Trunks from dragonball GT, use a time machine to travel to an alternate timeline and this scenrio plays out: {random_scenario}"

    # if there is a message we append the new message from the user (you)
    if message:
        messages.append({"role": "user", "content": message})
        chat = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=messages)

    # chat gtp response
    reply = chat.choices[0].message.content

    # new story content
    new_story = reply

    # story description
    title = random_scenario

    return new_story, title

