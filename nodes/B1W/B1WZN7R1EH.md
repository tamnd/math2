---
tag: B1WZN7R1EH
kind: definition
name: Gompertz growth model
msc: [92D25, 92C50]
defines: 9VAB0KT9WA
uses: [1YEMFQ1H32, X23CRWHRCH, 0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Gompertz_function
---

## Definition

Let $r > 0$ and $K > 0$ be constants.
The *Gompertz growth model* is the [[population model|1YEMFQ1H32]] given by the [[ordinary differential equation|0NT64JV96A]]
$$N'(t) = r \, N(t) \ln\!\left(\frac{K}{N(t)}\right), \qquad N(t) > 0.$$
For the initial size $N(0) = N_0 > 0$, its solution is
$$N(t) = K \exp\!\left( \ln\!\left(\frac{N_0}{K}\right) e^{-r t} \right).$$

## Remarks

Check of the solution: put $u = \ln(N/K)$; then $u' = N'/N = -r u$, so $u(t) = u(0) e^{-rt}$ with $u(0) = \ln(N_0/K)$.
So $N(t) \to K$ as $t \to \infty$ for each $N_0 > 0$, and $K$ is the [[carrying capacity|X23CRWHRCH]].
If $N_0 < K/e$, the solution has its inflection point when $N = K/e$, since $N'' = r N' (\ln(K/N) - 1)$.
Non-example: $N' = r N (1 - N/K)$ is the logistic model and not the Gompertz model; its per capita rate $r(1 - N/K)$ is linear in $N$ and not in $\ln N$.
The Gompertz function is often written as $f(t) = a \, e^{-b e^{-c t}}$ with $a, b, c > 0$; it matches the solution above with $a = K$, $b = \ln(K/N_0)$ and $c = r$ when $N_0 < K$.
