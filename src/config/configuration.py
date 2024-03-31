from src.constants import *
from src.utils.common import *
from src.entity.config_entity import (DataIngestionConfig, 
                                      DataValidationConfig, 
                                      DataTransformationConfig,
                                      ModelTrainerConfig)

class ConfigurationManager:
    def __init__(self, 
                 config_filepath = CONFIG_FILE_PATH,
                 schema_filepath = SCHEMA_FILE_PATH,
                 params_filepath = PARAMS_FILE_PATH):
        
        self.config = read_yaml(config_filepath)
        self.schema = read_yaml(schema_filepath)
        self.params = read_yaml(params_filepath)
    
        create_directories([self.config.artifacts_root])
    
    
    def get_data_ingestion_config(self) -> DataIngestionConfig:
        initialize = self.config.data_ingestion 

        create_directories([initialize.root_dir])
        
        data_ingestion_config = DataIngestionConfig(
            root_dir= initialize.root_dir,
            source_URL= initialize.source_URL,
            local_data_file= initialize.local_data_file,
            unzip_dir= initialize.unzip_dir
        )

        return data_ingestion_config
    

    def get_data_validation_config(self) -> DataValidationConfig:
        config = self.config.data_validation
        schema = self.schema.COLUMNS

        create_directories([config.root_dir])

        data_validation_config = DataValidationConfig(
            root_dir= config.root_dir,
            unzip_data_dir= config.unzip_data_dir,
            STATUS_FILE= config.STATUS_FILE,
            all_schema= schema
        )

        return data_validation_config
    

    def get_data_transformation_config(self) -> DataTransformationConfig:
        config = self.config.data_transformation
        create_directories([config.root_dir])

        data_transformation_config = DataTransformationConfig(
            root_dir= config.root_dir,
            data_path= config.data_path,
            preprocessing_data = config.preprocessing_data,
            train = config.train,
            test = config.test
        )

        return data_transformation_config
    
    def get_model_trainer_config(self) -> ModelTrainerConfig:
        config = self.config.model_trainer
        params = self.params.RandomForestClassifier
        schema = self.schema.TARGET_COLUMN

        create_directories([config.root_dir])

        model_trainer_config = ModelTrainerConfig(
            root_dir= config.root_dir,
            train_data_path= config.train_data_path,
            test_data_path= config.test_data_path,
            model_name = config.model_name,
            n_estimators= params.n_estimators,
            random_state= params.random_state,
            target_column= schema.name
            
        )
        
        return model_trainer_config 
    