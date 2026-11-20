---
tag: 0M8MHYERTY
kind: definition
name: Nilpotent endomorphism
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: ug2
defines: 063D5Z2C70
uses: [0PTF1PTJK0]
formal:
  - system: lean4
    library: mathlib
    decl: IsNilpotent
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: lead section
  - book: isbn:9783031410253
    locator: Chapter 8
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The map $T$ is *nilpotent* when $T^k = 0$ for some integer $k \ge 1$.
The least such $k$ is the *index* of $T$.
Here $T^k$ is the composite of $k$ copies of $T$.

## Notation

A matrix $A$ is nilpotent when the map $x \mapsto A x$ is nilpotent, see [[nilpotent matrix|07BSPZPSMF]].
In Mathlib, `IsNilpotent T` states that $T^k = 0$ for some natural number $k$.
For $T$ in the ring of endomorphisms this is the same notion, since $T^0 = \id_V$ is $0$ only when $V = 0$.

## Remarks

If $\dim V = n$ is finite and $T$ is nilpotent, then $T^n = 0$, by the [[characterizations of nilpotent maps|~662223db]].
In finite dimension, $T$ is nilpotent exactly when its characteristic polynomial is $t^n$.
Over an algebraically closed field, this means that $0$ is its only eigenvalue.
The derivative on the space of polynomials of degree less than $n$ is nilpotent of index $n$.

## Explanations

### L1 human

A nilpotent map destroys everything after a few steps.
Each application pushes vectors further towards zero, until they vanish.
The shift $e_1 \mapsto 0$, $e_2 \mapsto e_1$, $e_3 \mapsto e_2$ in $F^3$ is nilpotent of index $3$.

### L2 human

Let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

1. $N \ne 0$, so the index is not $1$.
2. $N^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0$.
3. So $N$ is nilpotent of index $2$.

The typical use is to check $T^n = 0$ in dimension $n$, which settles nilpotence in one computation.
The trap is to stop at $T^2 \ne 0$ and conclude that $T$ is not nilpotent; a higher power may still be $0$.

### L3 human

The same definition makes sense for an element of any ring: $x$ is nilpotent when $x^k = 0$ for some $k \ge 1$.
In an infinite-dimensional space, a map can kill each vector after finitely many steps without being nilpotent, as the derivative on all polynomials shows.
Such maps are called locally nilpotent.
