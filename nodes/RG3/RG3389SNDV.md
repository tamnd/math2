---
tag: RG3389SNDV
kind: definition
name: Satake diagram
msc: ["17B20", "22E46", "17B22"]
defines: KY3M36JCE8
uses: [K7VVYFE9YJ, 59DHW3BZTW, BB098JPWGA, CSBM217V1N, CS73JZQS66]
sources:
  - url: https://en.wikipedia.org/wiki/Satake_diagram
---

## Definition

Let $\mathfrak{g}_0$ be a finite-dimensional real semisimple Lie algebra with a [[Cartan decomposition|K7VVYFE9YJ]] $\mathfrak{g}_0 = \mathfrak{k} \oplus \mathfrak{p}$.
Let $\mathfrak{a}$ be a maximal abelian subspace of $\mathfrak{p}$, and let $\mathfrak{t}$ be a maximal abelian subspace of the centralizer of $\mathfrak{a}$ in $\mathfrak{k}$.
Then $\mathfrak{h} = (\mathfrak{t} \oplus \mathfrak{a}) \otimes_\R \C$ is a [[Cartan subalgebra|BB098JPWGA]] of the complexification $\mathfrak{g} = \mathfrak{g}_0 \otimes_\R \C$, of which $\mathfrak{g}_0$ is a [[real form|59DHW3BZTW]].
Let $\Phi$ be the roots of $(\mathfrak{g}, \mathfrak{h})$; they are real on $i\mathfrak{t} \oplus \mathfrak{a}$.
Order the dual of $i\mathfrak{t} \oplus \mathfrak{a}$ lexicographically with respect to a basis whose first vectors span the dual of $\mathfrak{a}$.
Let $\Delta$ be the base of [[simple roots|CSBM217V1N]] for the positive roots of this order.
The *Satake diagram* of $\mathfrak{g}_0$ is the [[Dynkin diagram|CS73JZQS66]] of $\Phi$ with vertex set $\Delta$, decorated as follows:

1. a vertex $\alpha$ is painted black if $\alpha$ vanishes on $\mathfrak{a}$, and white otherwise;
2. two distinct white vertices $\alpha, \beta$ are joined by a double-headed arrow if $\alpha$ and $\beta$ have the same restriction to $\mathfrak{a}$.

## Remarks

Example: for the compact real form $\mathfrak{su}(n)$ of $\mathfrak{sl}_n(\C)$, one has $\mathfrak{p} = 0$, so $\mathfrak{a} = 0$ and every vertex is black.
For $\mathfrak{sl}_n(\R)$, the space $\mathfrak{a}$ of diagonal matrices of trace $0$ is already a Cartan subalgebra.
No root vanishes on it, and distinct roots have distinct restrictions, so all vertices are white and there are no arrows.
Non-example: the diagram of $A_1$ with one white vertex is not the Satake diagram of $\mathfrak{su}(2)$.
For $\mathfrak{su}(2)$ the space $\mathfrak{a}$ is $0$, so the vertex must be black; the white vertex belongs to $\mathfrak{sl}_2(\R)$.
The Satake diagram does not depend on the choices, up to isomorphism of decorated diagrams.
Two real semisimple Lie algebras are isomorphic if and only if their Satake diagrams are isomorphic.
The restricted roots of $\mathfrak{g}_0$ with respect to $\mathfrak{a}$ are the nonzero restrictions to $\mathfrak{a}$ of the roots in $\Phi$.

## Explanations

### L1 human

A Satake diagram is a Dynkin diagram with black and white vertices and some arrows.
It records which simple roots see the noncompact directions $\mathfrak{a}$ of a real form, and which ones look alike from there.
