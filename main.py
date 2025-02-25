import argparse

from model import GridGameModel, TicTacToeWinConditions, WildTicTacToeWinConditions, NotaktoWinConditions, Pick15WinConditions
from view import View
from controller import Controller

def str_list(line: str) -> list[str]:
    return line.split(',')

def setup_parser():
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--size', type=int, default=3)
    parser.add_argument('-p', '--player_count', type=int, default=2)
    parser.add_argument(
        '--variant',
        choices=["tictactoe", "notakto", "wild", "pick15"],
        required=True,
    )
    parser.add_argument('-s', '--symbols', type=str_list, default=[])

    return parser


def make_model(args: argparse.Namespace):
    match args.variant:
        case "tictactoe":
            return GridGameModel(
                grid_size=args.size,
                player_count=args.player_count,
                player_symbols=args.symbols,
                win_condition = TicTacToeWinConditions(),
            )

        case "wild":
            return GridGameModel(
                grid_size=args.size,
                player_count=args.player_count,
                player_symbols=args.symbols,
                win_condition = WildTicTacToeWinConditions(),
            )

        case "notakto":
            return GridGameModel(
                grid_size=args.size,
                player_count=args.player_count,
                player_symbols=args.symbols,
                win_condition = NotaktoWinConditions(),
            )

        case "pick15":
            return GridGameModel(
                grid_size=args.size,
                player_count=args.player_count,
                player_symbols=args.symbols,
                win_condition = Pick15WinConditions(),
            )

def main():
    parser = setup_parser()
    args = parser.parse_args()

    model = make_model(args)
    view = View()
    controller = Controller(model, view)

    controller.start_game()


if __name__ == '__main__':
    main()
