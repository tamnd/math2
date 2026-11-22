---
tag: 088RYKAWK9
kind: concept
name: Spanning set
aliases: [generating-set]
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
uses: [0DTY8B9HMS, 0HR573CHNM]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: lead section
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.4
---

## Summary

A spanning set is a set of building blocks that is enough to make every vector of the space.
It is one half of the idea of a basis, and its size gives the first upper bound on how large a space can be.
A subset $S$ of a vector space $V$ is a *spanning set* of $V$ when its [[span|0DTY8B9HMS]] is all of $V$:
$$\operatorname{span}(S) = V.$$
Equivalently, every vector of $V$ is a linear combination of finitely many vectors of $S$, as the [[formal definition|0BJKVF90Z6]] states.
The other half of a basis is [[linear independence|0CRMGPAH83]].

## Motivation

Many spaces come to you as "everything you can build from these": the column space of a matrix is built from the columns, and the solutions of a homogeneous system are built from a few special solutions.
A spanning set is a finite description of a possibly infinite space.
Once you know that $S$ spans $V$, you can check a linear property on the vectors of $S$ alone, and it then holds for all of $V$.

How few vectors can do the job?
In $F^m$ the answer is $m$, and the reason is a count of pivots, made exact by the [[pivot test|D3PN42EP4X]].
The same question in a general space leads through the [[Steinitz exchange lemma|08ZDRN6H41]] to the [[dimension|03GSZ8RTZJ]].

## Notation

We say that $S$ *spans* $V$, or *generates* $V$, and write $\operatorname{span}(S) = V$.
A list $v_1, \dots, v_n$ spans $V$ when the set $\{v_1, \dots, v_n\}$ does, so repeating a vector in a list changes nothing here.
In Mathlib the statement is `Submodule.span F S = ⊤`, where `⊤` is the whole space as a submodule.

## Remarks

### Three spanning sets of the plane

The standard vectors $(1, 0)$ and $(0, 1)$ span $\mathbb{R}^2$, because $(a, b) = a(1, 0) + b(0, 1)$.
Adding $(1, 1)$ keeps a spanning set, since a larger set has a larger span.
Now a vector has several expressions, for example
$$(3, 2) = 3(1, 0) + 2(0, 1) + 0(1, 1) = 1(1, 0) + 0(0, 1) + 2(1, 1).$$
The pair $(1, 1)$ and $(1, -1)$ also spans, because $(a, b) = \tfrac{a + b}{2}(1, 1) + \tfrac{a - b}{2}(1, -1)$.
Check with $(3, 2)$: $\tfrac52 (1, 1) + \tfrac12 (1, -1) = (3, 2)$.

### More examples

The monomials $1, x, \dots, x^n$ span the polynomials of degree at most $n$, and all monomials together span $F[x]$.
Every space spans itself, and the empty set spans the zero space $\{0\}$, since the span of $\varnothing$ is $\{0\}$.

### Testing with pivots

In $F^m$ there is a mechanical test.
Put the vectors as the columns of a matrix $A$ and row reduce: the vectors span $F^m$ exactly when every row of the echelon form has a [[pivot|0BCMGDHZGR]], by the [[pivot test|D3PN42EP4X]].
For $(1, 0, 1)$, $(0, 1, 1)$ and $(1, 1, 0)$, subtract row 1 from row 3 and then row 2 from row 3:
$$\begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 1 & 1 & 0 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & -1 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & -2 \end{pmatrix}.$$
Each of the three rows has a pivot, so the three vectors span $\mathbb{R}^3$.
Since a matrix has at most one pivot in each column, a spanning set of $F^m$ needs at least $m$ vectors.

### What does not span

The vectors $(1, 2)$ and $(2, 4)$ do not span $\mathbb{R}^2$.
Every combination is $a(1, 2) + b(2, 4) = (a + 2b)(1, 2)$, so it lies on the line $y = 2x$, and $(1, 0)$ is never reached.
Two vectors never span $\mathbb{R}^3$, because their matrix has two columns and so at most two pivots for three rows.
The monomials do not span the space $F[[x]]$ of formal power series, because $1 + x + x^2 + \dots$ is not a finite combination of them.

### Making a spanning set smaller

A spanning set may contain waste.
If $v \in S$ is a combination of the other vectors of $S$, then $S$ without $v$ still spans, because each use of $v$ can be replaced by its expression.
Removing waste in this way leads to a basis, and [[every spanning set contains a basis|06MRNP4BNT]].
In the other direction, a superset of a spanning set always spans.
By the [[Steinitz exchange lemma|08ZDRN6H41]], no independent set is larger than a spanning set, and a space with a finite spanning set is [[finite-dimensional|0ZHWKQMVX5]].

### Watch out

A spanning set need not be independent, so the coefficients of a vector in it need not be unique, as the example with $(1, 1)$ above shows.
Also say which space is spanned.
The vectors $(1, 0, 0)$ and $(0, 1, 0)$ span the plane $z = 0$, but they do not span $\mathbb{R}^3$.

### Try it

First, do $(1, 2)$ and $(3, 4)$ span $\mathbb{R}^2$?
Row reduce the matrix with rows $(1, 3)$ and $(2, 4)$: subtracting twice row 1 gives the row $(0, -2)$, so both rows have pivots and the answer is yes.

Second, can four vectors span $\mathbb{R}^5$?
No, because a $5 \times 4$ matrix has at most four pivots, so one of the five rows has none.

## Explanations

### L1 human

A spanning set is a kit of building blocks from which you can make every vector of the space.
In the plane, the two arrows "one step east" and "one step north" are enough: to reach $(3, 2)$, go three steps east and two steps north.
A kit may hold more blocks than you need, such as an extra arrow pointing northeast.
Then a vector can be built in more than one way.
Removing the extra blocks, one at a time, leaves a smallest kit, which is a basis.

### L2 human

Here is a typical question: do $v_1 = (1, 2, 0)$, $v_2 = (0, 1, 1)$ and $v_3 = (1, 3, 1)$ span $\mathbb{R}^3$?
Put them as columns and row reduce:
$$\begin{pmatrix} 1 & 0 & 1 \\ 2 & 1 & 3 \\ 0 & 1 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 1 & 1 \end{pmatrix} \to \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \\ 0 & 0 & 0 \end{pmatrix}.$$
The third row has no pivot, so the vectors do not span $\mathbb{R}^3$.
The reason is visible: $v_3 = v_1 + v_2$, so the three vectors span only the plane spanned by $v_1$ and $v_2$.
The typical use of the test is exactly this: it either confirms that a set spans, or it points to a redundant vector and a missing direction.

### L3 human

In a module over a ring, a spanning set is a generating set, and a module with a finite one is finitely generated.
Over a field, a minimal spanning set is always a basis, but over $\mathbb{Z}$ the set $\{2, 3\}$ generates $\mathbb{Z}$ and is minimal, while no subset of it is a basis, since $\{2\}$ and $\{3\}$ do not generate $\mathbb{Z}$.
A surjective linear map sends a spanning set to a spanning set, and the sub-area on [[linear maps|9080WQTZ3M]] uses this to compute images.
