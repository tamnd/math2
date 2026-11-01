---
tag: 4CDFMKKZ01
kind: statement
role: theorem
name: Quartic formula
msc: ["12E12", 12D10]
uses: [00EHX6FWC0, J7YS0DA3HQ, FB6J5WAT5V]
about: [J7YS0DA3HQ]
sources:
  - url: https://en.wikipedia.org/wiki/Quartic_equation
---

## Statement

Let $a, b, c, d, e \in \C$ with $a \ne 0$.
Put
$$p = \frac{8ac - 3b^2}{8a^2}, \qquad q = \frac{b^3 - 4abc + 8a^2 d}{8a^3}, \qquad r = \frac{16ab^2c - 3b^4 - 64a^2bd + 256a^3e}{256a^4}.$$
Then $x$ is a [[root|00EHX6FWC0]] of $ax^4 + bx^3 + cx^2 + dx + e$ if and only if $y = x + \frac{b}{4a}$ is a root of $y^4 + py^2 + qy + r$.
Assume $q \ne 0$.
Let $m$ be a root of the resolvent cubic
$$8m^3 + 8pm^2 + (2p^2 - 8r)m - q^2,$$
and let $s$ be a square root of $2m$.
Then $m \ne 0$, $s \ne 0$, and the four roots of $y^4 + py^2 + qy + r$, counted with multiplicity, are
$$\frac{s \pm \sqrt{-2p - 2m - 2q/s}}{2} \qquad \text{and} \qquad \frac{-s \pm \sqrt{-2p - 2m + 2q/s}}{2},$$
where $\sqrt{z}$ denotes either square root of $z$.

## Remarks

Since $q \ne 0$, the constant term $-q^2$ of the resolvent cubic is nonzero, so $m \ne 0$.
The resolvent cubic says exactly that $(y^2 + \frac{p}{2} + m)^2 - (y^4 + py^2 + qy + r) = 2my^2 - qy + (m^2 + pm + \frac{p^2}{4} - r)$ is the square $(sy - \frac{q}{2s})^2$.
So the quartic factors as $(y^2 + sy + \frac{p}{2} + m - \frac{q}{2s})(y^2 - sy + \frac{p}{2} + m + \frac{q}{2s})$, and the quadratic formula gives the four roots.
The resolvent cubic itself is solved by the [[cubic formula|FB6J5WAT5V]], so all roots are radical expressions in the coefficients.
If $q = 0$, the equation $y^4 + py^2 + r = 0$ is a quadratic in $y^2$, and $y^2 = \frac{-p \pm \sqrt{p^2 - 4r}}{2}$.
Example: for $y^4 - 2y^2 + 8y - 3$, the value $m = 2$ is a root of $8m^3 - 16m^2 + 32m - 64$, so $s = 2$ and the factors are $y^2 + 2y - 1$ and $y^2 - 2y + 3$.

## Explanations

### L1 human

The quartic formula gives the roots of any equation of degree $4$ using arithmetic, square roots and cube roots.
The trick is to add a well-chosen quantity $m$ to both sides so that both become perfect squares.
Finding $m$ needs a cubic equation, which the cubic formula solves.

### L2 human

This method is due to Ferrari, and it shows that every quartic is [[solvable by radicals|J7YS0DA3HQ]].
In Galois terms, $S_4$ is solvable, with the normal subgroup $V_4$ of order $4$ and quotient $S_3$.
If $y_1, y_2, y_3, y_4$ are the roots, each root $m$ of the resolvent cubic has the form $\frac{1}{2}(y_i + y_j)^2$, and $(y_1 + y_2)^2$ is fixed by $V_4$.
This is why a cubic appears.
For degree $5$ no such reduction exists, by the [[Abel–Ruffini theorem|163A2WQQJX]].
