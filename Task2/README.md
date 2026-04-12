
#  LangChain Deep Technical Blog – Implementation

##  Overview

This repository contains the implementation for the **Gen-AI Internship Assignment: Deep Technical Blog on LangChain**.

The objective of this project is to understand and demonstrate how **LLM-powered applications** are built using modular components such as prompts, chains, memory, and tools.

---

##  Objectives

* Understand the architecture of LLM-based systems
* Implement core concepts behind LangChain
* Build a simple end-to-end pipeline using transformer models
* Demonstrate real-world use of Generative AI components

---

## 🛠️ Technologies Used

* Python
* HuggingFace Transformers
* FAISS (for vector search)
* Jupyter Notebook / Google Colab

---

##  Key Concepts Implemented

###  1. LLM (Language Model)

A lightweight HuggingFace model (`distilgpt2`) is used to simulate text generation.

---

###  2. Prompting

Custom prompt templates are used to guide model responses.

---

###  3. Chains

Sequential processing of input → prompt → model → output is implemented manually to simulate LangChain pipelines.

---

###  4. Memory

A simple conversational memory is implemented using accumulated chat history to simulate context retention.

---

###  5. Tools

A basic calculator tool is implemented to demonstrate external tool usage within AI workflows.

---

###  6. Document Loading

Text files are loaded and processed to simulate document ingestion.

---

###  7. Vector Search (Retrieval)

A simple similarity-based retrieval system is implemented to mimic vector database behavior.

---

###  8. End-to-End Pipeline

A complete pipeline demonstrates how user input flows through the system to generate output.

---

##  Architecture

```
User Input
   ↓
Prompt Template
   ↓
Language Model (LLM)
   ↓
Processing (Chain / Memory / Tools)
   ↓
Output
```

---

##  Important Note

Due to rapid updates and dependency conflicts in LangChain, the core concepts were implemented manually using HuggingFace transformers.

This approach ensures:

* Stable execution
* Clear understanding of internal workings
* Faster performance without API dependencies

---

##  Features

* No API key required
* Lightweight and fast execution
* Fully runnable in Google Colab
* Covers all major LangChain concepts

---

##  How to Run

1. Open the notebook in Google Colab
2. Install dependencies:

   ```bash
   pip install transformers faiss-cpu
   ```
3. Run all cells sequentially

---

## 📁 Project Structure

```
├── Task2.ipynb   # Main notebook
├── README.md              
```

---

##  Learning Outcomes

* Understanding LLM pipelines
* Implementing modular AI systems
* Simulating LangChain architecture
* Handling real-world development constraints

---

##  Conclusion

This project demonstrates how modern AI applications can be built by combining prompts, models, memory, and tools into a structured pipeline.

It provides a strong foundation for building scalable **Generative AI applications**.

---

##  Submission Links

* Blog: https://medium.com/@laharivungarala/langchain-architecture-components-and-real-world-applications-570ea78599b9



