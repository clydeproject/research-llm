# Research LLM Service

A Docker Compose setup for running vLLM with OpenAI GPT-OSS-120B model.

## Quick Start

### Docker Compose (Single Node)
```bash
# Start the service
docker-compose up -d
```

### Docker Swarm (Multi-Node)
```bash
# Initialize swarm (if not already done)
docker swarm init

# Label nodes with GPUs (optional, for better placement)
docker node update --label-add gpu=true $(docker node ls -q)

# Deploy the stack
docker stack deploy -c docker-compose.swarm.yml research-llm

# Check service status
docker service ls
docker service ps research-llm_research-llm
```

## Prerequisites

- NVIDIA GPU with drivers installed
- Docker with NVIDIA Container Toolkit
- Sufficient GPU memory (recommended 24GB+ for the 120B model)
- For Swarm: All nodes must have NVIDIA Container Toolkit installed

## Usage

- **Service URL**: http://localhost:8000
- **View logs**: 
  - Compose: `docker-compose logs -f research-llm`
  - Swarm: `docker service logs -f research-llm_research-llm`
- **Stop service**: 
  - Compose: `docker-compose down`
  - Swarm: `docker stack rm research-llm`

## Configuration

- Tensor parallel size: 2
- GPU memory utilization: 90%
- Max model length: 131,072 tokens
- Data type: bfloat16

## Model Storage

Models are cached in `./model-storage/` directory. The model will be automatically downloaded on first run (~10.5GB).

## Troubleshooting

1. **Out of memory**: Reduce `--max-model-len` or `--gpu-memory-utilization`
2. **Container fails to start**: Ensure NVIDIA Container Toolkit is properly installed
