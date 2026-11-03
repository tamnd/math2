---
tag: RPTB1Z49H4
kind: definition
name: SIS and SEIR models
msc: [92D30, 34C60]
defines: P1ANHAY6XY
uses: [BX5ZA16MM6, 0P97V20RW7]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
---

## Definition

Let $N > 0$ be the population size, $\beta > 0$ the transmission rate and $\gamma > 0$ the recovery rate.

1. The *SIS model* is the [[compartmental model|BX5ZA16MM6]] for nonnegative functions $S, I$ with $S(0) + I(0) = N$ given by
$$S' = -\frac{\beta S I}{N} + \gamma I, \qquad I' = \frac{\beta S I}{N} - \gamma I.$$
2. Let moreover $\sigma > 0$ be the rate at which exposed hosts become infectious.
   The *SEIR model* is the compartmental model for nonnegative functions $S, E, I, R$ with $S(0) + E(0) + I(0) + R(0) = N$ given by
$$S' = -\frac{\beta S I}{N}, \quad E' = \frac{\beta S I}{N} - \sigma E, \quad I' = \sigma E - \gamma I, \quad R' = \gamma I.$$

Both are systems of [[ordinary differential equations|0P97V20RW7]], and the total population stays equal to $N$.

## Remarks

In the SIS model, $S = N - I$ gives the single equation $I' = I \left( \beta (N - I)/N - \gamma \right)$.
If $\beta > \gamma$, every solution with $I(0) > 0$ tends to the endemic level $I^{*} = N (1 - \gamma / \beta)$.
If $\beta \le \gamma$, every solution tends to $0$.

Example: for $N = 100$, $\beta = 2$ and $\gamma = 1$, the SIS endemic level is $I^{*} = 50$.
Check: $I' = 50 \, (2 \cdot 50/100 - 1) = 0$ at $I = 50$.

Non-example: the [[SIR model|J5FHBDJGJA]] is not an SIS model, since its recovered hosts never return to $S$.

In the SEIR model, the mean latent period is $1/\sigma$ and the mean infectious period is $1/\gamma$.
Without births and deaths, its basic reproduction number is $\beta / \gamma$, the same as for the SIR model.
