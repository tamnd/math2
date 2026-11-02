---
tag: NHY3HE7RCN
kind: definition
name: Surgery theory
msc: [57R65, 57R67]
defines: MHHN8386TG
uses: [F45VQ47GPV, T62369RFH6, T8BVGPPSZP]
sources:
  - url: https://en.wikipedia.org/wiki/Surgery_theory
---

## Definition

Let $M$ be a smooth manifold of dimension $n$, and let $p, q \ge 0$ be integers with $p + q = n$.
Let $\varphi \colon S^p \times D^q \to M$ be a smooth embedding, where $S^p$ is the $p$-[[sphere|T62369RFH6]] and $D^q$ the closed $q$-disc.
The *surgery* on $M$ along $\varphi$ is the following manifold:
$$M' = \bigl(M \setminus \varphi(S^p \times \operatorname{int} D^q)\bigr) \cup_{\varphi} \bigl(D^{p+1} \times S^{q-1}\bigr).$$
Here the two pieces are glued along their common boundary $S^p \times S^{q-1}$ by $\varphi$, and corners are smoothed.
The number $p$ is the index of the surgery.
*Surgery theory* is the study of manifolds through such operations.
Its central problem is to turn a degree one normal map into a homotopy equivalence by a sequence of surgeries.

## Remarks

The *trace* of the surgery is $W = (M \times [0, 1]) \cup_{\varphi \times \set{1}} (D^{p+1} \times D^q)$, a $(p+1)$-handle attached to $M \times [0,1]$.
It is a [[cobordism|T8BVGPPSZP]] from $M$ to $M'$, and every compact cobordism is obtained by a finite sequence of such traces.
Example: let $M = S^1 \times S^1$ and $\varphi$ an embedding of $S^1 \times D^1$ as an annulus around the meridian circle.
Removing the open annulus leaves a cylinder $S^1 \times [0,1]$, and gluing in two discs $D^2 \times S^0$ caps it to $S^2$.
So surgery of index $1$ on a torus along a meridian gives the sphere.
Non-example: let $C$ be the core circle of a Möbius band inside $\R P^2$.
Every tubular neighbourhood of $C$ is a Möbius band and not an annulus, so $C$ has no neighbourhood of the form $S^1 \times D^1$.
So there is no embedding $\varphi$ as in the definition with core $C$, and no surgery along $C$ is defined.

## Explanations

### L1 human

To do surgery, find a sphere with a product neighbourhood inside a manifold and cut that neighbourhood out.
Then fill the hole with the other natural piece that has the same boundary.
Surgery along a non-separating circle in a surface removes a handle; surgery along two points adds one.
The operation changes the topology in a controlled way, and the trace records it as a cobordism.
