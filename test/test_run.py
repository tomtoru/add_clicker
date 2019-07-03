import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from api import click


if __name__ == "__main__":
    freq = 1024 # select [262, 294, 330, 349, 392, 440, 494, 523]
    click = click.Click(1, freq, 8000.0)

    # data = click.create_single_click(0.5)
    # data = 4 * data
    # click.save_sound(data, 16, 1, "OK_single_click.wav")

    click.create_click(180, 210, 4)


print("--end--")
