![This is a alt text.](https://imgs.search.brave.com/RAK6ZelPhHDXLP_KJ-xXmBkYxbSfVGHPLc7aRLnx-VI/rs:fit:1200:934:1/g:ce/aHR0cHM6Ly93d3cu/cGF5ZmlybWEuY29t/L3dwLWNvbnRlbnQv/dXBsb2Fkcy8yMDE1/LzA4L2FnZ3JlZ2F0/b3IuanBn "cool-pic")


## Inputs
###### Real-Time Inputs
Barcharts

    - Interval:{ 1 Hour or 1 Minute}
    - ?


Historical Data Inputs

    ?? This is probably best for the model instead

## Output

Event entries for the database (Stock-recorder)

## General Sequence of Events

1. Accept input data from Barcharts
    
2. Parse inputs into common datatype

3. Enter parsed data into stock-recorder database

#### Database stucture



    Database: stock-recorder
    Table: SPY-1H

#### Event record layout:
    
    { time, high, low, close, volume }


## Links

You may be using [Markdown Live Preview](https://markdownlivepreview.com/).
https://www.barchart.com/my/price-history/historical

