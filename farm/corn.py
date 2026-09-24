"""Bu modül çiftlikteki mısır ekinini (Corn) tanımlar."""

class Corn:
    """Mısır ekininin büyüme ve olgunlaşma durumunu takip eden sınıf."""
    def __init__(self):
        """Başlangıç tahıl sayısını sıfır olarak ayarlar."""
        self.grains = 0

    def water(self):
        """Sulama işlemi yapıldığında tahıl miktarını 10 artırır."""
        self.grains += 10

    def ripe(self):
        """Tahıl sayısı 15 veya üzerindeyse mısırın olgunlaştığını belirtir."""
        return self.grains >= 15
