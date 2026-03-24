#  BHAVYA — Graph-Based Fraud Detection Engine

BHAVYA is a high-performance fraud detection system that models financial transactions as a **graph network** to detect suspicious patterns like circular money flow, structuring, and mule accounts.

---

##  Core Idea

Traditional systems analyze transactions individually. 
BHAVYA analyzes **relationships between transactions** using a graph database.

This allows detection of:
-  Circular transaction loops (A → B → C → A)
-  Structuring (₹48k–₹50k repeated transfers)
-  High-risk accounts (central nodes)

---

##  Tech Stack

### Backend (Ubuntu)
- **FastAPI** — API server
- **Memgraph** — Graph database
- **Docker** — Containerized DB
- **Pandas** — CSV processing

### Frontend (Windows)
- React + Vite (planned)
- Cytoscape.js (graph visualization)

---

##  Data Flow
