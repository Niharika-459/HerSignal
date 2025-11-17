# HerSignal Deployment Guide

## Local Setup

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Git

### Installation Steps

```bash
# Clone the repository
git clone https://github.com/Niharika-459/HerSignal.git
cd HerSignal

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### Run the Agent

```bash
# Start the HerSignal agent
python -m src.her_signal_agent

# Or run with Python directly
python src/her_signal_agent.py
```

## Configuration

Edit `config/config.yaml` to customize agent settings:
- Sensor parameters
- Risk thresholds
- Communication settings
- Privacy options

## Features

### Core Functionality
- Real-time location tracking
- Distress detection via sensors
- Instant emergency alerts
- Multi-agent coordination
- Incident logging

### Safety Features
- End-to-end encryption
- Privacy-first design
- Offline fallback
- User consent controls

## Cloud Deployment (Optional)

### Deploy to Heroku
```bash
# Login to Heroku
heroku login

# Create app
heroku create your-app-name

# Push code
git push heroku main

# View logs
heroku logs --tail
```

### Environment Variables
Set these on your cloud platform:
```
AGENT_MODE=production
LOG_LEVEL=INFO
ENCRYPTION_KEY=your_key
POLICE_API=your_endpoint
```

## Docker Deployment

```bash
# Build Docker image
docker build -t hersignal .

# Run container
docker run -p 5000:5000 hersignal

# Stop container
docker stop <container_id>
```

## Testing

```bash
# Run unit tests
pytest tests/ -v

# Run with coverage
pytest --cov=src tests/

# Run specific test
pytest tests/test_agent.py::test_activate -v
```

## Troubleshooting

### Issue: "ModuleNotFoundError"
**Solution**: Install all dependencies
```bash
pip install -r requirements.txt
```

### Issue: "Permission denied" on Linux/macOS
**Solution**: Make script executable
```bash
chmod +x src/her_signal_agent.py
```

### Issue: Port already in use
**Solution**: Kill process using port
```bash
# On Windows:
netstat -ano | findstr :5000
taskkill /PID <PID> /F

# On macOS/Linux:
lsof -ti:5000 | xargs kill -9
```

## Performance Monitoring

Monitor these metrics:
- Alert response time
- Detection accuracy
- False positive rate
- System uptime

## Security Best Practices

1. Keep credentials in `.env` file
2. Use HTTPS for all communications
3. Regularly update dependencies
4. Enable logging for audits
5. Encrypt sensitive data

## Support & Documentation

- GitHub Issues: https://github.com/Niharika-459/HerSignal/issues
- Documentation: See docs/ folder
- API Reference: docs/API_REFERENCE.md

## License

MIT License - See LICENSE file for details
