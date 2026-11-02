---
tag: P2QJ7NPW3Y
kind: statement
role: theorem
name: Propagation of singularities
msc: [35A18, 35A21, 35A27]
uses: [3T5Q9WVQX8, F31T650DKY, C5EH3B4BEP]
about: [3T5Q9WVQX8]
sources:
  - url: https://en.wikipedia.org/wiki/Wave_front_set
---

## Statement

Let $X \subseteq \R^n$ be open and let $P = \sum_{\abs{\alpha} \le m} a_\alpha(x) D^\alpha$ be a linear differential operator of order $m$ with $C^\infty$ coefficients on $X$, where $D^\alpha = (-i\partial)^\alpha$.
Assume that its [[principal symbol|F31T650DKY]] $p(x, \xi) = \sum_{\abs{\alpha} = m} a_\alpha(x)\xi^\alpha$ is real-valued.
Let $u$ be a distribution on $X$ with $P u \in C^\infty(X)$, and let $\operatorname{WF}(u)$ be its [[wave front set|3T5Q9WVQX8]].
Then:

1. $\operatorname{WF}(u) \subseteq \set{(x, \xi) \in X \times (\R^n \setminus \set{0}) : p(x, \xi) = 0}$;
2. $\operatorname{WF}(u)$ is invariant under the flow of the [[Hamiltonian vector field|C5EH3B4BEP]] $H_p = \sum_{j} \big( \partial_{\xi_j} p\, \partial_{x_j} - \partial_{x_j} p\, \partial_{\xi_j} \big)$ on this set. That is, if $(x_0, \xi_0) \in \operatorname{WF}(u)$, then $\operatorname{WF}(u)$ contains the null bicharacteristic through $(x_0, \xi_0)$, as long as it stays in $X \times (\R^n \setminus \set{0})$.

## Remarks

Part 1 is microlocal elliptic regularity: where $p(x, \xi) \ne 0$, the operator $P$ has a microlocal parametrix, so $u$ is smooth in that direction.
Part 2 is due to Hörmander and to Duistermaat and Hörmander.
One proof uses a positive commutator argument: a pseudo-differential operator whose symbol grows along $H_p$ gives energy estimates that carry smoothness from one point of a bicharacteristic to the next.
Example: for the wave operator $P = \partial_t^2 - \Delta$ on $\R^{n+1}$, the symbol is $p = -\tau^2 + \abs{\xi}^2$ in the dual variables $(\tau, \xi)$ of $(t, x)$, and the null bicharacteristics project to the light rays $x = x_0 \pm t\,\xi_0/\abs{\xi_0}$.
So a singularity of a solution of the wave equation travels along a straight line at speed $1$ in its own direction.
Part 1 holds even without the assumption that $p$ is real.
Let $P$ be elliptic, such as the Cauchy–Riemann operator $\frac{1}{2}(\partial_x + i\partial_y)$ on $\R^2$.
Then its principal symbol has no zero with $\xi \ne 0$.
Microlocal elliptic regularity gives $\operatorname{WF}(u) = \emptyset$, so $u$ is smooth and there is nothing to propagate.

## Explanations

### L1 human

A singularity of a solution, such as a sharp edge or a jump, does not appear or disappear at random.
It moves along special curves, the rays of the equation, in a definite direction.
For the wave equation the rays are the straight lines along which light travels, so a sharp flash stays sharp and moves at the speed of light.
This is the precise form of the idea that singularities of waves travel like particles.

### L2 human

The theorem is a central result of microlocal analysis.
It locates singularities not only in space but also in direction, via the wave front set, and shows that they move along the bicharacteristics of the principal symbol.
For hyperbolic equations it gives the mathematical foundation of geometric optics: singularities follow the rays obtained from the eikonal equation.
It is used in inverse problems, in scattering theory and in the study of the wave equation on manifolds, where the rays are geodesics.
