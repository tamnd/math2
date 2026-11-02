---
tag: FPXZMN0CH5
kind: definition
name: Floer homology
msc: [53D40]
defines: NCKFPAGHXF
uses: [CAN490EPRT, C5EH3B4BEP, 0AA97XA70K, 9SYWRGVTRS, N469E47V75]
sources:
  - url: https://en.wikipedia.org/wiki/Floer_homology
---

## Definition

This defines Hamiltonian Floer homology with coefficients in $\F_2$ in the simplest setting.
Let $(M, \omega)$ be a closed [[symplectic manifold|CAN490EPRT]] such that $\int_{S^2} v^* \omega = 0$ for every smooth map $v \colon S^2 \to M$.
Let $H \colon (\R / \Z) \times M \to \R$ be smooth, write $H_t = H(t, \cdot)$, and let $X_{H_t}$ be the [[Hamiltonian vector field|C5EH3B4BEP]] of $H_t$.

1. Let $\mathcal{P}(H)$ be the set of contractible loops $x \colon \R / \Z \to M$ with $x'(t) = X_{H_t}(x(t))$, the contractible $1$-[[periodic orbits|0AA97XA70K]].
Assume that each of them is nondegenerate: the linearized time-$1$ flow at $x(0)$ does not have $1$ as an eigenvalue.
2. Let $J = (J_t)_{t \in \R / \Z}$ be a family of [[almost complex structures|9SYWRGVTRS]] compatible with $\omega$.
For $x, y \in \mathcal{P}(H)$, let $\mathcal{M}(x, y)$ be the set of smooth maps $u \colon \R \times (\R / \Z) \to M$ with
$$\partial_s u + J_t(u) \left( \partial_t u - X_{H_t}(u) \right) = 0, \qquad \lim_{s \to -\infty} u(s, t) = x(t), \qquad \lim_{s \to +\infty} u(s, t) = y(t),$$
on which $\R$ acts by translation in $s$.
3. For generic $J$, each set $\mathcal{M}(x, y)$ is a smooth manifold. When it has dimension $1$, let $n(x, y) \in \F_2$ be the number modulo $2$ of elements of $\mathcal{M}(x, y) / \R$. Otherwise let $n(x, y) = 0$.
4. Let $CF(H)$ be the $\F_2$-vector space with basis $\mathcal{P}(H)$, and let $\partial \colon CF(H) \to CF(H)$ be the linear map with $\partial x = \sum_{y} n(x, y)\, y$.

Then $\partial \circ \partial = 0$, so $(CF(H), \partial)$ is a [[chain complex|WQ82C0M3QB]].
The *Floer homology* of $(H, J)$ is $HF(H, J) = \ker \partial / \im \partial$.

## Remarks

The solutions $u$ in clause 2 are the negative gradient lines of the action functional on contractible loops, for the $L^2$ metric defined by $J$.
They are [[pseudoholomorphic curves|N469E47V75]] perturbed by $H$.
That $n(x, y)$ is finite and that $\partial^2 = 0$ are theorems of Floer, which rest on compactness of the moduli spaces; the assumption that $\omega = 0$ on spheres rules out sphere bubbling.
The homology does not depend on $(H, J)$ up to isomorphism, and Floer proved that it is isomorphic to the singular homology $H_*(M; \F_2)$.
Since $\dim CF(H)$ is the number of contractible $1$-periodic orbits, this gives the Arnold conjecture lower bound in this setting.
The complex can be graded by the Conley–Zehnder index when the first Chern class also vanishes on spheres.

Example: let $H$ be a $C^2$-small Morse function $f$ independent of $t$.
Then the $1$-periodic orbits are the constant loops at critical points of $f$, and the $t$-independent Floer cylinders are the gradient lines of $f$.
In this case the Floer complex agrees with the Morse complex of $f$.

Signs, and the order of $x$ and $y$, vary with the conventions for $X_H$ and for the action functional.
Lagrangian Floer homology is defined in the same way, with generators the intersection points of two Lagrangian submanifolds and with strips instead of cylinders.
