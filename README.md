# not-your-financial-advisor

`not-your-financial-advisor` is a Python-based project that provides a set of tools for analyzing stock and crypto market data and generating recommendations for potential investment opportunities. The main goal of this project is to leverage classic algorithmic detection patterns to detect profitable trading opportunities in the stock or crypto market.

## Project Overview

The project consists of the following main classes:

* `PatternDetector`: This class provides the core functionality for detecting trading patterns in stock and crypto market data. It uses a set of pre-defined patterns to analyze market data and generate potential trading opportunities.

* `MarketDataIngestor`: This class provides functionality for ingesting market data from different sources, such as stock market APIs and crypto market exchanges. It can parse different types of data formats and store them in a local database for further analysis.

* `Database`: This class provides a set of utilities for managing the local database used by the project. It can create tables, insert data, and perform basic queries.

* `Pattern`: This class defines the structure and behavior of individual trading patterns. It encapsulates the logic for analyzing market data and generating trading signals based on specific conditions.

## Future Goals

The project is currently in an early stage of development and is limited to classic algorithmic detection patterns. However, the ultimate goal is to integrate machine learning algorithms to help predict stocks with data such as annual reports and social media mentions. This would allow for more accurate and targeted trading recommendations based on a variety of factors.

## Getting Started

To get started with `not-your-financial-advisor`, simply clone the repository and install the required dependencies using `pip` or:
1. git clone https://github.com/yourusername/not-your-financial-advisor.git
2. cd not-your-financial-advisor
3. pip install -r requirements.txt
