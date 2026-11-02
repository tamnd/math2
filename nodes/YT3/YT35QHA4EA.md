---
tag: YT35QHA4EA
kind: definition
name: Compact quantum group
msc: [46L67, 20G42, 58B32]
defines: FHQKT6HPW2
uses: [0TVJZYB6SH]
sources:
  - url: https://en.wikipedia.org/wiki/Compact_quantum_group
---

## Definition

Let $A$ be a unital C*-algebra and let $A \otimes A$ denote its minimal C*-tensor product with itself.
A *compact quantum group* is a pair $(A, \Delta)$ where $\Delta \colon A \to A \otimes A$ is a unital $*$-homomorphism, called the comultiplication, such that:

1. $(\Delta \otimes \id) \circ \Delta = (\id \otimes \Delta) \circ \Delta$ (coassociativity);
2. the linear spans of $\set{\Delta(a)(1 \otimes b) : a, b \in A}$ and of $\set{\Delta(a)(b \otimes 1) : a, b \in A}$ are both norm-dense in $A \otimes A$ (cancellation).

## Remarks

Example: let $G$ be a [[compact|0TVJZYB6SH]] Hausdorff group and $A = C(G)$, so that $A \otimes A = C(G \times G)$.
Set $\Delta(f)(s, t) = f(st)$.
Coassociativity is the associativity $(rs)t = r(st)$.
The products $\Delta(f)(1 \otimes g)$ are the functions $(s, t) \mapsto f(st) g(t)$.
Since $(s, t) \mapsto (st, t)$ is a homeomorphism of $G \times G$, their span is a self-adjoint subalgebra that separates points and contains $1$.
So it is dense by the Stone–Weierstrass theorem, and the other span is handled in the same way.

Non-example: let $S = [0, 1]$ with ordinary multiplication, a compact semigroup that is not a group, and define $\Delta$ on $C(S)$ by the same formula.
Clause 1 holds, but every function $(s, t) \mapsto f(st) g(t)$ is constant in $s$ on the line $t = 0$.
This property passes to linear combinations and uniform limits, so the span is not dense, and clause 2 fails.

For commutative $A$, every compact quantum group is of the form $C(G)$ for a compact group $G$.
Every compact quantum group has a unique state $h$, the Haar state, with $(h \otimes \id)\Delta(a) = (\id \otimes h)\Delta(a) = h(a) 1$ for all $a \in A$; it plays the role of the Haar measure.
