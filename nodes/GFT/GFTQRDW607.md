---
tag: GFTQRDW607
kind: definition
name: Morin singularities
msc: [57R45, 58K40, 58K25]
defines: DF8CJ1A9MF
uses: [1JG3HFWX3T, VZXF7RNFKS, 0KZZ70ZHXP]
sources:
  - url: https://en.wikipedia.org/wiki/Singularity_theory
---

## Definition

Let $n \ge 1$ and $1 \le k \le n$.
Let $f \colon (\R^n, 0) \to (\R^n, 0)$ be a smooth map [[germ|VZXF7RNFKS]].
It is a *Morin singularity of order $k$* if there are germs of [[diffeomorphisms|0KZZ70ZHXP]] $\varphi$ and $\psi$ of $(\R^n, 0)$ with this property.
The germ $\psi \circ f \circ \varphi^{-1}$ is the germ at $0$ of
$$(u_1, \ldots, u_{n-1}, t) \mapsto \left(u_1, \ldots, u_{n-1}, \ t^{k+1} + \sum_{i=1}^{k-1} u_i t^i\right).$$

## Remarks

For $k = 1$ the normal form is $(u, t) \mapsto (u, t^2)$, the fold; for $k = 2$ it is $(u_1, \ldots, t) \mapsto (u_1, \ldots, t^3 + u_1 t)$, the cusp; for $k = 3$ it is the swallowtail.
Example: $f(x, y) = (x, y^3 + xy)$ is a Morin singularity of order $2$ with $\varphi$ and $\psi$ the identity.
The local algebra $\mathcal{E}_n / f^*(\mathfrak{m}_n) \mathcal{E}_n$ of a Morin singularity of order $k$ is $\R[t]/(t^{k+1})$, of dimension $k + 1$; this is an invariant of the germ up to the equivalence above.
Non-example: $f(x, y) = (x, y^4)$ has local algebra $\R[y]/(y^4)$ of dimension $4$, so it could only be of order $3$, which needs $n \ge 3$; hence it is not a Morin singularity.
Every Morin singularity is a stable germ of corank one, and its Thom–Boardman symbol is $(1, \ldots, 1, 0)$ with $k$ ones.
Morin proved that a germ with this symbol whose jet is transverse to the Boardman strata is a Morin singularity.
There are analogous normal forms for maps $\R^m \to \R^n$ with $m \ne n$, with extra terms in the remaining variables.
