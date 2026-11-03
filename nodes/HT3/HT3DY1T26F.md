---
tag: HT3DY1T26F
kind: definition
name: Twisted K-theory
msc: [19L50, 55N15]
defines: RXSNBNQGTB
uses: [HM2HHE3J51, 8HWGKWD6ZM, 06EKW1AKXF, 8E37E74XVP, H353HJA3E5, 9SJ4SC9FQX, 9E4JE4902G, 6N7BC70CX0, Z74J6D5B0J]
sources:
  - url: https://en.wikipedia.org/wiki/Twisted_K-theory
---

## Definition

Let $H$ be a separable infinite-dimensional complex [[Hilbert space|HM2HHE3J51]].
Let $U(H)$ be its unitary group with the [[operator norm|06EKW1AKXF]] topology.
Let $PU(H) = U(H)/U(1)$ be the projective unitary group, the quotient by the scalars of modulus $1$.
Let $\operatorname{Fred}(H)$ be the space of [[Fredholm operators|8HWGKWD6ZM]] with the norm topology.
The group $PU(H)$ acts on it by conjugation, $[u] \cdot T = u T u^{-1}$, which is well defined because scalars commute with $T$.
Let $X$ be a compact Hausdorff space and let $P \to X$ be a [[principal bundle|8E37E74XVP]] with structure group $PU(H)$.
The *twisted K-theory* of $X$ with twist $P$ is the set
$$K^0_P(X) = \set{\text{homotopy classes of continuous sections of } P \times_{PU(H)} \operatorname{Fred}(H) \to X}.$$
Pointwise composition of operators makes it an abelian group.

## Remarks

By [[Kuiper's theorem|9SJ4SC9FQX]], $U(H)$ is contractible, so $PU(H)$ is an Eilenberg–MacLane space $K(\Z, 2)$.
Hence principal $PU(H)$-bundles over $X$ are classified up to isomorphism by their Dixmier–Douady class in $H^3(X; \Z)$, and one writes $K^0_\tau(X)$ for a class $\tau \in H^3(X; \Z)$.

Example: if $P = X \times PU(H)$ is trivial, the sections are maps $X \to \operatorname{Fred}(H)$, and by the [[Atiyah–Jänich theorem|H353HJA3E5]] $K^0_P(X) \cong K^0(X)$, ordinary [[complex K-theory|9E4JE4902G]].

Example: let $X = S^3$, with twist $k$ times a generator of $H^3(S^3; \Z) \cong \Z$, where $k \ne 0$.
In the twisted [[Atiyah–Hirzebruch spectral sequence|Z74J6D5B0J]], the differential $d_3 \colon H^0(S^3; \Z) \to H^3(S^3; \Z)$ is, up to sign, the cup product with the twist.
So $d_3$ is multiplication by $k$.
So $K^0_\tau(S^3) = 0$ and $K^1_\tau(S^3) \cong \Z/k$.

Non-example: a principal $PU(n)$-bundle with $n$ finite has a Dixmier–Douady class of order dividing $n$.
So a twist of infinite order in $H^3(X; \Z)$ cannot be realized by finite-dimensional projective bundles, and the infinite-dimensional space $H$ in the definition cannot be replaced by $\C^n$ in general.

There are several equivalent models; Atiyah and Segal use other topologies on $\operatorname{Fred}(H)$ to treat equivariant and more general twists, and Rosenberg used continuous-trace C*-algebras.
