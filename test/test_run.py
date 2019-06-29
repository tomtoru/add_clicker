import sys
import pathlib
current_dir = pathlib.Path(__file__).resolve().parent
sys.path.append( str(current_dir) + '/../' )

from api import click


# memo
# BPMと拍数を入力→ベースとなるクリックを作成
# 時間が入力されたらその分だけ↑を引き延ばす

if __name__ == "__main__":
    freq = 1024 # select [262, 294, 330, 349, 392, 440, 494, 523]

    # make click
    data = click.click.create_sin_wave(1, freq, 8000.0, 0.1)
    click.click.save_sound(data, 8000, 16, 1, "click.wav")
    # make mute
    data = click.click.create_sin_wave(0, freq, 8000.0, 0.3)
    click.click.save_sound(data, 8000, 16, 1, "mute.wav")

    # make single click
    click.click.join_waves("click.wav", "mute.wav", "single_click.wav")
    click.click.join_waves("click.wav", "mute.wav", "tmp_single_click.wav")

    file_name = "tmp_single_click.wav"
    for c in range(20):
        click.click.join_waves(file_name, "single_click.wav", str(c) + "_click.wav")
        file_name = str(c) + "_click.wav"


print("--end--")
