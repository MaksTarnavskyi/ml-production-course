import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

sns.set_theme(style="darkgrid")
sns.set_color_codes("muted")
sns.despine(bottom=True)


def generate_plot(
    data: pd.DataFrame,
    x_column: str,
    y_column: str,
    title: str,
    save_path: str,
    resolution_dpi: int = 300,
    width: int = 7,
    height: int = 5,
):
    _, ax = plt.subplots(figsize=(width, height))
    ax = sns.barplot(x=x_column, y=y_column, data=data, color="b")
    _ = ax.bar_label(ax.containers[0])
    ax.set(title=title)
    plt.savefig(save_path, dpi=resolution_dpi)
