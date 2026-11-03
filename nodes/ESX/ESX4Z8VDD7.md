---
tag: ESX4Z8VDD7
kind: definition
name: Malthusian growth model
msc: [92D25]
defines: HQ5DZZYJMS
uses: [1YEMFQ1H32, 0NT64JV96A, 0J0FCWV32D, 00SVP6W3CB]
sources:
  - url: https://en.wikipedia.org/wiki/Malthusian_growth_model
---

## Definition

Let $r \in \R$ be a constant, called the Malthusian parameter or intrinsic growth rate.
The *Malthusian growth model* is the [[population model|1YEMFQ1H32]] given by the [[ordinary differential equation|0NT64JV96A]]
$$N'(t) = r \, N(t).$$
Here $N(t) \ge 0$ is the size of the population at time $t$.
For the initial size $N(0) = N_0 \ge 0$, its solution is $N(t) = N_0 e^{r t}$, an [[exponential function|0J0FCWV32D]] of $t$.

## Remarks

Example: with $r = \ln 2$ and $N_0 = 100$, the solution $N(t) = 100 \cdot 2^t$ satisfies $N' = (\ln 2) \, 100 \cdot 2^t = r N$, and it doubles at each unit of time.
Non-example: $N' = r N (1 - N/K)$ with $K > 0$ is not Malthusian, since its per capita rate $N'/N = r(1 - N/K)$ is not constant.
The discrete-time form is $N_{t+1} = \lambda N_t$ with $\lambda \ge 0$, with solution $N_t = \lambda^t N_0$; it corresponds to $r = \ln \lambda$ when $\lambda > 0$.
The population grows if $r > 0$, stays constant if $r = 0$, and decays to $0$ if $r < 0$.
The model is a special case of [[exponential growth and decay|00SVP6W3CB]].
