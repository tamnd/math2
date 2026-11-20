---
tag: 0TZAG60ZYT
kind: statement
role: theorem
name: Row rank equals column rank
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
about: [0ZC9YTXZRY, 069MCGX635, 03AJKXH1AV]
uses: [0EWQEYRVA8, 0EP73HK4C4, 0W809K6AW0]
formal:
  - system: lean4
    library: mathlib
    decl: Matrix.rank_transpose
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Proofs that column rank = row rank
  - book: isbn:9780134860244
    locator: Section 3.2
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L3738
    locator: ap-linear-algebra.tex:3738
  - url: https://github.com/jirilebl/diffyqs/blob/658bcae9fb710f3fae2c9da4ca4524ce157453af/ap-linear-algebra.tex#L4825
    locator: ap-linear-algebra.tex:4825
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section6-2.xml#L1144
    locator: src/section6-2.xml:1144
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section7-4.xml#L1628
    locator: src/section7-4.xml:1628
---

## Statement

Let $F$ be a field and let $A$ be an $m \times n$ matrix over $F$.
Then the dimension of the [[row space|069MCGX635]] of $A$ equals the dimension of the [[column space|03AJKXH1AV]] of $A$.
Equivalently, $\rank A^\top = \rank A$, where $A^\top$ is the [[transpose|09DXWYRD43]].

## Remarks

### Why each hypothesis is needed

- The entries must lie in a field, or at least in a commutative ring where rank makes sense.
  Over a noncommutative division ring, the left row rank equals the right column rank, but the left column rank can differ.
- The matrix may have any shape. For $m \ne n$, the row space and the column space lie in different spaces $F^n$ and $F^m$, but their dimensions agree.

### Consequences

- $\rank A \le \min(m, n)$, since the column space lies in $F^m$ and the row space lies in $F^n$.
- The [[four fundamental subspaces|~c3d8720b]] have dimensions $r$, $n - r$, $r$ and $m - r$.
- A square matrix has independent rows if and only if it has independent columns.
- The second half of the [[rank of a product|02FDWY55AS]], $\rank(AB) \le \rank B$, follows by transposing.

### Converse

The row space and the column space are different subspaces in general, even for square matrices.
For $\begin{pmatrix} 1 & 1 \\ 0 & 0 \end{pmatrix}$ the row space is spanned by $(1, 1)$ and the column space by $(1, 0)$.

### Generalizations

- For a linear map $T \colon V \to W$, the dual map $T^* \colon W^* \to V^*$ has the same rank as $T$.
- The [[determinantal rank|0BT9BYWVRY]], the largest order of a nonzero minor, equals both ranks.

## History

Several proofs are known, and Wikipedia lists proofs by row reduction, by linear combinations, by orthogonality and by duality.

## Explanations

### L1 human

The number of independent rows of a matrix always equals the number of independent columns.
This is surprising, because rows and columns live in different spaces.
For a $3 \times 5$ matrix, it shows at once that the rank is at most $3$.

### L2 human

There are several proofs.

- [[By row reduction|~1fa1acd5]]: both dimensions equal the number of pivots of the reduced row echelon form.
- [[By a rank factorization|S1C1ATEFW1]]: a basis of the column space gives $A = CR$ with $r$ rows in $R$, so the row rank is at most $r$.
- [[By orthogonality over the real numbers|~53093409]]: $A$ is injective on the row space, so the row space fits into the column space.
- By duality: the [[matrix of the dual map is the transpose|0ZPB3180AY]], and the [[dimension of the annihilator|06Q1EFVH0Q]] gives the equal ranks. This proof belongs to the sub-area on dual spaces.

### L3 human

The rank is the dimension of $\im T$ for the map $T(x) = Ax$, and the row rank is the rank of the dual map $T^*$.
The duality proof shows $\im T^* = (\ker T)^0$, the annihilator of the kernel, which has dimension $n - \dim \ker T = \rank T$.
In Mathlib the statement is `Matrix.rank_transpose`.
