---
tag: T5RW1VN8AN
kind: example
name: Green's function of the ball
msc: [31B10, 35J08]
instance_of: [M36SD56MWQ]
uses: [0YE5868HZB, BSJ8X2XRN9, 0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function_for_the_three-variable_Laplace_equation
---

## Example

Let $B = \set{x \in \R^3 : \abs{x} < 1}$ be the unit [[open ball|0YE5868HZB]].
For $x \in B$ with $x \ne 0$, let $x^* = x / \abs{x}^2$ be the inverse point of $x$ in the unit sphere; it lies outside $\overline{B}$.
Define, for $y \in \overline{B}$ with $y \ne x$,
$$G(x, y) = \frac{1}{4\pi} \left( \frac{1}{\abs{x - y}} - \frac{1}{\abs{x} \, \abs{y - x^*}} \right) \quad (x \ne 0), \qquad G(0, y) = \frac{1}{4\pi} \left( \frac{1}{\abs{y}} - 1 \right).$$
This is the [[Green's function|M36SD56MWQ]] of $B$, normalized so that $\Delta_y G(x, y) = -\delta_x$.
Check of the three properties, for $x \ne 0$:

1. The first term is the [[fundamental solution|BSJ8X2XRN9]] $\frac{1}{4\pi\abs{x - y}}$, which has the right singularity at $y = x$.
2. The second term is [[harmonic|0DEB0JMN0W]] in $y$ on $B$, because its singularity $x^*$ lies outside $\overline{B}$.
3. For $\abs{y} = 1$ one has $\abs{x}^2 \abs{y - x^*}^2 = \abs{x}^2 - 2 x \cdot y + 1 = \abs{x - y}^2$, so the two terms cancel and $G(x, y) = 0$.

For $x = 0$, the term $1/\abs{y}$ is the fundamental solution times $4\pi$, the constant $1$ is harmonic, and $G(0, y) = 0$ when $\abs{y} = 1$.

## Remarks

In $\R^n$ with $n \ge 3$ the same construction gives $G(x, y) = \Phi(x - y) - \Phi(\abs{x}(y - x^*))$, where $\Phi(z) = \frac{1}{(n-2)\sigma_{n-1}} \abs{z}^{2-n}$ and $\sigma_{n-1}$ is the area of the unit sphere.
The outward normal derivative of $-G(x, \cdot)$ on the sphere is the Poisson kernel of the ball.
The second term is the potential of an image charge of strength $1/\abs{x}$ placed at $x^*$.

## Explanations

### L1 human

To make the potential of a point charge vanish on a sphere, place a second, opposite charge at the mirror point outside the sphere.
The mirror point lies on the same ray, at distance $1/\abs{x}$ from the centre.
On the sphere the two potentials cancel exactly, and inside the ball the sum is the Green's function.
