---
tag: 0XYYT5KNTX
kind: concept
name: Internal direct sum of subspaces
aliases: [internal-direct-sum]
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
specializes: [0JMTY8MF54]
uses: [00YC1D652K, 0JMTY8MF54, 0V33SPH7RR]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_sum_of_modules
    locator: Internal direct sum
  - book: isbn:9783031410253
    locator: Section 1C
  - book: isbn:9780134860244
    locator: Section 1.3
  - url: https://hefferon.net/linearalgebra/
    locator: Chapter Two, Section III.4
---

## Summary

Let $V$ be a [[vector space|000AYPA9AJ]] over a field $F$, and let $U_1, \dots, U_k$ be [[subspaces|00YC1D652K]] of $V$.
The space $V$ is the *internal direct sum* of $U_1, \dots, U_k$, written $V = U_1 \oplus \cdots \oplus U_k$, when each $v \in V$ can be written in exactly one way as $v = u_1 + \cdots + u_k$ with $u_i \in U_i$ for each $i$.
For two subspaces, this holds exactly when the [[sum|0JMTY8MF54]] $U + W$ is $V$ and the [[intersection|0V33SPH7RR]] $U \cap W$ is $\{0\}$.
A direct sum splits a space into pieces that do not interact, so we can study vectors and linear maps one piece at a time.

## Motivation

A basis $b_1, \dots, b_n$ of $V$ splits each vector into unique components along the lines $F b_1, \dots, F b_n$.
Often we want to split a space into larger pieces: a plane and a line, or the even and the odd functions.
The sum $U + W$ of two subspaces gives each vector of $U + W$ as $u + w$, but this expression need not be unique.
For the $xy$-plane and the $yz$-plane in $\R^3$, the vector $(0, 1, 0)$ is $(0, 1, 0) + 0$ and also $0 + (0, 1, 0)$.
The direct sum is the case of a sum in which the expression is unique, so that the pieces behave like coordinates.

## Notation

We write $V = U \oplus W$ for two subspaces and $V = U_1 \oplus \cdots \oplus U_k = \bigoplus_{i=1}^k U_i$ for several.
The same symbol $\oplus$ denotes the [[external direct sum|0S7W6EG32V]] of spaces that are not inside a common space.
Some books use "direct sum" for the internal notion only, and other books use it for the external notion only.
The two notions agree up to a canonical isomorphism: the map $U_1 \times \cdots \times U_k \to V$, $(u_1, \dots, u_k) \mapsto u_1 + \cdots + u_k$, is bijective exactly when $V = U_1 \oplus \cdots \oplus U_k$.
Mathlib writes `IsCompl U W` for two subspaces with $U \cap W = 0$ and $U + W = V$, and `DirectSum.IsInternal` for a family of subspaces.
The external direct sum is `DirectSum` in Mathlib.

## Remarks

### Examples

- [[The plane as the direct sum of two lines|TBP8ZNSCGQ]]: $\R^2 = F(1, 0) \oplus F(1, 2)$, and the two lines need not be perpendicular.
- [[Even and odd functions|YK0X90WB6H]]: each function $\R \to \R$ is a unique sum of an even and an odd function.
- $\R^3$ is the direct sum of the $xy$-plane and the $z$-axis, since $(x, y, z) = (x, y, 0) + (0, 0, z)$ and the two meet only in $0$.
- Each square matrix over $\R$ is a unique sum of a symmetric and a skew-symmetric matrix, by the [[decomposition into symmetric and skew-symmetric parts|K284W6D15Z]].
- If $b_1, \dots, b_n$ is a [[basis|0KCQ9Y3QKA]] of $V$, then $V = F b_1 \oplus \cdots \oplus F b_n$, because coordinates are unique.

### Non-examples

