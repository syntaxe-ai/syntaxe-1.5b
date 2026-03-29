# ⚡ Syntaxe AI

> **Assistant de code open-source, local, gratuit — propulsé par les meilleurs LLMs.**  
> TypeScript · Python · Backend JS/Python · Architecture · Docker

![Version](https://img.shields.io/badge/version-1.0.0-22d3ee?style=flat-square)
![License](https://img.shields.io/badge/license-MIT-10b981?style=flat-square)
![Stack](https://img.shields.io/badge/stack-FastAPI%20%2B%20React%20%2B%20Ollama-f59e0b?style=flat-square)
![Models](https://img.shields.io/badge/models-DeepSeek%20R1%20%7C%20Llama%203.1%20%7C%20Mistral%20%7C%20CodeLlama-a855f7?style=flat-square)

---

## 🚀 Présentation

**Syntaxe AI** est un assistant de programmation complet que tu héberges toi-même.  
Zéro abonnement. Zéro API key. Tes données restent sur ton serveur.

### Ce que tu peux faire

- 💬 **Chat avec génération de code** — TypeScript, Python, JS, SQL, Docker
- ▶ **Exécution de code en live** — Python, JavaScript, TypeScript directement dans l'interface
- 🔄 **Multi-modèles** — Switch en un clic entre DeepSeek R1, Llama 3.1, Mistral, CodeLlama
- 📝 **Historique de conversations** — Sessions persistantes, plusieurs conversations en parallèle
- 🎯 **Spécialisé backend** — Architecture REST, FastAPI, Express, Fastify, bases de données

---

## 🧠 Comparaison des IA de code

Voici comment Syntaxe AI se positionne face aux solutions du marché :

| IA | Prix | Vie privée | Code qualité | TypeScript | Backend | Raisonnement | Open-source |
|----|------|-----------|-------------|------------|---------|-------------|-------------|
| **Syntaxe AI (Syntaxe 1.5b)** | 🟢 Gratuit | 🟢 100% local | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ |
| **Claude Sonnet (Anthropic)** | 🔴 Payant | 🟡 Cloud | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ❌ |
| **ChatGPT-4o (OpenAI)** | 🔴 Payant | 🟡 Cloud | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ❌ |
| **GitHub Copilot** | 🟡 $10/mois | 🟡 Cloud | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ❌ |
| **DeepSeek Chat (web)** | 🟢 Gratuit | 🔴 Serveurs CN | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | 🟡 Partiel |
| **Mistral Le Chat** | 🟢 Gratuit | 🟡 Cloud EU | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐⭐ | 🟡 Partiel |
| **Ollama seul (CLI)** | 🟢 Gratuit | 🟢 100% local | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐ | ⭐⭐⭐⭐⭐ | ✅ |

### Pourquoi Syntaxe AI plutôt que les autres ?

**vs Claude (Anthropic)** — Claude est probablement la meilleure IA de code disponible aujourd'hui, notamment sur les projets TypeScript complexes et l'architecture. Mais il est payant et tes données transitent par les serveurs d'Anthropic. Syntaxe AI te donne 80–90% de ses capacités, 100% local, 100% gratuit.

**vs ChatGPT-4o** — GPT-4o est bon, mais les hallucinations de librairies inexistantes sont fréquentes en code. Syntaxe 1.5b raisonne étape par étape avant de répondre, ce qui réduit drastiquement ces erreurs.

**vs GitHub Copilot** — Copilot est excellent pour l'autocomplétion en IDE. Syntaxe AI est meilleur pour la génération de fichiers entiers, l'architecture, et les explications détaillées. Les deux sont complémentaires.

**vs DeepSeek Chat (web)** — Inspire du modèle mais entraîné par Syntaxe, mais leurs serveurs sont en Chine. Tes données de code (clés API, logique métier) y transitent. Avec Syntaxe AI, tout reste chez toi.

---

## 📊 Benchmarks des modèles disponibles

| Modèle | HumanEval | MBPP | RAM | Vitesse | Idéal pour |
|--------|-----------|------|-----|---------|-----------|
| **DeepSeek R1 7B** | 79% | 74% | 5GB | Moyen | Algorithmes, debug, architecture |
| **Llama 3.1 8B** | 72% | 68% | 6GB | Rapide | Usage général, explication de code |
| **Mistral 7B** | 68% | 64% | 5GB | Très rapide | Prototypage rapide, Q&A |
| **CodeLlama 7B** | 76% | 71% | 5GB | Moyen | Complétion de code, refactoring |

> **HumanEval** : benchmark Python de génération de fonctions (OpenAI).  
> **MBPP** : Mostly Basic Python Problems — 374 problèmes de programmation.

---

## 🛠 Stack technique

```
syntaxe-ai/
├── backend/              # API Python
│   ├── main.py           # FastAPI — routes, streaming SSE, sessions
│   └── requirements.txt  # fastapi, uvicorn, httpx
├── frontend/             # Interface React
│   ├── src/
│   │   ├── App.tsx       # App complète (TypeScript strict)
│   │   └── main.tsx      # Entry point
│   ├── package.json
│   ├── tsconfig.json
│   └── vite.config.ts
└── README.md
```

**Backend**
- [FastAPI](https://fastapi.tiangolo.com/) — API async ultra-rapide
- [Ollama](https://ollama.com/) — Serveur LLM local
- [httpx](https://www.python-httpx.org/) — Client HTTP async pour le streaming
- Server-Sent Events (SSE) pour le streaming temps réel

**Frontend**
- [React 18](https://react.dev/) + [TypeScript](https://www.typescriptlang.org/) strict
- [Vite](https://vitejs.dev/) — Build ultra-rapide
- Syntax highlighting custom (zéro dépendance)
- Exécution de code via API backend

---

## ⚙ Installation

### Prérequis

- Python 3.11+
- Node.js 20+
- 6GB de RAM libre minimum
- Linux / macOS / WSL2

### 1. Installer Ollama

```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 2. Télécharger DeepSeek R1 7B

```bash
ollama pull deepseek-r1:7b
# Optionnel — autres modèles
ollama pull llama3.1:8b
ollama pull mistral:7b
ollama pull codellama:7b
```

### 3. Lancer le backend

```bash
cd backend
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000 --reload
```

### 4. Lancer le frontend

```bash
cd frontend
npm install
npm run dev
# → http://localhost:3000
```

---

## 🖥 Déploiement VPS

### RAM recommandée par modèle

| Modèle | RAM VPS minimum |
|--------|----------------|
| DeepSeek R1 7B | 8GB |
| Llama 3.1 8B | 10GB |
| Mistral 7B | 8GB |
| CodeLlama 7B | 8GB |

### Lancer en production avec systemd

```bash
# /etc/systemd/system/syntaxe-ai.service
[Unit]
Description=Syntaxe AI Backend
After=network.target

[Service]
WorkingDirectory=/root/syntaxe-ai/backend
ExecStart=uvicorn main:app --host 0.0.0.0 --port 8000 --workers 2
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
```

```bash
systemctl enable syntaxe-ai
systemctl start syntaxe-ai
```

### Nginx reverse proxy

```nginx
server {
    listen 80;
    server_name syntaxe.mondomaine.com;

    location /api/ {
        proxy_pass http://localhost:8000/;
        proxy_http_version 1.1;
        proxy_set_header Connection '';
        proxy_buffering off;           # ← important pour le streaming SSE
        chunked_transfer_encoding on;
    }

    location / {
        root /root/syntaxe-ai/frontend/dist;
        try_files $uri /index.html;
    }
}
```

---

## 🔌 API Reference

### POST `/chat`
Envoie un message, reçoit une réponse en streaming SSE.

```typescript
const res = await fetch("http://localhost:8000/chat", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    message: "Génère un middleware Express en TypeScript avec JWT",
    session_id: "uuid-optionnel",
    model: "deepseek-r1:7b"
  })
})
```

**Réponse SSE :**
```
data: {"type": "session_id", "session_id": "abc-123"}
data: {"type": "text", "content": "Voici..."}
data: {"type": "text", "content": " le middleware"}
data: {"type": "done"}
```

### POST `/execute`
Exécute du code Python, JavaScript ou TypeScript.

```typescript
const res = await fetch("http://localhost:8000/execute", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    code: "print('Hello, Syntaxe AI!')",
    language: "python"
  })
})
// → { stdout, stderr, exit_code, success }
```

### GET `/models`
Liste les modèles disponibles et leurs métadonnées.

### GET `/sessions` · POST `/session` · DELETE `/session/{id}`
Gestion des sessions de conversation.

---

## 🗺 Roadmap

- [ ] Authentification utilisateurs (JWT)
- [ ] Base de données PostgreSQL pour persister les sessions
- [ ] Support de fichiers uploadés (analyse de codebase)
- [ ] Intégration GitHub — analyse de PR, review de code
- [ ] Mode "Agent" — exécution autonome de tâches multi-étapes
- [ ] Extension VS Code
- [ ] Support GPU (CUDA) pour génération x10 plus rapide
- [ ] WebSocket au lieu de SSE pour une latence encore plus faible

---

## 🤝 Contribuer

```bash
git clone https://github.com/syntaxe-ai/syntaxe-ai
cd syntaxe-ai

# Backend
cd backend && pip install -r requirements.txt

# Frontend  
cd frontend && npm install
```

Les PRs sont les bienvenues. Ouvre une issue avant de travailler sur une grosse feature.

---

## 📄 Licence

MIT — Fais-en ce que tu veux.

---

<div align="center">
  Construit avec ❤️ par <strong>Dev Messy / Syntaxe</strong><br/>
  <sub>Propulsé par Ollama · Deepseek · FastAPI · React</sub>
</div>
