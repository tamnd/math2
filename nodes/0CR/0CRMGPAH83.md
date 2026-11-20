---
tag: 0CRMGPAH83
kind: concept
name: Linear independence
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0V8F3E48E6, 0JB3DP1BMF]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_independence
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-4.xml#L510
    locator: src/section2-4.xml:510
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.5
same_as:
  wikidata: Q27670
  wikipedia: Linear independence
---

## Summary

A family of vectors $(v_i)_{i \in I}$ in a vector space over $F$ is linearly independent when only the trivial [[linear combination|0V8F3E48E6]] of them equals $0$.
See the [[definition|0EVHJFTG9Z]].
Equivalently, no vector of the family is a combination of the others; this is the [[dependence lemma|H75GS7QVPB]].
Independence is the second half of the notion of a [[basis|0KCQ9Y3QKA]], and it makes coordinates unique.

## Motivation

A spanning set may have redundant vectors, which are combinations of the others.
Independence says that no vector is redundant, so each one adds a new direction.
Then each vector of the span has exactly one list of coefficients, and we can compute with these coefficients as coordinates.

## Notation

We say "$v_1, \dots, v_k$ are independent" for the family $(v_1, \dots, v_k)$.
A family that is not independent is *linearly dependent*, and a relation $\sum a_i v_i = 0$ with some $a_i \ne 0$ is a *dependence relation*.
In Mathlib, `LinearIndependent F v` is stated for a family `v : ι → V`, not for a set.

## Remarks

### Examples

1. $(1, 0), (1, 1)$ in $\R^2$: if $a(1, 0) + b(1, 1) = (a + b, b) = (0, 0)$, then $b = 0$ and then $a = 0$.
2. $1, x, x^2$ in $P_2(\R)$: if $a + bx + cx^2$ is the zero polynomial, then $a = b = c = 0$ by the definition of equality of polynomials.
3. The functions $\sin$ and $\cos$ on $\R$: if $a \sin t + b \cos t = 0$ for all $t$, then $t = 0$ gives $b = 0$, and $t = \pi/2$ gives $a = 0$.
4. The vectors $(1, 0, 1), (0, 1, 1), (1, 1, 0)$ are independent over $\R$ but dependent over $\mathbb{F}_2$; see [[this example|KFJ7M9FRXV]].
5. The empty family is independent, because it has no nontrivial combination.

### Non-examples

1. $(1, 2), (2, 4)$ are dependent: $2(1, 2) + (-1)(2, 4) = (0, 0)$ is a nontrivial relation.
2. The family $(v, v)$ with $v \ne 0$ is dependent, by the relation $1v + (-1)v = 0$, although the set $\set{v, v} = \set{v}$ is independent.
3. Each family that contains $0$ is dependent, by the relation $1 \cdot 0 = 0$.
4. Three vectors in $\R^2$ are always dependent, by the [[column test|76GG9B25A1]].

### Basic properties

1. A family of at least one vector is dependent if and only if one of its vectors is a combination of the others.
   See the [[dependence lemma|H75GS7QVPB]].
2. If $(v_1, \dots, v_k)$ is independent and $v \notin \operatorname{span}(v_1, \dots, v_k)$, then $(v_1, \dots, v_k, v)$ is independent.
3. A subfamily of an independent family is independent, and a superfamily of a dependent family is dependent.
4. In $F^m$, the columns of a matrix $A$ are independent exactly when every column of $A$ has a pivot.
   This holds exactly when $Ax = 0$ has only the solution $0$; see [[the column test|76GG9B25A1]].
5. For $n$ vectors in $F^n$, independence holds exactly when the matrix of the vectors has nonzero [[determinant|0C3CFHDN6R]]; see [[the determinant test|FBSAPTP1PR]].
6. By the [[Steinitz exchange lemma|08ZDRN6H41]], an independent family has at most as many vectors as each spanning set.

### History

Grassmann introduced linear dependence of his quantities in 1844.
The modern definition by the trivial relation appears in Peano's axiomatic work of 1888 and became standard in the twentieth century.

### Common errors

1. Families versus sets: the family $(v, v)$ is dependent, but the set $\set{v}$ is independent for $v \ne 0$. Mathlib works with families, so repeated vectors matter there.
2. Pairwise independence is not independence: $(1, 0), (0, 1), (1, 1)$ are pairwise independent in $\R^2$ but dependent as a family.
3. Independence depends on the field: see [[the example over $\mathbb{F}_2$|KFJ7M9FRXV]].
4. To show independence, start from $\sum a_i v_i = 0$ and prove all $a_i = 0$; finding one zero combination with zero coefficients proves nothing.

## Explanations

### L1 human

Vectors are linearly independent when none of them is redundant.
No vector can be built from the others, so each one adds a new direction.
Two arrows in the plane are independent exactly when they do not lie on one line.

### L2 human

To test independence of $v_1, \dots, v_n$ in $F^m$, place them as the columns of a matrix and row reduce.
They are independent exactly when every column gets a pivot.
Example: $(1, 2, 3), (4, 5, 6), (7, 8, 9)$ in $\R^3$.
Row reduction of the matrix with these columns gives the rows $(1, 4, 7)$, $(0, -3, -6)$ and $(0, 0, 0)$.
The third column has no pivot, so the vectors are dependent; indeed $(1, 2, 3) - 2(4, 5, 6) + (7, 8, 9) = 0$.

### L3 human

A family $v \colon I \to V$ is independent exactly when the linear map $F^{(I)} \to V$, $a \mapsto \sum_i a_i v_i$, is injective.
Independent sets form the independent sets of a [[matroid|PX31ZNYS3Z]] on $V$, and the exchange property of this matroid gives the [[dimension theorem|0WK0Y8RH1M]].
Over a ring, independence is weaker than "no vector is a combination of the others".
In $\Z$, the family $(2, 3)$ is dependent, by $3 \cdot 2 - 2 \cdot 3 = 0$, but neither entry is an integer multiple of the other.
