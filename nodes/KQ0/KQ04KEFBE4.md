---
tag: KQ04KEFBE4
kind: definition
name: Free functor
msc: ["08C05", "18A40", "08B20"]
defines: N353JF8RBK
uses: [WV3BPYCHVG, TZHF6ZM92S, GTS4DRRMZR, AJNZJD8442]
sources:
  - url: https://en.wikipedia.org/wiki/Free_object
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras, regarded as a category with homomorphisms, and let $U \colon \mathcal{V} \to \mathbf{Set}$ be its [[forgetful functor|WV3BPYCHVG]].
A *free functor* for $\mathcal{V}$ is a functor $F \colon \mathbf{Set} \to \mathcal{V}$ that is [[left adjoint|TZHF6ZM92S]] to $U$.
Explicitly, $F$ comes with maps $\eta_X \colon X \to U F(X)$, natural in $X$, with the following property.
For every algebra $A \in \mathcal{V}$ and every map $g \colon X \to U(A)$, there is a unique homomorphism $\bar g \colon F(X) \to A$ with $U(\bar g) \circ \eta_X = g$.

## Remarks

Such a functor exists for every variety: $F(X)$ is the [[free algebra|GTS4DRRMZR]] of $\mathcal{V}$ on $X$, and $F$ sends a map $h \colon X \to Y$ to the unique homomorphism $F(X) \to F(Y)$ that extends $\eta_Y \circ h$.
It is unique up to a unique natural isomorphism, as is any left adjoint.
More generally, a left adjoint of any forgetful functor $U \colon \mathcal{C} \to \mathcal{D}$ is called a free functor.

Example: for the variety of monoids, $F(X)$ is the monoid $X^*$ of finite words in $X$ under concatenation, and $\eta_X$ sends $x$ to the one-letter word $x$.
A map $g \colon X \to M$ into a monoid extends to $\bar g(x_1 \cdots x_n) = g(x_1) \cdots g(x_n)$, and this is the only homomorphism extending $g$.

Non-example: the functor from sets to groups that sends every set to the trivial group is not a free functor.
For $X = \set{x}$ and the map $x \mapsto 1$ into $\Z$, the only homomorphism from the trivial group to $\Z$ sends everything to $0$, so it does not extend $g$.
