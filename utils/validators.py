class Basic_Validators:
    def __init__(self):
        pass

    def has_no_space(self, text):
        return " " not in text.strip()
    
    def has_space(self, text):
        return " " in text.strip()

    def has_at_symbol(self, text):
        return "@" in text

    def has_valid_length(self, text, min_length, max_length):
        return min_length <= len(text) <= max_length

    def has_valid_interval(self, text, min_number, max_number):
        return min_number <= int(text) <= max_number

    def has_min_length(self, text, min_length):
        return len(text) >= min_length

    def has_only_digits(self, text):
        return text.isdigit()

    def has_only_letters(self, text):
        return text.isalpha()

    def has_more_than_8_letters(self, text):
        return sum(1 for char in text if char.isalpha()) > 8

    def has_more_than_8_caracters(self, text):
        return len(text) > 8

    def has_letter_and_digit(self, text):
        return any(char.isalpha() for char in text) and any(
            char.isdigit() for char in text
        )

    def has_special_character(self, text):
        special_characters = set('!@#$%^&*()_-+={}[]|\\:;"<>,.?/~')
        return any(char in special_characters for char in text)

    def check_space(self, text):
        while True:
            if self.has_no_space(text):
                return True, text
            else:
                text = input("(!) - Veuillez entrer un texte sans espace: ")

    def check_at_symbol(self, text):
        while True:
            if self.has_at_symbol(text):
                return True, text
            else:
                text = input("(!) - Veuillez entrer un email valide: ")

    def check_length(self, text, min_length, max_length):
        while True:
            if self.has_valid_length(text, min_length, max_length):
                return True, text
            else:
                text = input(
                    f"(!) - Veuillez entrer un texte de {min_length} à {max_length} caractères: "
                )

    def check_min_length(self, text, min_length):
        while True:
            if self.has_min_length(text, min_length):
                return True, text
            else:
                text = input(
                    f"(!) - Veuillez entrer un texte de {min_length} caractères minimum: "
                )

    def check_interval(self, text, min_number, max_number):
        while True:
            if text == "":
                break

            if self.has_only_digits(text):
                if self.has_valid_interval(text, min_number, max_number):
                    return True, text
                else:
                    text = input(
                        f"(!) - Veuillez entrer un nombre entre {min_number} et {max_number}: "
                    )
            else:
                text = input(
                    f"(!) - Veuillez entrer un nombre entre {min_number} et {max_number}: "
                )

    def check_digits(self, text):
        while True:
            if self.has_only_digits(text):
                return True, text
            else:
                text = input("(!) - Veuillez entrer uniquement des chiffres: ")

    def check_letters(self, text):
        while True:
            if self.has_only_letters(text):
                return True, text
            else:
                text = input(
                    "(!) - Veuillez entrer un texte avec uniquement des lettres: "
                )

    def check_no_letters(self, text):
        while True:
            if not self.has_only_letters(text):
                return True, text
            else:
                text = input("(!) - Veuillez entrer un texte sans lettre: ")

    def check_more_than_8_caracters(self, text):
        while True:
            if self.has_more_than_8_caracters(text):
                return True, text
            else:
                text = input(
                    f"(!) - Veuillez entrer un texte avec plus de 8 caractères: "
                )

    def check_letter_and_digit(self, text):
        while True:
            if self.has_letter_and_digit(text):
                return True, text
            else:
                text = input(
                    "(!) - Veuillez entrer un texte avec au moins une lettre et un chiffre: "
                )

    def check_min_length(self, text, min_length):
        while True:
            if self.has_min_length(text, min_length):
                return True, text
            else:
                text = input(
                    f"(!) - Veuillez entrer un texte avec au moins {min_length} caractères: "
                )

    def check_special_character(self, text):
        while True:
            if self.has_special_character(text):
                return True, text
            else:
                text = input(
                    "(!) - Veuillez entrer un texte avec au moins un caractère spécial: "
                )

    def check_no_special_character(self, text):
        while True:
            if not self.has_special_character(text):
                return True, text
            else:
                text = input("(!) - Veuillez entrer un texte sans caractère spécial: ")

    def check_empty(self, text):
        if text == "":
            return True, text
        return False, text


