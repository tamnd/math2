---
tag: D33V8HE0KY
kind: concept
name: Opposite structure
aliases: [opposite-group]
msc: [08A02, 20A05]
topics: [BAZT8JJ70S]
audience: ug1
uses: [0M418FE7BB, G5S1M9]
sources:
  - url: https://en.wikipedia.org/wiki/Opposite_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Opposite_ring
    locator: lead section
same_as:
  wikidata: Q3117899
  wikipedia: Opposite group
---

## Summary

Let $(G, \cdot)$ be a [[group|G5S1M9]].
The opposite group $G^{\mathrm{op}}$ is the same set $G$ with the reversed product $a \ast b = b \cdot a$.
The same construction works for any set with a [[binary operation|0M418FE7BB]], for example a [[monoid|0N6R902FG1]].
For a ring, the [[opposite ring|M8Q24XB0AF]] reverses the multiplication and keeps the addition.
The opposite of a group is again a group, and the inversion map $x \mapsto x^{-1}$ is an [[isomorphism|08MG7H8JW5]] from $G$ to $G^{\mathrm{op}}$.
The opposite structure matters because it turns each "right" notion into a "left" notion, so that a theorem about one side gives the theorem about the other side.

## Motivation

Many constructions in algebra come in a left form and a right form.
A group can act on a set from the left, $g \cdot x$, or from the right, $x \cdot g$.
A matrix can multiply a column vector from the left, or a row vector from the right.
A right version of a rule usually reverses the order of products.
For a right action, the product $gh$ acts by first $g$ and then $h$, while for a left action it acts by first $h$ and then $g$.
We do not want to prove each theorem twice.
The opposite structure reverses the order of products once and for all, so that each right object for $G$ becomes a left object for $G^{\mathrm{op}}$.

## Notation

The usual symbol is $G^{\mathrm{op}}$, and some books write $G^{\circ}$.
To keep track of the two products, some texts write $a^{\mathrm{op}}$ for the element $a$ viewed in $G^{\mathrm{op}}$, so that $a^{\mathrm{op}} b^{\mathrm{op}} = (ba)^{\mathrm{op}}$.
In this text, $a \ast b$ denotes the product in $G^{\mathrm{op}}$, and $ab$ denotes the product in $G$.
In Mathlib, the opposite of a type $\alpha$ with a multiplication is `MulOpposite α`, written $\alpha^{\mathrm{mop}}$, with the maps `op` and `unop`.

## Remarks

### Examples

1. For an [[abelian group|082GHNPJ53]], such as $(\mathbb{Z}, +)$, the opposite group is the group itself, because $b + a = a + b$.
2. [[The opposite group of S3|~c1eaa650]] has the product $\sigma \ast \tau = \tau \sigma$. For example, $(1\ 2) \ast (1\ 3) = (1\ 3)(1\ 2) = (1\ 2\ 3)$, while $(1\ 2)(1\ 3) = (1\ 3\ 2)$.
3. [[The transpose is an isomorphism from the general linear group to its opposite|~0df7430e]], because $(AB)^T = B^T A^T$.
4. For the ring $M_n(\mathbb{R})$ of real $n \times n$ matrices, the transpose is also an isomorphism from the ring to its opposite ring, because it keeps sums and reverses products.

### Non-examples

1. [[The identity map from S3 to its opposite group is not a homomorphism|~4235ecda]]: the condition $\mathrm{id}(ab) = \mathrm{id}(a) \ast \mathrm{id}(b)$ fails for $a = (1\ 2)$ and $b = (1\ 3)$.
2. The opposite of a monoid need not be isomorphic to the monoid. Let $T$ be the monoid of the $4$ maps from $\{0, 1\}$ to itself under composition. A constant map $c$ satisfies $c \circ g = c$ for all $g \in T$. In $T^{\mathrm{op}}$ no element $z$ satisfies $z \ast g = z$ for all $g$, because $z \ast g = g \circ z$ and the swap $g$ changes each $z$. An isomorphism keeps this property, so $T \not\cong T^{\mathrm{op}}$.
3. The opposite group of a group that is not abelian is not the same group: the set is the same, but the operation is different.

### Basic properties

Let $G$ be a group with identity $e$, and write $a \ast b = ba$.

1. $G^{\mathrm{op}}$ is a group with the same identity $e$ and the same inverses.
   - Closure: $ba \in G$ for all $a, b \in G$.
   - Associativity: $(a \ast b) \ast c = c(ba)$ and $a \ast (b \ast c) = (cb)a$, and these are equal by the associativity of $G$.
   - Identity: $e \ast a = ae = a$ and $a \ast e = ea = a$.
   - Inverses: $a \ast a^{-1} = a^{-1}a = e$ and $a^{-1} \ast a = a a^{-1} = e$.
2. $(G^{\mathrm{op}})^{\mathrm{op}} = G$, because reversing the product two times gives $a b$ back.
3. The inversion map $\iota \colon G \to G^{\mathrm{op}}$, $\iota(x) = x^{-1}$, is an isomorphism.
   - The product $(xy)(y^{-1}x^{-1})$ is $e$, so $(xy)^{-1} = y^{-1}x^{-1}$ by the [[uniqueness of inverses|0D9NDGE9KP]].
   - Thus $\iota(xy) = y^{-1}x^{-1} = x^{-1} \ast y^{-1} = \iota(x) \ast \iota(y)$, and $\iota$ is a homomorphism.
   - $\iota(\iota(x)) = (x^{-1})^{-1} = x$, so $\iota$ is its own inverse, and it is a bijection.
