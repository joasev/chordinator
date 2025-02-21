import pygame
from config.settings import Settings
from src.core.game_runner import GameRunner
from src.core.flashcard_game import FlashcardGame


def main():
    pygame.init()
    settings = Settings()
    settings.load_settings()

    #midi = MidiInput()
    #keyboard = KeyboardHandler()
    game_type = FlashcardGame(settings)
    #renderer = Renderer(game)
    ##Game(game, midi, keyboard, renderer).run()
    GameRunner(game_type).run()


if __name__ == "__main__":
    main()





