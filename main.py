from database.dp import create_player, get_player


def main():
    print("Game is started")

    create_player("alex")

    new_player = get_player(1)
    print("Player from DB :", new_player)


if __name__ == "__main__":
    main()
