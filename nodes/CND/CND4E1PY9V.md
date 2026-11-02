---
tag: CND4E1PY9V
kind: statement
role: theorem
name: Legendre duplication formula
msc: [33B15]
uses: [0V3FZMVB4K, 0NSD1TPHR0]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplication_theorem
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$.
For every $z \in \C$ with $2z \notin \set{0, -1, -2, \ldots}$,
$$\Gamma(z) \, \Gamma\!\left(z + \tfrac12\right) = 2^{1 - 2z} \sqrt{\pi} \; \Gamma(2z),$$
where $2^{1-2z} = e^{(1-2z)\ln 2}$.

## Remarks

One proof applies the [[Bohr–Mollerup theorem|QFF87AXWN2]] to $f(x) = 2^{x-1}\Gamma(\tfrac{x}{2})\Gamma(\tfrac{x+1}{2})/\sqrt{\pi}$ for $x > 0$: it satisfies $f(1) = 1$, $f(x+1) = x f(x)$, and $\ln f$ is convex, so $f = \Gamma$; then put $x = 2z$.
Another proof uses the [[beta function|QHNWVSC6AQ]]: the substitution $t \mapsto 4t(1-t)$ gives $B(z, z) = 2^{1-2z} B(z, \tfrac12)$.
The identity theorem extends the formula from $(0, \infty)$ to all allowed complex $z$.
Check at $z = 1$: the left side is $\Gamma(1)\Gamma(\tfrac32) = \tfrac{\sqrt{\pi}}{2}$, and the right side is $2^{-1}\sqrt{\pi}\,\Gamma(2) = \tfrac{\sqrt{\pi}}{2}$.
It is the case $m = 2$ of the [[Gauss multiplication formula|Y4759V8CY6]].
In Mathlib the statement is `Complex.Gamma_mul_Gamma_add_half`.

## Explanations

### L1 human

The duplication formula expresses $\Gamma$ at a doubled argument through two values of $\Gamma$ at half that size, half a unit apart.
For whole numbers it is a statement about factorials: $(2n)! = \frac{4^n}{\sqrt{\pi}}\, n! \, \Gamma(n + \tfrac12)$.

### L2 human

The formula is how one computes $\Gamma$ at half-integers, giving $\Gamma(n + \tfrac12) = \frac{(2n)!}{4^n n!}\sqrt{\pi}$.
It appears in the functional equation of the Riemann zeta function, where it converts between the symmetric form with $\Gamma(s/2)$ and the form with $\Gamma(s)$ and a cosine.
It also gives the volume of the unit ball in odd dimensions in closed form.
