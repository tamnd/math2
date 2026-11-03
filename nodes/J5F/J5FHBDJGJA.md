---
tag: J5FHBDJGJA
kind: concept
name: SIR model
msc: [92D30, 34C60]
specializes: [BX5ZA16MM6]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
    locator: The SIR model
---

## Summary

The SIR model is the basic [[compartmental model|BX5ZA16MM6]] of an epidemic with lasting immunity.
It splits a closed population into susceptible, infectious and removed hosts, and describes the epidemic by three ordinary differential equations.
Its analysis gives the threshold behaviour governed by the [[basic reproduction number|VY4H52692D]] and the final size of the epidemic.
It goes back to the 1927 work of Kermack and McKendrick.

## Explanations

### L1 human

Everyone in a town is either susceptible (S), infectious (I) or removed (R), meaning recovered and immune.
Susceptible people catch the disease when they meet infectious people, so new infections are proportional to $S \cdot I$.
Infectious people recover at a constant rate and then never get sick again.
Suppose an infectious person has $3$ infectious contacts per week and stays infectious for $1$ week.
Then in a fully susceptible town each case causes about $3$ new cases.
