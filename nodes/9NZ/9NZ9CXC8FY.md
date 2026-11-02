---
tag: 9NZ9CXC8FY
kind: statement
role: lemma
name: Hadamard's inequality in Fredholm theory
msc: [45B05, 15A45]
uses: [CGDN1X32NQ, ZM5G144PZG, PPX0AK81QV, HP5VJ9EBST, 0G4F0XB9X2]
about: [PPX0AK81QV]
sources:
  - url: https://en.wikipedia.org/wiki/Hadamard%27s_inequality
---

## Statement

Let $a < b$, let $K \colon [a, b] \times [a, b] \to \C$ be a [[continuous kernel|ZM5G144PZG]], and let $M = \max \abs{K}$.
Then for every $n \ge 1$ and all $x_1, \dots, x_n, y_1, \dots, y_n \in [a, b]$,
$$\abs{\det[K(x_i, y_j)]_{i,j=1}^{n}} \le n^{n/2} M^n.$$
Consequently, the $n$-th coefficient $c_n = \frac{1}{n!} \int_{[a, b]^n} \det[K(x_i, x_j)] \, dx$ of the [[Fredholm determinant|PPX0AK81QV]] satisfies
$$\abs{c_n} \le \frac{n^{n/2} \, M^n (b - a)^n}{n!},$$
and the series $\sum_n (-1)^n c_n \lambda^n$ converges for every $\lambda \in \C$.

## Remarks

The first bound is [[Hadamard's inequality|CGDN1X32NQ]] for the matrix $[K(x_i, y_j)]$: each column has $n$ entries of modulus at most $M$, so its Euclidean norm is at most $\sqrt{n} M$.
Integrating over $[a, b]^n$ gives the bound on $c_n$.
By Stirling's formula $n! \ge (n/e)^n$, so $\abs{c_n \lambda^n} \le \left(e M (b - a) \abs{\lambda}\right)^n / n^{n/2}$, and the $n$-th root of this tends to $0$.
Hence the radius of convergence is infinite, and $D$ is an [[entire function|0G4F0XB9X2]].

The same argument, applied to matrices of size $n + k$, shows that the series defining the [[Fredholm minors|HP5VJ9EBST]] converge for every $\lambda$, uniformly in the fixed points.

The crude bound $\abs{\det} \le n! \, M^n$, from expanding the determinant into $n!$ products, is not enough: it only gives $\abs{c_n} \le (M (b - a))^n$ and hence convergence for $\abs{\lambda} < 1 / (M (b - a))$.
The factor $n^{n/2}$ instead of $n!$ is what makes the whole theory work for every $\lambda$.

## Explanations

### L1 human

A determinant of size $n$ is a sum of $n!$ products, and that number grows very fast.
Hadamard's inequality shows that the determinant itself grows much more slowly, like $n^{n/2}$.
This is why the Fredholm determinant, a power series built from such determinants divided by $n!$, converges for every value of the parameter.

### L2 human

Fredholm needed exactly this estimate to show that his determinant and minors are entire functions of $\lambda$.
Without it, his formulas would only work near $\lambda = 0$, where the Neumann series already does the job.
