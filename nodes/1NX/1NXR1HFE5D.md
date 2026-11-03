---
tag: 1NXR1HFE5D
kind: definition
name: SIR model
msc: [92D30, 34C60]
defines: J5FHBDJGJA
uses: [BX5ZA16MM6, 0P97V20RW7]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
    locator: The SIR model
---

## Definition

Let $N > 0$ be the population size, $\beta > 0$ the transmission rate and $\gamma > 0$ the recovery rate.
The *SIR model* is the [[compartmental model|BX5ZA16MM6]] for functions $S, I, R \colon [0, \infty) \to [0, \infty)$ given by the [[ordinary differential equations|0P97V20RW7]]
$$S' = -\frac{\beta S I}{N}, \qquad I' = \frac{\beta S I}{N} - \gamma I, \qquad R' = \gamma I,$$
with initial values $S(0), I(0), R(0) \ge 0$ and $S(0) + I(0) + R(0) = N$.
Here $S$, $I$ and $R$ are the numbers of susceptible, infectious and removed hosts.

## Remarks

Adding the three equations gives $(S + I + R)' = 0$, so $S + I + R = N$ for all $t$.
The mean infectious period is $1/\gamma$, and the [[basic reproduction number|VY4H52692D]] is $R_0 = \beta / \gamma$.

Example: with $N = 1000$, $\beta = 0.3$ and $\gamma = 0.1$ per day, and $S(0) = 999$, $I(0) = 1$, one has $I'(0) = 0.3 \cdot 999 / 1000 - 0.1 > 0$.
So the number of infectious hosts grows at first, and $R_0 = 3$.

Non-example: the system $S' = -\beta S I / N$, $I' = \beta S I / N$ has no removal term.
It fails the definition because $\gamma = 0$, and in it every host eventually becomes infectious and stays so.

Some authors use the variables $s = S/N$, $i = I/N$, $r = R/N$, and then the infection term reads $\beta s i$.
A variant with births and deaths at equal rate $\mu$ adds $\mu N - \mu S$ to $S'$, $-\mu I$ to $I'$ and $-\mu R$ to $R'$.
