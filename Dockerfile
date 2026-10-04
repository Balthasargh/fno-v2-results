FROM python:3.12-slim

WORKDIR /app

RUN apt-get update && apt-get install -y --no-install-recommends \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

COPY pyproject.toml requirements.txt README.md ./
COPY src/ src/
COPY scripts/ scripts/
COPY results/ results/
COPY images/ images/

RUN pip install --no-cache-dir -e .

EXPOSE 8501

CMD ["python", "scripts/analyze_results.py"]
