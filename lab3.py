class Set:
    """
    Клас для представлення і виконання операцій над множинами.
    """

    def __init__(self, elements):
        """
        Конструктор класу.

        Args:
            elements: Множина елементів.
        """

        self.elements = set(elements)

    def __eq__(self, other):
        """
        Перевіряє рівність двох множин.

        Args:
            other: Інша множина.

        Returns:
            True, якщо множини рівні, False в іншому випадку.
        """

        return self.elements == other.elements

    def is_subset(self, other):
        """
        Перевіряє, чи є перша множина підмножиною другої.

        Args:
            other: Інша множина.

        Returns:
            True, якщо перша множина є підмножиною другої, False в іншому випадку.
        """

        return self.elements.issubset(other.elements)

    def to_bit_string(self):
        """
        Перетворює множину в бітовий рядок.

        Returns:
            Бітовий рядок, що представляє множину.
        """

        return "".join(["1" if i in self.elements else "0" for i in range(max(self.elements) + 1)])

    def union(self, other):
        """
        Повертає об'єднання двох множин.

        Args:
            other: Інша множина.

        Returns:
            Отримана множина.
        """

        return Set(self.elements | other.elements)

    def intersection(self, other):
        """
        Повертає перетин двох множин.

        Args:
            other: Інша множина.

        Returns:
            Отримана множина.
        """

        return Set(self.elements & other.elements)

    def difference(self, other):
        """
        Повертає різницю двох множин.

        Args:
            other: Інша множина.

        Returns:
            Отримана множина.
        """

        return Set(self.elements - other.elements)

    def symmetric_difference(self, other):
        """
        Повертає симетричну різницю двох множин.

        Args:
            other: Інша множина.

        Returns:
            Отримана множина.
        """

        return Set(self.elements ^ other.elements)


def main():
    """
    Основна функція програми.
    """

    # Введення множин

    A = input("Введіть множину A: ").split()
    B = input("Введіть множину B: ").split()

    # Створення множин

    A = Set(list(map(int, A)))
    B = Set(list(map(int, B)))

    # Виконання операцій над множинами

    print("Об'єднання:", A.union(B).elements)
    print("Перетин:", A.intersection(B).elements)
    print("Різниця:", A.difference(B).elements)
    print("Симетрична різниця:", A.symmetric_difference(B).elements)


if __name__ == "__main__":
    main()
