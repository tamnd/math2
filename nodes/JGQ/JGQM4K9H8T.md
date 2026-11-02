---
tag: JGQM4K9H8T
kind: definition
name: Free algebra
msc: [16S10, 16S15]
defines: 2P3Y2FRCSZ
uses: [0310REJJY8, CV013KHVJG, 3CTW1P4HBP, 0SDC934R52, P4J5JZDW0B, 1HM7ZYMPD7]
sources:
  - url: https://en.wikipedia.org/wiki/Free_algebra
---

## Definition

Let $k$ be a [[commutative ring|0310REJJY8]] with identity and let $X$ be a set.
Let $X^*$ be the [[free monoid|CV013KHVJG]] on $X$, with product given by concatenation.
Its elements are the finite words $x_1 x_2 \cdots x_n$ with $x_i \in X$, including the empty word $1$.
The *free algebra* $k\langle X \rangle$ is the free $k$-module with basis $X^*$, with the multiplication that extends concatenation of words $k$-bilinearly:
$$\Big(\sum_{u} a_u \, u\Big)\Big(\sum_{v} b_v \, v\Big) = \sum_{u, v} a_u b_v \, uv.$$
It is an [[associative algebra|3CTW1P4HBP]] over $k$ with identity the empty word.

## Remarks

Universal property: for every associative $k$-algebra $A$ with identity and every map $f \colon X \to A$, there is a unique homomorphism of $k$-algebras $\bar f \colon k\langle X \rangle \to A$ with $\bar f(x) = f(x)$ for $x \in X$.
It sends a word $x_1 \cdots x_n$ to $f(x_1) \cdots f(x_n)$.

Example: for $X = \set{x}$, the words are the powers $x^n$, and $k\langle x \rangle$ is the [[polynomial ring|0SDC934R52]] $k[x]$.

Non-example: for $X = \set{x, y}$, the polynomial ring $k[x, y]$ is not free on $X$.
The map $x \mapsto e_{12}$, $y \mapsto e_{21}$ into $2 \times 2$ matrices over $k$ has no extension to a homomorphism from $k[x, y]$, because $e_{12} e_{21} = e_{11} \ne e_{22} = e_{21} e_{12}$ while $xy = yx$ in $k[x, y]$.

The free algebra is the [[monoid ring|1HM7ZYMPD7]] $k[X^*]$.
It is isomorphic to the [[tensor algebra|P4J5JZDW0B]] $T(V)$ of the free $k$-module $V$ with basis $X$, graded by word length.
For $\abs{X} \ge 2$ and $k$ a field, it is a domain that is not commutative.
