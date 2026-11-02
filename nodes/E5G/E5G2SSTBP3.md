---
tag: E5G2SSTBP3
kind: definition
name: Schouten–Nijenhuis bracket
msc: [58A10, 17B70, 53D17]
defines: FJ1MDBZ680
uses: [F45VQ47GPV, 0299VCW1TH, 68FGQEBD6J, PJWK0PKN6Q, 0MDMZ965VE, A2KQ49Y4NF]
sources:
  - url: https://en.wikipedia.org/wiki/Schouten%E2%80%93Nijenhuis_bracket
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]].
For $p \ge 0$, let $\mathfrak{X}^p(M)$ be the space of $p$-vector fields, the smooth sections of the [[exterior power|0MDMZ965VE]] $\Lambda^p TM$.
So $\mathfrak{X}^0(M) = C^\infty(M)$, and $\mathfrak{X}^1(M)$ is the space of [[vector fields|0299VCW1TH]].
The *Schouten–Nijenhuis bracket* is the unique family of $\R$-bilinear maps $[\cdot, \cdot] \colon \mathfrak{X}^p(M) \times \mathfrak{X}^q(M) \to \mathfrak{X}^{p+q-1}(M)$ with these properties, for $P \in \mathfrak{X}^p(M)$, $Q \in \mathfrak{X}^q(M)$ and $R \in \mathfrak{X}^r(M)$.

1. For functions $f, g$: $[f, g] = 0$.
2. For a vector field $X$: $[X, P] = \mathcal{L}_X P$, the [[Lie derivative|PJWK0PKN6Q]]; in particular $[X, f] = X(f)$ and $[X, Y]$ is the [[Lie bracket|68FGQEBD6J]].
3. Graded antisymmetry: $[P, Q] = -(-1)^{(p-1)(q-1)} [Q, P]$.
4. Graded Leibniz rule: $[P, Q \wedge R] = [P, Q] \wedge R + (-1)^{(p-1)q}\, Q \wedge [P, R]$.

## Remarks

For vector fields $X_1, \dots, X_p$ and $Y_1, \dots, Y_q$ with $p, q \ge 1$, the bracket is
$$[X_1 \wedge \dots \wedge X_p,\ Y_1 \wedge \dots \wedge Y_q] = \sum_{i=1}^{p} \sum_{j=1}^{q} (-1)^{i+j} [X_i, Y_j] \wedge X_1 \wedge \dots \widehat{X_i} \dots \wedge X_p \wedge Y_1 \wedge \dots \widehat{Y_j} \dots \wedge Y_q,$$
where a hat marks an omitted factor.
The bracket also satisfies a graded Jacobi identity, so $\mathfrak{X}^{\bullet + 1}(M)$, with degrees shifted by one, is a graded Lie algebra.

A bivector field $\pi \in \mathfrak{X}^2(M)$ defines the bracket $\{f, g\} = \pi(df, dg)$ on functions.
This bracket satisfies the Jacobi identity, so that $\pi$ is a [[Poisson structure|A2KQ49Y4NF]], exactly when $[\pi, \pi] = 0$.

Example: on $\R^2$, let $\pi = \partial_x \wedge \partial_y$.
All brackets of the coordinate vector fields vanish, so the formula gives $[\pi, \pi] = 0$, and $\{f, g\} = f_x g_y - f_y g_x$ is the standard Poisson bracket.

Non-example: the wedge product $(P, Q) \mapsto P \wedge Q$ is bilinear but is not this bracket.
It fails property 2: for a vector field $X$ and a function $f$, it gives $X \wedge f = fX$, while property 2 requires the function $X(f)$.
