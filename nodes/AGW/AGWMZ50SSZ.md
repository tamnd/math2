---
tag: AGWMZ50SSZ
kind: statement
role: theorem
name: Khintchine inequality
msc: ["60E15", 42A61, 46B09]
uses: [0PNRKMRC55, 0WQNRCNY3M]
about: [0PNRKMRC55]
sources:
  - url: https://en.wikipedia.org/wiki/Khintchine_inequality
same_as:
  wikidata: Q6401711
  wikipedia: Khintchine inequality
---

## Statement

Let $0 < p < \infty$.
Let $\varepsilon_1, \varepsilon_2, \ldots$ be independent [[random variables|0PNRKMRC55]] with $\Pr(\varepsilon_k = 1) = \Pr(\varepsilon_k = -1) = 1/2$.
Then there are constants $A_p > 0$ and $B_p > 0$, depending only on $p$, with the following property.
For every $N \ge 1$ and all real numbers $a_1, \ldots, a_N$,
$$A_p \Big( \sum_{k=1}^{N} a_k^2 \Big)^{1/2} \le \Big( \mathbb{E} \Big\lvert \sum_{k=1}^{N} a_k \varepsilon_k \Big\rvert^p \Big)^{1/p} \le B_p \Big( \sum_{k=1}^{N} a_k^2 \Big)^{1/2},$$
where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]].

## Remarks

For $p = 2$ the middle term equals $\left(\sum a_k^2\right)^{1/2}$ exactly, since $\mathbb{E}[\varepsilon_j \varepsilon_k] = 0$ for $j \ne k$.
So one can take $A_p = 1$ for $p \ge 2$ and $B_p = 1$ for $p \le 2$, by monotonicity of $L^p$ norms on a probability space.

Proof idea for the upper bound: normalize to $\sum a_k^2 = 1$.
Since $\cosh t \le e^{t^2/2}$, independence gives $\mathbb{E} \exp\left(t \sum a_k \varepsilon_k\right) \le e^{t^2/2}$ for all real $t$.
This gives the tail bound $\Pr\left(\abs{\sum a_k \varepsilon_k} > s\right) \le 2 e^{-s^2/2}$, and integrating the tail bounds every moment.
The lower bound for $p < 2$ follows from the upper bound for some $q > 2$ by Hölder's inequality, which places $L^2$ between $L^p$ and $L^q$.

Example: for $N = 2$, $a_1 = a_2 = 1$ and $p = 1$, the sum $\varepsilon_1 + \varepsilon_2$ is $\pm 2$ with probability $1/2$ and $0$ otherwise, so $\mathbb{E}\abs{\varepsilon_1 + \varepsilon_2} = 1 = \frac{1}{\sqrt 2} \cdot \sqrt 2$.
This shows that $A_1 \le 1/\sqrt 2$; Szarek proved that $A_1 = 1/\sqrt 2$ is the best constant.

## Explanations

### L1 human

Flip $N$ fair coins and add the numbers $a_k$ with random signs.
The typical size of the result is the square root of the sum of the squares of the $a_k$, as in Pythagoras' theorem.
Khintchine's inequality says this holds for every way of measuring "typical size" by a $p$-th moment, up to a constant factor.
So random sign sums behave like Gaussian variables with the same variance.

### L2 human

In harmonic analysis the $\varepsilon_k$ are realized as the Rademacher functions $r_k(t) = \operatorname{sgn} \sin(2^k \pi t)$ on $[0, 1]$, and the inequality says that all $L^p$ norms are equivalent on their span.
Combined with Fubini's theorem it turns square-function estimates into estimates for random sums, a basic step in Littlewood–Paley theory.
In Banach space theory it is the starting point of the notions of type and cotype.
