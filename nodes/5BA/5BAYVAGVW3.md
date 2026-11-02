---
tag: 5BAYVAGVW3
kind: definition
name: Hyperfunction
msc: [46F15, 32A45]
defines: NECFJN169C
uses: [0NAHXR1FRH, 02BH3MCBQB, 0KPHENZ5S7]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperfunction
---

## Definition

Let $U \subseteq \R$ be an open set.
Let $V \subseteq \C$ be an open set with $V \cap \R = U$; then $U$ is a closed subset of $V$.
For an open set $W \subseteq \C$, let $\mathcal{O}(W)$ be the space of [[holomorphic functions|0NAHXR1FRH]] on $W$.
The space of *hyperfunctions* on $U$ is the quotient vector space
$$\mathcal{B}(U) = \mathcal{O}(V \setminus U) / \mathcal{O}(V),$$
where $\mathcal{O}(V)$ is embedded in $\mathcal{O}(V \setminus U)$ by restriction.
The class of $F \in \mathcal{O}(V \setminus U)$ is written $[F]$.

## Remarks

Up to canonical isomorphism, $\mathcal{B}(U)$ does not depend on the choice of $V$.
Write $F_+$ and $F_-$ for the restrictions of $F$ to the parts of $V$ above and below the real axis.
One thinks of $[F]$ as $F_+(x + i0) - F_-(x - i0)$.
When both boundary values exist as distributions, this difference is a distribution, and every distribution on $U$ arises this way.

Example: on $U = \R$ with $V = \C$, let $F(z) = -1/(2\pi i z)$ on $\C \setminus \R$.
The boundary values give $F_+(x + i0) - F_-(x - i0) = -\frac{1}{2\pi i}\left(\frac{1}{x + i0} - \frac{1}{x - i0}\right)$, and this is the [[Dirac delta|0KPHENZ5S7]].
So $\delta = [F]$.
A function holomorphic on all of $V$ gives the zero hyperfunction.

Non-example: for $U = (0,1)$, the set $V = \C$ does not qualify, because $V \cap \R = \R \neq U$.
With that choice, $\mathcal{O}(\C \setminus (0,1)) / \mathcal{O}(\C)$ would also see singularities at the end points $0$ and $1$, which lie outside $U$.

In several variables the definition uses relative sheaf cohomology of the sheaf of holomorphic functions instead of a quotient.
