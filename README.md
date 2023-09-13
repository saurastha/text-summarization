# text-summarization

## Overview

This project aims to fine-tune a pre-existing model for text summarization using a specific dataset. Text summarization is the process of generating a concise and coherent summary of a longer text while preserving its essential information. In this repository, we focus on fine-tuning a deep learning model for abstractive text summarization.

## File Structure

The project's file structure is organized as follows:

1. **config.yaml**: This configuration file stores directories for downloaded data, preprocessed data, trained models, and checkpoints. Users can modify these directories to suit their specific needs.

2. **params.yaml**: This file contains model parameters, allowing users to customize model settings according to their requirements.

3. **requirements.txt**: The list of dependencies required for the project can be found in this file. You can install them using<br> `pip install -r requirements.txt`.

4. **setup.py**: This script is responsible for creating Python packages for the project, making it easy to distribute and install.

5. **treeleaf_speech_lib/**:
   - **components/**: Contains modular components for data processing, data validation, data transformation and model training.
   - **config/**: Houses configuration-related code and settings.
   - **constants/**: Stores constants used throughout the project.
   - **entity/**: Defines data structures or entities used in the project.
   - **logging/**: Handles logging and provides useful debugging information.
   - **pipeline/**: Contains code for orchestrating data processing and training workflows.
   - **utils/**: Houses utility functions used across the project.

6. **main.py**: This script acts as the entry point and binds together all the code components. Users can run the project using<br> `python main.py`.

## Usage

To use the "text-summarization" for fine-tuning the Hugging face model, follow these steps:

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/saurastha/text-summarization.git
   ```

2. **Install Requirements**:  
   Install the required Python packages listed in the requirements.txt file using pip:
   ```bash
   pip install -r requirements.txt
   ```

3. **Modify Configuration**:  
   Edit the config.yaml and params.yaml files to specify the directories, model parameters, and other settings according to your specific project requirements.

4. **Run the Code**:  
    Execute the project using the main script:
    ```bash
    python main.py
    ```