---
language:
- en
license: mit
tags:
- grammar error check
- generated_from_trainer
datasets:
- cola
metrics:
- f1
model-index:
- name: results
  results:
  - task:
      name: Text Classification
      type: text-classification
    dataset:
      name: cola
      type: cola
    metrics:
    - name: F1
      type: f1
      value: 0.8342420937840785
---

# Model Card for my-cool-model

<!-- Provide a quick summary of what the model is/does. -->

#  Table of Contents

1. [Model Details](#model-details)
2. [Uses](#uses)
3. [Bias, Risks, and Limitations](#bias-risks-and-limitations)
4. [Training Details](#training-details)
5. [Evaluation](#evaluation)
6. [Model Examination](#model-examination-optional)
7. [Environmental Impact](#environmental-impact)
8. [Technical Specifications](#technical-specifications-optional)
9. [Citation](#citation-optional)
10. [Glossary](#glossary-optional)
11. [More Information](#more-information-optional)
12. [Model Card Authors](#model-card-authors-optional)
13. [Model Card Contact](#model-card-contact)
14. [How To Get Started With the Model](#how-to-get-started-with-the-model)


# Model Details

## Model Description

<!-- Provide a longer summary of what this model is. -->

this model does this and that

- **Developed by:** Nate Raw
- **Shared by [optional]:** [More Information Needed]
- **Model type:** [More Information Needed]
- **Language(s) (NLP):** en
- **License:** mit
- **Related Models [optional]:** [More Information Needed]
    - **Parent Model [optional]:** [More Information Needed]
- **Resources for more information:** https://github.com/huggingface/huggingface_hub

# Uses

<!-- Address questions around how the model is intended to be used, including the foreseeable users of the model and those affected by the model. -->

## Direct Use

<!-- This section is for the model use without fine-tuning or plugging into a larger ecosystem/app. -->

[More Information Needed]

## Downstream Use [optional]

<!-- This section is for the model use when fine-tuned for a task, or when plugged into a larger ecosystem/app -->

[More Information Needed]

## Out-of-Scope Use

<!-- This section addresses misuse, malicious use, and uses that the model will not work well for. -->

[More Information Needed]

# Bias, Risks, and Limitations

<!-- This section is meant to convey both technical and sociotechnical limitations. -->

[More Information Needed]

## Recommendations

<!-- This section is meant to convey recommendations with respect to the bias, risk, and technical limitations. -->

Users (both direct and downstream) should be made aware of the risks, biases and limitations of the model. More information needed for further recomendations.

# Training Details

## Training Data

<!-- This should link to a Data Card, perhaps with a short stub of information on what the training data is all about as well as documentation related to data pre-processing or additional filtering. -->

[More Information Needed]

## Training Procedure [optional]

<!-- This relates heavily to the Technical Specifications. Content here should link to that section when it is relevant to the training procedure. -->

### Training hyperparameters

The following hyperparameters were used during training:
- learning_rate: 5e-05
- train_batch_size: 32
- eval_batch_size: 32
- seed: 42
- optimizer: Adam with betas=(0.9,0.999) and epsilon=1e-08
- lr_scheduler_type: linear
- num_epochs: 5

### Training results

| Training Loss | Epoch | Step | Validation Loss | F1     | F0.5   |
|:-------------:|:-----:|:----:|:---------------:|:------:|:------:|
| 0.6184        | 0.5   | 100  | 0.5980          | 0.8342 | 0.7588 |
| 0.6075        | 1.0   | 200  | 0.5971          | 0.8342 | 0.7588 |
| 0.6153        | 1.49  | 300  | 0.5966          | 0.8342 | 0.7588 |
| 0.6049        | 1.99  | 400  | 0.5969          | 0.8342 | 0.7588 |
| 0.6046        | 2.49  | 500  | 0.5972          | 0.8342 | 0.7588 |
| 0.6068        | 2.99  | 600  | 0.5962          | 0.8342 | 0.7588 |
| 0.6064        | 3.48  | 700  | 0.5970          | 0.8342 | 0.7588 |
| 0.597         | 3.98  | 800  | 0.5969          | 0.8342 | 0.7588 |
| 0.6043        | 4.48  | 900  | 0.5996          | 0.8342 | 0.7588 |
| 0.5947        | 4.98  | 1000 | 0.5989          | 0.8342 | 0.7588 |


### Framework versions

- Transformers 4.22.1
- Pytorch 1.12.1
- Datasets 2.4.0
- Tokenizers 0.12.1

### Preprocessing

[More Information Needed]

### Speeds, Sizes, Times

<!-- This section provides information about throughput, start/end time, checkpoint size if relevant, etc. -->

[More Information Needed]

# Evaluation

<!-- This section describes the evaluation protocols and provides the results. -->

## Testing Data, Factors & Metrics

### Testing Data

<!-- This should link to a Data Card if possible. -->

[More Information Needed]

### Factors

<!-- These are the things the evaluation is disaggregating by, e.g., subpopulations or domains. -->

[More Information Needed]

### Metrics

<!-- These are the evaluation metrics being used, ideally with a description of why. -->

[More Information Needed]

## Results

This model is a fine-tuned version of [prajjwal1/bert-tiny](https://huggingface.co/prajjwal1/bert-tiny) on the cola dataset.
It achieves the following results on the evaluation set:
- Loss: 0.5972
- F1: 0.8342
- F0.5: 0.7588

# Model Examination [optional]

<!-- Relevant interpretability work for the model goes here -->

[More Information Needed]

# Environmental Impact

<!-- Total emissions (in grams of CO2eq) and additional considerations, such as electricity usage, go here. Edit the suggested text below accordingly -->

Carbon emissions can be estimated using the [Machine Learning Impact calculator](https://mlco2.github.io/impact#compute) presented in [Lacoste et al. (2019)](https://arxiv.org/abs/1910.09700).

- **Hardware Type:** [More Information Needed]
- **Hours used:** [More Information Needed]
- **Cloud Provider:** [More Information Needed]
- **Compute Region:** [More Information Needed]
- **Carbon Emitted:** [More Information Needed]

# Technical Specifications [optional]

## Model Architecture and Objective

[More Information Needed]

## Compute Infrastructure

[More Information Needed]

### Hardware

[More Information Needed]

### Software

[More Information Needed]

# Citation [optional]

<!-- If there is a paper or blog post introducing the model, the APA and Bibtex information for that should go in this section. -->

**BibTeX:**

[More Information Needed]

**APA:**

[More Information Needed]

# Glossary [optional]

<!-- If relevant, include terms and calculations in this section that can help readers understand the model or model card. -->

[More Information Needed]

# More Information [optional]

[More Information Needed]

# Model Card Authors [optional]

[More Information Needed]

# Model Card Contact

[More Information Needed]

# How to Get Started with the Model

Use the code below to get started with the model.

<details>
<summary> Click to expand </summary>

[More Information Needed]

</details>