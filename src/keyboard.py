from src.item import Item


class MixinChangeLang:
    _language = 'EN'

    @property
    def language(self):
        return self._language

    def change_lang(self):
        if self._language == 'RU':
            self._language = 'EN'
        else:
            self._language = 'RU'

        return self


class Keyboard(Item, MixinChangeLang):
    pass
