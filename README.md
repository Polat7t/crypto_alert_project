# Crypto Alert & Monitoring Telegram Bot 🚀

A lightweight Python automation script that continuously monitors the live price of Bitcoin (BTC) via the official Binance API and sends instant alert notifications to a Telegram chat if the price drops below a specific target threshold.

This project demonstrates production-ready API integrations, environment variable security, error handling, and asynchronous-like background loops.

## ✨ Features
* **Real-time Price Fetching:** Directly connects to Binance API (`/api/v3/ticker/price`) using the `requests` library.
* **Continuous 24/7 Monitoring:** Runs an infinite execution loop with configurable safety intervals.
* **Instant Telegram Alerts:** Leverages Telegram Bot API to push immediate alerts for market drops.
* **High Security Standards:** Fully decouples sensitive tokens and chat IDs from the source code using `.env` variables.
* **Graceful Termination:** Handles keyboard interruptions cleanly without breaking logs.

## 🛠️ Tech Stack
* Python 3.x
* `requests` (HTTP client)
* `python-dotenv` (Configuration management)

## 📦 Installation & Setup

1. Clone the repository and navigate to the project directory:
```bash
git clone https://github.com/your_name/crypto_alert_project.git
cd crypto-alert-bot
