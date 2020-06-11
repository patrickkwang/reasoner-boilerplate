# Boilerplate Reasoner API

__Access Swagger UI at `http://HOST:8011/docs`.__

## Installation

### Local Installation

```bash
pip install -r requirements
```

### Docker Installation

```bash
docker build -t reasoner .
```

## Deployment

### Local Deployment

```bash
./main.sh
```

### Docker Deployment

```bash
docker run -p 8011:8011 --name reasoner -d reasoner
```
