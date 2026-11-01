---
tag: XGZ2YYCNWK
kind: definition
name: Analytic combinatorics
msc: [05A16, 05A15, 30B10]
defines: YJK71RKVEB
uses: [0PHAC833JF, 0N288P2TB5, 081WKEDK6C, EX382NQTGP]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_combinatorics
---

## Definition

Let $(a_n)_{n \ge 0}$ be a sequence of counts with [[generating function|0PHAC833JF]] $A(z) = \sum_{n} a_n z^n$ or $\sum_n a_n z^n / n!$.
*Analytic combinatorics* is the branch of [[enumerative combinatorics|EX382NQTGP]] that derives the asymptotic behaviour of $a_n$ as $n \to \infty$ from $A$.
Here $A$ is viewed as an [[analytic function|081WKEDK6C]] of a complex variable $z$.
Its main methods are:

1. location of the dominant singularities, which fixes the exponential growth rate;
2. singularity analysis, which transfers the local behaviour of $A$ near a dominant singularity to the coefficients;
3. saddle-point estimates of the Cauchy coefficient integral, mainly for entire functions $A$.

## Remarks

The basic principle is the Cauchy–Hadamard formula.
If $A$ has [[radius of convergence|0N288P2TB5]] $\rho$ with $0 < \rho < \infty$, then $\limsup_{n \to \infty} \abs{a_n}^{1/n} = 1/\rho$.
When $a_n \ge 0$, Pringsheim's theorem says that $z = \rho$ is itself a singularity of $A$.

Example: the Catalan generating function is $C(z) = \frac{1 - \sqrt{1 - 4z}}{2z}$.
Its dominant singularity is $z = 1/4$, where $C$ behaves like $2 - 2\sqrt{1 - 4z}$.
Singularity analysis then gives $C_n \sim \frac{4^n}{\sqrt{\pi}\, n^{3/2}}$.

Non-example: a proof that $\binom{2n}{n} \le 4^n$ by counting subsets is not analytic combinatorics.
It uses no property of a generating function as a function of a complex variable.
