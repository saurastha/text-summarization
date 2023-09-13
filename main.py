from textSummarization.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from textSummarization.pipeline.stage_02_data_validation import DataValidationTrainingPipeline
# from textSummarization.pipeline.stage_03_data_transformation import DataTransformationTrainingPipeline
# from textSummarization.pipeline.stage_04_model_training import ModelTrainingPipeline
# from textSummarization.pipeline.stage_05_model_evaluation import ModelEvaluationPipeline
from textSummarization.logging import logger

STAGE_NAME = 'Data Ingestion Stage'

try:
    logger.info(f'>>>> stage {STAGE_NAME} started <<<<')
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f'>>>> stage {STAGE_NAME} completed <<<<\n\nx===========x')

except Exception as e:
    logger.exception(e)
    raise e