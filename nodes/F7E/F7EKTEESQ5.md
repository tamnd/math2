---
tag: F7EKTEESQ5
kind: statement
role: proposition
name: Beltrami identity
msc: [49K05, 70H03]
uses: [PS0VV149ET, JRQZ803Q5Y, 09EGC6F8PT]
about: [PS0VV149ET]
sources:
  - url: https://en.wikipedia.org/wiki/Beltrami_identity
same_as:
  wikidata: Q3303275
  wikipedia: Beltrami identity
---

## Statement

Let $a < b$, and let $L \colon \R \times \R \to \R$, written $L(z, p)$, be a function of class $C^2$ that does not depend on the independent variable $x$.
Write $L_z$ and $L_p$ for its [[partial derivatives|09EGC6F8PT]].
Let $y \in C^2([a, b])$ solve the [[Euler–Lagrange equation|PS0VV149ET]]
$$\frac{d}{dx} L_p\big(y(x), y'(x)\big) = L_z\big(y(x), y'(x)\big) \quad \text{on } [a, b].$$
Then there is a constant $C$ with
$$L\big(y(x), y'(x)\big) - y'(x) \, L_p\big(y(x), y'(x)\big) = C \quad \text{for all } x \in [a, b].$$

## Remarks

The proof is one differentiation.
The derivative of $L(y, y') - y' L_p(y, y')$ is $L_z y' + L_p y'' - y'' L_p - y' \frac{d}{dx} L_p = y' \big(L_z - \frac{d}{dx} L_p\big)$, which is $0$ by the Euler–Lagrange equation.

Example: for the [[minimal surface of revolution|AEG6QWEFRG]] one has $L(z, p) = z \sqrt{1 + p^2}$.
Then $L - p L_p = z / \sqrt{1 + p^2}$, so $y / \sqrt{1 + y'^2} = C$.
For $C > 0$ the solutions are the catenaries $y(x) = C \cosh\big((x - d)/C\big)$.

A partial converse holds: if the quantity is constant and $y'(x) \ne 0$, then the Euler–Lagrange equation holds at $x$.
So constant solutions $y' = 0$ of the identity must be checked separately.

## Explanations

### L1 human

When the integrand of a variational problem does not depend on position along the axis, one quantity stays constant along every solution.
This replaces a second-order equation by a first-order one, which is often easy to solve.
It is how the brachistochrone and the hanging chain are solved by hand.

### L2 human

In mechanics, with $x$ as time and $L$ the Lagrangian, the quantity $y' L_p - L$ is the energy, the Hamiltonian.
The identity is then conservation of energy for a time-independent Lagrangian, a special case of [[Noether's theorem|XHPDM5T2JG]] for time translations.
It is used in the [[brachistochrone problem|ZWQ5JBR6XF]] and the [[catenary problem|8REBFQD6E0]].
