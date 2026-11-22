---
tag: CBC72TX3NQ
kind: concept
name: Up to
aliases: [up-to-isomorphism, unique-up-to, modulo]
msc: ["00A35"]
topics: [BP0WAF23HB]
audience: ug1
uses: [5P955TVSS2, 0G8VEZ3WTK, 0W95W33CMP]
sources:
  - url: https://en.wikipedia.org/wiki/Up_to
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Up_to
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Up_to
    locator: Group theory
---

## Summary

"Up to" tells the reader which differences a statement ignores.
"The prime factorization of $12$ is unique up to the order of the factors" means that $2 \cdot 2 \cdot 3$ and $3 \cdot 2 \cdot 2$ count as the same factorization, and that every other factorization is one of these reorderings.

Precisely, let $\sim$ be an [[equivalence relation|0G8VEZ3WTK]] on a set $X$, and let $P$ be a property of elements of $X$.
The statement "$x$ with $P(x)$ is unique up to $\sim$" means
$$\exists x \, P(x) \quad \text{and} \quad \forall x \, \forall y \, \big( P(x) \land P(y) \Rightarrow x \sim y \big).$$
Equivalently, the set $\{x \in X : P(x)\}$ is nonempty and lies inside one [[equivalence class|0W95W33CMP]] of $\sim$.
Every correct use of "up to" names, or makes clear from context, the relation $\sim$.

## Motivation

Many uniqueness theorems are false for strict equality and true for a coarser relation.
The factorization $12 = 2 \cdot 2 \cdot 3$ is not unique as a list, because $3 \cdot 2 \cdot 2$ is a different list.
The [[fundamental theorem of arithmetic|084HH1NDCB]] still says something exact: any two factorizations into primes are related by reordering.
"Up to order" states this in two words, where the alternative is a statement about multisets or a rule that sorts the factors.

The phrase appears everywhere.
Calculus finds antiderivatives up to an added constant, algebra classifies groups up to isomorphism, and number theory computes modulo $n$, which means up to congruence modulo $n$.
[[Definite descriptions|5P955TVSS2]] and [[well-defined|HNGZEBKVY2]] operations both meet the phrase when "the" object is unique only up to a relation.

## Notation

Each common form of the phrase has its own relation.
"Up to order" relates two lists when one is a reordering of the other.
"Up to sign" relates $x$ and $y$ when $x = \pm y$.
"Up to a constant" relates two functions on an interval when their difference is constant.
"Up to isomorphism" uses the relation $\cong$, "is isomorphic to".
"Modulo $n$" uses congruence, $a \equiv b \pmod{n}$ when $n \mid a - b$.
"Modulo a subgroup $H$" relates $g$ and $g'$ when $g^{-1} g' \in H$.
"Unique up to unique isomorphism" says more: any two solutions are related by exactly one isomorphism that respects the defining data.

## Remarks

### Three worked cases

The real solutions of $x^2 = 4$ are unique up to sign.
Existence holds, since $2^2 = 4$.
If $x^2 = 4$ and $y^2 = 4$, then
$$0 = x^2 - y^2 = (x - y)(x + y),$$
so $x = y$ or $x = -y$, which means $x \sim y$ for the relation $x = \pm y$.

[[Prime factorization is unique up to order and sign|SPS8DBXJ9R]] works out the factorization case, where the relation allows both reordering and a change of sign of each factor.
[[Antiderivatives on an interval are unique up to a constant|QFCQQTBFWC]] uses the mean value theorem to show that two antiderivatives of one function differ by a constant.

In group theory, every [[cyclic group|0KVGH0J5B3]] of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$, so the cyclic group of order $n$ is unique up to isomorphism, by the [[classification of cyclic groups|0736AXH2ME]].
In linear algebra, a [[basis|0KCQ9Y3QKA]] of a vector space is far from unique, but any two bases have the same number of elements, so the [[dimension|03GSZ8RTZJ]] is well defined.

### Name the relation

Without its relation, "up to" says nothing definite.
"There is only one group of order $3$" is true up to isomorphism.
It is false for strict equality, since $\{0, 1, 2\}$ with addition modulo $3$ and $\{1, \omega, \omega^2\}$ with complex multiplication, where $\omega = e^{2\pi i/3}$, are different sets.
So an author should name the relation, and a reader who cannot find it should ask.

