---
tag: Y4A92XVXP0
kind: statement
role: theorem
name: Jefimenko's equations
msc: [78A25, 35Q61]
uses: [9BWWD4QK8Y, 9Q1NE5EP37, YZ7Q9DP8RT, XRED3C547P, EDBPDTG7BS, RA4GE6185Q]
about: [YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Jefimenko%27s_equations
same_as:
  wikidata: Q1321084
  wikipedia: Jefimenko's equations
---

## Statement

Let $\varepsilon_0, \mu_0 > 0$ and $c = 1/\sqrt{\varepsilon_0 \mu_0}$.
Let $\rho \colon \R^3 \times \R \to \R$ and $J \colon \R^3 \times \R \to \R^3$ be twice continuously differentiable charge and current densities that vanish outside a fixed bounded set of $\R^3$ and satisfy $\partial_t \rho + \nabla \cdot J = 0$.
Let $E$ and $B$ be the fields $E = -\nabla \varphi - \partial_t A$ and $B = \nabla \times A$ of the [[retarded potentials|9Q1NE5EP37]] $\varphi, A$ of $\rho, J$.
For $r, r' \in \R^3$ write $R = r - r'$ and $t_r = t - \abs{R}/c$.
Then
$$E(r, t) = \frac{1}{4 \pi \varepsilon_0} \int_{\R^3} \left[ \frac{R}{\abs{R}^3} \rho(r', t_r) + \frac{R}{c \abs{R}^2} \partial_t \rho(r', t_r) - \frac{1}{c^2 \abs{R}} \partial_t J(r', t_r) \right] d^3 r',$$
$$B(r, t) = \frac{\mu_0}{4 \pi} \int_{\R^3} \left[ \frac{J(r', t_r)}{\abs{R}^3} + \frac{\partial_t J(r', t_r)}{c \abs{R}^2} \right] \times R \; d^3 r'.$$
These $E$ and $B$ solve [[Maxwell's equations|9BWWD4QK8Y]] with sources $\rho$ and $J$.

## Remarks

The proof differentiates the retarded potentials under the integral sign.
The derivative of $\rho(r', t - \abs{r - r'}/c)$ in $r$ has two parts: one from the factor $1 / \abs{r - r'}$ and one from the retarded time, which brings in $\partial_t \rho$ and a factor $-R / (c \abs{R})$.
The time derivative of $A$ gives the term with $\partial_t J$, and the curl of $A$ gives $B$ in the same way.
The continuity equation is what makes the retarded potentials satisfy the Lorenz gauge, so that the fields solve Maxwell's equations.

Example: for static sources, $\partial_t \rho = 0$ and $\partial_t J = 0$, and the delay plays no role.
The formulas reduce to Coulomb's law for the [[electric field|YZ7Q9DP8RT]] and the [[Biot–Savart law|RA4GE6185Q]] for the [[magnetic field|XRED3C547P]].
The terms that decay like $1/\abs{R}$, those with $\partial_t \rho$ and $\partial_t J$, dominate far from the sources; they carry the radiation.

## Explanations

### L1 human

Jefimenko's equations give the electric and magnetic fields directly from the charges and currents, without passing through potentials.
They look like Coulomb's law and the Biot–Savart law, with each source read at an earlier time and with extra terms for sources that change in time.
The extra terms fall off more slowly with distance, which is why changing currents can send signals far away.

### L2 human

They are the field form of the retarded solution of Maxwell's equations, in the same way that the retarded potentials are its potential form.
They show that the fields are determined by the retarded values of $\rho$, $\partial_t \rho$ and $\partial_t J$ alone.
In particular a changing magnetic field is not a separate cause of the electric field here: both fields are caused by the sources.
For a single point charge the integrals become the fields of the Liénard–Wiechert potentials.
