# PatchCore Novelty Detector

PatchCore is a machine learning system for **visual novelty detection**. Given a set of normal (defect-free) images,
it learns what "normal" looks like and flags any new image that deviates from that learned normality.

It requires **no novel examples** during training only normal images are needed. This makes it well suited for
industrial inspection scenarios where defects are rare or hard to collect in advance.

---

## How It Works

The system operates in two phases: **training** and **inference**.

```
FIT                               PREDICT
─────────────────────────         ─────────────────────────
Normal images                     New image
      │                                  │
      ▼                                  ▼
Extract patch embeddings      Extract patch embeddings
      │                                  │
      ▼                                  ▼
Build memory bank             Compare to memory bank
      │                                  │
      ▼                                  ▼
Calibrate threshold           Novelty score + heatmap
```

---

## Training Phase

### Step 1 — Feature Extraction

Each training image is passed through a pre-trained neural network (backbone). The network extracts a rich
representation of each spatial region of the image , these are called **patch embeddings**.

Each image produces a grid of embeddings. The result is a large collection of vectors
representing all the normal visual patterns seen during training.

### Step 2 — Memory Bank Construction

All patch embeddings from all training images are collected into a **memory bank**. This bank represents the full
distribution of normal appearance.

Since storing every single patch would be expensive, a **coreset subsampling** step reduces the bank to a compact
representative subset while preserving coverage of the normal distribution. The goal is maximum coverage with
minimum size.

### Step 3 — Index Building

The reduced memory bank is loaded into a fast nearest-neighbour index. This structure allows very efficient
similarity search at inference time.

### Step 4 — Threshold Calibration

A separate set of defect-free images (calibration set) is passed through the system. Each image receives a
novelty score. The **decision threshold** is set at a chosen percentile of these scores. Images scoring above
the threshold at inference time are flagged as novel.


---

## Inference Phase

### Step 1 — Feature Extraction

The input image is processed by the same backbone used during training, producing patch embeddings.

### Step 2 — Nearest-Neighbour Search

For each patch embedding of the input image, the system finds its nearest neighbour in the memory bank.
The distance to that neighbour measures how unusual that patch is : a large distance means the patch does
not resemble anything seen during training.

### Step 3 — Score Aggregation

The per-patch distances are aggregated into a single **image-level novelty score**. This makes the score
sensitive to localised novel regions without being dominated by the many normal patches.

### Step 4 — Decision

The image-level novelty score is compared to the calibrated threshold:

```
novelty score > threshold  →  NOVEL   (label = 1)
novelty score ≤ threshold  →  NORMAL  (label = 0)
```

### Step 5 — Heatmap Generation

The per-patch distances are spatially arranged and upsampled back to the original image resolution, producing
a **novelty heatmap** that highlights which regions contributed most to the novelty score.

---

## Key Concepts

### Patch Embeddings

Instead of representing the whole image with a single vector, PatchCore works at the **patch level**.Each
spatial region of the image gets its own embedding. This allows the system to localise novel regions rather
than just classify the whole image as normal or novel.

### Memory Bank

The memory bank is the system's learned representation of normality. It is a collection of vectors, each
describing a normal visual pattern. At inference time, any input patch that is far from all memory bank
entries is considered novel.

### Novelty Score

The novelty score of an image reflects the degree of deviation from the learned normal distribution.
A patch that looks completely different from anything seen during training produces a high distance,
which propagates into a high image-level novelty score.

### Decision Threshold

The threshold separates normal images from novel ones. It is calibrated automatically from the calibration
set at training time. Images with a novelty score above the threshold are flagged as novel at inference time.


