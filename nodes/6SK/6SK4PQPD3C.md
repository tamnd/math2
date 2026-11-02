---
tag: 6SK4PQPD3C
kind: statement
role: theorem
name: Gagliardo–Nirenberg interpolation inequality
msc: ["46E35", 26D10]
uses: [C3EC148VZD, SASP14MA1Z, B03CA692K3]
about: [M4CEZ5K9HP]
sources:
  - url: https://en.wikipedia.org/wiki/Gagliardo%E2%80%93Nirenberg_interpolation_inequality
same_as:
  wikidata: Q5516877
  wikipedia: Gagliardo–Nirenberg interpolation inequality
---

## Statement

Let $n \ge 1$, let $j$ and $m$ be integers with $0 \le j < m$, and let $1 \le q, r \le \infty$.
Let $\theta$ be a real number with $j/m \le \theta \le 1$, and define $p$ by
$$\frac{1}{p} = \frac{j}{n} + \theta \Big( \frac{1}{r} - \frac{m}{n} \Big) + \frac{1 - \theta}{q},$$
assuming that $1 \le p \le \infty$.
For an integer $k \ge 0$ write $\abs{D^k u}$ for the Euclidean norm of the vector of all partial derivatives of $u$ of order $k$.
Assume that it is not the case that $1 < r < \infty$, $m - j - n/r$ is a nonnegative integer and $\theta = 1$.
Then there is a constant $C = C(n, m, j, q, r, \theta)$ such that
$$\norm{D^j u}_{L^p(\R^n)} \le C \, \norm{D^m u}_{L^r(\R^n)}^{\theta} \, \norm{u}_{L^q(\R^n)}^{1 - \theta}$$
for every smooth function $u \colon \R^n \to \R$ with compact support.

## Remarks

The relation defining $p$ is forced by scaling: under $u(x) \mapsto u(\lambda x)$ both sides must change by the same power of $\lambda$.
The proof combines the [[Sobolev inequality|B03CA692K3]] with one-dimensional bounds obtained by integration by parts, such as $\norm{u'}_{L^{p}(\R)}^2 \le C \norm{u}_{L^{q}(\R)} \norm{u''}_{L^{r}(\R)}$ for $\frac{2}{p} = \frac{1}{q} + \frac{1}{r}$.
The inequality extends by density to functions in $L^q(\R^n)$ whose [[weak derivatives|C3EC148VZD]] of order $m$ lie in $L^r(\R^n)$, with an extra condition at infinity when $j = 0$, $rm < n$ and $q = \infty$.

The excluded case is a real exception.
For $n = 2$, $m = 1$, $j = 0$ and $r = 2$, the choice $\theta = 1$ gives $p = \infty$, and the inequality $\norm{u}_{L^\infty} \le C \norm{\nabla u}_{L^2}$ fails on $\R^2$.

A common special case is Ladyzhenskaya's inequality in the plane: $\norm{u}_{L^4(\R^2)}^2 \le C \norm{u}_{L^2(\R^2)} \norm{\nabla u}_{L^2(\R^2)}$, which is the case $n = 2$, $j = 0$, $m = 1$, $q = r = 2$, $\theta = 1/2$.

## Explanations

### L1 human

The inequality bounds an intermediate quantity by two extreme ones: a lower derivative is controlled by the function and a higher derivative together.
It is like saying that if a curve is not too high and does not bend too much, then its slope cannot be too large.
The weights $\theta$ and $1 - \theta$ say how much each of the two extremes contributes.

### L2 human

In nonlinear evolution equations one usually controls the $L^q$ norm of a solution by a conservation law and some higher derivative by an energy estimate.
The Gagliardo–Nirenberg inequality then bounds the intermediate norms that appear in the nonlinear terms.
For $\theta = 1$ and $j = 0$, $m = 1$, it reduces to the [[Sobolev inequality|B03CA692K3]] on $\R^n$.
It is a basic tool for the Navier–Stokes and nonlinear Schrödinger equations.
