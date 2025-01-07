FROM ghcr.io/astral-sh/uv:python3.13-bookworm AS builder

WORKDIR /app

# Enable bytecode compilation
ENV UV_COMPILE_BYTECODE=1

# Build sub-dependencies
COPY packages/ packages/
RUN cd packages/e3dc && uv build --package e3dc

# Copy and install application dependencies with frozen lock
COPY pyproject.toml uv.lock ./
RUN uv sync --frozen --no-install-project --no-dev
RUN uv pip install /app/packages/e3dc/dist/e3dc-*.whl

FROM python:3.13-bookworm AS runner

WORKDIR /app

# Copy packages and application
COPY --from=builder /app/.venv .venv
COPY src/ src/

# Set path to venv to allow uvicorn command to be resolved
ENV PATH="/app/.venv/bin:$PATH"

EXPOSE 8000

CMD ["fastapi", "run", "src/app/main.py"]
