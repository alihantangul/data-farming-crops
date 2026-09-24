# pylint: disable=too-few-public-methods


"""Bu modül çiftlikteki genel ekin (Crop) şablonunu tanımlar."""

class Crop:
    """Tüm ekinlerin ortak özelliklerini barındıran ana sınıf."""

    def __init__(self):
        """Başlangıç tahıl sayısını sıfır olarak ayarlar."""
        self.grains = 0

    def water(self):
        """Sulama işlemi yapıldığında tahıl miktarını 10 artırır."""
        self.grains += 10

    def ripe(self):
        """Tahıl sayısı 15 veya üzerindeyse ekinin olgunlaştığını belirtir."""
        return self.grains >= 15
