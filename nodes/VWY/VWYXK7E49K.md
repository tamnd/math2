---
tag: VWYXK7E49K
kind: definition
name: Comma category
msc: [18A25]
defines: PC6HG1JEGM
uses: [28NQ0KRHD3, 859F0TFVA3, WV898P4X16]
sources:
  - url: https://en.wikipedia.org/wiki/Comma_category
---

## Definition

Let $S \colon \mathcal{A} \to \mathcal{C}$ and $T \colon \mathcal{B} \to \mathcal{C}$ be [[functors|28NQ0KRHD3]].
The *comma category* $(S \downarrow T)$ is defined as follows:

1. its objects are the triples $(A, B, h)$ with $A$ an object of $\mathcal{A}$, $B$ an object of $\mathcal{B}$ and $h \colon S(A) \to T(B)$ a [[morphism|859F0TFVA3]] of $\mathcal{C}$;
2. a morphism $(A, B, h) \to (A', B', h')$ is a pair $(f, g)$ with $f \colon A \to A'$ in $\mathcal{A}$ and $g \colon B \to B'$ in $\mathcal{B}$ such that $T(g) \circ h = h' \circ S(f)$;
3. composition is $(f', g') \circ (f, g) = (f' \circ f, g' \circ g)$, and the identity of $(A, B, h)$ is $(1_A, 1_B)$.

## Remarks

The condition in clause 2 says that the square with sides $S(f)$, $h'$, $h$ and $T(g)$ is a [[commutative diagram|WV898P4X16]]; pasting two such squares shows that composites are again morphisms.
Example: with $S = T = 1_{\mathcal{C}}$, the comma category is the arrow category of $\mathcal{C}$, whose objects are the morphisms $h \colon X \to Y$.
In the arrow category of sets, the pair $(f, g)$ with $f = g = (x \mapsto -x)$ is a morphism from $h = (x \mapsto x^3)$ on $\R$ to itself, since $(-x)^3 = -x^3$.
Non-example: for $h = (x \mapsto x^2)$ on $\R$, the same pair $(f, g)$ is not a morphism from $h$ to $h$, since $-x^2 \ne (-x)^2$ when $x \ne 0$.
When $\mathcal{A}$ is the category with one object and one morphism, $S$ picks an object $X$ of $\mathcal{C}$ and one writes $(X \downarrow T)$.
There are projection functors from $(S \downarrow T)$ to $\mathcal{A}$ and to $\mathcal{B}$.
