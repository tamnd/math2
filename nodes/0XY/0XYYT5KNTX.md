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

A direct sum cuts a vector space into pieces so that every vector splits into one part from each piece, and in only one way.
The pieces then act like coordinates, except that each piece can be a whole line, a plane or a bigger subspace.
Let $V$ be a [[vector space|000AYPA9AJ]] over a field $F$, and let $U_1, \dots, U_k$ be [[subspaces|00YC1D652K]] of $V$.
The space $V$ is the *internal direct sum* of $U_1, \dots, U_k$, written $V = U_1 \oplus \cdots \oplus U_k$, when each $v \in V$ can be written in exactly one way as
$$v = u_1 + u_2 + \cdots + u_k, \qquad u_i \in U_i \text{ for each } i.$$
For two subspaces there is a short test: $V = U \oplus W$ exactly when the [[sum|0JMTY8MF54]] $U + W$ is all of $V$ and the [[intersection|0V33SPH7RR]] $U \cap W$ is $\{0\}$.

## Motivation

A basis $b_1, \dots, b_n$ of $V$ splits each vector into unique components along the lines $F b_1, \dots, F b_n$.
Often we want coarser pieces than lines.
A problem in $\R^3$ may have a natural plane and a natural axis, and a function on $\R$ has an even part and an odd part.
The sum $U + W$ of two subspaces already writes each of its vectors as $u + w$, but this expression need not be unique.
For the $xy$-plane and the $yz$-plane in $\R^3$, the vector $(0, 1, 0)$ equals $(0, 1, 0) + 0$ and also $0 + (0, 1, 0)$.
The direct sum is the case where the expression is unique, so that the two pieces never get in each other's way.

Once a space is split, many questions split with it.
A linear map that sends each piece into itself has a [[block diagonal|001T5FJDC1]] matrix in a basis built from the pieces, so it can be studied one block at a time.
The same idea returns later as [[complements|0M83V17KHX]], [[projections|033DA1WE8Y]], eigenspace decompositions and the [[orthogonal complement|0XJXTBCB2T]].

## Notation

We write $V = U \oplus W$ for two subspaces and $V = U_1 \oplus \cdots \oplus U_k = \bigoplus_{i=1}^k U_i$ for several.
The same symbol $\oplus$ also denotes the [[external direct sum|0S7W6EG32V]], which builds a new space out of spaces that are not inside a common space.
Some books use "direct sum" for the internal notion only, and other books for the external notion only, so check which one a book means.
The two notions agree up to a canonical isomorphism: the addition map $(u_1, \dots, u_k) \mapsto u_1 + \cdots + u_k$ from the external sum to $V$ is bijective exactly when $V = U_1 \oplus \cdots \oplus U_k$.
Mathlib writes `IsCompl U W` for two subspaces with $U \cap W = 0$ and $U + W = V$, `DirectSum.IsInternal` for a family of subspaces, and `DirectSum` for the external sum.

## Remarks

### A first decomposition

Take the line $U = \R(1, 0)$ and the line $W = \R(1, 2)$ in the plane.
To split the vector $(3, 4)$, solve $(3, 4) = a(1, 0) + b(1, 2)$.
The second coordinate gives $2b = 4$, so $b = 2$, and then the first coordinate gives $a + 2 = 3$, so $a = 1$:
$$(3, 4) = (1, 0) + (2, 4).$$
The same steps work for every $(x, y)$, with $b = y/2$ and $a = x - y/2$, and they leave no choice.
So every vector splits, and it splits in only one way, which means $\R^2 = U \oplus W$.
The lines are not perpendicular, and no inner product is needed; [[the plane as the direct sum of two lines|TBP8ZNSCGQ]] works this out in full.

### Three standard splittings

The space $\R^3$ is the direct sum of the $xy$-plane and the $z$-axis, since $(x, y, z) = (x, y, 0) + (0, 0, z)$ and the two meet only in $0$.
Every function $f \colon \R \to \R$ is the sum of the even function $\tfrac12 (f(x) + f(-x))$ and the odd function $\tfrac12 (f(x) - f(-x))$, and only the zero function is both even and odd, so the [[even and odd functions|YK0X90WB6H]] split the space of all functions.
In the same way every real square matrix is a unique sum of a symmetric and a skew-symmetric matrix, by the [[decomposition into symmetric and skew-symmetric parts|K284W6D15Z]].
Finally, a [[basis|0KCQ9Y3QKA]] $b_1, \dots, b_n$ of $V$ gives $V = F b_1 \oplus \cdots \oplus F b_n$, because coordinates are unique.

### How to test for a direct sum

Uniqueness can be tested on the zero vector alone.
Two expressions $u + w = u' + w'$ of one vector give the expression $(u - u') + (w - w') = 0$ of zero, and a vector $x \ne 0$ in $U \cap W$ gives the second expression $x + (-x) = 0$.
So the sum of two subspaces is direct exactly when $U \cap W = \{0\}$, by the [[criteria for a direct sum of two subspaces|20A0K3KBZD]].
In a finite-dimensional space, a count of dimensions can replace the check that $U + W = V$: by the [[dimension criterion|P4JG9DJ2HH]], $V = U \oplus W$ exactly when $U \cap W = \{0\}$ and $\dim U + \dim W = \dim V$.
For example, a line and a plane through $0$ in $\R^3$ split the space exactly when the line does not lie in the plane, since $1 + 2 = 3$.

