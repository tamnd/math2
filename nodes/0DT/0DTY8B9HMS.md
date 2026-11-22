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

The span of some vectors is everything you can reach from them by scaling and adding.
It turns a handful of vectors into a whole subspace, and it is the way most subspaces in practice are described.
For a subset $S$ of a vector space $V$ over a field $F$, the *linear span* of $S$ is the set of all [[linear combinations|0V8F3E48E6]] of finitely many vectors of $S$:
$$\operatorname{span}(S) = \{a_1 v_1 + \dots + a_k v_k : k \ge 0, \ a_i \in F, \ v_i \in S\}.$$
The [[formal definition|0HR573CHNM]] states this, and a [[theorem|2BX666XF68]] gives the equivalent form: $\operatorname{span}(S)$ is the smallest subspace of $V$ that contains $S$.

## Motivation

A subspace is often handed to you by a few vectors that lie in it: the columns of a matrix, two directions in a plane, or two solutions of a differential equation.
The span is the subspace that these vectors generate.
For example, every solution of $y'' + y = 0$ has the form $a \cos t + b \sin t$, so the solution space is the span of $\cos$ and $\sin$.

The span also turns a question about equations into a question about vectors.
Asking whether $b$ lies in the span of the columns of $A$ is the same as asking whether $Ax = b$ has a solution.
Building on span, a [[spanning set|088RYKAWK9]] is a set whose span is everything, and a [[basis|0KCQ9Y3QKA]] is a spanning set with no waste.

## Notation

Books write $\operatorname{span}(S)$, $\operatorname{span}(v_1, \dots, v_k)$, $\operatorname{Span}\{v_1, \dots, v_k\}$ or $\langle S \rangle$.
When the field matters, write $\operatorname{span}_F(S)$.
If $\operatorname{span}(S) = V$, we say that $S$ *spans* $V$, or that $S$ *generates* $V$.
In Mathlib the span is `Submodule.span F S`, and it is defined as the smallest submodule that contains `S`.

## Remarks

### A plane from two vectors

Take $v_1 = (1, 0, 1)$ and $v_2 = (0, 1, 1)$ in $\mathbb{R}^3$.
A general combination is
$$a(1, 0, 1) + b(0, 1, 1) = (a, b, a + b).$$
So every vector of the span satisfies $z = x + y$.
Conversely, a vector $(x, y, z)$ with $z = x + y$ is the combination with $a = x$ and $b = y$.
So the span is exactly the plane $z = x + y$ through the origin.

### More spans

The span of one nonzero vector $(1, 2, 3)$ is the line of all $(t, 2t, 3t)$.
In $F[x]$, the span of $1$, $x$ and $x^2$ is the [[space of polynomials|0JGZCDT5DN]] of degree at most $2$.
The span of the columns of a matrix $A$ is its [[column space|03AJKXH1AV]].
The span of the empty set is $\{0\}$, because the only combination of no vectors is the empty sum, whose value is $0$.

### Two ways to see the span

The definition builds the span from inside, as a set of combinations.
There is also a view from outside: the span is the intersection of all subspaces that contain $S$.
The two views agree because the combinations already form a subspace, and every subspace that contains $S$ must contain all of them, as [[the smallest subspace theorem|2BX666XF68]] proves.
From this you get the first rules.
If $S \subseteq T$, then $\operatorname{span}(S) \subseteq \operatorname{span}(T)$.
Taking the span twice changes nothing, and $S$ is a subspace exactly when $\operatorname{span}(S) = S$.
The span of a union is the [[sum|0JMTY8MF54]] of the spans, $\operatorname{span}(S \cup T) = \operatorname{span}(S) + \operatorname{span}(T)$.

### Adding a redundant vector

If $v$ already lies in $\operatorname{span}(S)$, then adding $v$ to $S$ does not make the span larger.
Each combination that uses $v$ can be rewritten without $v$, by substituting its expression in terms of $S$.
For example, $(1, 1, 2) = v_1 + v_2$ lies in the plane above, so $v_1$, $v_2$ and $(1, 1, 2)$ still span only that plane.
This is the step behind the [[linear dependence lemma|H75GS7QVPB]].

### What is not a span

The set of all $a(1, 0) + b(0, 1)$ with $a, b \ge 0$ is the closed first quadrant.
It is not a span, because $(1, 0)$ lies in it and $-1 \cdot (1, 0)$ does not.
A finite set such as $\{(1, 0, 1), (0, 1, 1)\}$ is not its own span either, because it does not contain $0$.

### Watch out

The span of $\varnothing$ is $\{0\}$, not $\varnothing$.
The span of a finite set is usually an infinite set: over $\mathbb{R}$, one nonzero vector spans a whole line.
The span also depends on the field: inside $\mathbb{R}$, $\operatorname{span}_\mathbb{R}(1) = \mathbb{R}$, but $\operatorname{span}_\mathbb{Q}(1) = \mathbb{Q}$.

### Try it

First, describe the span of $(1, 2)$ and $(2, 4)$ in $\mathbb{R}^2$.
Since $(2, 4) = 2(1, 2)$, the second vector adds nothing, and the span is the line $y = 2x$.

Second, is $(2, 3, 5)$ in the span of $(1, 0, 1)$ and $(0, 1, 1)$?
Yes, since $5 = 2 + 3$: it equals $2(1, 0, 1) + 3(0, 1, 1)$.

## Explanations

### L1 human

Think of each vector as a direction you are allowed to walk in, forward or backward, as far as you like.
The span is the set of all places you can reach.
With one direction in space you reach a line.
With two directions that do not lie on one line you reach a whole flat plane through the starting point.
A third direction that lies in that plane takes you nowhere new.

### L2 human

Here is the standard test in $F^m$: is $b = (1, 1, 3)$ in the span of $v_1 = (1, 0, 1)$ and $v_2 = (0, 1, 1)$?
We look for $x_1$ and $x_2$ with $x_1 v_1 + x_2 v_2 = b$, which means
$$x_1 = 1, \qquad x_2 = 1, \qquad x_1 + x_2 = 3.$$
The first two equations fix $x_1 = x_2 = 1$, and then the third says $2 = 3$.
The system is inconsistent, so $b$ is not in the span.
This matches the picture: $(1, 1, 3)$ breaks the equation $z = x + y$ of the plane.
In general, row reduce the augmented matrix $[v_1 \ \cdots \ v_k \mid b]$; the vector $b$ lies in the span exactly when the last column has no [[pivot|0BCMGDHZGR]].

### L3 human

The map $S \mapsto \operatorname{span}(S)$ is a closure operator on the subsets of $V$: it is extensive, monotone and idempotent.
It also has the exchange property: if $w \in \operatorname{span}(S \cup \{v\})$ and $w \notin \operatorname{span}(S)$, then $v \in \operatorname{span}(S \cup \{w\})$.
A closure operator with this property defines a [[matroid|PX31ZNYS3Z]], and the theory of bases and dimension holds in that generality.
The same construction gives the submodule generated by a subset of a module, the subgroup generated by a subset of a group and the ideal generated by a subset of a ring, but over rings the exchange property fails.
