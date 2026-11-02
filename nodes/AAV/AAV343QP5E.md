---
tag: AAV343QP5E
kind: definition
name: Presentation of an algebra
msc: [08B20, 08A50]
defines: 43M1WFPYGQ
uses: [GTS4DRRMZR, AJNZJD8442, QP06QH2Q7C, N5KE7FH6CX, PZMGQMDN25]
sources:
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]], let $X$ be a set, and let $F = F_{\mathcal{V}}(X)$ be the [[free algebra|GTS4DRRMZR]] of $\mathcal{V}$ on $X$.
Let $R$ be a set of pairs $(s, t)$ of elements of $F$, called *relations* and written $s = t$.
Let $\theta_R$ be the [[congruence generated|QP06QH2Q7C]] by $R$ on $F$.
The algebra *presented* by $X$ and $R$ in $\mathcal{V}$ is the [[quotient algebra|N5KE7FH6CX]]
$$\langle X \mid R \rangle_{\mathcal{V}} = F / \theta_R.$$
A *presentation* of an algebra $A \in \mathcal{V}$ is a pair $(X, R)$ with an [[isomorphism|PZMGQMDN25]] $\langle X \mid R \rangle_{\mathcal{V}} \to A$.
The algebra $A$ is *finitely presented* in $\mathcal{V}$ if it has a presentation with $X$ and $R$ finite.

## Remarks

The presented algebra has this universal property.
Let $B \in \mathcal{V}$ and let $f \colon X \to B$ be a map under which each relation $s = t$ holds in $B$.
Then there is exactly one homomorphism $\langle X \mid R \rangle_{\mathcal{V}} \to B$ that extends $f$.
Every $A \in \mathcal{V}$ has a presentation: take $X = A$ and $R$ the kernel of the homomorphism $F_{\mathcal{V}}(A) \to A$ that extends the identity map.
Example: in the variety of commutative monoids, $\langle a \mid a^2 = a^3 \rangle$ is the monoid $\set{1, a, a^2}$ with $a^3 = a^2$.
The relation holds there, and the universal property is checked by sending $a$ to any element $b$ with $b^2 = b^3$.
Non-example: the same pair $(\set{a}, \set{a^2 = a^3})$ does not present $\Z / 2\Z$ as a commutative monoid, since in $\Z / 2\Z = \set{1, a}$ one has $a^2 = 1$ and $a^3 = a$, so the relation $a^2 = a^3$ fails.
The presented algebra depends on the variety: $\langle a, b \mid \ \rangle$ is $\N^2$ in commutative monoids and the free monoid on two letters in monoids.
