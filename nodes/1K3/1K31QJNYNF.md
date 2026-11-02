---
tag: 1K31QJNYNF
kind: definition
name: Handle decomposition
msc: [57R65, 57N99]
defines: 9V11N8VVTP
uses: [F45VQ47GPV, 7DS6B2BFK8, VKFW27WXEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Handle_decomposition
---

## Definition

Let $n \ge 1$ and $0 \le k \le n$, and let $D^j$ be the closed unit ball of $\R^j$.
An $n$-dimensional *$k$-handle* is $H = D^k \times D^{n-k}$; its *attaching region* is $\partial D^k \times D^{n-k}$.
Let $X$ be a smooth $n$-dimensional [[manifold with boundary|7DS6B2BFK8]], and let $\varphi \colon \partial D^k \times D^{n-k} \to \partial X$ be a smooth embedding onto a [[submanifold|VKFW27WXEZ]] of $\partial X$.
The result of *attaching a $k$-handle* to $X$ along $\varphi$ is $X \cup_\varphi H$.
It is the union of $X$ and $H$ with $y$ and $\varphi(y)$ identified, with corners smoothed.
Let $M$ be a compact smooth $n$-manifold, possibly with boundary.
A *handle decomposition* of $M$ is a finite chain $\emptyset = M_{-1} \subseteq M_0 \subseteq \cdots \subseteq M_r = M$ of smooth manifolds with boundary.
Each $M_i$ must be obtained from $M_{i-1}$ by attaching one handle, up to diffeomorphism.

## Remarks

The first step attaches a $0$-handle $D^0 \times D^n = D^n$ to the empty set, whose attaching region is empty.
A relative version starts from $\partial_0 M \times [0, 1]$ for a part $\partial_0 M$ of the boundary instead of the empty set; this is the form used for cobordisms.
Example: the sphere $S^n$ has a handle decomposition with one $0$-handle and one $n$-handle: the northern and southern hemispheres, glued along the equator $\partial D^n \times D^0 = S^{n-1}$.
Non-example: gluing a second disc $D^2$ to $D^2$ along a single arc of its boundary circle is not a handle attachment.
In dimension $2$ the attaching region of a $1$-handle is $\partial D^1 \times D^1$, two disjoint arcs.
That of a $2$-handle is the whole circle $\partial D^2 \times D^0$, and that of a $0$-handle is empty; none of them is a single arc.
If $f \colon M \to [a, b]$ is a Morse function with critical values in $(a, b)$, then each critical point of index $k$ gives one $k$-handle in a handle decomposition of $M$ relative to $f^{-1}(a)$.
