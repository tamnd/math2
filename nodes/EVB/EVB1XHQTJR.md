---
tag: EVB1XHQTJR
kind: definition
name: Local coefficient system
msc: [55N25]
defines: M58WRZ7PFM
uses: [0CQHFPGJ45, ZBHGXJF24E, S1XK3HXHFX, 082GHNPJ53, 0NZ8JA25WK]
sources:
  - url: https://en.wikipedia.org/wiki/Local_system
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]] with [[fundamental groupoid|ZBHGXJF24E]] $\Pi_1(X)$.
A *local coefficient system* (or *local system*) of [[abelian groups|082GHNPJ53]] on $X$ is a functor $L \colon \Pi_1(X) \to \mathrm{Ab}$.
In detail, it consists of:

1. an abelian group $L_x$ for each point $x \in X$;
2. an isomorphism $L_\gamma \colon L_x \to L_y$ for each path-homotopy class $\gamma$ of paths from $x$ to $y$;

such that $L_{\gamma \cdot \gamma'} = L_{\gamma'} \circ L_\gamma$ for composable classes and $L_\gamma = \id$ for the class of a constant path.

## Remarks

Let $X$ be path-connected and $x_0 \in X$.
Then a local system is determined up to isomorphism by the group $L_{x_0}$ with its action of the [[fundamental group|S1XK3HXHFX]] $\pi_1(X, x_0)$.
This is the same as a [[module|0NZ8JA25WK]] over the group ring $\Z[\pi_1(X, x_0)]$.
If $X$ is locally path-connected and semilocally simply connected, local systems are the same as locally constant sheaves of abelian groups on $X$.

Example: on the circle $S^1$, let $L_x = \Z$ for every $x$, and let transport along a path that winds $k$ times multiply by $(-1)^k$.
This respects composition, since $(-1)^{k + l} = (-1)^k (-1)^l$, so it is a local system.
It is not isomorphic to the constant system $\Z$, since the generator of $\pi_1(S^1)$ acts by $-1$ rather than $1$.

Non-example: on $S^1$, assigning to every path the same isomorphism $n \mapsto -n$ fails the clause on constant paths, which must act by the identity.

The orientation system of an $n$-manifold $M$, with $L_x = H_n(M, M \setminus \set{x}; \Z)$, is the main example; it is constant exactly when $M$ is orientable.