- [[Three lines in the plane|FRMQ1JB4RB]] that meet pairwise only in $0$ do not form a direct sum: the condition of unique expression fails.
- The $xy$-plane and the $yz$-plane of $\R^3$ have sum $\R^3$, but they meet in the $y$-axis, so the condition $U \cap W = \{0\}$ fails.
- [[The $x$-axis and the $y$-axis in $\R^3$|PAJHW0002P]] meet only in $0$, but their sum is a plane, so they are not a direct sum decomposition of $\R^3$.

### Basic properties

- The [[criteria for a direct sum of two subspaces|20A0K3KBZD]]: $U + W$ is direct if and only if $U \cap W = \{0\}$, if and only if $0 = u + w$ forces $u = w = 0$.
- The [[dimension criterion|P4JG9DJ2HH]]: for finite-dimensional $V$, we have $V = U \oplus W$ if and only if $U \cap W = \{0\}$ and $\dim U + \dim W = \dim V$.
- The [[criterion for several subspaces|FVKY28HHBC]]: $U_1 + \cdots + U_k$ is direct if and only if each $U_i$ meets $U_1 + \cdots + U_{i-1}$ only in $0$.
- If $V = U \oplus W$, then $W$ is a [[complement|0M83V17KHX]] of $U$, and each complement of $U$ is isomorphic to $V / U$.
- The decompositions $V = U \oplus W$ correspond exactly to the [[projections|033DA1WE8Y]] on $V$, by the [[theorem on projections and decompositions|2ZX5Q7V4VN]].

### History

The dimension formula for a sum of subspaces carries the name of Grassmann, who studied sums and intersections of subspaces in his Ausdehnungslehre.
Today the symbol $\oplus$ is standard for both the internal and the external direct sum.

### Common errors

- Checking only the pairwise intersections for three or more subspaces. The three lines of the non-example show that this test is not enough.
- Confusing the sum $U + W$ with the union $U \cup W$. The union of two lines in $\R^2$ is not a subspace, but their sum is the whole plane.
- Thinking that the summands must be perpendicular. Direct sums need no inner product, and the lines $F(1, 0)$ and $F(1, 2)$ form one.

## Explanations

### L1 human

A direct sum cuts a space into pieces so that every vector splits into one part in each piece, in only one way.
In the plane, take the horizontal line and the line through $(1, 2)$.
The point $(3, 4)$ is $(1, 0)$ on the first line plus $(2, 4)$ on the second line.
No other choice of two such parts gives $(3, 4)$.
This works like coordinates, but each piece can be a whole line or a whole plane.

### L2 human

We check that $\R^3 = U \oplus W$ for the plane $U = \{(x, y, z) : z = 0\}$ and the line $W = \R (1, 1, 1)$.

1. $U$ and $W$ are subspaces: $U$ is the kernel of $(x, y, z) \mapsto z$, and $W$ is a span.
2. $U \cap W = \{0\}$: a vector $t(1, 1, 1)$ lies in $U$ only when $t = 0$.
3. $\dim U + \dim W = 2 + 1 = 3 = \dim \R^3$.
4. By the [[dimension criterion|P4JG9DJ2HH]], $\R^3 = U \oplus W$.
5. Explicitly, $(x, y, z) = (x - z, y - z, 0) + z(1, 1, 1)$.

A direct sum is used to split a problem into smaller ones.
If a linear map sends $U$ into $U$ and $W$ into $W$, then its matrix in a basis adapted to the sum is [[block diagonal|001T5FJDC1]].
The trap is the case of three or more subspaces, where pairwise zero intersections do not give a direct sum.

### L3 human

The internal direct sum is the case where the canonical map from the [[external direct sum|0S7W6EG32V]] $\bigoplus_i U_i$ to $V$ is an isomorphism.
In the lattice of subspaces, $V = U \oplus W$ says that $W$ is a lattice complement of $U$, which is why Mathlib uses `IsCompl`.
For modules over a ring, a submodule need not have a complement, and the direct summands are exactly the images of idempotent endomorphisms.
Direct sums return in the eigenspace and generalized eigenspace decompositions, in the primary decomposition of an operator, and in the [[orthogonal complement|0XJXTBCB2T]] of an inner product space.
