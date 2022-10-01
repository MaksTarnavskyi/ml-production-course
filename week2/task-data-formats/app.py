import logging
from pathlib import Path
from typing import Optional

import hydra
import numpy as np
import pandas as pd
import yaml
from omegaconf import DictConfig, OmegaConf
from src.measurement import (
    check_folder,
    generate_dataset,
    measure_file_size,
    measure_load_time,
    measure_save_time,
)
from src.visualization import generate_plot

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s] {%(name)s:%(lineno)d} %(levelname)s - %(message)s",
)
LOGGER = logging.getLogger("app")


@hydra.main(version_base="1.2", config_path="configs", config_name="default")
def app(conf: DictConfig) -> None:
    conf_str = yaml.dump(OmegaConf.to_object(conf), sort_keys=False)
    LOGGER.info("Config:\n" + conf_str)

    df = generate_dataset(
        n_rows=conf.n_rows, n_columns=conf.n_columns, fill_value=conf.fill_value
    )
    check_folder(conf.data_folder)
    check_folder(conf.metric_folder)
    check_folder(conf.plot_folder)
    perform_time_measurement(conf, operation="save", data_df=df)
    perform_size_measurement(conf)
    perform_time_measurement(conf, operation="load")


def perform_time_measurement(
    conf: DictConfig,
    operation: str,
    data_df: Optional[pd.DataFrame] = None,
):
    LOGGER.info(f"Perform {operation} measurement")

    measured_time_values = []
    for file_format in conf.file_formats:
        execution_times = []
        for _ in range(conf.n_iterations):
            if operation == "save":
                seconds = measure_save_time(
                    data_df, conf.data_folder, conf.file_name, file_format
                )
            elif operation == "load":
                seconds = measure_load_time(
                    conf.data_folder, conf.file_name, file_format
                )
            else:
                raise ValueError("Unknown operation")
            execution_times.append(seconds)
        mean_execution_time = np.mean(execution_times)
        measured_time_values.append(
            {"file_format": file_format, "execution_time_sec": mean_execution_time}
        )
        LOGGER.info(
            f"Mean {operation} time for {file_format} = {round(mean_execution_time, 3)} seconds"
        )

    measurements_df = pd.DataFrame(measured_time_values)
    measurements_df = measurements_df.sort_values(
        by="execution_time_sec", ascending=False
    ).round(3)
    measurements_df.to_json(
        Path(conf.metric_folder, f"measurements_for_{operation}.json"), orient="records"
    )

    generate_plot(
        data=measurements_df,
        x_column="execution_time_sec",
        y_column="file_format",
        title=f"Execution time in seconds for {operation}",
        save_path=f"{conf.plot_folder}/chart-{operation}-measurement.png",
    )
    LOGGER.info(f"Plot for {operation} is generated")


def perform_size_measurement(conf: DictConfig):
    LOGGER.info("Perform file size measurement")

    measured_size_values = []
    for file_format in conf.file_formats:
        file_size_in_megabytes = measure_file_size(
            conf.data_folder, conf.file_name, file_format
        )
        measured_size_values.append(
            {"file_format": file_format, "size_megabytes": file_size_in_megabytes}
        )
        LOGGER.info(
            f"File size for {file_format} = {round(file_size_in_megabytes,3)} MB"
        )
    measurements_df = pd.DataFrame(measured_size_values)
    measurements_df = measurements_df.sort_values(
        by="size_megabytes", ascending=False
    ).round(3)
    measurements_df.to_json(
        Path(conf.metric_folder, "measurements_for_file_size.json"), orient="records"
    )

    generate_plot(
        data=measurements_df,
        x_column="size_megabytes",
        y_column="file_format",
        title="File size in megabytes",
        save_path=f"{conf.plot_folder}/chart-file-size.png",
    )
    LOGGER.info("Plot for file size is generated")


if __name__ == "__main__":
    app()
