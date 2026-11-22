---
tag: MRQW28BQ7D
kind: example
name: The group axioms as an axiomatic system
msc: ["00A35", "20A05"]
topics: [N4P3E53HM0]
audience: ug1
instance_of: [GD2JBXJV5Z]
uses: [GD2JBXJV5Z, G5S1M9, 0M418FE7BB, 0K8F7PVDMX, 07WYQPB8E3, 0ZNZH0EXFX, 0D9NDGE9KP]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
  - book: isbn:9780471433347
    locator: Section 1.1
---

## Example

We read the axioms of a [[group|G5S1M9]] as an [[axiom system|GD2JBXJV5Z]] and derive a first theorem from them, naming the axiom behind each step.

The primitive terms are a set $G$ and a [[binary operation|0M418FE7BB]] $*$ on $G$.
The system says nothing about what the elements of $G$ are or how $*$ is computed.
There are three axioms.

- G1 ([[associativity|0K8F7PVDMX]]): for all $a, b, c \in G$, $(a * b) * c = a * (b * c)$.
- G2 (identity): there is an element $e \in G$ with $e * a = a$ and $a * e = a$ for all $a \in G$.
- G3 (inverses): for each $a \in G$ there is an element $a' \in G$ with $a * a' = e$ and $a' * a = e$.

An element $e$ as in G2 is called an [[identity element|07WYQPB8E3]], and an element $a'$ as in G3 is called an [[inverse|0ZNZH0EXFX]] of $a$.

Theorem: the identity element is unique, and each element has exactly one inverse.

1. Let $e$ and $f$ both satisfy G2.
   Then $e * f = f$ because $e$ is an identity, and $e * f = e$ because $f$ is an identity.
   So $e = f$.
2. Let $b$ and $c$ both be inverses of $a$.
   We start from $b$ and use G2, then G3 for $c$, then G1, then G3 for $b$, then G2 again.
   $$b = b * e = b * (a * c) = (b * a) * c = e * c = c.$$
3. So $a$ has only one inverse.

The theorem is the lemma on the [[uniqueness of identity and inverses|0D9NDGE9KP]].
It is what makes the notation $a^{-1}$, "the inverse of $a$", legitimate.

## Remarks

The example shows all four parts of the method at once.
The primitive terms are $G$ and $*$, the axioms are G1 to G3, the definitions name the identity and the inverses, and the theorem is derived from these alone.
No step uses a property of a particular group, so the theorem holds in every group.
In $(\mathbb{Z}, +)$ it says that $0$ is the only identity and $-a$ the only inverse of $a$.
In the nonzero rationals under multiplication it says the same of $1$ and $1/a$.

What happens when we drop an axiom?
Without G3 the system describes monoids.
Part 1 of the proof used only G2, so a monoid still has one identity.
Part 2 used only G1, G2 and the two equations $b * a = e$ and $a * c = e$, so in a monoid an element has at most one two-sided inverse.

Without G1 the chain in part 2 breaks at the regrouping step, and uniqueness of inverses can fail.
Take the set $\{e, a, b\}$ with $e$ as identity, and let every product of two elements of $\{a, b\}$ be $e$.
Then $a * a = e$ and $a * b = b * a = e$, so $a$ has the two inverses $a$ and $b$.
Check that associativity fails:
$$(a * a) * b = e * b = b, \qquad a * (a * b) = a * e = a.$$

## Explanations

### L1 human

The rules of a group say only three things about an operation such as adding whole numbers.
Grouping does not matter, there is a "do nothing" element, and each element can be undone.
From these three rules alone we can show that there is only one "do nothing" element.
For addition it is $0$, because $0 + 5 = 5$.
The argument never uses the fact that the elements are numbers, so it works for every group.

### L2 human

We check the theorem in one concrete group, the integers modulo $4$ under addition, $G = \{0, 1, 2, 3\}$.

1. The element $0$ is an identity, because $0 + a = a$ for each $a \in G$.
2. No other element is an identity, because adding it to $1$ changes $1$: $1 + 1 = 2$, $2 + 1 = 3$ and $3 + 1 = 0$.
3. The inverse of $1$ is $3$, because $1 + 3 = 4 \equiv 0 \pmod 4$.
4. No other element is an inverse of $1$, because $1 + 0 = 1$, $1 + 1 = 2$ and $1 + 2 = 3$, and none of these is $0$.

The check agrees with the theorem, but it covers one group, while the proof covers all groups at once.
That is the reason to work from axioms.
Watch out: in $\mathbb{Z}/4\mathbb{Z}$ the order of the factors does not matter, but commutativity is not a group axiom.
So the general proof keeps $b * (a * c)$ and $(b * a) * c$ in the order that the axioms allow, and never swaps two factors.
