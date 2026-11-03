---
tag: 8AE0GE4EVE
kind: definition
name: London equations
msc: [82D55, 35Q60]
defines: SEW0D1Z5WE
uses: [9BWWD4QK8Y, 0NF6GQNXMY]
sources:
  - url: https://en.wikipedia.org/wiki/London_equations
---

## Definition

Consider a superconductor in $\R^3$ whose superconducting charge carriers have charge $q$, mass $m$ and number density $n_s > 0$.
Let $\mathbf{j}_s$ be the supercurrent density, $\mathbf{E}$ the electric field and $\mathbf{B}$ the magnetic field.
The *London equations* are
$$\frac{\partial \mathbf{j}_s}{\partial t} = \frac{n_s q^2}{m} \mathbf{E}, \qquad \nabla \times \mathbf{j}_s = -\frac{n_s q^2}{m} \mathbf{B},$$
where $\nabla \times$ is the [[curl|0NF6GQNXMY]].
The *London penetration depth* is $\lambda_L = \sqrt{m / (\mu_0 n_s q^2)}$, where $\mu_0$ is the vacuum permeability.

## Remarks

In a static situation, Ampère's law $\nabla \times \mathbf{B} = \mu_0 \mathbf{j}_s$ from [[Maxwell's equations|9BWWD4QK8Y]] and $\nabla \cdot \mathbf{B} = 0$ turn the second equation into $\nabla^2 \mathbf{B} = \mathbf{B} / \lambda_L^2$.
Example: let the superconductor fill $x > 0$ and let $\mathbf{B} = B(x) \mathbf{e}_z$ with $B(0) = B_0$ and $B$ bounded.
The equation becomes $B'' = B / \lambda_L^2$, whose bounded solution is $B(x) = B_0 e^{-x/\lambda_L}$.
Then $\mathbf{j}_s = \mu_0^{-1} \nabla \times \mathbf{B} = (B_0 / (\mu_0 \lambda_L)) e^{-x/\lambda_L} \mathbf{e}_y$, and one checks $\nabla \times \mathbf{j}_s = -(n_s q^2/m) \mathbf{B}$.
Non-example: a perfect conductor obeys the first equation but not the second.
For it, $\partial \mathbf{B} / \partial t$ decays inside, so the field is frozen in, but a field present before cooling is not expelled.
With the vector potential $\mathbf{A}$ in the London gauge, the two equations combine into $\mathbf{j}_s = -(n_s q^2 / m) \mathbf{A}$.

## Explanations

### L1 human

The first equation says that an electric field accelerates the supercurrent without any resistance.
The second equation says that the curl of the current is tied to the magnetic field with a minus sign.
Together with Maxwell's equations this forces the magnetic field to vanish deep inside the superconductor.
