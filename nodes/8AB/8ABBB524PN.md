---
tag: 8ABBB524PN
kind: statement
role: theorem
name: Final size equation
msc: [92D30, 34C60]
uses: [J5FHBDJGJA, VY4H52692D]
about: [J5FHBDJGJA]
sources:
  - url: https://en.wikipedia.org/wiki/Kermack%E2%80%93McKendrick_theory
---

## Statement

Consider the [[SIR model|J5FHBDJGJA]] with population size $N$, transmission rate $\beta > 0$, recovery rate $\gamma > 0$, and [[basic reproduction number|VY4H52692D]] $R_0 = \beta / \gamma$.
Let $S(0) = S_0 > 0$, $I(0) = I_0 > 0$ and $R(0) = 0$, and let $S_\infty = \lim_{t \to \infty} S(t)$.
Then $S_\infty$ is the unique solution in $(0, N / R_0)$ of
$$\ln \frac{S_0}{S_\infty} = \frac{R_0}{N} \left( N - S_\infty \right).$$

In the limit $I_0 \to 0$ and $S_0 \to N$ with $R_0 > 1$, the fraction $z = 1 - S_\infty / N$ of the population ever infected is the unique root in $(0, 1)$ of
$$z = 1 - e^{-R_0 z}.$$

## Remarks

Proof idea: along solutions $dS/dR = -R_0 S / N$, so $S(t) = S_0 \exp(-R_0 R(t) / N)$.
As $t \to \infty$, $I(t) \to 0$, so $R(t) \to N - S_\infty$, and taking logarithms gives the equation.
The limit satisfies $S_\infty < N / R_0$, since otherwise $I' = \gamma I (R_0 S / N - 1) > 0$ for all $t$, which contradicts $I(t) \to 0$.
Uniqueness follows because the function $s \mapsto \ln(S_0 / s) - R_0 (N - s)/N$ is strictly decreasing on $(0, N/R_0)$.

Example: for $R_0 = 2$, the root of $z = 1 - e^{-2z}$ is $z \approx 0.797$.
Check: $1 - e^{-1.594} \approx 1 - 0.203 = 0.797$.
So about $80\%$ of the population is infected over the course of the epidemic.

The hypothesis $R_0 > 1$ is needed in the limiting form: for $R_0 \le 1$ the only root in $[0, 1)$ is $z = 0$, so the epidemic stays negligible.
The root can be written as $z = 1 + W(-R_0 e^{-R_0}) / R_0$, where $W$ is the principal branch of the [[Lambert W function|R1XGWTVY3N]].

## Explanations

### L1 human

The final size equation tells what fraction of a population will have been infected when an epidemic is over.
It needs only one number, $R_0$.
With $R_0 = 2$ about $80\%$ get infected, and with $R_0 = 3$ about $94\%$.
Some people always escape, even though the disease spreads well.

### L2 human

The equation comes from a conserved quantity of the SIR model and does not need the solution in time.
The same equation holds for many models with the same $R_0$, such as SEIR, as long as the population mixes homogeneously.
The overshoot is visible: the final susceptible fraction $1 - z$ is below the level $1/R_0$ at which the epidemic peaked.
It also describes the size of large outbreaks in stochastic models such as the [[Reed–Frost model|DG0ZDTRKHW]] in the limit of a large population.
