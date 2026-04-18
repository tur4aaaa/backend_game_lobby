import logging
from database.dp import create_player, get_player


def main():
    logging.info("Game is started")

    create_player("alex")

    new_player = get_player(1)
    logging.info("Player from DB :", new_player)


if __name__ == "__main__":
    main()
