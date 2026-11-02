---
tag: QADCFWETJC
kind: statement
role: theorem
name: Rubio de Francia extrapolation theorem
msc: [42B25, 42B20]
uses: [T86RSJ8M86, SASP14MA1Z, VX1A56P5KQ, S9BKNBRV4H]
about: [T86RSJ8M86]
sources:
  - url: https://en.wikipedia.org/wiki/Muckenhoupt_weights
---

## Statement

Let $n \ge 1$ and $1 \le p_0 < \infty$.
For a weight $w$ on $\R^n$ and $1 \le p < \infty$, write $\norm{g}_{L^p(w)} = \left( \int_{\R^n} \abs{g}^p \, w \, dx \right)^{1/p}$, and let $[w]_{A_p}$ be the constant of the [[Muckenhoupt class|T86RSJ8M86]] $A_p$.
Let $\mathcal{F}$ be a family of pairs $(f, g)$ of nonnegative measurable functions on $\R^n$.
Assume that there is an increasing function $N \colon [1, \infty) \to [0, \infty)$ such that
$$\norm{f}_{L^{p_0}(w)} \le N([w]_{A_{p_0}}) \, \norm{g}_{L^{p_0}(w)}$$
for every $w \in A_{p_0}$ and every $(f, g) \in \mathcal{F}$ with $\norm{f}_{L^{p_0}(w)} < \infty$.
Then let $1 < p < \infty$ and $w \in A_p$.
There is a constant $C$, depending only on $n$, $p$, $p_0$, $N$ and $[w]_{A_p}$, such that
$$\norm{f}_{L^p(w)} \le C \norm{g}_{L^p(w)}$$
for every $(f, g) \in \mathcal{F}$ with $\norm{f}_{L^p(w)} < \infty$.

## Remarks

In the typical use, the pairs are $(\abs{Tf}, \abs{f})$ for an operator $T$.
Assume $T$ is bounded on $L^{p_0}(w)$ for all $w \in A_{p_0}$, with a bound depending only on $[w]_{A_{p_0}}$.
Then $T$ is bounded on $L^p(w)$ for all $1 < p < \infty$ and all $w \in A_p$.
In particular, taking $w = 1$, one exponent $p_0$ gives unweighted bounds for all $1 < p < \infty$.

The proof uses the Rubio de Francia algorithm.
Let $v$ be a weight and $q > 1$ such that the [[maximal operator|VX1A56P5KQ]] $M$ is bounded on $L^q(v)$, with norm $\norm{M}$.
For $h \ge 0$ in $L^q(v)$, set $Rh = \sum_{k \ge 0} \frac{M^k h}{(2\norm{M})^k}$, where $M^k$ is the $k$-th iterate.
Then $h \le Rh$, $\norm{Rh}_{L^q(v)} \le 2 \norm{h}_{L^q(v)}$, and $M(Rh) \le 2 \norm{M} \, Rh$, so $Rh$ is an $A_1$ weight.
These $A_1$ weights are combined into an $A_{p_0}$ weight to which the hypothesis applies, and [[Muckenhoupt's theorem|S9BKNBRV4H]] controls the constants.

## Explanations

### L1 human

Proving an inequality for one exponent $p$ is often much easier than for all of them, for example $p = 2$ where Fourier methods work.
Extrapolation says that if the inequality holds for one exponent and for all Muckenhoupt weights at that exponent, then it holds for all exponents $1 < p < \infty$ and all corresponding weights.
So weights act as a bridge between different exponents.

### L2 human

The theorem is a main reason to prove weighted inequalities.
A single weighted $L^2$ bound for a Calderón–Zygmund operator, a commutator or a square function yields all the $L^p$ bounds, weighted and unweighted.
It also gives vector-valued inequalities almost for free, since a sum $\left( \sum_j \abs{T f_j}^q \right)^{1/q}$ can be treated by applying the pair formulation to suitable functions.
It relies on the theory of $A_p$ weights, in particular on Muckenhoupt's theorem and on the factorization of $A_p$ weights as $w = w_1 w_2^{1 - p}$ with $w_1, w_2 \in A_1$.
