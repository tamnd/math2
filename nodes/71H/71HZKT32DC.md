---
tag: 71HZKT32DC
kind: example
name: Non-linear sigma model
msc: [81T40, "58E20", 53C43]
illustrates: [W031YNVRE3, KZJYG9DS3M]
uses: [7CBT4SM83Y, 8AGSK9S92W]
sources:
  - url: https://en.wikipedia.org/wiki/Non-linear_sigma_model
same_as:
  wikidata: Q924571
  wikipedia: Non-linear sigma model
---

## Example

Let $(\Sigma, h)$ be a [[Riemannian manifold|7CBT4SM83Y]] of dimension $d$, the spacetime, and let $(M, g)$ be a Riemannian manifold, the target.
The *non-linear sigma model* with target $M$ is the following field theory.
Its fields are smooth maps $\phi \colon \Sigma \to M$, and its action is
$$S(\phi) = \frac{1}{2 \lambda} \int_\Sigma h^{ij}(x) \, g_{ab}(\phi(x)) \, \partial_i \phi^a \, \partial_j \phi^b \, \mathrm{vol}_h,$$
where $\lambda > 0$ is a coupling constant and $\phi^a$ are local coordinates of $\phi$.
Up to the factor $1/\lambda$, this is the Dirichlet energy of $\phi$, so the classical solutions are the [[harmonic maps|8AGSK9S92W]] from $\Sigma$ to $M$.

Check with the $O(N)$ model: take $M = S^{N-1} \subset \R^N$ with the round metric.
A map is then a function $\phi \colon \Sigma \to \R^N$ with $\phi \cdot \phi = 1$, and $S(\phi) = \frac{1}{2\lambda} \int_\Sigma \abs{\nabla\phi}^2$.
Adding a Lagrange multiplier for the constraint, the Euler–Lagrange equation is $\Delta\phi + \abs{\nabla\phi}^2 \phi = 0$, the harmonic map equation into the sphere.
The action is invariant under the group $O(N)$ acting on $\R^N$, which gives the model its name.
The model is non-linear because the constraint $\phi \cdot \phi = 1$ makes the space of fields non-linear, even though the action looks quadratic.

## Remarks

In two dimensions the action is invariant under conformal changes of $h$, and the $O(N)$ model with $N \ge 3$ is asymptotically free, as shown by Polyakov in 1975.
The two-dimensional $O(3)$ model has instanton solutions, the holomorphic and antiholomorphic maps from the Riemann sphere to $S^2$, classified by their degree.
The two-dimensional model, with the target metric allowed to be Lorentzian, is the starting point of string theory, where $\Sigma$ is the worldsheet and $M$ is spacetime.
In four dimensions, the sigma model with target a Lie group describes pions at low energies.

## Explanations

### L1 human

In a sigma model the field at each point of spacetime is not a number but a point of a curved space, such as a direction on a sphere.
A typical picture is a magnet in which each tiny arrow points somewhere on a sphere and wants to point like its neighbours.
The energy measures how much the field bends from point to point, and the most relaxed configurations are harmonic maps.
Because the target is curved, even this simple-looking theory is interacting.
