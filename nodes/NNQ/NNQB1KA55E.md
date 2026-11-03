---
tag: NNQB1KA55E
kind: statement
role: theorem
name: Neumann formula for mutual inductance
msc: [78A30]
uses: [K1STN67XQ0, RA4GE6185Q, 8PEMR2J7EF, 0H5MR9B6GT, 0AKRKVHW94]
about: [K1STN67XQ0]
sources:
  - url: https://en.wikipedia.org/wiki/Inductance
---

## Statement

Let $C_1$ and $C_2$ be disjoint closed piecewise $C^1$ curves in $\R^3$, each modelling a thin wire in vacuum.
Let $\mu_0 > 0$ be the vacuum permeability.
Then the [[mutual inductance|K1STN67XQ0]] of $C_1$ and $C_2$ is the double integral
$$M_{12} = \frac{\mu_0}{4 \pi} \oint_{C_1} \oint_{C_2} \frac{d\ell_1 \cdot d\ell_2}{\abs{x_1 - x_2}},$$
where $x_1 \in C_1$, $x_2 \in C_2$.
Here $d\ell_1$ and $d\ell_2$ are the oriented line elements.
In particular $M_{12} = M_{21}$.

## Remarks

A steady current $I_1$ in $C_1$ has the [[magnetic vector potential|8PEMR2J7EF]] $A_1(x) = \frac{\mu_0 I_1}{4 \pi} \oint_{C_1} \frac{d\ell_1}{\abs{x - x_1}}$, whose curl is the field given by the [[Biot–Savart law|RA4GE6185Q]].
By [[Stokes' theorem|0AKRKVHW94]], the flux of $\nabla \times A_1$ through a surface bounded by $C_2$ equals the [[line integral|0H5MR9B6GT]] $\oint_{C_2} A_1 \cdot d\ell_2$.
Dividing by $I_1$ gives the formula.
The integrand is symmetric under exchange of the two curves, which proves $M_{12} = M_{21}$.

The formula needs the curves to be disjoint.
For $C_1 = C_2$ the integrand blows up like $1 / \abs{x_1 - x_2}$ along the diagonal, and the double integral diverges, which is why self-inductance needs a wire of positive thickness.

Example: take two coaxial circles of radii $a$ and $b$ far apart at distance $d$.
To leading order in $1/d$ the formula gives $M_{12} \approx \mu_0 \pi a^2 b^2 / (2 d^3)$, the value for two small coaxial magnetic dipoles.

## Explanations

### L1 human

The formula computes how strongly two loops of wire are magnetically coupled, using only their shapes.
It adds up, over every pair of small pieces of the two loops, the alignment of the two pieces divided by their distance.
Pieces that run parallel and close together count the most.
It shows at once that the coupling of loop one to loop two equals the coupling of loop two to loop one.

### L2 human

The Neumann formula is the magnetostatic analogue of writing the interaction energy of two charge distributions as a double integral against the Coulomb kernel $1 / \abs{x - y}$.
The magnetic energy of two currents is $\frac{1}{2} L_{11} I_1^2 + M_{12} I_1 I_2 + \frac{1}{2} L_{22} I_2^2$, so the formula also gives the force between two circuits by differentiating $M_{12} I_1 I_2$ with respect to their relative position.
In numerical work, inductances of printed circuits are often computed by discretising this double line integral.
