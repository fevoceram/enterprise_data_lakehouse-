from src.batch_pipeline import run_batch_pipeline
import yaml

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

run_batch_pipeline(
    input_path=config["paths"]["raw_data"],
    output_path=config["paths"]["processed_data"]
)
