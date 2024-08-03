import random
import string


class Utils:

    #
    @staticmethod
    def generate_random_lowercase_string(min_length, max_length):
        """
            Generates a random string containing lowercase letters, digits, and underscores.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_lowercase + string.digits + '_'
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username

    @staticmethod
    def generate_random_string(min_length, max_length):
        """
            Generates a random string containing uppercase and lowercase letters, digits, and underscores.
            Args:
                min_length (int): The minimum length of the generated string.
                max_length (int): The maximum length of the generated string.
            Returns:
                str: A randomly generated string.
        """
        characters = string.ascii_letters + string.digits + '_'
        username = ''.join(random.choice(characters) for _ in range(random.randint(min_length, max_length)))
        return username
