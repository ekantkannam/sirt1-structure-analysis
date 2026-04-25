import json
import matplotlib.pyplot as plt
import numpy as np
import os

# Configuration
SCORES_FILE = "data/scores.json"
OUTPUT_PLOT = "results/sirt1_idr_map.png"
IDR_THRESHOLD = 50.0  # pLDDT < 50 strongly indicates Intrinsic Disorder

def map_longevity_idrs():
    try:
        if not os.path.exists(SCORES_FILE):
            print(f"Data file not found at {SCORES_FILE}. Waiting for AlphaFold results...")
            return

        with open(SCORES_FILE, 'r') as f:
            data = json.load(f)
            
        # ColabFold stores confidence scores in the 'plddt' array
        plddt_scores = np.array(data.get('plddt', []))
        
        if len(plddt_scores) == 0:
            print("No pLDDT scores found in JSON.")
            return

        residues = np.arange(1, len(plddt_scores) + 1)
        
        # Plotting
        plt.figure(figsize=(12, 6))
        
        # Main score line
        plt.plot(residues, plddt_scores, color='#2c3e50', linewidth=1.5, label='AlphaFold pLDDT Score')
        
        # Highlight IDRs (Intrinsically Disordered Regions)
        idr_mask = plddt_scores < IDR_THRESHOLD
        plt.fill_between(residues, plddt_scores, 0, where=idr_mask, color='#e74c3c', alpha=0.5, label='Predicted IDR (Disordered Region)')
        
        plt.axhline(y=IDR_THRESHOLD, color='#7f8c8d', linestyle='--', linewidth=1)
        
        plt.title('SIRT1 (Longevity Protein) Structural Confidence & IDR Mapping', fontsize=14, fontweight='bold')
        plt.xlabel('Amino Acid Residue Position', fontsize=12)
        plt.ylabel('AlphaFold Confidence (pLDDT)', fontsize=12)
        plt.ylim(0, 100)
        plt.legend(loc='lower right')
        plt.grid(axis='y', linestyle='--', alpha=0.7)
        plt.tight_layout()
        
        plt.savefig(OUTPUT_PLOT, dpi=300)
        print(f"Analysis complete. IDR map saved to {OUTPUT_PLOT}")

    except Exception as e:
        print(f"Execution error: {e}")

if __name__ == "__main__":
    map_longevity_idrs()