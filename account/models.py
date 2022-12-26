from django.db import models


def create_activation_code(self):
    import uuid
    code = str(uuid.uuid4())
    self.activation_code = code