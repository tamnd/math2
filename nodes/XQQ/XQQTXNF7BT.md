---
tag: XQQTXNF7BT
kind: statement
role: theorem
name: Threshold theorem of epidemiology
msc: [92D30, 34C60]
uses: [J5FHBDJGJA, VY4H52692D]
about: [J5FHBDJGJA, VY4H52692D]
sources:
  - url: https://en.wikipedia.org/wiki/Basic_reproduction_number
---

## Statement

Consider the [[SIR model|J5FHBDJGJA]] with population size $N$, transmission rate $\beta > 0$ and recovery rate $\gamma > 0$.
Let $R_0 = \beta / \gamma$ be its [[basic reproduction number|VY4H52692D]].
Let $S(0) = S_0 > 0$ and $I(0) = I_0 > 0$.

1. If $R_0 S_0 / N \le 1$, then $I$ is strictly decreasing on $[0, \infty)$ and tends to $0$.
2. If $R_0 S_0 / N > 1$, then $I$ first increases strictly, reaches its maximum at the unique time $t^{*}$ with $S(t^{*}) = N / R_0$, and then decreases strictly to $0$.

In case 2 the maximum is
$$I_{\max} = I_0 + S_0 - \frac{N}{R_0} \left( 1 + \ln \frac{R_0 S_0}{N} \right).$$

## Remarks

Proof idea: the equation $I' = \gamma I \left( R_0 S / N - 1 \right)$ shows that $I$ grows exactly while $S > N / R_0$.
Since $S' < 0$, the function $S$ decreases strictly, so $S$ crosses the level $N / R_0$ at most once.
The function $S + I - (N / R_0) \ln S$ has derivative $0$ along solutions.
Evaluating it at $t = 0$ and at $S = N / R_0$ gives $I_{\max}$.

Example: for $N = 1000$, $R_0 = 2$, $S_0 = 999$ and $I_0 = 1$, one has $R_0 S_0 / N = 1.998 > 1$.
So an epidemic occurs, and its peak comes when $S$ has fallen to $500$.
The formula gives $I_{\max} = 1000 - 500 (1 + \ln 1.998) \approx 154$.

The hypothesis $I_0 > 0$ is needed: with $I_0 = 0$ the solution stays at $I = 0$ forever.

## Explanations

### L1 human

An epidemic takes off only if one case, in the present population, causes more than one new case.
In the SIR model this means that $R_0$ times the fraction of susceptible people is larger than $1$.
If so, the number of sick people rises until enough people are immune, and then falls.
If not, the number of sick people falls from the start.

### L2 human

The theorem is the original threshold result of Kermack and McKendrick, stated in terms of $R_0$.
The threshold involves $R_0 S_0 / N$, the effective reproduction number at time $0$, not $R_0$ alone.
This is why vaccination works: lowering $S_0$ below $N / R_0$ prevents an epidemic, which is the [[herd immunity threshold|XS908PP9W5]].
For general compartmental models, the analogous result says that the disease-free equilibrium is locally asymptotically stable when $R_0 < 1$ and unstable when $R_0 > 1$, with $R_0$ computed from the [[next-generation matrix|KY7W9E9ECS]].
