---
tag: HMC733EFMD
kind: statement
role: theorem
name: Abel–Plana formula
msc: [65B15, "30E20", 40A25]
uses: [0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Abel–Plana_formula
same_as:
  wikidata: Q4666730
  wikipedia: Abel–Plana formula
---

## Statement

Let $f$ be continuous on the closed half-plane $\set{z \in \C : \operatorname{Re} z \ge 0}$ and [[holomorphic|0NAHXR1FRH]] on the open half-plane $\operatorname{Re} z > 0$.
Assume there are constants $C > 0$ and $\varepsilon > 0$ with $\abs{f(z)} \le C / \abs{z}^{1 + \varepsilon}$ for all $z \ne 0$ with $\operatorname{Re} z \ge 0$.
Then
$$\sum_{n=0}^{\infty} f(n) = \int_0^\infty f(x)\,dx + \frac{f(0)}{2} + i \int_0^\infty \frac{f(it) - f(-it)}{e^{2\pi t} - 1}\,dt.$$

## Remarks

Proof idea: the kernels $1/(e^{\mp 2\pi i z} - 1)$ have simple poles at the integers.
Apply the residue theorem to $f$ times such a kernel on large rectangles in the upper and the lower quarter planes, with one side on the imaginary axis.
The residues at the integers produce the sum, the decay of $f$ kills the far sides, and the sides on the imaginary axis give the last integral.

Example: $f(z) = 1/(z + 1)^2$ satisfies the hypotheses with $\varepsilon = 1$, since $\abs{z + 1} \ge \abs{z}$ when $\operatorname{Re} z \ge 0$.
Here $f(it) - f(-it) = -4it/(1 + t^2)^2$, so the formula reads
$$\frac{\pi^2}{6} = 1 + \frac12 + 4 \int_0^\infty \frac{t}{(1 + t^2)^2 (e^{2\pi t} - 1)}\,dt.$$
Applied to $f(z) = (z + a)^{-s}$ it gives an integral formula for the [[Hurwitz zeta function|G4SW7HJG88]].

Some decay or growth condition is needed for both sides to make sense: for $f = 1$ the series and the integral $\int_0^\infty f$ both diverge.

## Explanations

### L1 human

The formula compares a sum $f(0) + f(1) + f(2) + \cdots$ with the integral $\int_0^\infty f$.
The difference is half of the first term plus a correction that only uses the values of $f$ on the imaginary axis.
This correction is often small and easy to estimate, because of the rapidly growing factor $e^{2\pi t}$.
So the formula turns hard sums into integrals.

### L2 human

The Abel–Plana formula is an exact alternative to the [[Euler–Maclaurin formula|9P839VB8S7]] for functions that extend holomorphically to the right half-plane.
Euler–Maclaurin gives an asymptotic series with Bernoulli numbers, while Abel–Plana gives one convergent integral.
Expanding $f(it) - f(-it)$ in powers of $t$ and integrating term by term recovers the Euler–Maclaurin terms, since $\int_0^\infty t^{2k-1} / (e^{2\pi t} - 1)\,dt$ is a multiple of a Bernoulli number.
It is a standard tool for the zeta functions and for the analytic continuation of series in physics, such as the computation of Casimir energies.
