---
tag: M8A98HYHG2
kind: definition
name: Commutator of a ring
msc: [17A01, 17B60]
defines: T2HH02QC2M
uses: [YP5TQ6WFVN]
sources:
  - url: https://en.wikipedia.org/wiki/Commutator
    locator: Ring theory
---

## Definition

Let $A$ be a [[nonassociative ring|YP5TQ6WFVN]], for example an associative ring.
The *commutator* of $x, y \in A$ is the element
$$[x, y] = xy - yx$$
of $A$.

## Remarks

The commutator is biadditive, and $[x, x] = 0$ and $[y, x] = -[x, y]$ for all $x, y$.
So $[x, y] = 0$ if and only if $xy = yx$.
If $A$ is associative, then for all $x, y, z \in A$:
$$[x, [y, z]] + [y, [z, x]] + [z, [x, y]] = 0 \quad \text{and} \quad [x, yz] = [x, y]z + y[x, z].$$
The first is the [[Jacobi identity|ZKFN197MBR]], so $(A, [\cdot, \cdot])$ is a Lie ring; the second says that $y \mapsto [x, y]$ is a derivation.
Example: in the $2 \times 2$ real matrices, $E = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $F = \begin{pmatrix} 0 & 0 \\ 1 & 0 \end{pmatrix}$ give $EF - FE = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix} \neq 0$.
In a commutative ring every commutator is $0$.
The *anticommutator* is $xy + yx$.
