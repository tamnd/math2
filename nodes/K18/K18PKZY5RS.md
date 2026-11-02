---
tag: K18PKZY5RS
kind: statement
role: theorem
name: Local parametrization theorem
msc: [32B10, 32B05]
uses: [7VPJWF0AZ7, VMDTGTMN9P, 15XEBGNGHC, 3XZRRE165N, VKFW27WXEZ]
about: [7VPJWF0AZ7]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_analytic_variety
---

## Statement

Let $A_0$ be an [[irreducible analytic germ|7VPJWF0AZ7]] at $0 \in \C^n$.
Then there are an integer $d$ with $0 \le d \le n$ and linear coordinates $z = (z', z'')$ on $\C^n$ with $z' \in \C^d$ and $z'' \in \C^{n-d}$.
There are also open polydiscs $U' \subseteq \C^d$ and $U'' \subseteq \C^{n-d}$ centred at $0$.
With $U = U' \times U''$ and $\pi(z', z'') = z'$, the following properties hold.

1. There is a representative $A$ of $A_0$ that is an [[analytic subset|VMDTGTMN9P]] of $U$, and $\pi \colon A \to U'$ is a surjective [[proper map|15XEBGNGHC]] with finite fibres.
2. There are an analytic subset $\Delta \subsetneq U'$ and an integer $k \ge 1$ such that $\pi \colon A \setminus \pi^{-1}(\Delta) \to U' \setminus \Delta$ is a $k$-sheeted [[covering map|3XZRRE165N]].
3. The set $A \setminus \pi^{-1}(\Delta)$ is a connected complex [[submanifold|VKFW27WXEZ]] of $U$ of dimension $d$, and it is dense in $A$.

## Remarks

The integer $d$ is the dimension of the germ $A_0$, and the coordinates can be taken generic: a dense open set of linear coordinate systems works.
The proof uses the ideal $\mathfrak{p}$ of $A_0$, which is prime, and Noether normalization in the analytic setting.
After a generic change of coordinates, the Weierstrass preparation theorem makes $\mathcal{O}_{n,0}/\mathfrak{p}$ a finite extension of $\mathcal{O}_{d,0}$, the germs in $z'$ alone.
Here $d$ is the largest number of variables for which $\mathcal{O}_{d,0} \to \mathcal{O}_{n,0}/\mathfrak{p}$ is injective.
A primitive element of the fraction field extension and its discriminant give the set $\Delta$ and the number $k$ of sheets.
Example: for the cusp $A = \set{z_1^2 = z_2^3}$ in $\C^2$, take $z' = z_2$ and $\pi(z_1, z_2) = z_2$.
Over $z_2 \ne 0$ the fibre consists of the two square roots of $z_2^3$, so $\Delta = \set{0}$ and $k = 2$; the set $A \setminus \set{0}$ is the image of the punctured disc under $t \mapsto (t^3, t^2)$, hence connected.
Irreducibility is needed for the connectedness in part 3.
For $A = \set{z_1 z_2 = 0}$ and any linear projection to a line with finite fibres on $A$, the complement of $\pi^{-1}(\Delta)$ has a component in each axis.

## Explanations

### L1 human

The theorem describes what an irreducible analytic set looks like near a point.
After a good choice of coordinates, it is a finite branched cover of a ball in $\C^d$.
Over most points of the ball there are exactly $k$ points of the set, and these sheets come together only over a thin set.
So locally an analytic set is a many-valued graph over a $d$-dimensional ball.

### L2 human

The local parametrization is the basic structure theorem of local analytic geometry.
It gives the dimension of an analytic set and shows that the regular points are dense.
It also yields the Rückert Nullstellensatz, and it is the analytic counterpart of Noether normalization for affine varieties.
The number $k$ of sheets for generic coordinates is the multiplicity of the germ at $0$.
