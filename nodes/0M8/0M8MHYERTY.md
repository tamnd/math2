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

A nilpotent endomorphism is a linear map from a space to itself that some power sends to zero.
Let $F$ be a field, let $V$ be a vector space over $F$, and let $T \colon V \to V$ be an [[endomorphism|0J7H0YBFDJ]].
The map $T$ is *nilpotent* when $T^k = 0$ for some integer $k \ge 1$.
The least such $k$ is the *index* of $T$.
Here $T^k$ is the composite of $k$ copies of $T$.

## Notation

A matrix $A$ is nilpotent when the map $x \mapsto A x$ is nilpotent, see [[nilpotent matrix|07BSPZPSMF]].
In Mathlib, `IsNilpotent T` states that $T^k = 0$ for some natural number $k$, where $k = 0$ is allowed.
For endomorphisms this is the same notion, because $T^0 = \id_V$ is $0$ only when $V = 0$, and then $T = 0$ as well.

## Remarks

The definition asks for one power $k$ that works for every vector at the same time.
This is the point of the condition, since a map can send each vector to zero after finitely many steps and still have no zero power.
The derivative on all real polynomials is such a map, because $D^k x^k = k! \ne 0$ for every $k$.
In finite dimension the two ideas agree, and $T^n = 0$ when $\dim V = n$, by the [[characterizations of nilpotent maps|FSKECQK1GW]].

For a small example, the derivative on real polynomials of degree less than $n$ is nilpotent of index $n$, because $D^{n-1} x^{n-1} = (n-1)! \ne 0$ and $D^n = 0$.
For a case that fails, the identity $\id_V$ on $V \ne 0$ has $\id_V^k = \id_V \ne 0$ for every $k$, so it is not nilpotent.
In finite dimension, $T$ is nilpotent exactly when $p_T = t^n$, and over an algebraically closed field this means that $0$ is its only eigenvalue.
The concept page [[nilpotent endomorphism|063D5Z2C70]] has more examples.

## Explanations

### L1 human

A nilpotent map destroys everything after a few steps.
The shift $e_1 \mapsto 0$, $e_2 \mapsto e_1$, $e_3 \mapsto e_2$ in $F^3$ is an example.
It needs three steps to send $e_3$ to zero, so its index is $3$.

### L2 human

Let $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$.

1. The matrix $N$ is not zero, so the index is not $1$.
2. Multiply row by column:
$$N^2 = \begin{pmatrix} 0 \cdot 0 + 1 \cdot 0 & 0 \cdot 1 + 1 \cdot 0 \\ 0 & 0 \end{pmatrix} = 0.$$
3. So $N$ is nilpotent of index $2$.

The typical use is to check $T^n = 0$ in dimension $n$, which settles nilpotence in one computation.
Watch out: $T^2 \ne 0$ does not show that $T$ is not nilpotent, since a higher power may still be $0$.

### L3 human

The same definition makes sense for an element of any ring: $x$ is nilpotent when $x^k = 0$ for some $k \ge 1$.
A map that sends each vector to zero after finitely many steps, like the derivative on all polynomials, is called locally nilpotent.
