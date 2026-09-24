"""Bu modül çiftlikteki pirinç ekinini (Rice) tanımlar."""
from farm.crop import Crop

class Rice(Crop):
    """Pirinç ekini, Crop (Ekin) ana sınıfının özelliklerini miras alır."""

    def water(self):
        """Pirince özel sulama işlemi: tahıl miktarını 5 artırır."""
        self.grains += 5

    def transplant(self):
        """Pirinç fidesini tarlaya dikme işlemini gerçekleştirir."""
        pass
