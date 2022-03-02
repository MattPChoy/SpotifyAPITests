
class Secrets:
    def __init__(self, secrets_fp):
        self.secret_contents = []
        with open(secrets_fp, "r") as secrets:
            self.secret_contents = secrets.read()

        # Now, parse the secrets
        self.secret_contents = self.secret_contents.split('\n')
        # Remove lines starting with '#'
        self.secret_contents = \
            [s for s in self.secret_contents if len(s) > 0 and (s.strip())[0] != '#']

    def get_secrets(self):
        # Use list comprehension to return a copy of the list
        return [s for s in self.secret_contents]
