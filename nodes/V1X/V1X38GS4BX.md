---
tag: V1X38GS4BX
kind: definition
name: Auslander–Reiten quiver
msc: [16G70]
defines: 125Z033VCQ
uses: [RE9YFFS3TS, 3CTW1P4HBP, E2P29GCD9T, M5D95FN7G3]
sources:
  - url: https://en.wikipedia.org/wiki/Auslander%E2%80%93Reiten_theory
---

## Definition

Let $k$ be an algebraically closed field and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $k$.
Let $M$ and $N$ be finitely generated left $A$-modules.
Let $\operatorname{rad}(M, N)$ be the space of morphisms $f \colon M \to N$ such that $h f g$ is never an isomorphism, for $X$ [[indecomposable|E2P29GCD9T]], $g \colon X \to M$ and $h \colon N \to X$.
Let $\operatorname{rad}^2(M, N)$ be the space spanned by the composites $f_2 f_1$ with $f_1 \in \operatorname{rad}(M, Y)$ and $f_2 \in \operatorname{rad}(Y, N)$ for some module $Y$.
The *Auslander–Reiten quiver* of $A$ is the [[quiver|RE9YFFS3TS]] $\Gamma_A$ such that:

1. its vertices are the isomorphism classes $[M]$ of indecomposable finitely generated $A$-modules;
2. the number of arrows $[M] \to [N]$ is $\dim_k \operatorname{rad}(M, N) / \operatorname{rad}^2(M, N)$.

It comes with the partial bijection $\tau$ on vertices, the Auslander–Reiten translation, defined on the classes of non-projective modules.

## Remarks

For indecomposable $M$ and $N$, the nonzero elements of $\operatorname{rad}(M, N) \setminus \operatorname{rad}^2(M, N)$ are exactly the irreducible morphisms.
Let $0 \to \tau N \to E \to N \to 0$ be an [[almost split sequence|M5D95FN7G3]], with $E = \bigoplus_r E_r^{m_r}$ and $E_r$ indecomposable.
Then the arrows ending at $[N]$ start exactly at the classes $[E_r]$, and the arrows starting at $[\tau N]$ end exactly there.
Example: for the path algebra of $1 \to 2$, the indecomposable modules are $S_2 = P_2$, $P_1$ and $S_1$.
The quiver is $[S_2] \to [P_1] \to [S_1]$, with $\tau [S_1] = [S_2]$, coming from the almost split sequence $0 \to S_2 \to P_1 \to S_1 \to 0$.
Non-example: there is no arrow $[S_2] \to [S_1]$, since $\Hom(S_2, S_1) = 0$.
