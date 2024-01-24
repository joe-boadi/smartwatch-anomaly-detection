_(Still under scrutiny and build, raise an issue for recommendations)_

# IoT Vulnerabilities: Case of Smart Watch
## Table of  Content
- [Introduction](#introduction)
- [Scope of Project](#scope-of-project)
- [Project folder structure](#project-folder-structure)
- [Setting Up and Getting Started](#setting-up-and-getting-started)

## Introduction 
There are intrusion detection system (IDS) applications that can be installed on smartwatches. These applications are designed to detect and prevent unauthorized access to smartwatches and other IoT devices. A comprehensive survey of the latest IDSs designed for the IoT model is available in the Journal of Cloud Computing. The article provides deep insight into the IoT architecture, emerging security vulnerabilities, and their relation to the layers of the IoT architecture. It also presents key considerations for the development of such IDSs as a future outlook.

- [Intrusion detection systems for IoT-based smart ... - SpringerOpen. ](https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-018-0123-6)
- [A critical review of intrusion detection systems in the internet of .... ](https://cybersecurity.springeropen.com/articles/10.1186/s42400-021-00077-7)
- [Intrusion Detection System (IDS): Types, Techniques, and Applications. ](https://www.knowledgehut.com/blog/security/intrusion-detection-system)

## Some examples of intrusion detection system (IDS) applications that can be installed on smartwatches:

1. **Suricata**: A network-based IDS software that operates at the application layer for greater visibility.
2. **Zeek**: A network monitor and network-based intrusion prevention system.
3. **Security Onion**: A network monitoring and security tool made up of elements pulled in from other free tools.

- [12 Best Intrusion Detection System (IDS) Software 2024 - Comparitech. ](https://www.comparitech.com/net-admin/network-intrusion-detection-tools/)
- [Intrusion detection systems for IoT-based smart ... - SpringerOpen. ](https://journalofcloudcomputing.springeropen.com/articles/10.1186/s13677-018-0123-6)
- [IoT-based smart environment using intelligent intrusion detection system. ](https://link.springer.com/article/10.1007/s00500-021-06028-1)


## Scope of Project
Developing an algorithm to identify authentication anomaly detection using AI/ML in support of intrusion detection for smartwatches. Although, there are already several research papers and articles that discuss the use of AI/ML in intrusion detection systems (IDS) for IoT devices, including smartwatches. These IDSs are designed to detect and prevent unauthorized access to smartwatches and other IoT devices.

### Steps to consider:

1. **Data Collection**: Collecting data is the first step in developing an AI/ML-based IDS. You will need to collect data on the normal behavior of smartwatches and the types of attacks that they are vulnerable to.
    - ### Data History:
        - The [ADRepository-Anomaly-detection-datasets](https://github.com/GuansongPang/anomaly-detection-datasets) is a continuously updated collection of popular real-world datasets used for anomaly detection which is forked to this project.

        - The repository contains datasets that are converted from imbalanced classification datasets, while others contain real anomalies. The datasets are available in various formats, including tabular data (categorical and numerical data), time series data, graph data, image data, and video data.

    - __This project uses [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/) to scrape the data (if applicable).__

2. **Feature Extraction**: Once you have collected the data, you will need to extract features that can be used to train your AI/ML model. These features should be relevant to the types of attacks that you are trying to detect. __[PCA](https://www.machinelearningplus.com/machine-learning/principal-components-analysis-pca-better-explained/) Recommended__

3. **Model Training**: After extracting the features, you will need to train your AI/ML model using the collected data. You can use various machine learning algorithms such as decision trees, random forests, and neural networks to train your model and this project uses 
    - __[Random Forest](https://www.ibm.com/topics/random-forest) to train your model to detect authentication anomalies__

4. **Testing and Validation**: Once you have trained your model, you will need to test and validate it using a separate dataset. This will help you determine the accuracy of your model and identify any areas that need improvement.
    -  __[k-fold cross-validation](https://machinelearningmastery.com/k-fold-cross-validation/) to test and validate__

- [Securing the Digital World: Protecting smart infrastructures and .... ](https://arxiv.org/pdf/2401.01342)
- [A data-driven approach for intrusion and anomaly detection using ....]( https://link.springer.com/article/10.1007/s00500-023-09037-4)
- [An Embedded AI-Based Smart Intrusion Detection System for ... - Springer. ](https://link.springer.com/chapter/10.1007/978-3-031-23201-5_2)

## Project folder structure
**Proposed Folder structure**

```project/
├── data/
│   ├── raw/
│   ├── processed/
│   └── interim/

├── models/

├── notebooks/

├── src/
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── utils/
│   └── visualization/

├── tests/
├── README.md
├── requirements.txt
└── setup.py
```
_However you can structure according to your preference._

## Setting Up and Getting Started
_(Intentionally left blank)_