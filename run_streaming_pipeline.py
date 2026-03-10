from src.streaming_pipeline import run_streaming_pipeline
import yaml

# Load config
with open("config/config.yaml") as f:
    config = yaml.safe_load(f)

run_streaming_pipeline(
    input_path=config["paths"]["streaming_input"],
    output_path=config["paths"]["processed_data"]
)
