---
tag: ZBNQEJ09QE
kind: definition
name: Power series in several variables
msc: [32A05]
defines: R3QTCPTJK7
uses: [BH57D2FBNR, 0PJXBR6QA3, 0YBDSJARWN]
sources:
  - url: https://en.wikipedia.org/wiki/Power_series
---

## Definition

Let $n \ge 1$ and let $\N^n$ be the set of [[multi-indices|0PJXBR6QA3]] $\alpha = (\alpha_1, \dots, \alpha_n)$ with $\alpha_j \ge 0$ integers.
For $w \in \C^n$, write $w^\alpha = w_1^{\alpha_1} \cdots w_n^{\alpha_n}$, with $w_j^0 = 1$.
Let $a \in \C^n$ and let $(c_\alpha)_{\alpha \in \N^n}$ be complex numbers.
The *power series* with centre $a$ and coefficients $c_\alpha$ is the formal sum
$$\sum_{\alpha \in \N^n} c_\alpha (z - a)^\alpha.$$
It *converges* at $z \in \C^n$ if $\sum_{\alpha \in \N^n} \abs{c_\alpha} \abs{(z - a)^\alpha} < \infty$.
Its *sum* at such a point is the sum of the family $(c_\alpha (z - a)^\alpha)_\alpha$, which does not depend on the order of the terms.

## Remarks

Convergence here is [[absolute convergence|0YBDSJARWN]], since the index set $\N^n$ has no preferred order when $n \ge 2$.
Example: for $n = 2$, $a = 0$ and $c_\alpha = 1$ for all $\alpha$, at $z = (1/2, 1/3)$ the sum of absolute values is $\sum_j 2^{-j} \sum_k 3^{-k} = 2 \cdot \tfrac32 = 3 < \infty$, so the series converges, with sum $3$.
Non-example: the same series at $z = (1/2, 1)$ has the terms $2^{-j}$ with $k$ arbitrary, so the sum of absolute values is infinite and the series does not converge there.
Grouping by total degree $\abs{\alpha} = \alpha_1 + \cdots + \alpha_n$ writes the series as $\sum_{m \ge 0} P_m(z - a)$, with $P_m$ a homogeneous polynomial of degree $m$.
For $n = 1$ this is the ordinary [[power series|0MZB06ST2B]], and in that case absolute convergence holds at every point inside the disc of convergence.
