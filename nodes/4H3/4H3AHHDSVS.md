---
tag: 4H3AHHDSVS
kind: definition
name: Poisson manifold
msc: [53D17]
defines: A2KQ49Y4NF
uses: [F45VQ47GPV]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_manifold
---

## Definition

Let $M$ be a [[smooth manifold|F45VQ47GPV]] and let $C^\infty(M)$ be the algebra of smooth real functions on $M$.
A *Poisson bracket* on $M$ is a map $\{\cdot, \cdot\} \colon C^\infty(M) \times C^\infty(M) \to C^\infty(M)$ such that for all $f, g, h \in C^\infty(M)$:

1. it is bilinear over $\R$;
2. it is antisymmetric: $\{f, g\} = -\{g, f\}$;
3. it satisfies the Jacobi identity: $\{f, \{g, h\}\} + \{g, \{h, f\}\} + \{h, \{f, g\}\} = 0$;
4. it satisfies the Leibniz rule: $\{f, gh\} = \{f, g\}\, h + g\, \{f, h\}$.

A *Poisson manifold* is a smooth manifold with a Poisson bracket.

## Remarks

Clauses 1 to 3 say that $(C^\infty(M), \{\cdot, \cdot\})$ is a Lie algebra over $\R$.
By clause 4, there is a unique bivector field $\pi$, a section of $\Lambda^2 TM$, with $\{f, g\} = \pi(df, dg)$; the Jacobi identity is then the condition $[\pi, \pi] = 0$ for the Schouten bracket.

Example: every [[symplectic manifold|CAN490EPRT]] with its [[Poisson bracket|2S0MXDT4YH]] is a Poisson manifold.
Another example is the dual $\mathfrak{g}^*$ of a finite-dimensional Lie algebra $\mathfrak{g}$, with $\{f, g\}(\xi) = \langle \xi, [df_\xi, dg_\xi] \rangle$, where $df_\xi \in (\mathfrak{g}^*)^* = \mathfrak{g}$.
On $\mathfrak{g}^*$ for $\mathfrak{g} = \mathfrak{so}(3)$ with suitable coordinates, $\{x, y\} = z$, $\{y, z\} = x$ and $\{z, x\} = y$.

Non-example: on $\R^3$, define a bracket by clauses 1, 2, 4 and $\{x, y\} = 1$, $\{z, x\} = x$, $\{y, z\} = 0$.
Then $\{x, \{y, z\}\} + \{y, \{z, x\}\} + \{z, \{x, y\}\} = 0 + \{y, x\} + \{z, 1\} = -1$, so the Jacobi identity fails.