### What a direct sum is not

The $xy$-plane and the $yz$-plane of $\R^3$ have sum $\R^3$, but they share the $y$-axis, so the expression of $(0, 1, 0)$ is not unique.
The $x$-axis and the $y$-axis in $\R^3$ meet only in $0$, so their sum is direct, but that sum is the $xy$-plane, and [[the two axes do not split space|PAJHW0002P]].
The statement $V = U \oplus W$ makes two claims at once, that the sum is direct and that it equals $V$, and each of these examples fails one of them.

### Watch out: several summands

For three or more subspaces, the two-subspace test does not extend pair by pair.
Take the lines $U_1 = \R(1, 0)$, $U_2 = \R(0, 1)$ and $U_3 = \R(1, 1)$ in $\R^2$.
Any two of them meet only in $0$, yet the vector $(1, 1)$ has the two expressions
$$(1, 1) = 0 + 0 + (1, 1) = (1, 0) + (0, 1) + 0,$$
so the sum is not direct; see [[three lines in the plane|FRMQ1JB4RB]].
The correct test compares each subspace with the sum of the earlier ones: the [[criterion for several subspaces|FVKY28HHBC]] asks that $U_i \cap (U_1 + \cdots + U_{i-1}) = \{0\}$ for each $i \ge 2$.
Here $U_3 \cap (U_1 + U_2) = U_3$, and the test fails at once.

### Two more traps

Do not confuse the sum $U + W$ with the union $U \cup W$.
The union of the two coordinate axes in $\R^2$ does not contain $(1, 1)$, so it is not a subspace, while their sum is the whole plane.
Do not assume that the pieces must be perpendicular either.
The lines through $(1, 0)$ and $(1, 2)$ above form a direct sum, and the definition never mentions angles.

### History

The formula $\dim(U + W) + \dim(U \cap W) = \dim U + \dim W$, from which the dimension test follows, is named after Hermann Grassmann.
His *Ausdehnungslehre* of 1844 was an early study of linear spaces of arbitrary dimension.

### Try it

First, decide whether $\R^3 = U \oplus W$ for the plane $U = \{(x, y, z) : z = 0\}$ and the line $W = \R(1, 1, 1)$.
Yes: a vector $t(1, 1, 1)$ lies in $U$ only for $t = 0$, and $1 + 2 = 3$, so the dimension criterion applies.

Second, write $(2, 5, 3)$ in that decomposition.
Take $t = 3$ to remove the third coordinate: $(2, 5, 3) = (-1, 2, 0) + 3(1, 1, 1)$.

## Explanations

### L1 human

Think of a direct sum as a pair of rulers laid along two different lines in the plane.
Every point can be reached by a step along the first ruler and then a step along the second, and there is only one way to do it.
For the horizontal line and the line through $(1, 2)$, the point $(3, 4)$ is the step $(1, 0)$ followed by the step $(2, 4)$.
The rulers need not cross at a right angle.
In bigger spaces the "rulers" can be whole planes, but the rule is the same: one piece from each, one way only.

### L2 human

Here is a typical computation: show that $\R^3 = U \oplus W$ for $U = \{(x, y, z) : z = 0\}$ and $W = \R(1, 1, 1)$, and find the two parts of a general vector.
Both are subspaces, since $U$ is the kernel of $(x, y, z) \mapsto z$ and $W$ is a span.
A vector $t(1, 1, 1)$ of $W$ has third coordinate $t$, so it lies in $U$ only when $t = 0$, and $U \cap W = \{0\}$.
The dimensions add up, since $\dim U + \dim W = 2 + 1 = 3$, so the [[dimension criterion|P4JG9DJ2HH]] gives $\R^3 = U \oplus W$.
To find the parts, subtract enough of $(1, 1, 1)$ to kill the third coordinate:
$$(x, y, z) = (x - z, y - z, 0) + z(1, 1, 1).$$
Check: the right side has entries $x - z + z$, $y - z + z$ and $0 + z$.
The decomposition is what you use to split a problem: a linear map that keeps $U$ and $W$ in place has a block diagonal matrix in the basis $(1, 0, 0), (0, 1, 0), (1, 1, 1)$.

### L3 human

The internal direct sum is the case where the canonical map from the [[external direct sum|0S7W6EG32V]] $\bigoplus_i U_i$ to $V$ is an isomorphism.
In the lattice of subspaces, $V = U \oplus W$ says that $W$ is a lattice complement of $U$, which is why Mathlib calls it `IsCompl`.
The lattice is modular but not distributive, and the three lines in the plane already witness this, which is why pairwise tests fail for several summands.
For modules over a ring, a submodule need not have a complement, and the direct summands of a module are exactly the images of its idempotent endomorphisms.
Direct sums return in the [[existence of complements|0P9T8WHNMH]], in [[quotient spaces|0BR3FY5Q8M]], in the eigenspace and primary decompositions of an operator, and in the orthogonal decomposition of an inner product space.
