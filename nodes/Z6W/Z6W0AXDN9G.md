---
tag: Z6W0AXDN9G
kind: statement
role: proposition
name: Scaling relations among critical exponents
msc: [82B27, 82B28]
uses: [SQ41AZGZ2P, KC0Q95A2ED, ENWMTRJRND]
about: [SQ41AZGZ2P]
sources:
  - url: https://en.wikipedia.org/wiki/Critical_exponent
---

## Statement

Consider a system in dimension $d$ near a critical point, with the [[critical exponents|SQ41AZGZ2P]] $\alpha, \beta, \gamma, \delta, \nu, \eta$.
Assume the [[Widom scaling hypothesis|KC0Q95A2ED]] for the singular free energy $f_s(t, h)$.
Assume also that, at $h = 0$, the two-point [[correlation function|ENWMTRJRND]] has the scaling form $G(x, t) = \abs{x}^{-(d - 2 + \eta)} \, g(\abs{x} / \xi)$ with $\xi \sim \abs{t}^{-\nu}$, and that $f_s \sim \xi^{-d}$.
Then:

1. Rushbrooke: $\alpha + 2\beta + \gamma = 2$;
2. Widom: $\gamma = \beta(\delta - 1)$;
3. Fisher: $\gamma = \nu(2 - \eta)$;
4. Josephson, or hyperscaling: $d \nu = 2 - \alpha$.

## Remarks

Relations 1 and 2 follow from the exponents $\alpha = 2 - 1/a$, $\beta = (1 - b)/a$, $\gamma = (2b - 1)/a$ and $\delta = b/(1 - b)$ given by the Widom hypothesis.
For relation 3, the susceptibility is the integral of $G$ over space, and the substitution $x = \xi y$ gives $\chi \sim \xi^{2 - \eta} \sim \abs{t}^{-\nu(2 - \eta)}$.
For relation 4, $f_s \sim \xi^{-d} \sim \abs{t}^{d\nu}$, while $f_s \sim \abs{t}^{2 - \alpha}$ by the definition of $\alpha$.

Example: the two-dimensional Ising model has $\alpha = 0$, $\beta = 1/8$, $\gamma = 7/4$, $\delta = 15$, $\nu = 1$ and $\eta = 1/4$.
All four relations hold: $0 + 1/4 + 7/4 = 2$, $\frac{1}{8} \cdot 14 = \frac{7}{4}$, $1 \cdot (2 - \frac{1}{4}) = \frac{7}{4}$ and $2 \cdot 1 = 2 - 0$.

The hypothesis $f_s \sim \xi^{-d}$ is necessary for relation 4.
Mean-field exponents $\alpha = 0$ and $\nu = 1/2$ satisfy $d\nu = 2 - \alpha$ only for $d = 4$, and above four dimensions hyperscaling fails while relations 1 to 3 still hold.

## Explanations

### L1 human

Near a critical point there are six standard exponents, but they are not independent.
Four simple equations tie them together, so two of them determine the rest.
The equations come from the idea that near the critical point the system has only one relevant length, the correlation length.

### L2 human

The relations 1 and 2 involve only thermodynamics, and the [[Rushbrooke inequality|BJ8QPXCCF5]] shows that relation 1 holds at least as an inequality in general.
The relations 3 and 4 involve the correlation length, and relation 4 contains the dimension $d$ explicitly.
The renormalization group derives all four from two scaling dimensions at a fixed point.
They are used to check numerical estimates of exponents and to compute the missing ones from the measured ones.
