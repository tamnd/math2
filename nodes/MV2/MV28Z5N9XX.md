---
tag: MV28Z5N9XX
kind: statement
role: theorem
name: Smith normal form
msc: [15A21, 13F10, 15B36]
uses: [0CMD0BCH8T, 0EB9N0S33C, 0PG2H7WKGG, 0BT9BYWVRY, 0C8WYW4KYQ, 0WHCA4SVP2]
about: [0WHCA4SVP2]
sources:
  - url: https://en.wikipedia.org/wiki/Smith_normal_form
same_as:
  wikidata: Q7545384
  wikipedia: Smith normal form
---

## Statement

Let $R$ be a [[principal ideal domain|0CMD0BCH8T]], and let $A$ be an $m \times n$ matrix over $R$.
Then there are an [[invertible|0EB9N0S33C]] $m \times m$ matrix $P$ and an invertible $n \times n$ matrix $Q$ over $R$, an integer $r \ge 0$, and nonzero $d_1, \dots, d_r \in R$ such that:

1. $PAQ$ is the $m \times n$ matrix with diagonal entries $d_1, \dots, d_r, 0, \dots, 0$ and all other entries $0$;
2. $d_i$ [[divides|0PG2H7WKGG]] $d_{i+1}$ for $1 \le i < r$.

The number $r$ is the rank of $A$, and the elements $d_1, \dots, d_r$ are unique up to multiplication by units of $R$.

## Remarks

Over a Euclidean domain such as $\Z$ or $F[x]$, the proof is an algorithm.
Row and column operations move an entry of smallest size to the top left corner.
Division with remainder then reduces the rest of its row and column.
This is repeated until the corner entry divides all other entries.
Then the process continues on the remaining block.
Uniqueness follows because $d_1 d_2 \cdots d_k$ is a [[greatest common divisor|0C8WYW4KYQ]] of the $k \times k$ [[minors|0BT9BYWVRY]] of $A$, and this gcd does not change under multiplication by invertible matrices.

Example over $\Z$: for $A = \begin{pmatrix} 2 & 4 \\ 6 & 8 \end{pmatrix}$, the gcd of the entries is $2$ and $\det A = -8$.
So $d_1 = 2$ and $d_1 d_2 = 8$ up to sign, and the Smith normal form is $\operatorname{diag}(2, 4)$.

The hypothesis that $R$ is a principal ideal domain is needed.
Over $\Z[x]$, the $1 \times 2$ matrix $(2 \;\; x)$ has no Smith normal form: $d_1$ would generate the ideal $(2, x)$, which is not principal.

The $d_i$ are the [[invariant factors|0WHCA4SVP2]] of $A$.

## Explanations

### L1 human

Any matrix over the integers can be brought to diagonal form by invertible integer row and column operations.
Moreover, each diagonal entry divides the next one, and these entries do not depend on the choice of operations.
They are a complete set of invariants of the matrix up to such operations.

### L2 human

The Smith normal form of a presentation matrix gives the structure theorem for finitely generated modules over a principal ideal domain.
For $R = \Z$ this is the [[structure theorem for finitely generated abelian groups|0RY0B72XAS]].
Applied to $xI - M$ over $F[x]$, it gives the invariant factors of a square matrix $M$ over a field $F$, hence the rational canonical form.
Two square matrices $M$ and $N$ over $F$ are similar if and only if $xI - M$ and $xI - N$ have the same Smith normal form.
