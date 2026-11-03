---
tag: XBQHT2BFF0
kind: definition
name: Laplace–Runge–Lenz vector
msc: [70F05, 70H33, 70F15]
defines: 94SBY80FZS
uses: [APR7XN00N3, 37Q4BTJMXW, 7147M98XNR, TYXD1T6FRX, 0262JP0NV9]
sources:
  - url: https://en.wikipedia.org/wiki/Laplace%E2%80%93Runge%E2%80%93Lenz_vector
---

## Definition

Let $m > 0$ and $k \in \R$.
Consider a particle of mass $m$ at position $r \in \R^3 \setminus \set{0}$ that moves under the [[central force|APR7XN00N3]] $F(r) = - k \, r / \norm{r}^3$.
Let $p = m r'$ be its [[momentum|37Q4BTJMXW]] and $L = r \times p$ its [[angular momentum|7147M98XNR]] about the origin.
The *Laplace–Runge–Lenz vector* of the particle is
$$A = p \times L - m k \, \frac{r}{\norm{r}}.$$

## Remarks

Along every motion $A$ is constant, so it is a [[first integral|0262JP0NV9]].
Check: $p' = - k r / \norm{r}^3$ and $L' = 0$, so $(p \times L)' = - \frac{k m}{\norm{r}^3} \, r \times (r \times r') = \frac{k m}{\norm{r}^3} \left( \norm{r}^2 r' - (r \cdot r') \, r \right)$, and this equals $m k \left( \frac{r}{\norm{r}} \right)'$.
Moreover $A \cdot L = 0$, so $A$ lies in the plane of the orbit.

Example: for $k > 0$ and a circular orbit of radius $\rho$, the speed is $v$ with $m v^2 = k / \rho$; then $p \times L$ has length $m v \cdot m \rho v = m k$ and points outward, so $A = 0$.
For $k > 0$ and $L \neq 0$, taking the dot product of $A$ with $r$ gives the orbit $\norm{r} = \frac{\norm{L}^2 / (m k)}{1 + e \cos \theta}$, where $\theta$ is the angle between $r$ and $A$ and $e = \norm{A} / (m k)$ is the eccentricity.
So $A$ points to the pericentre, as in the [[Kepler problem|TYXD1T6FRX]].

For a central force that is not of inverse-square form, for example $F(r) = - k \, r / \norm{r}^4$, the vector $A$ defined by the same formula is not constant, and orbits generally precess.
Some authors use $A / (m k)$, the eccentricity vector, or divide by $m$ to work per unit mass.

## Explanations

### L1 human

The vector combines the momentum, the angular momentum and the direction to the particle.
In an inverse-square force field, such as gravity of a point mass, it never changes, and it points to the place where the particle comes closest to the centre.
