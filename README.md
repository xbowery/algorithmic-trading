# Trading Algorithms

This repository contains some frequently used algorithms that are used in trading.

## Time Weighted Average Price

This repository contains the algorithm for calculating the Time Weighted Average Price (TWAP) of a particular security, over a specific time period.

The mathematical expression of the TWAP algorithm can be found below:


**Time Weighted Average Price Algorithm**
```math
\hat{P}_{daily} = {\frac{(P_{open} + P_{high} + P_{low} + P_{close})}4} $$
```

``` math
$$ TWAP_n = {\frac{1}n}\sum_{i=1}^n\hat{P}_i $$
```

This repository uses the xbbg package, so please do ensure your machine is connected to the Bloomberg Terminal before running the `bloomberg_twap.py` script.

### Streamlit View

The local Streamlit viewer can be viewed using a machine with the Bloomberg Terminal connected.

A sample view of the viewer is shown below:
![TWAP Streamlit Viewer](https://github.com/xbowery/algorithmic-trading/assets/69230356/04ba830f-6380-4192-8ef8-f856fe6e9f8a)
