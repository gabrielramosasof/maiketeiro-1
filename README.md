# MAIKETEIRO

Assistente pessoal de marketing alimentado por IA para automatizar e otimizar workflows de criação de conteúdo.

## Visão Geral

Maiketeiro é uma suite completa de ferramentas e scripts gerenciados por um agente de IA, projetada para simplificar e automatizar tarefas de marketing de conteúdo. Desde o processamento de vídeo até a geração de ideias criativas, o Maiketeiro centraliza todas as ferramentas necessárias para produção de conteúdo de alta qualidade.

## Funcionalidades

### Processamento de Mídia
- **Edição de Vídeo**: Scripts FFmpeg para cortes, conversões e otimizações
- **Transcrição Automática**: Conversão de áudio/vídeo em texto
- **Cortes Inteligentes**: Identificação e extração de trechos relevantes

### Geração de Conteúdo
- **Legendas Automáticas**: Criação e sincronização de legendas
- **Ideias de Publicações**: Sugestões criativas para redes sociais
- **Prompts para IA**: Geração de prompts otimizados para:
  - **VEO3**: Modelo de vídeo
  - **Image4**: Modelo de geração de imagens

### Agente de IA
Um agente inteligente que orquestra e controla todas as ferramentas, automatizando workflows completos de criação de conteúdo.

## Estrutura do Projeto

```
maiketeiro/
├── scripts/          # Scripts de automação
│   ├── ffmpeg/      # Processamento de vídeo
│   ├── transcribe/  # Transcrição de áudio
│   └── cuts/        # Cortes e edições
├── ai-agent/        # Agente de IA
└── utils/           # Utilitários diversos
```

## Começando

### Pré-requisitos

- Node.js 18+
- FFmpeg instalado no sistema
- Credenciais de API para serviços de IA

### Instalação

#### Opção 1: Docker (Recomendado)

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/maiketeiro.git
cd maiketeiro

# Execute com Docker Compose
docker-compose up -d

# Acesse em http://localhost:8501
```

#### Opção 2: Instalação Local

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/maiketeiro.git

# Entre no diretório
cd maiketeiro

# Instale as dependências
npm install

# Configure as variáveis de ambiente
cp .env.example .env
```

### Uso Básico

#### Com Docker

```bash
# Execute o dashboard
docker-compose up

# Execute em background
docker-compose up -d

# Pare os containers
docker-compose down
```

#### Local

```bash
# Execute o assistente
npm start

# Processar um vídeo
npm run process-video -- input.mp4

# Gerar transcrição
npm run transcribe -- audio.mp3
```

## Casos de Uso

- **Criadores de Conteúdo**: Automatize edição e publicação
- **Agências de Marketing**: Escale produção de conteúdo
- **Social Media**: Gere ideias e legendas rapidamente
- **Podcasters**: Transcreva e corte episódios automaticamente

## Docker

O projeto inclui configuração completa para containerização com Docker:

### Arquivos Docker

- `Dockerfile`: Configuração multi-stage para produção
- `docker-compose.yml`: Orquestração para desenvolvimento
- `.dockerignore`: Otimização de build

### Recursos Docker

- **Imagem Base**: Python 3.11 slim para tamanho reduzido
- **Multi-stage Build**: Otimização de camadas e cache
- **Segurança**: Usuário não-root e permissões adequadas
- **Health Checks**: Verificação automática de saúde da aplicação
- **Hot Reload**: Desenvolvimento com montagem de volumes

### Comandos Úteis

```bash
# Construir imagem
docker build -t maiketeiro .

# Executar container
docker run -p 8501:8501 maiketeiro

# Desenvolvimento com hot reload
docker-compose up

# Logs dos containers
docker-compose logs -f

# Limpar containers e imagens
docker-compose down --rmi all
```

## Tecnologias

- Node.js
- FFmpeg
- APIs de IA (OpenAI, Anthropic, Google)
- Python (para scripts específicos)
- Docker & Docker Compose

## Contribuindo

Contribuições são bem-vindas! Por favor, abra uma issue ou pull request.

## Licença

MIT License - veja o arquivo LICENSE para detalhes.

## Autor

Gabriel Ramos

## Suporte

Para questões e suporte, abra uma issue no repositório.

Aqui está uma lista completa dos componentes encontrados na sua página do Claude Code Templates:

**🤖 Agentes (27):**
- Podcast Metadata Specialist (ffmpeg-clip-team/podcast-metadata-specialist)
- Podcast Content Analyzer (ffmpeg-clip-team/podcast-content-analyzer)
- Podcast Transcriber (ffmpeg-clip-team/podcast-transcriber)
- Audio Quality Controller (ffmpeg-clip-team/audio-quality-controller)
- Audio Mixer (ffmpeg-clip-team/audio-mixer)
- Timestamp Precision Specialist (ffmpeg-clip-team/timestamp-precision-specialist)
- Video Editor (ffmpeg-clip-team/video-editor)
- Social Media Clip Creator (ffmpeg-clip-team/social-media-clip-creator)
- Social Media Copywriter (podcast-creator-team/social-media-copywriter)
- Twitter Ai Influencer Manager (podcast-creator-team/twitter-ai-influencer-manager)
- Comprehensive Researcher (podcast-creator-team/comprehensive-researcher)
- Project Supervisor Orchestrator (podcast-creator-team/project-supervisor-orchestrator)
- Market Research Analyst (podcast-creator-team/market-research-analyst)
- Documentation Expert (expert-advisors/documentation-expert)
- Database Architect (database/database-architect)
- Database Optimization (database/database-optimization)
- Database Admin (database/database-admin)
- Database Optimizer (database/database-optimizer)
- Supabase Schema Architect (database/supabase-schema-architect)
- Cli Ui Designer (development-team/cli-ui-designer)
- Frontend Developer (development-team/frontend-developer)
- Backend Architect (development-team/backend-architect)
- Code Reviewer (development-tools/code-reviewer)
- Error Detective (development-tools/error-detective)
- Test Engineer (development-tools/test-engineer)
- Mcp Expert (development-tools/mcp-expert)
- Command Expert (development-tools/command-expert)

**⚡ Commands (3):**
- Architecture Review (team/architecture-review)
- Docs Maintenance (documentation/docs-maintenance)
- Generate Api Documentation (documentation/generate-api-documentation)

**⚙️ Settings (0):**
- Nenhum item adicionado

**🪝 Hooks (0):**
- Nenhum item adicionado

**🔌 MCPs (5):**
- Context7 (devtools/context7)
- Playwright Mcp Server (browser_automation/playwright-mcp-server)
- Chrome Devtools (devtools/chrome-devtools)
- Markitdown (devtools/markitdown)
- Grafana (devtools/grafana)

**🎨 Skills (0):**
- Nenhum item adicionado[1]

Se precisar da lista expandida de todos os agentes, comandos ou MCPs do site, posso ajudar a navegar e capturar todos!

[1](https://www.aitmpl.com/agents)
