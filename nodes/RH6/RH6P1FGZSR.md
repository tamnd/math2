---
tag: RH6P1FGZSR
kind: definition
name: Representation of a quiver
msc: [16G20]
defines: TXVWFWP6VQ
uses: [RE9YFFS3TS, 04C5ZBG1WT, 000AYPA9AJ, 0NRYHJPQG2]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $Q = (Q_0, Q_1, s, t)$ be a [[quiver|RE9YFFS3TS]].
A *representation* $V$ of $Q$ over $k$ consists of:

1. a [[vector space|000AYPA9AJ]] $V_i$ over $k$ for each vertex $i \in Q_0$;
2. a [[linear map|0NRYHJPQG2]] $V_a \colon V_{s(a)} \to V_{t(a)}$ for each arrow $a \in Q_1$.

A *morphism* $\varphi \colon V \to W$ of representations is a family of linear maps $\varphi_i \colon V_i \to W_i$, $i \in Q_0$, such that $\varphi_{t(a)} \circ V_a = W_a \circ \varphi_{s(a)}$ for every arrow $a$.
If $Q_0$ is finite and each $V_i$ is finite-dimensional, $V$ is *finite-dimensional*, and its *dimension vector* is $(\dim V_i)_{i \in Q_0}$.

## Remarks

Example: for the quiver $1 \to 2$ with arrow $a$, the data $V_1 = V_2 = k$ and $V_a = \id_k$ form a representation with dimension vector $(1, 1)$.
Non-example: for the same quiver, a vector space at each vertex with a linear map $V_2 \to V_1$ is not a representation.
Clause 2 asks for a map from the source of $a$ to its target.
Direct sums are taken vertexwise, and a nonzero representation is indecomposable if it is not a direct sum of two nonzero representations.
For a finite quiver, representations of $Q$ correspond to left modules over the [[path algebra|2PYANBGXFD]] $kQ$, and this is an equivalence of categories.