The relation must also be an equivalence relation, or "the same" has no coherent meaning.
"Up to a small error" is not a precise use, because "differ by less than $0.1$" is not transitive: $0$ and $0.06$ are close, $0.06$ and $0.12$ are close, but $0$ and $0.12$ are not.

### What it is not

Some claims of uniqueness up to a relation are false.
[[Groups of order 4 are not unique up to isomorphism|9D79T5TH50]]: $\mathbb{Z}/4\mathbb{Z}$ has an element of order $4$ and the Klein four-group has none.
A real $2 \times 2$ matrix is not determined up to [[similarity|0E89HQATM8]] by its determinant.
The matrices
$$I = \begin{pmatrix} 1 & 0 \\ 0 & 1 \end{pmatrix}, \qquad J = \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$$
both have determinant $1$, but $P I P^{-1} = I$ for every invertible $P$, so $J$ is not similar to $I$.

### The rules you can use

A coarser relation gives a weaker statement.
Uniqueness up to equality is the strongest case, and if $x \sim y$ always implies $x \approx y$, then uniqueness up to $\sim$ implies uniqueness up to $\approx$.

A quantity computed from a solution has one value exactly when it is constant on each class of $\sim$.
For example, all cyclic groups of order $n$ have the same number of generators, because an isomorphism sends generators to generators.
So "the number of generators of the cyclic group of order $n$" is a legal phrase, and it equals the number of $k$ in $\{1, \dots, n\}$ with $\gcd(k, n) = 1$.

### Watch out

The common error is to use a property of one representative that the relation does not preserve.
"The cyclic group of order $3$ contains the number $2$" is true for $\mathbb{Z}/3\mathbb{Z}$ written as $\{0, 1, 2\}$ and false for $\{1, \omega, \omega^2\}$.
So it is not a statement about the group up to isomorphism.
"The cyclic group of order $3$ has two generators" is fine, because isomorphisms preserve it.

A second error runs the other way.
A student who proves "the factorization of $6$ is unique" and then lists $2 \cdot 3$ and $3 \cdot 2$ as two factorizations has used two different relations in one argument.

### History

Gauss introduced congruence with respect to a modulus, and the sign $\equiv$, in his *Disquisitiones Arithmeticae* of 1801.
Eilenberg and Mac Lane introduced category theory in 1945, and the phrase "unique up to unique isomorphism" is a part of its language.

### Try it

First, are the real solutions of $x^2 = x$ unique up to sign?
No: the solutions are $0$ and $1$, and $1 \ne \pm 0$.

Second, is a line through the origin in $\mathbb{R}^2$ determined by a nonzero direction vector up to some relation?
Yes, up to multiplication by a nonzero scalar: $v$ and $w$ give the same line exactly when $w = c v$ for some $c \ne 0$.

## Explanations

### L1 human

"Up to" tells us which differences we choose to ignore.
We may say that there is only one way to split $12$ into prime factors, up to order.
The splittings $2 \cdot 2 \cdot 3$ and $3 \cdot 2 \cdot 2$ use the same primes in a different order.
By saying "up to order", we agree to count them as the same splitting.
Then there really is exactly one splitting of $12$.

### L2 human

Here is a typical problem: find all functions $F$ on $\mathbb{R}$ with $F'(x) = 2x$ and $F(1) = 5$.
One antiderivative is $x^2$, and antiderivatives on an interval are unique up to an added constant.
So every solution has the form
$$F(x) = x^2 + C.$$
The condition $F(1) = 5$ gives $1 + C = 5$, so $C = 4$.
Check: $F(x) = x^2 + 4$ has $F'(x) = 2x$ and $F(1) = 5$.
The pattern is common: a uniqueness theorem up to $\sim$ reduces the problem to one class, and one extra condition picks one element of the class.

### L3 human

Category theory gives the strongest common form of "up to".
An object defined by a [[universal property|EN4DD2FAJH]] is unique up to a unique isomorphism that respects the structure maps, so any two choices are identified in exactly one way.
Statements that are invariant under isomorphism may then speak of "the" product or "the" limit.
In Mathlib, `CategoryTheory.Limits.IsLimit.conePointUniqueUpToIso` gives this isomorphism between two limit cones.
Homotopy type theory goes further: with the univalence axiom, isomorphic structures are equal, so every statement in the theory is invariant under isomorphism.
