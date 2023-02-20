![This is a alt text.](https://imgs.search.brave.com/BG5DEbR07fAgnR10LlmWEuKkS55T-qGefRKem9J4lPg/rs:fit:528:245:1/g:ce/aHR0cHM6Ly9taXJv/Lm1lZGl1bS5jb20v/bWF4LzEwNTYvMSo2/eW9PdFNxTEZ1M0tM/c19fRERZcm9nLnBu/Zw "cool-pic")


## Inputs
#### Stock-recorder Database

#### Parameters
* ticker_symbol
* pattern_types

## Outputs
#### Pattern detection event entries in stock-recorder DB

## General Sequence of Events

1. User specifies pattern_types and ticker_symbol to scan for when starting script

2. Loops over input data from stock-recorder DB, scanning for patterns

3. Detects pattern event

4. Reports detection event to stock-recorder db


#### Database stucture

    Database: stock-recorder
    Table: SPY-1H * Used by aggregator
    Table: SPY-1H-patterns
    
#### Pattern Detection record layout:
    
    { time, pattern_type, slope/value }


## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).
https://www.barchart.com/my/price-history/historical

