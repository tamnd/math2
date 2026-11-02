---
tag: CZW4BPZPZC
kind: definition
name: Endomorphism monoid
msc: [08A35, 20M20]
defines: QFE3FKNQQ1
uses: [983GZBQYT4, KBXSZC6BV1, 0N6R902FG1, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism
---

## Definition

Let $\mathbf{A}$ be a [[structure|983GZBQYT4]] with domain $A$.
An *endomorphism* of $\mathbf{A}$ is a [[homomorphism|KBXSZC6BV1]] from $\mathbf{A}$ to $\mathbf{A}$.
Let $E$ be the set of endomorphisms of $\mathbf{A}$, let $\circ$ be [[composition|0THBK9V825]] and let $\id_A$ be the identity map of $A$.
The *endomorphism monoid* of $\mathbf{A}$ is the [[monoid|0N6R902FG1]] $\End(\mathbf{A}) = (E, \circ, \id_A)$.

## Remarks

The composite of two homomorphisms is a homomorphism and $\id_A$ is a homomorphism, so $E$ is closed under $\circ$ and contains $\id_A$; composition is associative.

Example: let $\mathbf{A} = (\Z, +, 0)$.
Each endomorphism $h$ satisfies $h(x) = x\,h(1)$ for all $x \in \Z$, by induction on $x \ge 0$ and $h(-x) = -h(x)$.
So $h \mapsto h(1)$ is an isomorphism from $\End(\mathbf{A})$ to the monoid $(\Z, \cdot, 1)$, since $(g \circ h)(1) = g(1)\,h(1)$.

Non-example: the map $x \mapsto x + 1$ lies in the monoid of all maps $\Z \to \Z$ but not in $\End(\Z, +, 0)$, because it sends $0$ to $1$.

The invertible elements of $\End(\mathbf{A})$ are the automorphisms of $\mathbf{A}$.
