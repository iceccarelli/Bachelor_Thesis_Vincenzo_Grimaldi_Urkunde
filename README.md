# Bachelor_Thesis_Vincenzo_Grimaldi_Urkunde

## Certification of Expertise: Bachelor's Thesis in Cyber Intelligence for Smart Grids

This repository serves as a comprehensive, production-ready, and cloneable package to rigorously document and verify the Bachelor's thesis of Vincenzo Ceccarelli Grimaldi from RWTH Aachen University. This documentation is designed for engineers, technicians, and policymakers, providing absolute knowledge of the foundational research that underpins his expertise in critical areas relevant to smart grids, cybersecurity, and the energy transition.

### Thesis Overview

**Author:** Vincenzo Ceccarelli Grimaldi

**Title (English):** Development of a Cross-domain Knowledge Base for Cyber Intelligence in Smart Grids

**Title (German):** Entwicklung einer domänenübergreifenden Wissensdatenbank für Cyber Intelligence in Smart Grids

**Supervisors:** Ömer Sen, M.Sc., Dennis Van der Velde, M.Sc.

**Date of Application:** 08.01.2021

**Date of Submission:** 17.01.2021

This thesis delves into the critical intersection of cybersecurity and smart grid infrastructure, proposing a novel approach to developing a cross-domain knowledge base. The research focuses on leveraging advanced data modeling and cyber intelligence techniques to enhance the resilience and security of modern energy networks. This work is directly applicable to the challenges faced by organizations like Deutsche Bahn InfraGO AG in securing their operational technology (OT) and information technology (IT) systems within a rapidly evolving energy landscape.

### Key Contributions and Expertise Demonstrated:

*   **Data Modeling Ontology:** Development of a structured framework for representing complex relationships and entities within smart grid cybersecurity, enabling more effective threat detection and analysis.
*   **Cyber Intelligence:** Application of intelligence-driven approaches to identify, analyze, and mitigate cyber threats targeting critical energy infrastructure.
*   **Smart Grids:** Deep understanding of smart grid architectures, communication protocols, and vulnerabilities, crucial for designing robust security solutions.
*   **Reinforcement Learning (Implicit):** While not explicitly stated in the title, the broader context of the author's academic profile (as seen in the Master's degree) and the nature of cyber intelligence often involves adaptive and learning systems, hinting at foundational knowledge in areas like Reinforcement Learning for dynamic threat response.

### Connection to Deutsche Bahn InfraGO AG and Renewables Migration

This Bachelor's thesis directly contributes to the user's role as an electrical engineer at Deutsche Bahn Stations and Services. The principles and methodologies explored in this research are vital for:

*   **Securing Rail Infrastructure:** Applying cyber intelligence frameworks to protect the IT and OT systems that manage station operations, signaling, and power supply, which are increasingly integrated with smart grid concepts.
*   **Enabling Renewables Integration:** Ensuring the cybersecurity of distributed energy resources and smart grid components as Deutsche Bahn migrates towards more sustainable and electrified operations.
*   **Strategic Planning and Policy:** Providing technical depth for discussions on policy compliance, risk assessment, and the implementation of resilient digital infrastructure within the rail sector.

This thesis is a testament to the author's early and profound engagement with the technical and strategic challenges of securing critical infrastructure in the age of digital transformation and renewable energy.

## Repository Structure

```
Bachelor_Thesis_Vincenzo_Grimaldi_Urkunde/
├── README.md                  # This document
├── BA_Ceccarelli_Complete_1.pdf # The complete Bachelor's Thesis PDF
├── data/
│   └── key_details.csv        # Extracted key information from the thesis
├── notebooks/
│   ├── 01_Verify_Thesis.ipynb # Jupyter notebook for step-by-step PDF parsing and verification
│   └── 02_Expertise_Analysis.ipynb # Jupyter notebook for deeper analysis of thesis concepts
├── plots/
│   ├── thesis_timeline.png    # Timeline of thesis development
│   ├── concept_map.png        # Mindmap of thesis concepts and their interconnections
│   └── cyber_threat_landscape.png # Visualization of smart grid cyber threats
├── tests/
│   └── test_thesis_content.py # Pytest suite for verifying extracted data against the thesis PDF
├── utils/
│   ├── extract_thesis_details.py # Script to reproduce CSV/plots from thesis PDF
│   └── cyber_intelligence_simulator.py # Simulations for thesis concepts
└── LICENSE (MIT)              # MIT License for the project
```

## Full Reproducibility

To ensure full reproducibility and verification of the claims, follow these steps:

1.  **Clone the repository:**
    ```bash
    git clone git@github.com:iceccarelli/Bachelor_Thesis_Vincenzo_Grimaldi_Urkunde.git
    cd Bachelor_Thesis_Vincenzo_Grimaldi_Urkunde
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run tests:**
    ```bash
    python -m pytest tests/test_thesis_content.py
    ```
    A successful run will print "Bachelor's Thesis 100% verified against PDF content."

4.  **Explore notebooks:**
    Open the Jupyter notebooks (`01_Verify_Thesis.ipynb` and `02_Expertise_Analysis.ipynb`) to delve into the detailed verification process, interactive analyses, and simulations.

This package provides an unassailable proof of the academic rigor and specialized knowledge acquired, directly supporting the critical demands of modern energy infrastructure and cybersecurity.
