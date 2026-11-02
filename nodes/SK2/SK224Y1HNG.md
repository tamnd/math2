---
tag: SK224Y1HNG
kind: definition
name: Monodromy
msc: [34M35, 34M03]
defines: C8HD62AB6Q
uses: [037ZNY7NAG, 0H1GN6P9R5, 0M3YQJ81NB, 0NAHXR1FRH, WYGRXCG2RN, 0FCHE902D7]
sources:
  - url: https://en.wikipedia.org/wiki/Monodromy
---

## Definition

Let $U \subseteq \C$ be a connected open set, and let $A \colon U \to \C^{n \times n}$ be [[holomorphic|0NAHXR1FRH]].
Consider the [[linear system|037ZNY7NAG]] $Y' = A(z)\, Y$, fix $z_0 \in U$, and let $\Phi$ be a [[fundamental matrix|0H1GN6P9R5]] of the system on a disc around $z_0$ in $U$.
Let $\gamma$ be a loop in $U$ based at $z_0$.
The [[analytic continuation|0M3YQJ81NB]] of $\Phi$ along $\gamma$ is again a fundamental matrix near $z_0$, so it equals $\Phi\, M_\gamma$ for a unique matrix $M_\gamma \in \mathrm{GL}_n(\C)$.
The matrix $M_\gamma$ is the *monodromy matrix* of $\gamma$.
It depends only on the homotopy class $[\gamma]$ of $\gamma$ in the fundamental group $\pi_1(U, z_0)$.
The map
$$\rho \colon \pi_1(U, z_0) \to \mathrm{GL}_n(\C), \qquad \rho([\gamma]) = M_\gamma^{-1},$$
is a group homomorphism, the *monodromy representation* of the system, and its image is the *monodromy group*.

## Remarks

Continuing $\Phi$ along $\gamma_1$ and then along $\gamma_2$ gives $\Phi M_{\gamma_2} M_{\gamma_1}$, so $\gamma \mapsto M_\gamma$ reverses products; taking inverses makes $\rho$ a [[representation|WYGRXCG2RN]] of $\pi_1$ in the [[general linear group|0FCHE902D7]].
Changing $\Phi$ to $\Phi C$ with $C$ invertible conjugates every $M_\gamma$ by $C$, so the representation is determined up to conjugation.
The same definition applies to a scalar equation of order $n$, using a fundamental system of solutions.

Example: for $y' = \frac{a}{z} y$ on $U = \C \setminus \set{0}$ with $a \in \C$, take $\Phi(z) = z^a = e^{a \log z}$ near $z_0 = 1$.
Continuation once counterclockwise around $0$ adds $2 \pi i$ to $\log z$, so $M_\gamma = e^{2 \pi i a}$.
The monodromy is trivial exactly when $a \in \Z$.

Non-example: for $y' = y$ on $\C$, the monodromy is trivial.
The solution $e^z$ is single-valued and $U = \C$ is simply connected, so every monodromy matrix is $1$.
