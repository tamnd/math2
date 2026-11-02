---
tag: S9BKNBRV4H
kind: statement
role: theorem
name: Muckenhoupt's theorem
msc: [42B25]
uses: [T86RSJ8M86, VX1A56P5KQ, SASP14MA1Z, 9534R6VMY0, R1PHMVBJ9J, NSCEBXM7ZM]
about: [T86RSJ8M86, VX1A56P5KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Muckenhoupt_weights
---

## Statement

Let $n \ge 1$, let $w$ be a weight on $\R^n$, and let $M$ be the [[Hardy–Littlewood maximal function|VX1A56P5KQ]] operator.
For $1 \le p < \infty$ write $L^p(w)$ for the [[Lp space|SASP14MA1Z]] of the measure $w(x) \, dx$, and $w(E) = \int_E w \, dx$.

1. For $1 < p < \infty$, there is a constant $C$ with $\int_{\R^n} (Mf)^p \, w \, dx \le C \int_{\R^n} \abs{f}^p \, w \, dx$ for all $f \in L^p(w)$ if and only if $w$ is in the [[Muckenhoupt class|T86RSJ8M86]] $A_p$.
2. There is a constant $C$ with $w(\set{Mf > \lambda}) \le \frac{C}{\lambda} \int_{\R^n} \abs{f} \, w \, dx$ for all $f \in L^1(w)$ and $\lambda > 0$ if and only if $w \in A_1$.

## Remarks

Necessity in part 1 comes from testing on one cube.
Let $\sigma = w^{-1/(p - 1)}$ and $f = \sigma \mathbf{1}_Q$.
On $Q$ one has $Mf \ge \frac{1}{\abs{Q}} \int_Q \sigma$, and inserting this in the inequality gives the $A_p$ bound for $Q$, after a cut-off to make $f \in L^p(w)$.
For sufficiency, one first shows the [[weak-type|9534R6VMY0]] bound on $L^p(w)$ from the $A_p$ condition and the covering argument.
Then one uses that an $A_p$ weight is also in $A_{p - \varepsilon}$ for some $\varepsilon > 0$, which follows from a reverse Hölder inequality, and interpolates with the [[Marcinkiewicz interpolation theorem|R1PHMVBJ9J]].

Example: $w(x) = \abs{x}$ on $\R$ is not in $A_2$, and indeed the weighted inequality fails for $p = 2$.
For $0 < \delta < 1$ let $f = \abs{x}^{-1} \mathbf{1}_{[\delta, 1]}$; then $\int f^2 w = \log(1/\delta)$.
For $x \in [-1, 1]$ the interval of radius $2$ centred at $x$ contains $[\delta, 1]$, so $Mf(x) \ge \frac{1}{4} \log(1/\delta)$.
Hence $\int (Mf)^2 w \ge \frac{1}{16} \log^2(1/\delta)$, and the ratio of the two sides tends to infinity as $\delta \to 0$.

## Explanations

### L1 human

The maximal function is bounded on ordinary $L^p$ for $p > 1$.
The theorem says for which weights this stays true when the $L^p$ norm is weighted.
The answer is a simple test on cubes, the $A_p$ condition.

### L2 human

Muckenhoupt proved the theorem in 1972.
Shortly after, Hunt, Muckenhoupt and Wheeden showed that the same $A_p$ condition characterizes the weights for which the [[Hilbert transform|NSCEBXM7ZM]] is bounded on $L^p(w)$, $1 < p < \infty$.
Coifman and Fefferman extended the sufficiency to general Calderón–Zygmund operators.
The theorem is the starting point of weighted theory, including extrapolation and the sharp dependence of operator norms on $[w]_{A_p}$.
