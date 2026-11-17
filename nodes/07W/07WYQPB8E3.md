---
tag: 07WYQPB8E3
kind: concept
name: Identity element
aliases: [neutral-element]
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
uses: [0M418FE7BB]
sources:
  - url: https://en.wikipedia.org/wiki/Identity_element
    locator: Definitions
  - book: isbn:9780471433347
    locator: Section 1.1
same_as:
  wikidata: Q185813
  wikipedia: Identity element
inventory: [75FBJRN7YR]
---

## Summary

Let $S$ be a set with a [[binary operation|0M418FE7BB]] $\ast$.
An element $e \in S$ is a left identity when $e \ast a = a$ for all $a \in S$, and a right identity when $a \ast e = a$ for all $a \in S$.
An identity element, or two-sided identity, is an element that is both a left identity and a right identity.
An operation has at most one identity element, and the existence of an identity is one of the axioms of a [[group|G5S1M9]].

## Motivation

Some elements do nothing in an operation.
Adding $0$ does not change a number, multiplying by $1$ does not change a number, and the function that sends each point to itself does not change a function when we compose with it.
These elements play the same role for their operations, so we give the role a name.
An identity element is also needed to define inverses: $b$ undoes $a$ when $a \ast b$ is the element that does nothing.

## Notation

The identity of a group is usually written $e$.
In multiplicative notation it is also written $1$, and in additive notation it is written $0$.
The identity matrix is written $I$ or $I_n$, and the identity function on a set $X$ is written $\mathrm{id}_X$.
When there is a risk of confusion, the group is put as an index, as in $e_G$ or $1_G$.

## Remarks

### Examples

1. The number $0$ is the identity for addition on $\mathbb{N}$, [[integers|0C4JS9RF5M]], [[rational numbers|0NCJ5WXN6Z]], [[real numbers|08J2M1JYAG]] and [[complex numbers|09FTAET5Z4]], because $a + 0 = 0 + a = a$.
2. The number $1$ is the identity for multiplication on the same sets, because $a \cdot 1 = 1 \cdot a = a$.
3. [[The identity matrix is the identity for matrix multiplication|~0899dd0e]] on the $n \times n$ matrices.
4. [[The identity function is the identity for composition|~7d84ada2]] on the functions from a set to itself.
5. For the subsets of a set $X$, the empty set is the identity for union, and $X$ is the identity for intersection.
6. For the operation $a \ast b = a + b + ab$ on $\mathbb{Z}$, the identity is $0$, because $a \ast 0 = a + 0 + 0 = a$ and $0 \ast a = a$.

### Non-examples

1. [[For the operation a ∗ b = b, each element is a left identity and no element is an identity|~4d23ee8a]], on a set with at least two elements.
2. Addition on the positive integers $\{1, 2, 3, \ldots\}$ has no identity, because $a + e = a$ forces $e = 0$, and $0$ is not a positive integer.
3. Subtraction on $\mathbb{Z}$ has the right identity $0$, because $a - 0 = a$. It has no left identity: $e - a = a$ for all $a$ would give $e = 2a$ for all $a$, which is impossible.
4. Multiplication on the even integers has no identity, because $e \cdot 2 = 2$ forces $e = 1$, and $1$ is not even.
5. The operation $\max$ on $\mathbb{R}$ has no identity, because $\max(e, e - 1) = e \neq e - 1$. On $\mathbb{N}$, the identity for $\max$ is $0$.

### Basic properties

1. If $e$ is a left identity and $f$ is a right identity, then $e = f$. Indeed, $e \ast f = f$ because $e$ is a left identity, and $e \ast f = e$ because $f$ is a right identity.
2. So an operation has at most one identity element: two identities $e$ and $f$ give $e = f$ by property 1. For a group, this is part 1 of the lemma on the [[uniqueness of identity and inverses|0D9NDGE9KP]].
3. An operation can have several left identities, as in non-example 1. By property 1, it then has no right identity.
4. The identity satisfies $e \ast e = e$. In a group, it is the only element with this property: if $gg = g$, then $g = g^{-1}gg = g^{-1}g = e$.
5. A subset can have an identity that is different from the identity of the whole set. For multiplication on $\mathbb{R}$, the subset $\{0\}$ is closed, and its identity is $0$, not $1$.
6. A [[semigroup|0XMEM406JM]] with an identity element is a [[monoid|0N6R902FG1]].

### History

The numbers $0$ and $1$ were used with these properties in arithmetic long before the general idea had a name.
In his paper of 1854, Arthur Cayley wrote the identity of a group as $1$, as in his equation $\theta^n = 1$.

### Common errors

1. Only one side is checked. The number $0$ is a right identity for subtraction, but not an identity, because $0 - 3 \neq 3$.
2. The identity is attached to the set and not to the operation. On $\mathbb{Z}$, the identity is $0$ for addition and $1$ for multiplication.
3. The equation is checked for one element only. The identity must satisfy $e \ast a = a$ for each $a$: from $2 \cdot 0 = 0$ we cannot conclude that $2$ is an identity for multiplication.
4. The identity of a subset is assumed to be the identity of the whole set, as property 5 shows.

## Explanations

### L1 human

An identity element is an element that does nothing.
When we add $0$ to a number, the number does not change: $7 + 0 = 7$.
When we multiply a number by $1$, the number does not change: $7 \times 1 = 7$.
So $0$ is the identity for adding, and $1$ is the identity for multiplying.
The identity must do nothing on both sides: $0 + 7 = 7$ too.

### L2 human

To find an identity for an operation given by a formula, solve the equation $a \ast e = a$ for $e$, check that the solution does not depend on $a$, and then check the other side.
For example, let $a \ast b = a + b - 3$ on $\mathbb{Z}$.

1. The equation $a \ast e = a$ is $a + e - 3 = a$, so $e = 3$.
2. The solution $e = 3$ does not depend on $a$.
3. On the other side, $3 \ast a = 3 + a - 3 = a$.
4. So $3$ is the identity element of $\ast$.

If the solution of step 1 depends on $a$, there is no right identity.
For $a \ast b = ab + 1$ on $\mathbb{Z}$, the equation $ae + 1 = a$ gives $e = 1 - 1/a$ for $a \neq 0$, which changes with $a$, so there is no right identity.
A trap is to stop after step 1, as in subtraction, where the right identity is not a left identity.

### L3 human

A set with an associative operation and an identity is a [[monoid|0N6R902FG1]], and a set with any operation and an identity is a [[unital magma|KNDSJAYMSY]].
In universal algebra, a group is a set with three operations, and the identity is the nullary one: a constant $e$.
A homomorphism of groups maps the identity to the identity automatically, but a homomorphism of monoids must be required to do so.
In a ring, the identity for multiplication is often called the unity, and some authors allow rings without it.
In category theory, each object has an identity morphism, and a monoid is the same as a category with one object.
The [[Eckmann–Hilton argument|EJJYCPWHPA]] starts from two operations that each have an identity element, and its first step shows that the two identities are equal.
