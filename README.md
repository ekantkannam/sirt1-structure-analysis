# SIRT1 Longevity Protein: Structural Analysis

## Overview
This repository contains an automated pipeline for predicting and analyzing the structural dynamics of SIRT1 (Sirtuin 1), a critical protein targeted in anti-aging and longevity research. 

## Methodology
1. **Structural Prediction:** AlphaFold2 was utilized via Google Colab GPUs to compute the 3D structure of the 747-amino-acid Human SIRT1 sequence.
2. **Confidence Mapping:** The resulting `.json` prediction scores were parsed to map pLDDT confidence metrics across the sequence length.
3. **IDR Identification:** Intrinsically Disordered Regions (IDRs) areas of high flexibility crucial for SIRT1's interaction with longevity pathways were mathematically isolated where pLDDT < 50.

## Results
The generated mapping visually isolates the structured catalytic core of the protein from its highly flexible N- and C-terminal tails, providing a foundation for targeted drug-discovery and binding-site analysis.
