---
tag: YM68BCKBXC
kind: statement
role: theorem
name: Multiplication theorem
msc: [33B15, 11B68, 11M35]
uses: [0H5SYBSED9, BXQKBJJGFG, G4SW7HJG88, HWRRXB0YXS, Y4759V8CY6]
about: [0H5SYBSED9, BXQKBJJGFG, G4SW7HJG88, HWRRXB0YXS]
sources:
  - url: https://en.wikipedia.org/wiki/Multiplication_theorem
same_as:
  wikidata: Q98831
  wikipedia: Multiplication theorem
---

## Statement

Let $m \ge 1$ be an integer.

1. For the [[gamma function|0H5SYBSED9]] and every $z \in \C$ with $mz \notin \set{0, -1, -2, \dots}$,
$$\prod_{k=0}^{m-1} \Gamma\!\left(z + \frac{k}{m}\right) = (2\pi)^{(m-1)/2}\, m^{1/2 - mz}\, \Gamma(mz).$$
2. For the [[digamma function|HWRRXB0YXS]] $\psi = \Gamma'/\Gamma$ and the same $z$,
$$\psi(mz) = \ln m + \frac{1}{m} \sum_{k=0}^{m-1} \psi\!\left(z + \frac{k}{m}\right).$$
3. For the [[Bernoulli polynomials|BXQKBJJGFG]] $B_n$, $n \ge 0$, and every $x \in \C$,
$$B_n(mx) = m^{n-1} \sum_{k=0}^{m-1} B_n\!\left(x + \frac{k}{m}\right).$$
4. For the [[Hurwitz zeta function|G4SW7HJG88]] $\zeta(s, a) = \sum_{j \ge 0} (j + a)^{-s}$, every real $x > 0$ and every $s$ with $\operatorname{Re} s > 1$,
$$\sum_{k=0}^{m-1} \zeta\!\left(s, x + \frac{k}{m}\right) = m^{s} \zeta(s, mx).$$

## Remarks

Part 1 is the [[Gauss multiplication formula|Y4759V8CY6]], and part 2 follows from it by taking the logarithmic derivative.
Part 4 comes from splitting the sum defining $\zeta(s, mx) = m^{-s} \sum_{j \ge 0} (j/m + x)^{-s}$ according to the residue $k$ of $j$ modulo $m$.
Part 3 follows from the generating function $t e^{xt}/(e^t - 1) = \sum_n B_n(x) t^n/n!$: summing over $k$ gives a geometric sum that collapses to the generating function at $mx$ with $t$ replaced by $t/m$.
For $m = 2$, part 1 is the Legendre duplication formula, and part 3 gives $B_n(2x) = 2^{n-1}\big(B_n(x) + B_n(x + \tfrac{1}{2})\big)$.
At $x = 0$ and $n = 1$ this reads $B_1(0) = B_1(0) + B_1(\tfrac{1}{2})$, consistent with $B_1(\tfrac{1}{2}) = 0$.

## Explanations

### L1 human

Several classical functions have a rule for what happens when the argument is multiplied by a whole number $m$.
The value at $mx$ can be recovered from the values at the $m$ evenly spaced points $x, x + 1/m, \dots, x + (m-1)/m$.
These rules hold for the gamma function, for the Bernoulli polynomials and for the Hurwitz zeta function, among others.

### L2 human

All these functions satisfy a simple difference equation in $x$, such as $\Gamma(x + 1) = x\Gamma(x)$ or $B_n(x + 1) - B_n(x) = n x^{n-1}$.
The sum or product over the $m$ shifted points satisfies the same kind of equation in the variable $mx$.
A uniqueness argument for that difference equation identifies it with the function at $mx$.
For the gamma function this uniqueness is the Bohr–Mollerup theorem.
The formulas are used to compute special values, such as $\Gamma(1/2) = \sqrt{\pi}$, and they connect to distribution relations in number theory.
