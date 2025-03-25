# LLM Beginner Project: Tokenization and Text Generation

**A beginner-friendly project exploring the foundations of Large Language Models (LLMs). This project focuses on tokenization, text generation using GPT-2, and adopting Test-Driven Development (TDD) practices.**

---

## 🚀 Features

- **Tokenization**: Learn how text is converted into tokens that LLMs can understand.
- **Text Generation**: Generate creative text from input prompts using GPT-2.
- **Test-Driven Development (TDD)**: Implement robust test cases using `pytest`.
- **Pre-trained Models**: Leverage Hugging Face Transformers for efficient NLP workflows.

---

## 📂 Project Structure

 src/
  ├── text_generator.py 
  # Main script for text generation 
  ├── tests/ 
  │ ├── test_tokenizer.py 
  # Tests for tokenizer functionality 
  │ ├── test_text_generator.py 
  # Tests for text generation 
  ├── requirements.txt
 # Dependency file 
 ├── README.md
 # This file

 
---

## 📖 Getting Started

### Prerequisites
1. Install **Python 3.9+**.
2. Install **Git**.
3. Install a virtual environment tool like `venv`.

---

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/<YourUsername>/LLM-101.git
   cd LLM-101

2. Set up and activate a virtual environment:
    ```bash
    python -m venv llm_project_env
    llm_project_env\Scripts\activate

3. Install dependencies:
    ```bash
    pip install -r requirements.txt


## 🚦 How to Run the Project

1. Run the Text Generator Script:

    bash
    python src\text_generator.py
    This script generates text based on input prompts using GPT-2.

2. Run Tests: Use pytest to ensure everything is working correctly:

    bash
    pytest tests/

## 🧪 Experimentation and Next Steps

  - Explore tokenization using different text samples in test_tokenizer.py.

  - Modify text_generator.py to experiment with longer or creative text prompts.

  - Fine-tune GPT-2 or try other pre-trained models from Hugging Face.

## ⚙️ Technologies Used

  - Python 3.9
  - PyTorch
  - Hugging Face Transformers
  - pytest
  - Virtual Environments

## 📄 License
  This project is licensed under the MIT License - see the LICENSE file for details.

## ✨ Acknowledgments
  Special thanks to Hugging Face for providing accessible tools for natural language processing and to the open-source community for their contributions to AI development.