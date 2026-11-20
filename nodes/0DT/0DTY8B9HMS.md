---
tag: 0DTY8B9HMS
kind: concept
name: Linear span
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
specializes: [00YC1D652K]
uses: [0V8F3E48E6, 00YC1D652K]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_span
    locator: Definition
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section2-3.xml#L253
    locator: src/section2-3.xml:253
  - book: isbn:9783031410253
    locator: Section 2A
  - book: isbn:9780134860244
    locator: Section 1.4
same_as:
  wikidata: Q209812
  wikipedia: Linear span
inventory: [TJ0X2DJ1E9]
---

## Summary

The linear span of a subset $S$ of a vector space $V$ is the set of all [[linear combinations|0V8F3E48E6]] of finitely many vectors of $S$.
See the [[definition|0HR573CHNM]].
It is the [[smallest subspace that contains $S$|~13840ba2]].
So the span describes a subspace from inside, by combinations, while the intersection of all subspaces that contain $S$ describes it from outside.

## Motivation

A subspace is often given by a few vectors, such as the columns of a matrix or the solutions of a differential equation.
The span is the subspace that these vectors generate.
The question "is $b$ in the span of the columns of $A$?" is the question "is $Ax = b$ consistent?".

## Notation

We write $\operatorname{span}(S)$, $\operatorname{span}(v_1, \dots, v_k)$, $\langle S \rangle$ or $F S$.
If $\operatorname{span}(S) = V$, we say that $S$ *spans* $V$, or that $S$ is a [[spanning set|088RYKAWK9]].
In Mathlib, the span is `Submodule.span F S`.

## Remarks

### Examples

1. In $\R^3$, $\operatorname{span}((1, 0, 1), (0, 1, 1)) = \set{(a, b, a + b) : a, b \in \R}$, the plane $z = x + y$. Check: $a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b)$, and $(x, y, z)$ with $z = x + y$ is the combination with $a = x$, $b = y$.
2. In $\R^3$, the span of the nonzero vector $(1, 2, 3)$ is the line $\set{(t, 2t, 3t)}$.
3. In $F[x]$, $\operatorname{span}(1, x, x^2) = P_2(F)$, the [[polynomials|0JGZCDT5DN]] of degree at most $2$.
4. $\operatorname{span}(\varnothing) = \set{0}$, because the only combination of no vectors is the empty sum $0$.
5. The span of the columns of a matrix $A$ is its [[column space|03AJKXH1AV]].

### Non-examples

1. The set $\set{a(1, 0) + b(0, 1) : a, b \ge 0}$ is the first quadrant, a cone; it is not the span, because it fails closure under the scalar $-1$.
2. The set $\set{(1, 0, 1), (0, 1, 1)}$ itself is not its span: it does not contain $0$, so it fails condition 1 of a subspace.

### Basic properties

1. $\operatorname{span}(S)$ is a subspace that contains $S$, and it lies in each subspace that contains $S$; see [[this statement|~13840ba2]].
2. If $S \subseteq T$, then $\operatorname{span}(S) \subseteq \operatorname{span}(T)$.
3. $\operatorname{span}(\operatorname{span}(S)) = \operatorname{span}(S)$, and $S$ is a subspace if and only if $\operatorname{span}(S) = S$.
4. $\operatorname{span}(S \cup T) = \operatorname{span}(S) + \operatorname{span}(T)$, the [[sum|0JMTY8MF54]] of the spans.
5. If $v \in \operatorname{span}(S)$, then $\operatorname{span}(S \cup \set{v}) = \operatorname{span}(S)$; this is the key step of the [[dependence lemma|~ddec9473]].

### History

Grassmann studied the spans of finitely many quantities in his *Ausdehnungslehre* of 1844.
Peano gave the axiomatic setting for such spans in 1888.

### Common errors

1. The span of $\varnothing$ is $\set{0}$, not $\varnothing$.
2. The span of a finite set is usually infinite: over $\R$, the span of one nonzero vector is a whole line.
3. Over a different field the span changes: $\operatorname{span}_\R(1) = \R$, but $\operatorname{span}_\Q(1) = \Q$ inside $\R$.

## Explanations

### L1 human

The span of some vectors is everything we can reach from them by scaling and adding.
Two arrows in space that do not point along the same line span a whole plane.
The span is always a subspace.

### L2 human

To test whether $b \in \operatorname{span}(v_1, \dots, v_k)$ in $F^m$, row reduce the augmented matrix $[v_1 \ \cdots \ v_k \mid b]$.
The vector $b$ lies in the span exactly when the last column has no pivot.
Example: $b = (1, 1, 3)$ and $v_1 = (1, 0, 1)$, $v_2 = (0, 1, 1)$.
The equations $a = 1$, $b' = 1$ and $a + b' = 3$ are inconsistent, because $1 + 1 \ne 3$.
So $(1, 1, 3)$ is not in the plane $z = x + y$, which matches the description in example 1.

### L3 human

The span operator $S \mapsto \operatorname{span}(S)$ is a closure operator on subsets of $V$.
It has the exchange property: if $w \in \operatorname{span}(S \cup \set{v})$ and $w \notin \operatorname{span}(S)$, then $v \in \operatorname{span}(S \cup \set{w})$.
This property makes the independent sets of $V$ into a [[matroid|PX31ZNYS3Z]], and the theory of bases and dimension follows from it.
