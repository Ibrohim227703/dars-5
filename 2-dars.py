import p


class product:
    def __init__(self, image, is_liked, created_at, updated_at):
        self.image = image
        self.is_liked = is_liked
        self.created_at = created_at
        self.updated_at = updated_at


P = product()
p.save()
