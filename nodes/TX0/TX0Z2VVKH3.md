---
tag: TX0Z2VVKH3
kind: statement
role: theorem
name: Frostman's theorem
msc: [31A15, 30C85]
uses: [0R6EWFKRCF, 464NN2K4FZ, W3NVXBEMRQ, 46NHWJHW44, W9N1TR1X8P]
about: [464NN2K4FZ]
sources:
  - url: https://en.wikipedia.org/wiki/Capacity_of_a_set
---

## Statement

Let $K$ be a [[compact set|0R6EWFKRCF]] in $\C$ with positive logarithmic capacity.
Let $\nu$ be its [[equilibrium measure|464NN2K4FZ]] and let $V(K)$ be its [[Robin constant|W3NVXBEMRQ]].
Let $U^\nu(z) = \int \log \frac{1}{\abs{z - w}} \, d\nu(w)$ be the [[logarithmic potential|46NHWJHW44]] of $\nu$.
Then:

1. $U^\nu(z) \le V(K)$ for every $z \in \C$.
2. $U^\nu(z) = V(K)$ for every $z \in K \setminus E$, where $E$ is an $F_\sigma$ subset of the boundary $\partial K$ of [[capacity zero|W9N1TR1X8P]].

## Remarks

Proof idea: suppose that $U^\nu < V(K)$ on a compact subset of $K$ of positive capacity, or $U^\nu > V(K)$ on a set of positive $\nu$-measure.
Then moving a little mass of $\nu$ lowers the energy, which contradicts minimality.
This gives $U^\nu \ge V(K)$ on $K$ outside a set of capacity zero and $U^\nu \le V(K)$ on the support of $\nu$.
The maximum principle for potentials then extends the upper bound from the support of $\nu$ to all of $\C$.
A separate argument shows that the support of $\nu$ lies in $\partial K$.

Example: for the unit circle, $\nu = d\theta / 2\pi$ and $U^\nu(z) = -\log \max(\abs{z}, 1)$.
This is $0 = V(K)$ on the closed unit disc and negative outside, as the theorem says.
The exceptional set $E$ cannot be dropped in general: it can contain boundary points that are irregular for the Dirichlet problem, where the potential is strictly below $V(K)$.

## Explanations

### L1 human

When a unit charge sits in equilibrium on a conductor $K$, the voltage it creates is the same at almost every point of $K$.
Nowhere in the plane is the voltage higher than this value.
The only exceptions on $K$ form a set so thin that it has capacity zero.

### L2 human

Frostman's theorem is the bridge between the energy definition of capacity and the Green function.
On the unbounded component $\Omega$ of $\C \setminus K$, the function $g(z) = V(K) - U^\nu(z)$ is the Green function of $\Omega$ with pole at infinity.
The exceptional set $E$ is linked to the boundary points that are irregular for the Dirichlet problem.
The Kellogg–Evans theorem says that such points form a set of capacity zero.
The theorem is also the basic tool for computing capacities: a probability measure on $K$ whose potential is constant on all of $K$ must be the equilibrium measure.
