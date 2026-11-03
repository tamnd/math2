---
tag: KVS235Z4HR
kind: problem
name: Multivariate moment problem
msc: [44A60, 14P10, 47A57]
uses: [CS7TWHY7JM, PR11BZQQPG, 0PJXBR6QA3, 07GNX8GCYP, FQTXV6BQZG, BX5WSK8ZCT]
about: [CS7TWHY7JM, 01XAHPADBA]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_problem
history:
  posed_by: "T. H. Hildebrandt and I. J. Schoenberg"
  first_stated: "1933"
  notes: "Hildebrandt and Schoenberg solved the moment problem on the unit cube in several dimensions in 1933, the earliest known multivariate treatment. Haviland extended the approach to arbitrary closed sets in 1935 and 1936."
---

## Problem

Let $d \ge 1$ and let $K$ be a closed subset of $\R^d$.
For a [[multi-index|0PJXBR6QA3]] $\alpha = (\alpha_1, \ldots, \alpha_d) \in \N^d$ write $x^\alpha = x_1^{\alpha_1} \cdots x_d^{\alpha_d}$.
Let $(m_\alpha)_{\alpha \in \N^d}$ be a family of real numbers.

1. Existence: decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on $\R^d$ with [[support|FQTXV6BQZG]] in $K$ and the following property. Every $x^\alpha$ is $\mu$-integrable and $m_\alpha = \int x^\alpha \, d\mu(x)$ for all $\alpha \in \N^d$.
2. Uniqueness: when such a measure exists, decide whether it is the only one.

## Remarks

For $d = 1$ this is the classical [[moment problem|CS7TWHY7JM]].
Let $L$ be the linear functional on the real [[polynomials|07GNX8GCYP]] in $x_1, \ldots, x_d$ with $L(x^\alpha) = m_\alpha$.
The Riesz–Haviland theorem says that a solution exists if and only if $L(p) \ge 0$ for every polynomial $p$ with $p \ge 0$ on $K$.
For $d = 1$ and $K = \R$ every nonnegative polynomial is a sum of squares, so this reduces to positivity of Hankel matrices.
For $d \ge 2$ there are nonnegative polynomials that are not sums of squares, and the condition $L(p^2) \ge 0$ for all $p$ is no longer sufficient for $K = \R^d$.
For a compact basic closed [[semialgebraic set|BX5WSK8ZCT]] $K = \set{x : g_1(x) \ge 0, \ldots, g_r(x) \ge 0}$, Schmüdgen's theorem gives a solution if and only if $L(\sigma g_1^{e_1} \cdots g_r^{e_r}) \ge 0$ for every sum of squares $\sigma$ and every $e \in \set{0, 1}^r$.
Example: the family $m_\alpha = \prod_{i=1}^{d} 1/(\alpha_i + 1)$ is solved by Lebesgue measure on the cube $[0, 1]^d$, and the solution is unique since $K$ is compact.

## Explanations

### L1 human

The moments of a mass distribution in the plane or in space are averages of products of powers of the coordinates, such as $x$, $y$, $x^2$, $xy$ and $y^2$.
The multivariate moment problem asks whether a given table of such numbers comes from some mass distribution, and whether that distribution is unique.
In one variable a test with positive matrices settles the existence question.
In several variables this test is not enough, because a polynomial can be nonnegative everywhere without being a sum of squares.
This links the problem to real algebraic geometry and to optimization over polynomials.
