class Snake:
    """A dangerous and/or harmless serpent."""
    pass


class Cobra(Snake):
    """Definitely dangerous, yup."""
    """KEVINS LOUD EDIT"""
    def bite(self, other):
        """Deliver a dose of venom."""
        pass

    
class BoaConstrictor(Snake):
    """This one gives really good hugs."""
    
    def squeeze(self, other):
        """Give a hug."""
        from bear import hug
        hug(self, other, kill=True)

    
class BoatConstrictor(BoaConstrictor):
    """Loose snakes sink ships?"""
    print("Abandon ship! Hugging snake on the loose!")

