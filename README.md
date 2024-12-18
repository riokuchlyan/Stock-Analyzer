# Stock Sentiment Analyzer

The **Stock Sentiment Analyzer** is a Python-based application that leverages APIs and machine learning techniques to provide sentiment analysis for stock market-related news. This project features a user-friendly graphical interface built using **CustomTkinter**, integrates real-time stock data from **Polygon.io**, and conducts sentiment analysis on news articles fetched via the **NewsAPI.org** API.

To ensure secure storage of sensitive information, API keys are hidden through configuration files excluded from version control. This project is released under the **GNU General Public License v3.0**.

---

## Features

- **Real-Time Stock Data**: Fetches and displays the latest stock market data using the Polygon.io API.
- **Sentiment Analysis**: Analyzes sentiment from relevant news articles fetched through NewsAPI.org.
- **CustomTkinter GUI**: A modern, user-friendly interface for interacting with the application.
- **Secure API Key Management**: API keys are stored in configuration files and excluded from GitHub repositories for enhanced security.
- **Cross-Platform Compatibility**: Designed to work seamlessly on macOS, Windows, and Linux.

---

## Getting Started

### Prerequisites
To run the project, ensure you have the following installed:
- Python 3.9 or higher
- pip (Python package manager)
- An active **Polygon.io** API key
- An active **NewsAPI.org** API key

### Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/stock-sentiment-analyzer.git
   cd stock-sentiment-analyzer

	2.	Install the required Python packages:

pip install -r requirements.txt


	3.	Create a configuration file (config.ini) in the project root:

[API_KEYS]
POLYGON_API_KEY = your_polygon_api_key
NEWS_API_KEY = your_news_api_key


	4.	Run the application:

python main.py

Usage
	1.	Launch the application by running main.py.
	2.	Enter the stock ticker symbol (e.g., AAPL for Apple).
	3.	Click “Fetch Data” to retrieve the latest stock data and news.
	4.	View the sentiment analysis summary and detailed article insights within the GUI.

File Structure

stock-sentiment-analyzer/
├── main.py              # Entry point of the application
├── LICENSE              # GNU GPL v3.0 license
└── README.md            # Project documentation

Security
	•	API Key Protection: API keys are stored in a config.ini file and are ignored in .gitignore to prevent accidental exposure.
	•	Local Execution: The application is designed to run locally, reducing the risk of unauthorized access to your data.

License

This project is licensed under the GNU General Public License v3.0. You are free to modify, distribute, and use this project, provided you retain the original license terms.

Contributing

Contributions are welcome! If you have ideas for improvement or encounter bugs, feel free to submit an issue or a pull request.

Acknowledgments
	•	CustomTkinter for the GUI framework
	•	Polygon.io for stock market data
	•	NewsAPI.org for news and article data
	•	The Python open-source community for libraries that make this project possible.

Disclaimer

This tool is for informational purposes only and should not be used for financial decision-making without independent research.
