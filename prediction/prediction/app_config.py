from environs import Env

env = Env()

training_service_config = {
    "host": env("TRAINING_SERVICE_HOST"),
    "port": env("TRAINING_SERVICE_PORT"),
    "api_train_path": env("TRAINING_SERVICE_API_TRAIN_PATH"),
    "timeout": env.int("TRAINING_REQUESTS_TIMEOUT"),
    "appinsights_key": env("APP_INSIGHTS_INSTRUMENTATION_KEY")
}

mlflow_models_mapping = env.json('MLFLOW_MODELS_MAPPING')
service_config = {
    "service_name": env("SERVICE_NAME"),
    "log_level": env.log_level("LOG_LEVEL", "INFO"),
    "port": env.int("PORT", 80)
}
