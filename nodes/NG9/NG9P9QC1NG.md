---
tag: NG9P9QC1NG
kind: definition
name: Subalgebra
msc: [16S99, 13B02, 08A30]
defines: 7CHG6SD365
uses: [1TZSV19D85, 0859D58WPD, 0RGZ10DFPG]
sources:
  - url: https://en.wikipedia.org/wiki/Subalgebra
---

## Definition

Let $K$ be a commutative ring and let $A$ be an [[associative algebra|1TZSV19D85]] over $K$ with unit element $1$.
A *subalgebra* of $A$ is a subset $B \subseteq A$ such that:

1. $1 \in B$.
2. If $a, b \in B$, then $a + b \in B$ and $ab \in B$.
3. If $k \in K$ and $b \in B$, then $kb \in B$.

## Remarks

Clause 3 with $k = -1$ gives $-b \in B$, so $B$ is a [[subring|0859D58WPD]] of $A$ and a [[submodule|0RGZ10DFPG]] of the $K$-module $A$.
With the operations of $A$, the set $B$ is then a $K$-algebra.
Let $\eta \colon K \to A$, $k \mapsto k1$, be the structure map.
A subset $B$ is a subalgebra exactly when it is a subring of $A$ that contains $\eta(K)$, because $kb = \eta(k)b$.

Example: in the $\R$-algebra $M_2(\R)$ of real $2 \times 2$ matrices, the set of upper triangular matrices is a subalgebra.
The identity matrix is upper triangular, and sums and real multiples of upper triangular matrices are upper triangular.
For upper triangular $P$ and $Q$, the $(2,1)$ entry of $PQ$ is $p_{21} q_{11} + p_{22} q_{21} = 0$, since $p_{21} = q_{21} = 0$.

Non-example: in the $\R$-algebra $\R[x]$, the set $\Z[x]$ of polynomials with integer coefficients satisfies clauses 1 and 2 but not clause 3.
For $k = 1/2$ and $b = 1$ the product $kb = 1/2$ is not in $\Z[x]$.
So $\Z[x]$ is a subring of $\R[x]$ but not an $\R$-subalgebra.

Some authors work with algebras without a unit element and drop clause 1.
For a field $K$, a subalgebra is a linear subspace of $A$ that contains $1$ and is closed under multiplication.
