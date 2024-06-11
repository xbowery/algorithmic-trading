# Trading Algorithms

This repository contains some frequently used algorithms that are used in trading.

## Execution Algorithms

### Time Weighted Average Price

This repository contains the algorithm for calculating the Time Weighted Average Price (TWAP) of a particular security, over a specific time period.

The TWAP algorithm is used to **spread the order evenly within a specified time frame**.

The mathematical expression of the TWAP algorithm can be found below:


**Time Weighted Average Price Algorithm**
```math
\hat{P}_{daily} = {\frac{(P_{open} + P_{high} + P_{low} + P_{close})}4} $$
```

where:

- $`\hat{P}_{daily}`$ is the average daily price of the security
- $`P_{open}`$ is the open price of the security for the day
- $`P_{high}`$ is the high price of the security for the day
- $`P_{low}`$ is the low price of the security for the day
- $`P_{close}`$ is the close price of the security for the day

``` math
$$ TWAP_n = {\frac{1}n}\sum_{i=1}^n\hat{P}_i $$
```

This repository uses the xbbg package, so please do ensure your machine is connected to the Bloomberg Terminal before running the `bloomberg_twap.py` script.

#### Streamlit View

The local Streamlit viewer can be viewed using a machine with the Bloomberg Terminal connected.

A sample view of the viewer is shown below:
![TWAP Streamlit Viewer](https://github.com/xbowery/algorithmic-trading/assets/69230356/04ba830f-6380-4192-8ef8-f856fe6e9f8a)

A separate browser tab will open showing the line chart of the TWAP price:
![TWAP Streamlit Viewer 2](https://github.com/xbowery/algorithmic-trading/assets/69230356/c55ef996-24d2-4d06-8a98-749851db4268)


### (Intraday) Volume Weighted Average Price

This repository contains the algorithm for calculating the intraday Volume Weighted Average Price (VWAP) of a particular security, over a specific time period.

The VWAP algorithm is used to **execute trades in line with the average price over a specified period**.

The mathematical expression of the VWAP algorithm can be found below:


**Volume Weighted Average Price Algorithm**
```math
$$ P_i = {\frac{(H_i + L_i + C_i)}3} $$
```

where: 
- $`P_i`$ is the price of the security at the i-th interval
- $`H_i`$ is the high price for at the i-th interval
- $`L_i`$ is the low price for at the i-th interval
- $`C_i`$ is the close price for at the i-th interval

``` math
$$ VWAP_i = {\frac{\sum(P_i * V_i)}{\sum(V_i)}} $$
```

#### Streamlit View

The local Streamlit viewer can be viewed using a machine with the Bloomberg Terminal connected.

A sample view of the viewer is shown below:
![VWAP Streamlit Viewer](https://github.com/xbowery/algorithmic-trading/assets/69230356/e279e496-3b98-463e-b4e6-8d9aed3cc4c2)


A separate browser tab will open showing the line chart of the VWAP prices at different times:
![VWAP Streamlit Viewer 2](https://github.com/xbowery/algorithmic-trading/assets/69230356/18f6faba-8945-4f73-a420-e148f0874d89)
