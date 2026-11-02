---
tag: QYZNMEM1ZZ
kind: definition
name: Spin structure
msc: [53C27, 57R15]
defines: RSPZ9TCFQ8
uses: [7CBT4SM83Y, 913WEQERBE, F4HWTRNXAP, 8E37E74XVP, JQCK7A210W]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_structure
---

## Definition

Let $(M, g)$ be an [[oriented|913WEQERBE]] [[Riemannian manifold|7CBT4SM83Y]] of dimension $n \ge 2$.
Let $P_{SO}(M)$ be its bundle of oriented orthonormal frames, a principal $SO(n)$-bundle (see [[frame bundle|F4HWTRNXAP]]).
Let $\rho \colon \operatorname{Spin}(n) \to SO(n)$ be the double covering homomorphism from the [[spin group|JJSXXJQGEH]].
A *spin structure* on $(M, g)$ is a pair $(P, \xi)$ such that:

1. $P$ is a [[principal|8E37E74XVP]] $\operatorname{Spin}(n)$-bundle over $M$.
2. $\xi \colon P \to P_{SO}(M)$ is a smooth map that commutes with the projections to $M$.
3. $\xi(p \cdot a) = \xi(p) \cdot \rho(a)$ for all $p \in P$ and $a \in \operatorname{Spin}(n)$.

Two spin structures $(P, \xi)$ and $(P', \xi')$ are equivalent if there is a $\operatorname{Spin}(n)$-equivariant bundle isomorphism $\phi \colon P \to P'$ with $\xi' \circ \phi = \xi$.

## Remarks

Clauses 1 to 3 imply that $\xi$ is a two-sheeted covering map.
An oriented manifold admits a spin structure if and only if its second [[Stiefel–Whitney class|JQCK7A210W]] $w_2(TM)$ vanishes.
In that case the equivalence classes of spin structures are in bijection with $H^1(M; \Z/2)$, after one class is fixed.
Existence and the set of classes do not depend on the choice of the metric $g$.

Example: the sphere $S^n$ with $n \ge 2$ has $w_2 = 0$, because its tangent bundle becomes trivial after adding a trivial line bundle.
Since $H^1(S^n; \Z/2) = 0$, it has exactly one spin structure up to equivalence.
For $S^n$ it is $\operatorname{Spin}(n+1) \to SO(n+1) = P_{SO}(S^n)$.

Non-example: the complex projective plane $\C P^2$ is oriented but $w_2(T\C P^2) \ne 0$, so no pair $(P, \xi)$ satisfies the clauses.
A manifold with a spin structure is called a *spin manifold*.
