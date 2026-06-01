# Makefile for Music Bot - Convenient commands

.PHONY: help install setup test run run-docker stop logs clean

help:
	@echo "🎵 Telegram Music Bot - Available Commands"
	@echo "==========================================="
	@echo ""
	@echo "Installation & Setup:"
	@echo "  make install      - Install all dependencies"
	@echo "  make setup        - Setup environment and create .env"
	@echo "  make test         - Test configuration"
	@echo ""
	@echo "Running the Bot:"
	@echo "  make run          - Run bot locally"
	@echo "  make run-docker   - Run bot with Docker"
	@echo ""
	@echo "Maintenance:"
	@echo "  make stop         - Stop running bot"
	@echo "  make logs         - View bot logs"
	@echo "  make clean        - Clean cache and logs"
	@echo ""
	@echo "Development:"
	@echo "  make format       - Format code with black"
	@echo "  make lint         - Check code with flake8"
	@echo ""

install:
	@echo "📦 Installing dependencies..."
	pip install --upgrade pip
	pip install -r requirements.txt
	@echo "✅ Dependencies installed!"

setup:
	@echo "⚙️  Setting up bot..."
	@if [ ! -f .env ]; then \
		cp .env.example .env; \
		echo "📝 Created .env file - Please edit it with your credentials"; \
	fi
	mkdir -p downloads logs
	@echo "✅ Setup complete!"

test:
	@echo "🔍 Testing configuration..."
	python test_config.py

run:
	@echo "🚀 Starting Music Bot..."
	python bot.py

run-docker:
	@echo "🐳 Starting bot with Docker..."
	docker-compose up -d
	@echo "✅ Bot started! View logs with: make logs-docker"

stop:
	@echo "⏹️  Stopping bot..."
	pkill -f "python bot.py" || echo "Bot not running"
	@echo "✅ Bot stopped!"

stop-docker:
	@echo "⏹️  Stopping Docker containers..."
	docker-compose down
	@echo "✅ Containers stopped!"

logs:
	@echo "📋 Showing bot logs..."
	tail -f logs/bot.log

logs-docker:
	@echo "📋 Showing Docker logs..."
	docker-compose logs -f music_bot

clean:
	@echo "🧹 Cleaning up..."
	rm -rf __pycache__
	rm -rf downloads/*
	rm -rf logs/*
	rm -rf .pytest_cache
	rm -rf *.egg-info
	@echo "✅ Cleaned!"

format:
	@echo "🎨 Formatting code..."
	black *.py
	@echo "✅ Formatting complete!"

lint:
	@echo "🔎 Linting code..."
	flake8 *.py --max-line-length=120
	@echo "✅ Linting complete!"

venv:
	@echo "📦 Creating virtual environment..."
	python3 -m venv venv
	@echo "✅ Virtual environment created!"
	@echo "   Activate with: source venv/bin/activate"

dev-install: venv install
	@echo "📦 Installing development dependencies..."
	pip install -r requirements-dev.txt
	@echo "✅ Dev environment ready!"

freeze:
	pip freeze > requirements.txt
	@echo "✅ Requirements frozen!"

# Default target
.DEFAULT_GOAL := help