4. The operations of $G$ and $G^{\mathrm{op}}$ are equal exactly when $G$ is abelian, because $a \ast b = ab$ means $ba = ab$.
5. A map $f \colon G \to H$ is a homomorphism from $G^{\mathrm{op}}$ to $H$ exactly when $f(ab) = f(b)f(a)$ for all $a, b$. Such a map is called an antihomomorphism from $G$ to $H$.
6. The [[Cayley table|0YB2NRP0T5]] of $G^{\mathrm{op}}$ is the Cayley table of $G$ reflected in its main diagonal.

### Right actions

A right action of $G$ on a set $X$ is a map $X \times G \to X$, $(x, g) \mapsto x \cdot g$, with $x \cdot e = x$ and $x \cdot (gh) = (x \cdot g) \cdot h$ for all $x \in X$ and $g, h \in G$.
Define $g \star x = x \cdot g$.
We check that $\star$ is a left [[group action|0WCY42EV9V]] of $G^{\mathrm{op}}$ on $X$.

1. Identity: $e \star x = x \cdot e = x$.
2. Compatibility: $(a \ast b) \star x = x \cdot (ba) = (x \cdot b) \cdot a = a \star (b \star x)$.

So a right action of $G$ is the same thing as a left action of $G^{\mathrm{op}}$.
With the isomorphism $\iota$, it also gives a left action of $G$ itself, by $g \bullet x = x \cdot g^{-1}$.
For example, $(gh) \bullet x = x \cdot (h^{-1}g^{-1}) = (x \cdot h^{-1}) \cdot g^{-1} = g \bullet (h \bullet x)$.

### History

Arthur Cayley introduced the transpose of a matrix in 1858.
The rule $(AB)^T = B^T A^T$ shows that the transpose is an isomorphism from the matrix ring to its opposite ring.
For groups, the inversion map gives the same kind of isomorphism, so every group is isomorphic to its opposite group.

### Common errors

1. The order is reversed only half way. In $G^{\mathrm{op}}$, the product of $a$ and $b$ is $ba$, and the product of $a$, $b$ and $c$ is $cba$, not $bac$.
2. The isomorphism $G \cong G^{\mathrm{op}}$ is taken to be the identity map. The identity map is a homomorphism $G \to G^{\mathrm{op}}$ only when $G$ is abelian, and the isomorphism in general is $x \mapsto x^{-1}$.
3. The fact that each group is isomorphic to its opposite is extended to monoids and rings, where it can fail, as non-example 2 shows.

## Explanations

### L1 human

The opposite group reads every product backwards.
Think of the moves of a puzzle, where "$a$ then $b$" gives a new move.
In the opposite group, the product of $a$ and $b$ means "$b$ then $a$".
For ordinary addition nothing changes, because $2 + 3$ and $3 + 2$ are both $5$.
For moves of a puzzle the order matters, so the opposite group has a different rule.
Still, the opposite group has the same shape as the old one: if we replace each move by the move that undoes it, the two rules match.

### L2 human

We check that $\iota(x) = x^{-1}$ respects products in a concrete group, the [[symmetric group|0515A6D2Y1]] $S_3$, with permutations composed from right to left.

1. Take $x = (1\ 2)$ and $y = (1\ 3)$. Then $xy = (1\ 2)(1\ 3) = (1\ 3\ 2)$.
2. So $\iota(xy) = (1\ 3\ 2)^{-1} = (1\ 2\ 3)$.
3. A transposition is its own inverse, so $\iota(x) = (1\ 2)$ and $\iota(y) = (1\ 3)$.
4. In $S_3^{\mathrm{op}}$, $\iota(x) \ast \iota(y) = \iota(y)\iota(x) = (1\ 3)(1\ 2) = (1\ 2\ 3)$.
5. Steps 2 and 4 give the same element, as the rule $\iota(xy) = \iota(x) \ast \iota(y)$ says.

The typical use is to move a result about left actions or left modules to right actions or right modules.
A trap is to use the same symbol for the products of $G$ and of $G^{\mathrm{op}}$ in one computation; keep two symbols until the computation ends.

### L3 human

In the language of categories, a group is a category with one object in which every morphism is invertible.
The opposite group is then the [[opposite category|DAMK8XE1FR]], with the direction of every arrow reversed.
For a ring $R$, a right $R$-module is the same thing as a left $R^{\mathrm{op}}$-module, and the endomorphism ring of $R$ as a left module over itself is isomorphic to $R^{\mathrm{op}}$.
For a central simple algebra $A$ over a field, the class of $A^{\mathrm{op}}$ is the inverse of the class of $A$ in the [[Brauer group|BEW48TA9WZ]].
For groups the construction gives nothing new up to isomorphism, but it fixes the order of products in the definitions of right actions, right cosets and anti-homomorphisms in later sub-areas.
