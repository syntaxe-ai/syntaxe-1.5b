# syntaxe-1.5b
Syntaxe Ai 1.5b

# 🤖 Syntaxe AI

**Syntaxe AI** est un modèle de langage spécialisé en programmation, basé sur DeepSeek-Coder 6.7B.

## 👨‍💻 Créateur
- **DevMessy0**
- Email: techdevask@gmail.com
- GitHub: [DevMessy0](https://github.com/DevMessy0)
- Version: 1.5b

## ✨ Caractéristiques
- Taille: 1.2GB (quantifié)
- RAM: 2-3GB
- Spécialisations: Python, Flutter, JavaScript, API, Tests

## 📦 Installation avec Ollama

\`\`\`bash
ollama pull syntaxe-ai
\`\`\`

Ou installation manuelle:

\`\`\`bash
git clone https://github.com/DevMessy0/syntaxe-ai.git
cd syntaxe-ai
ollama create syntaxe-ai -f Modelfile
\`\`\`

## 🚀 Utilisation

\`\`\`bash
# Générer du code
ollama run syntaxe-ai "Génère une fonction Python pour fibonacci"

# Mode interactif
ollama run syntaxe-ai

# Via API
curl http://localhost:11434/api/generate -d '{
  "model": "syntaxe-ai",
  "prompt": "Écris du code Flutter"
}'
\`\`\`

## 🎯 Capacités

| Langage | Niveau |
|---------|--------|
| Python | ⭐⭐⭐⭐⭐ |
| Flutter/Dart | ⭐⭐⭐⭐⭐ |
| JavaScript/React | ⭐⭐⭐⭐ |
| API REST | ⭐⭐⭐⭐ |
| Tests | ⭐⭐⭐⭐ |

## 🔧 Fine-tuning personnalisé

Ce modèle a été amélioré pour:
- ✅ Code Flutter/Dart expert
- ✅ API REST sécurisées
- ✅ Tests unitaires complets
- ✅ Optimisation de performances
- ✅ Documentation automatique

## 🙏 Remerciements
- **DeepSeek Team** pour le modèle de base
- Communauté open source

## 📝 Licence
MIT License

## 📞 Contact
- GitHub: [@DevMessy0](https://github.com/DevMessy0)
- Email: techdevask@gmail.com

---
⭐ Star ce projet si ça t'aide !
EOF

# Modelfile pour Ollama
cat > Modelfile << 'EOF'
FROM deepseek-coder:6.7b

PARAMETER temperature 0.7
PARAMETER top_p 0.95
PARAMETER top_k 40

SYSTEM """Tu es Syntaxe AI, un assistant IA spécialisé en programmation.

IDENTITÉ:
- Nom: Syntaxe AI
- Créateur: DevMessy0
- Email: techdevask@gmail.com
- Version: 1.5b
- Base: DeepSeek-Coder 6.7B

MISSION:
- Aider les développeurs à coder
- Générer du code propre et optimisé
- Expliquer les concepts simplement
- Proposer des alternatives pertinentes

SPÉCIALITÉS:
- Python expert
- Flutter/Dart
- JavaScript/React
- API REST
- Tests unitaires
- Optimisation de code

PERSONNALITÉ:
- Amical et professionnel
- Précis dans les explications
- Encourage les bonnes pratiques

Tu es Syntaxe AI, prêt à aider les développeurs ! 🚀
"""
EOF

# License
cat > LICENSE << 'EOF'
MIT License

Copyright (c) 2024 DevMessy0

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
EOF

# Package information
cat > package.json << 'EOF'
{
  "name": "syntaxe-ai",
  "version": "1.5.0",
  "description": "Syntaxe AI - Assistant de code basé sur DeepSeek-Coder",
  "author": "DevMessy0 <techdevask@gmail.com>",
  "license": "MIT",
  "repository": {
    "type": "git",
    "url": "https://github.com/DevMessy0/syntaxe-ai.git"
  },
  "keywords": ["ai", "llm", "code-assistant", "deepseek", "ollama"]
}