class Validators(Basic_Validators):
    def __init__(self):
        super().__init__()

    def remove_white_spaces(self, text):
        return text.strip(" ")

    def validator_simple_text(
        self, input_name: str, input_display: str, is_update: bool
    ):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name

                val_1 = self.check_no_special_character(input_name)
                # val_2 = self.check_letters(val_1[1])

                validators = [val_1[0]]

                if all(validators):
                    return val_1[1]

            # Classic check
            val_1 = self.check_no_special_character(input_name)
            # val_2 = self.check_letters(val_1[1])

            validators = [val_1[0]]

            if all(validators):
                return val_1[1]

    def validator_email(self, input_name: str, input_display: str, is_update: bool):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name
                val_1 = self.check_space(input_name)
                val_2 = self.check_at_symbol(val_1[1])
                val_3 = self.check_length(val_2[1], 5, 50)

                validators = (val_1[0], val_2[0], val_3[0])

                if all(validators):
                    return val_3[1]

            # Classic check
            val_1 = self.check_space(input_name)
            val_2 = self.check_at_symbol(val_1[1])
            val_3 = self.check_length(val_2[1], 5, 50)

            validators = (val_1[0], val_2[0], val_3[0])

            if all(validators):
                return val_3[1]

    def validator_password(self, input_name: str, input_display: str, is_update: bool):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name
                val_1 = self.check_space(input_name)
                val_2 = self.check_more_than_8_caracters(val_1[1])
                val_3 = self.check_letter_and_digit(val_2[1])
                val_4 = self.check_special_character(val_3[1])

                validators = [val_1[0], val_2[0], val_3[0], val_4[0]]

                if all(validators):
                    return val_4[1]

            # Classic check
            val_1 = self.check_space(input_name)
            val_2 = self.check_more_than_8_caracters(val_1[1])
            val_3 = self.check_letter_and_digit(val_2[1])
            val_4 = self.check_special_character(val_3[1])

            validators = [val_1[0], val_2[0], val_3[0], val_4[0]]

            if all(validators):
                return val_4[1]

    def validator_phone(self, input_name: str, input_display: str, is_update: bool):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name
                val_1 = self.check_space(input_name)
                val_2 = self.check_digits(val_1[1])
                val_3 = self.check_length(val_2[1], 0, 13)

                validators = [val_1[0], val_2[0], val_3[0]]

                if all(validators):
                    return val_3[1]

            # Classic check
            val_1 = self.check_space(input_name)
            val_2 = self.check_digits(val_1[1])
            val_3 = self.check_length(val_2[1], 0, 13)

            validators = [val_1[0], val_2[0], val_3[0]]

            if all(validators):
                return val_3[1]

    def validator_id(self, input_name: str, input_display: str, is_update: bool):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name
                val_1 = self.check_space(input_name)
                val_2 = self.check_digits(val_1[1])

                validators = [val_1[0], val_2[0]]

                if all(validators):
                    return val_2[1]

            # Classic check
            val_1 = self.check_space(input_name)
            val_2 = self.check_digits(val_1[1])

            validators = [val_1[0], val_2[0]]

            if all(validators):
                return val_2[1]

    def validator_role(self, input_name: str, input_display: str, is_update: bool):
        while True:
            input_name = input(f"{input_display}")
            input_name = self.remove_white_spaces(input_name)

            # Check if is update and if input is empty
            if is_update:
                if input_name == "":
                    return input_name
                val_1 = self.check_space(input_name)
                val_2 = self.check_digits(val_1[1])
                val_3 = self.check_length(val_2[1], 0, 1)
                val_4 = self.check_interval(val_3[1], 1, 3)

                validators = [val_1[0], val_2[0], val_3[0], val_4[0]]

                if all(validators):
                    return val_4[1]

            # Classic check
            val_1 = self.check_space(input_name)
            val_2 = self.check_digits(val_1[1])
            val_3 = self.check_length(val_2[1], 0, 1)
            val_4 = self.check_interval(val_3[1], 1, 3)

            validators = [val_1[0], val_2[0], val_3[0], val_4[0]]

            if all(validators):
                return val_4[1]

    def validator_home(self, input_name: str, input_display: str, user: object):
        input_name = input(f"{input_display}")
        input_name = self.remove_white_spaces(input_name)

        while True:
            val_1 = self.check_space(input_name)
            val_2 = self.check_digits(val_1[1])
            val_3 = self.check_length(val_2[1], 0, 1)

            if user.is_superuser is True:
                val_4 = self.check_interval(val_3[1], 1, 5)
            else:
                if user.role_id == 1:
                    val_4 = self.check_interval(val_3[1], 1, 4)
                elif user.role_id == 2:
                    val_4 = self.check_interval(val_3[1], 1, 4)
                elif user.role_id == 3:
                    val_4 = self.check_interval(val_3[1], 1, 5)
                else:
                    raise Exception("Unknown role, please contact the administrator")

            validators = [val_1[0], val_2[0], val_3[0], val_4[0]]

            if all(validators):
                return val_4[1]

    def validator_menu_choice(self, interval_min, interval_max):
        choice = input("Votre choix : ")

        while True:
            val_1 = self.check_digits(choice)
            val_2 = self.check_interval(val_1[1], interval_min, interval_max)

            validators = [val_1[0], val_2[0]]

            if all(validators):
                return val_2[1]
