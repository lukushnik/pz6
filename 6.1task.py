# Клас інтерфейсу
class TextComponent:
    def render(self) -> str:
        pass

# Конкретний компонент
class SimpleTextComponent(TextComponent):
    def render(self) -> str:
        return "Simple Text"

# Декоратор
class TextDecorator(TextComponent):
    def __init__(self, wrapped: TextComponent):
        self._wrapped = wrapped

    def render(self) -> str:
        return self._wrapped.render()

# Конкретний декоратор
class BoldTextDecorator(TextDecorator):
    def render(self) -> str:
        original_text = super().render()
        return f"<b>{original_text}</b>"

# Ще один конкретний декоратор
class ItalicTextDecorator(TextDecorator):
    def render(self) -> str:
        original_text = super().render()
        return f"<i>{original_text}</i>"
