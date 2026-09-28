from __future__ import annotations

from pathlib import Path

import matplotlib.image as mpimg
import matplotlib.pyplot as plt
from matplotlib.offsetbox import AnnotationBbox, OffsetImage
from matplotlib.widgets import TextBox

from .probability import probability_dataframe


def _render_dashboard(ax, df, row_index: int) -> None:
    ax.clear()
    row = df.iloc[row_index]
    bars = row[["Box 1", "Box 2", "Box 3"]]
    bars.plot(ax=ax, kind="bar", rot=0)
    ax.set_title("Box distribution")
    ax.set_ylabel("Proportion")


def _render_coin_history(ax, df, row_index: int, column_prefix: str) -> None:
    ax.clear()
    row = df.iloc[row_index]
    series = row[[f"{column_prefix}: Gold", f"{column_prefix}: Silver"]]
    series.plot(ax=ax, kind="bar", rot=0)
    ax.set_title(f"{column_prefix} coin distribution")
    ax.set_ylabel("Proportion")


def _render_conditionals(ax, df, row_index: int) -> None:
    ax.clear()
    ax.plot(df.index[: row_index + 1], df["Gold"].iloc[: row_index + 1], label="Gold")
    ax.plot(df.index[: row_index + 1], df["Silver"].iloc[: row_index + 1], label="Silver")
    ax.set_title("Probability the second coin matches the first")
    ax.set_xlabel("Iteration")
    ax.set_ylabel("Probability")
    ax.legend()


def _render_image_panel(ax) -> None:
    image_path = Path(__file__).resolve().parent.parent / "Bertrand_Box_Paradox.jpg"
    ax.set_xticks([])
    ax.set_yticks([])
    if image_path.exists():
        arr = mpimg.imread(image_path)
        imagebox = OffsetImage(arr, zoom=0.3)
        ax.add_artist(AnnotationBbox(imagebox, (0.5, 0.5)))
    ax.set_title("Bertrand's Box")
    ax.axis("off")


def build_plot(iterations: int = 10) -> tuple[plt.Figure, list[plt.Axes]]:
    df = probability_dataframe(iterations)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))

    _render_image_panel(axes[0, 0])
    _render_coin_history(axes[0, 1], df, iterations - 1, "First Coin")
    _render_coin_history(axes[1, 1], df, iterations - 1, "Second Coin")
    _render_dashboard(axes[1, 0], df, iterations - 1)
    _render_conditionals(axes[0, 2], df, iterations - 1)
    _render_conditionals(axes[1, 2], df, iterations - 1)

    return fig, axes


def main() -> None:
    initial_df = probability_dataframe(10)
    fig, axes = plt.subplots(2, 3, figsize=(14, 8))

    _render_image_panel(axes[0, 0])
    _render_coin_history(axes[0, 1], initial_df, initial_df.index[-1], "First Coin")
    _render_coin_history(axes[1, 1], initial_df, initial_df.index[-1], "Second Coin")
    _render_dashboard(axes[1, 0], initial_df, initial_df.index[-1])
    _render_conditionals(axes[0, 2], initial_df, initial_df.index[-1])
    _render_conditionals(axes[1, 2], initial_df, initial_df.index[-1])

    def submit(iterations_text: str) -> None:
        try:
            iterations = max(1, min(1000, int(iterations_text)))
        except ValueError:
            return

        updated_df = probability_dataframe(iterations)
        last_index = updated_df.index[-1]

        for ax in axes.flat:
            ax.clear()

        _render_image_panel(axes[0, 0])
        _render_coin_history(axes[0, 1], updated_df, last_index, "First Coin")
        _render_coin_history(axes[1, 1], updated_df, last_index, "Second Coin")
        _render_dashboard(axes[1, 0], updated_df, last_index)
        _render_conditionals(axes[0, 2], updated_df, last_index)
        _render_conditionals(axes[1, 2], updated_df, last_index)

        fig.canvas.draw_idle()

    axbox = plt.axes([0.5, 0.001, 0.10, 0.065])
    text_box = TextBox(axbox, "Iterations (1 to 1000)", initial="10", label_pad=0.25)
    text_box.on_submit(submit)

    plt.show()


if __name__ == "__main__":
    main()
