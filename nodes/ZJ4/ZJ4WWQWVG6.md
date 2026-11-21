---
tag: ZJ4WWQWVG6
kind: example
name: Fields do not form a universal class
aliases: [fields-not-universal-class]
msc: ["03C52", "12L12"]
topics: [JYJHB4YBAH]
audience: grad
not_instance_of:
  - target: ZSTEZ3PRT9
    note: "The ring of integers is a substructure of the field of rationals and is not a field, so the class of fields is not closed under substructures."
uses: [ZSTEZ3PRT9, 04C5ZBG1WT, 676H7EGTKJ, 9RN0KYXNT1]
sources:
  - book: isbn:9780521587136
---

## Example

Let $L = \set{+, -, \cdot, 0, 1}$ be the signature of rings, with $-$ unary.
The class of [[fields|04C5ZBG1WT]] is an elementary class, axiomatized by the commutative ring axioms, $0 \ne 1$, and $\forall x \, \exists y \, (x = 0 \vee x \cdot y = 1)$.
It is not a [[universal class|ZSTEZ3PRT9]].

1. Every universal class is closed under [[substructures|676H7EGTKJ]].
2. The integers $\mathbb{Z}$ form an $L$-substructure of $\mathbb{Q}$, since $\mathbb{Z}$ contains $0$ and $1$ and is closed under $+$, $-$ and $\cdot$.
3. $\mathbb{Q}$ is a field, but $\mathbb{Z}$ is not, since $2$ has no inverse in $\mathbb{Z}$.
4. So the class of fields is not closed under substructures, and no set of universal sentences axiomatizes it.

## Remarks

The obstruction is the inverse axiom, which has the form $\forall \exists$.
The other field axioms are universal, and their models are the commutative rings with $0 \ne 1$, a universal class that contains $\mathbb{Z}$.
The universal theory of fields has as models exactly the substructures of fields, which are the integral domains, by the [[Łoś-Tarski theorem|9RN0KYXNT1]] applied to this class.
If one adds a unary symbol ${}^{-1}$ for the inverse, with $0^{-1} = 0$, the class of fields becomes universal: the axiom $\forall x \, (x = 0 \vee x \cdot x^{-1} = 1)$ is universal, and substructures are now closed under inverses.
So whether a class is universal depends on the signature, not only on the structures.

## Explanations

### L1 human

The whole numbers sit inside the fractions, and adding, subtracting and multiplying whole numbers gives whole numbers.
But fractions let you divide by any nonzero number, and whole numbers do not: $1/2$ is missing.
So a piece of a field need not be a field.
Rules that only say "for all" are always inherited by pieces, so fields cannot be described by such rules alone.

### L2 human

We check that the integral domains are the substructures of fields.

1. A subring of a field has no zero divisors, since $ab = 0$ with $a \ne 0$ gives $b = a^{-1} a b = 0$ in the field.
2. Conversely, an integral domain $D$ embeds in its field of fractions, by $a \mapsto a/1$.
3. So the models of the universal theory of fields are the integral domains, and $\mathbb{Z}$ is one of them.

The same test works for any class: find a structure in the class and a substructure outside it.
A trap is to use the subset $\set{0}$ of $\mathbb{Q}$; it is not a substructure, since it does not contain the constant $1$.
