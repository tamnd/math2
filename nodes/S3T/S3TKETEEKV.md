---
tag: S3TKETEEKV
kind: statement
role: theorem
name: Kermack–McKendrick theory
msc: [92D30, 34C60]
uses: [J5FHBDJGJA]
about: [J5FHBDJGJA]
sources:
  - url: https://en.wikipedia.org/wiki/Kermack%E2%80%93McKendrick_theory
same_as:
  wikidata: Q17067396
  wikipedia: Kermack–McKendrick theory
---

## Statement

Consider the [[SIR model|J5FHBDJGJA]] with population size $N$, transmission rate $\beta > 0$ and recovery rate $\gamma > 0$.
Let $S(0) = S_0 > 0$, $I(0) = I_0 > 0$ and $R(0) = 0$.

1. The function $S$ is strictly decreasing, $R$ is strictly increasing, and the limits $S_\infty = \lim_{t \to \infty} S(t)$ and $R_\infty = \lim_{t \to \infty} R(t)$ exist.
2. $\lim_{t \to \infty} I(t) = 0$.
3. $S_\infty > 0$, so the epidemic ends before all susceptible hosts are infected.
4. The number $I(t)$ increases at time $0$ if and only if $S_0 > \gamma N / \beta$.

## Remarks

Proof idea: $S' = -\beta S I / N < 0$ and $R' = \gamma I > 0$ give monotonicity, and both functions are bounded, so they converge.
Since $R$ is bounded and $R' = \gamma I$, the integral $\int_0^\infty I \, dt$ is finite, which forces $I \to 0$ because $I$ is uniformly continuous.
Dividing $S'$ by $R'$ gives $dS/dR = -\beta S / (\gamma N)$, so $S(t) = S_0 \exp \left( -\beta R(t) / (\gamma N) \right)$.
As $R(t) \le N$, this gives $S_\infty \ge S_0 e^{-\beta / \gamma} > 0$.
Part 4 follows from $I'(0) = I_0 \left( \beta S_0 / N - \gamma \right)$.

Example: with $\beta / \gamma = 2$ and almost the whole population susceptible, about $20\%$ of the population escapes infection, as the [[final size equation|8ABBB524PN]] shows.

Part 4 is the starting point of the [[threshold theorem of epidemiology|XQQTXNF7BT]].

## Explanations

### L1 human

In 1927 Kermack and McKendrick asked why epidemics stop.
Their answer, in this model, is that an epidemic ends because infected people recover faster than they find new susceptible people.
It does not end because everyone has been infected: some susceptible people always remain.
They also found a threshold: an epidemic starts only if there are enough susceptible people.

### L2 human

The original 1927 paper treats a more general model, in which infectivity and recovery may depend on the time since infection.
The SIR model is the special case with constant rates, and it already shows all the main conclusions.
The key tool is the conserved quantity obtained from $dS/dR$, which also yields the [[final size equation|8ABBB524PN]].
These results remain the basis of deterministic epidemic theory and guide the use of the [[basic reproduction number|VY4H52692D]].
