---
tag: 0CXXJNG5B6
kind: statement
role: theorem
name: First isomorphism theorem
aliases: [fundamental-theorem-on-homomorphisms]
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
about: [0KYX2N69J0, 08MG7H8JW5, 0S21GNW9ZB, 0W88CEGQP1]
uses: [0JYTG5K9Y4, 0W88CEGQP1, 0S21GNW9ZB, 0C9ZKYSPYR, 0KYX2N69J0, 08MG7H8JW5, 0GJ83E78A5]
formal:
  - system: lean4
    library: mathlib
    decl: QuotientGroup.quotientKerEquivRange
    match: variant
    adapter: Math2.Match.first_iso
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Theorem A (groups)
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_on_homomorphisms
    locator: Group-theoretic version
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
    locator: Note on numbers and names
---

## Statement

Let $G$ and $H$ be [[groups|G5S1M9]], and let $\varphi \colon G \to H$ be a [[group homomorphism|0JYTG5K9Y4]].
Then the [[kernel|0W88CEGQP1]] $\ker \varphi$ is a normal subgroup of $G$, and the [[image|0S21GNW9ZB]] $\operatorname{im} \varphi$ is a subgroup of $H$.
The formula $\bar{\varphi}(g \ker \varphi) = \varphi(g)$ gives a well defined [[isomorphism|08MG7H8JW5]]
$$\bar{\varphi} \colon G/\ker \varphi \to \operatorname{im} \varphi$$
from the [[quotient group|0KYX2N69J0]] $G/\ker \varphi$ to the image of $\varphi$.
In particular, if $\varphi$ is surjective, then $G/\ker \varphi \cong H$.

The proof is in [[the proof of the first isomorphism theorem|H4QSPK0XTZ]].

## Remarks

The kernel is normal by [[this statement|0C9ZKYSPYR]].
The theorem is the special case $N = \ker \varphi$ of the [[universal property of the quotient group|0GJ83E78A5]], with the target replaced by the image.
Thus $\varphi$ is the composite of three maps: the projection $G \to G/\ker \varphi$, the isomorphism $\bar{\varphi}$, and the inclusion $\operatorname{im} \varphi \to H$.

### Why each hypothesis is needed

- The map must be a homomorphism. The map $u \mapsto u^2$ from $\mathbb{Z}$ to $\mathbb{Z}$ has the image $\{0, 1, 4, 9, \dots\}$. This set is not closed under addition, because $1 + 4 = 5$ is not a square, so the image is not a group.
- The target of $\bar{\varphi}$ must be the image, not $H$. The inclusion $A_3 \to S_3$ of the [[alternating group|0Z5905Q73D]] in the [[symmetric group|0515A6D2Y1]] has a trivial kernel. So $A_3/\{e\} \cong A_3$ has order $3$, but $S_3$ has order $6$.

### Consequences

