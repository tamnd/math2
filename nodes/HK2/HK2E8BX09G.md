---
tag: HK2E8BX09G
kind: statement
role: theorem
name: Ampère's circuital law
msc: [78A30]
uses: [XRED3C547P, RA4GE6185Q, 0H5MR9B6GT, 026J1MG2NW, 0NF6GQNXMY, 0AKRKVHW94, 9BWWD4QK8Y]
about: [XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Amp%C3%A8re%27s_circuital_law
same_as:
  wikidata: Q51500
  wikipedia: Ampère's circuital law
---

## Statement

Let $\mu_0 > 0$ be the vacuum permeability.
Let $J \colon \R^3 \to \R^3$ be a continuously differentiable steady current density with compact support and $\nabla \cdot J = 0$.
Let $B$ be its [[magnetic field|XRED3C547P]], given by the [[Biot–Savart law|RA4GE6185Q]].
Then $B$ is continuously differentiable and its [[curl|0NF6GQNXMY]] is
$$\nabla \times B = \mu_0 J \quad \text{on } \R^3.$$
Equivalently, for every compact oriented smooth surface $S \subset \R^3$ with boundary curve $\partial S$ oriented compatibly,
$$\oint_{\partial S} B \cdot d\ell = \mu_0 \int_S J \cdot n \, dA.$$

## Remarks

The two forms are equivalent by [[Stokes' theorem|0AKRKVHW94]].
The left side is the [[line integral|0H5MR9B6GT]] of $B$ around $\partial S$.
The right side is $\mu_0$ times the [[flux|026J1MG2NW]] of $J$ through $S$, the current through $S$.
The proof writes $B = \nabla \times A$ with $A = \frac{\mu_0}{4\pi} \int J(y) / \abs{x - y} \, dy$, and uses $\nabla \times (\nabla \times A) = \nabla (\nabla \cdot A) - \Delta A$.
Here $\Delta A = -\mu_0 J$ by Poisson's equation, and $\nabla \cdot A = 0$ because $\nabla \cdot J = 0$.
Without $\nabla \cdot J = 0$ the law fails, since $\nabla \cdot (\nabla \times B) = 0$ would force $\nabla \cdot J = 0$.
For time-dependent fields Maxwell added the displacement current: $\nabla \times B = \mu_0 J + \mu_0 \varepsilon_0 \partial_t E$.
Example: for a long straight wire with current $I$, a circle of radius $s$ around the wire gives $2 \pi s \abs{B} = \mu_0 I$, so $\abs{B} = \mu_0 I / (2 \pi s)$.

## Explanations

### L1 human

Walk once around a closed loop and add up the magnetic field along your path.
Ampère's law says that the result is proportional to the electric current passing through the loop.
Currents outside the loop add nothing.

### L2 human

Ampère's law is the magnetostatic analogue of Gauss's law: with symmetry it gives fields without integration.
It yields the field $\mu_0 n I$ inside a long solenoid with $n$ turns per unit length, and the field of a toroidal coil.
With Maxwell's correction it becomes one of [[Maxwell's equations|9BWWD4QK8Y]], and the correction is exactly what makes the equations consistent with charge conservation.
