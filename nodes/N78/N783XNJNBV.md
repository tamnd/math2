---
tag: N783XNJNBV
kind: statement
role: theorem
name: Homomorphism theorem
msc: [08A30, 08A05]
uses: [QJGPT2W0FT, KBXSZC6BV1, DCSXXT4SER, N5KE7FH6CX]
about: [N5KE7FH6CX, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms
same_as:
  wikidata: Q1187646
  wikipedia: Fundamental theorem on homomorphisms
---

## Statement

Let $\mathbf{A}$ and $\mathbf{B}$ be [[algebras|QJGPT2W0FT]] of the same signature and let $\alpha \colon \mathbf{A} \to \mathbf{B}$ be a [[homomorphism|KBXSZC6BV1]].
Let $\ker \alpha = \set{(a, b) \in A \times A : \alpha(a) = \alpha(b)}$.
Let $\theta$ be a [[congruence|DCSXXT4SER]] on $\mathbf{A}$ with $\theta \subseteq \ker \alpha$, and let $\nu \colon \mathbf{A} \to \mathbf{A}/\theta$ be the natural map onto the [[quotient algebra|N5KE7FH6CX]].

1. The relation $\ker \alpha$ is a congruence on $\mathbf{A}$.
2. There is a unique homomorphism $\beta \colon \mathbf{A}/\theta \to \mathbf{B}$ with $\beta \circ \nu = \alpha$.
3. The map $\beta$ is injective if and only if $\theta = \ker \alpha$.
4. In particular, $a/\ker \alpha \mapsto \alpha(a)$ is an isomorphism from $\mathbf{A}/\ker \alpha$ onto the subalgebra $\alpha(\mathbf{A})$ of $\mathbf{B}$.

## Remarks

Proof idea.
Compatibility of $\ker \alpha$ follows from $\alpha(f(a_1, \dots, a_n)) = f(\alpha(a_1), \dots, \alpha(a_n))$.
Put $\beta(a/\theta) = \alpha(a)$; this is well defined because $\theta \subseteq \ker \alpha$, and it is a homomorphism because $\alpha$ and $\nu$ are.
Uniqueness holds since $\nu$ is surjective, and $\beta(a/\theta) = \beta(b/\theta)$ means $(a, b) \in \ker \alpha$.

Example: the ring homomorphism $\Z \to \Z/n\Z$ has kernel congruence modulo $n$, so the quotient of $\Z$ by this congruence is isomorphic to $\Z/n\Z$.
For groups, part 4 is the [[first isomorphism theorem|0CXXJNG5B6]].

## Explanations

### L1 human

A homomorphism may send several elements to the same place.
If you glue together exactly the elements with the same image, what is left is a copy of the image.
So every homomorphic image of an algebra is, up to isomorphism, a quotient of it.

### L2 human

Part 2 is the universal property of the quotient: maps out of $\mathbf{A}/\theta$ are the maps out of $\mathbf{A}$ that do not separate $\theta$-related elements.
Part 1, together with $\ker \nu = \theta$, shows that congruences are exactly the kernels of homomorphisms.
With the [[correspondence theorem|JG7WB75BHC]] it yields the other isomorphism theorems.
It is basic in the proof of [[Birkhoff's HSP theorem|5083DHSK82]], since it identifies the class operator $H$ with taking quotients.