- If $G$ is finite, then $|G| = |\ker \varphi| \cdot |\operatorname{im} \varphi|$. This follows from $|G| = [G : \ker \varphi] \cdot |\ker \varphi|$ ([[this statement|04DC0SRN2K]]), because $[G : \ker \varphi] = |G/\ker \varphi|$.
- Thus $|\operatorname{im} \varphi|$ divides $|G|$. By [[Lagrange's theorem|3C53TD]], it also divides $|H|$ when $H$ is finite. For example, each homomorphism $\mathbb{Z}/3\mathbb{Z} \to \mathbb{Z}/4\mathbb{Z}$ is trivial, because $1$ is the only common divisor of $3$ and $4$.
- Reduction modulo $n$ is a surjective homomorphism from $\mathbb{Z}$ to the [[integers modulo n|03VFZ2WETT]], with kernel $n\mathbb{Z}$. So $\mathbb{Z}/n\mathbb{Z}$ is isomorphic to the integers modulo $n$ ([[this example|0YJ3WRR9RY]]).
- The real numbers modulo the integers are isomorphic to the circle group, through $x \mapsto e^{2\pi i x}$ ([[this example|FV86TFARY4]]).
- The determinant gives $\mathrm{GL}_n(F)/\mathrm{SL}_n(F) \cong F^\times$ for a field $F$ ([[this example|0YZ3T5Q7XN]]).
- For $n \ge 2$, the [[sign of a permutation|0JEJJCB0EX]] gives $S_n/A_n \cong \{1, -1\}$.
- The map that sends $g$ to the [[inner automorphism|0RN00NTM3S]] $x \mapsto gxg^{-1}$ has the [[centre|0DZ93493VN]] $Z(G)$ as its kernel. So $G/Z(G) \cong \operatorname{Inn}(G)$.

### Converse

Each normal subgroup $N$ of $G$ is the kernel of a homomorphism, namely the projection $G \to G/N$.
Thus the normal subgroups of $G$ are exactly the kernels of homomorphisms from $G$.
Together with the theorem, this shows that the quotient groups of $G$ are, up to isomorphism, exactly the images of homomorphisms from $G$.

### Generalizations

- The same theorem holds for ring homomorphisms, with ideals in the place of normal subgroups ([[first isomorphism theorem for rings|0ZMYX7GMH0]]).
- It holds for linear maps, with subspaces in the place of normal subgroups ([[first isomorphism theorem for linear maps|0MTBGVZ4XJ]]), and for module homomorphisms.
- In universal algebra, it holds for any algebraic structure, with congruence relations in the place of kernels.

### Names

Books do not agree on the names and the numbers of the isomorphism theorems.
Some books call this result the fundamental theorem on homomorphisms or the homomorphism theorem.
Some of these books then give the numbers "first" and "second" to the results that are called the second and third isomorphism theorems here.
In this collection, the [[second isomorphism theorem|0PPP2J2DJV]] is about $H/(H \cap N)$, and the [[third isomorphism theorem|0TJ1V9DDPC]] is about $(G/N)/(M/N)$.

## History

Emmy Noether stated the isomorphism theorems in general form, for modules, in a paper of 1927 in Mathematische Annalen.

## Explanations

### L1 human

A homomorphism can send many elements to the same element.
The elements that go to the identity form the kernel.
Two elements go to the same element exactly when they are in the same coset of the kernel.
So the homomorphism glues each coset of the kernel to one point, and it loses no other information.
The glued group is the quotient by the kernel, and it is a copy of the image.
For example, the map that sends an integer to its remainder modulo $n$ glues together the integers with the same remainder, and the result is a copy of the integers modulo $n$.

### L2 human

A worked example uses $\varphi \colon \mathbb{Z} \to \mathbb{C}^\times$, $\varphi(k) = i^k$, where $\mathbb{C}^\times$ is the group of nonzero complex numbers under multiplication.

1. The map is a homomorphism, because $i^{k + l} = i^k i^l$ by the [[laws of exponents|00DRK90Z6K]].
2. The powers of $i$ repeat with period $4$: $i^0 = 1$, $i^1 = i$, $i^2 = -1$, $i^3 = -i$, $i^4 = 1$. So the image is $\{1, i, -1, -i\}$.
3. We get $i^k = 1$ exactly when $4$ divides $k$. So the kernel is $4\mathbb{Z}$.
4. By the theorem, $\mathbb{Z}/4\mathbb{Z} \cong \{1, i, -1, -i\}$, through $k + 4\mathbb{Z} \mapsto i^k$.
5. For a check of the counting formula, use the map $k + 8\mathbb{Z} \mapsto i^k$ on $\mathbb{Z}/8\mathbb{Z}$. It is defined by the universal property, because $8\mathbb{Z} \subseteq 4\mathbb{Z}$. Its kernel $\{0 + 8\mathbb{Z}, 4 + 8\mathbb{Z}\}$ has order $2$, its image has order $4$, and $2 \cdot 4 = 8$.

The typical use is to prove $G/N \cong Q$ for given groups.
We find a surjective homomorphism $G \to Q$ and we show that its kernel is $N$.
Then the theorem gives the isomorphism, and we do not check well definedness by hand.

A common error is to write $G/\ker \varphi \cong H$ when $\varphi$ is not surjective.
In general, the quotient is isomorphic only to the image, which can be a proper subgroup of $H$.
A second error is to forget to compute the kernel exactly: it is not enough to show that $N \subseteq \ker \varphi$.

### L3 human

The theorem says that every homomorphism factors as a surjection followed by an injection, through $G/\ker \varphi$.
In the [[category of groups|2CX7RPPXA9]], this is the image factorization: the coimage $G/\ker \varphi$ and the image $\operatorname{im} \varphi$ agree.
In the language of exact sequences, the sequence $1 \to \ker \varphi \to G \to \operatorname{im} \varphi \to 1$ is a short exact sequence.
The same pattern holds in every abelian category and in universal algebra.
The second and third isomorphism theorems and the correspondence theorem follow from this theorem, applied to suitable homomorphisms.
