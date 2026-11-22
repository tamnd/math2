---
tag: 0PTF1PTJK0
kind: definition
name: Endomorphism
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
defines: 0J7H0YBFDJ
uses: [0RJF668P1T]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Definition

An endomorphism is a linear map from a space to the same space, and an automorphism is one that can be undone.

Let $F$ be a field and let $V$ be a vector space over $F$.
An *endomorphism* of $V$ is a [[linear map|0RJF668P1T]] $T \colon V \to V$.
An *automorphism* of $V$ is a bijective endomorphism of $V$.

## Notation

The set of endomorphisms of $V$ is written $\End_F(V)$, $\End(V)$ or $L(V)$, and the set of automorphisms is written $GL(V)$ or $\Aut(V)$.
An endomorphism is also called a *linear operator* on $V$.
For $k \ge 0$, the power $T^k$ is $T$ composed with itself $k$ times, with $T^0 = \id_V$.

## Remarks

The condition is that the source and the target are the same space, not only spaces of the same dimension.
For example, $T(x, y) = (x + y, \; y)$ is an endomorphism of $\R^2$.
A failing case is the coefficient map $P_2 \to \R^3$, which is linear and bijective but goes between two different spaces.

Since the target is $V$, the composite $T \circ T$ is defined.
So powers $T^k$ and polynomials $a_0 \id_V + a_1 T + \dots + a_k T^k$ are again endomorphisms.
By the lemma on inverses, the inverse of an automorphism is linear, so it is again an automorphism.
The [[concept page|0J7H0YBFDJ]] has more examples and the main properties.

## Explanations

### L1 human

An endomorphism is a linear map from a space to the same space.
An automorphism is an endomorphism that can be undone.

### L2 human

The map $T(x, y) = (x + y, \; y)$ of $\R^2$ is an endomorphism, and $T^2(x, y) = T(x + y, y) = (x + 2y, \; y)$.
It is an automorphism, with inverse $(x, y) \mapsto (x - y, \; y)$.
Watch out: a map $\R^2 \to \R^3$ is not an endomorphism, since its target is a different space.
