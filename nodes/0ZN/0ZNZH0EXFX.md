---
tag: 0ZNZH0EXFX
kind: concept
name: Inverse element
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
uses: [0M418FE7BB, 07WYQPB8E3]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
  - book: isbn:9780471433347
    locator: Section 1.1
same_as:
  wikidata: Q338057
  wikipedia: Inverse element
inventory: [FEBX9EH0B8]
---

## Summary

Let $S$ be a set with a [[binary operation|0M418FE7BB]] $\ast$ and an [[identity element|07WYQPB8E3]] $e$, and let $a \in S$.
An element $b$ is a left inverse of $a$ when $b \ast a = e$, and a right inverse of $a$ when $a \ast b = e$.
An inverse, or two-sided inverse, of $a$ is an element that is both a left inverse and a right inverse of $a$, and an element with an inverse is called invertible.
The existence of an inverse for each element is one of the axioms of a [[group|G5S1M9]].

## Motivation

An inverse undoes an element.
If we add $5$ and then add $-5$, we come back to where we started.
Inverses let us solve equations: from $a \ast x = c$ we get $x = b \ast c$, where $b$ is an inverse of $a$, because $b \ast (a \ast x) = (b \ast a) \ast x = x$ for an [[associative|0K8F7PVDMX]] operation.
Subtraction and division are addition of the inverse and multiplication by the inverse.
The concept of an inverse element gives one name to all these ways to undo an operation.

## Notation

In multiplicative notation, the inverse of $a$ is written $a^{-1}$.
In additive notation, it is written $-a$.
The inverse of an invertible matrix $A$ is written $A^{-1}$, and the inverse of a bijection $f$ is written $f^{-1}$.
For a function, $f^{-1}$ is the inverse function, not the function $1/f$.
The inverse is defined with respect to an operation and its identity, so the same element can have different inverses for different operations: in $\mathbb{Q}$, the inverse of $2$ is $-2$ for addition and $\tfrac{1}{2}$ for multiplication.

## Remarks

### Examples

1. For addition on the [[integers|0C4JS9RF5M]], [[rational numbers|0NCJ5WXN6Z]], [[real numbers|08J2M1JYAG]] and [[complex numbers|09FTAET5Z4]], each $a$ has the inverse $-a$, because $a + (-a) = (-a) + a = 0$.
2. For multiplication on $\mathbb{Q}$, $\mathbb{R}$ and $\mathbb{C}$, each $a \neq 0$ has the inverse $1/a$, because $a \cdot (1/a) = (1/a) \cdot a = 1$.
3. [[An invertible 2 × 2 matrix has the inverse given by the determinant formula|8XWC7RKNN1]].
4. [[For multiplication modulo 7, each nonzero class has an inverse|B9ZN1SK225]]: for example, $3 \cdot 5 = 15 \equiv 1 \pmod{7}$.
5. A [[bijective|0GG9TVW90M]] function $f \colon X \to X$ has the inverse function $f^{-1}$ for [[composition|0THBK9V825]], because $f \circ f^{-1} = f^{-1} \circ f = \mathrm{id}_X$.
6. For the operation $a \ast b = a + b + ab$ on $\mathbb{Z}$, with identity $0$, the element $-2$ is its own inverse: $(-2) \ast (-2) = -2 - 2 + 4 = 0$.

### Non-examples

1. [[The shift n ↦ n + 1 on ℕ has a left inverse but no inverse|M9QVG263VV]] in the monoid of functions $\mathbb{N} \to \mathbb{N}$.
2. The integer $2$ has no inverse for multiplication on $\mathbb{Z}$, because $2b = 1$ has no solution $b \in \mathbb{Z}$.
3. The number $0$ has no inverse for multiplication on $\mathbb{Q}$, because $0 \cdot b = 0 \neq 1$ for each $b$.
4. The matrix $A = \begin{pmatrix} 1 & 0 \\ 0 & 0 \end{pmatrix}$ has no inverse for matrix multiplication, because the second row of each product $AB$ is zero, so $AB \neq I_2$.
5. For addition on $\mathbb{N}$, the element $1$ has no inverse, because $1 + b \geq 1 > 0$ for each $b \in \mathbb{N}$.

### Basic properties

1. Let $\ast$ be associative with identity $e$. If $b$ is a left inverse and $c$ is a right inverse of $a$, then $b = c$. Indeed, $b = b \ast e = b \ast (a \ast c) = (b \ast a) \ast c = e \ast c = c$.
2. So, for an associative operation, an element has at most one inverse. For groups, this is part 2 of the lemma on the [[uniqueness of identity and inverses|0D9NDGE9KP]]. Without associativity, an element can have two inverses, as an example in that lemma shows.
3. The inverse of a product reverses the order: if $a$ and $b$ are invertible, then $(ab)^{-1} = b^{-1}a^{-1}$. Indeed, $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1} = aa^{-1} = e$, and in the same way $(b^{-1}a^{-1})(ab) = e$. Also $(a^{-1})^{-1} = a$. Both rules are in the lemma on the [[uniqueness of identity and inverses|0D9NDGE9KP]].
4. The identity is its own inverse, because $e \ast e = e$.
5. An invertible element can be cancelled: if $a \ast x = a \ast y$, then $x = a^{-1} \ast (a \ast x) = a^{-1} \ast (a \ast y) = y$. This is the [[cancellation property|6CR9A0EWPN]].
6. In a finite [[monoid|0N6R902FG1]] $M$, a left inverse is a two-sided inverse. Let $ba = e$. The map $x \mapsto ax$ from $M$ to $M$ is injective, because $ax = ay$ gives $bax = bay$, so $x = y$. An injective map from a finite set to itself is surjective, so $ac = e$ for some $c \in M$. By property 1, $c = b$, so $ab = e$.
7. The same holds for square matrices: [[a one-sided inverse of a square matrix is two-sided|0753Y2X5K6]].
8. For a nonempty set $X$, a function $f \colon X \to X$ has a [[left inverse|05SG20AMXH]] for composition exactly when $f$ is [[injective|09NWETVTNY]], and a [[right inverse|0WWRD82HD2]] exactly when $f$ is [[surjective|01RVCMSN5N]]. For infinite $X$, the second statement uses the axiom of choice.

### History

Subtraction and division, the inverse operations of addition and multiplication, are as old as arithmetic.
In 1843, William Rowan Hamilton found the quaternions, in which each nonzero element has an inverse for a multiplication that is not commutative.

### Common errors

1. The order is not reversed: $(ab)^{-1}$ is written $a^{-1}b^{-1}$. In a group that is not [[abelian|082GHNPJ53]], this is false in general. To undo "socks, then shoes", we must remove the shoes first.
2. Only one side is checked in a structure where one side is not enough. In the monoid of functions $\mathbb{N} \to \mathbb{N}$, a left inverse need not be a right inverse. In a group, one side is enough, by the lemma on the [[uniqueness of identity and inverses|0D9NDGE9KP]].
3. The operation is not stated. The number $2$ is invertible in $\mathbb{Z}$ for addition, but not for multiplication.
4. The notation $f^{-1}$ is read as $1/f$. For $f(x) = x^3$ on $\mathbb{R}$, $f^{-1}(x)$ is the cube root of $x$, not $1/x^3$.

## Explanations

### L1 human

An inverse is an element that undoes another element.
For adding, the inverse of $5$ is $-5$, because $5 + (-5) = 0$, and adding $0$ does nothing.
For multiplying, the inverse of $5$ is $\tfrac{1}{5}$, because $5 \times \tfrac{1}{5} = 1$, and multiplying by $1$ does nothing.
The number $0$ has no inverse for multiplying, because $0$ times any number is $0$, never $1$.

### L2 human

We show that a product of two invertible elements is invertible, with the inverse in the reverse order.
Let $M$ be a monoid with identity $e$, and let $a, b \in M$ have inverses $a^{-1}$ and $b^{-1}$.

1. By associativity, $(ab)(b^{-1}a^{-1}) = a(bb^{-1})a^{-1}$.
2. Since $bb^{-1} = e$ and $ae = a$, this is $aa^{-1}$, which is $e$.
3. By associativity, $(b^{-1}a^{-1})(ab) = b^{-1}(a^{-1}a)b$.
4. Since $a^{-1}a = e$ and $b^{-1}e = b^{-1}$, this is $b^{-1}b$, which is $e$.
5. By steps 2 and 4, $b^{-1}a^{-1}$ is a two-sided inverse of $ab$.

The typical use of inverses is to solve an equation: from $ax = c$, multiply on the left by $a^{-1}$ to get $x = a^{-1}c$.
A trap is to multiply on the wrong side: in a group that is not abelian, $ax = c$ gives $x = a^{-1}c$, and $ca^{-1}$ is a different element in general.

### L3 human

The invertible elements of a monoid form a group, the group of units, and an important example is the [[group of units of Z/n|0F8X8ZRQ53]].
In a ring, the invertible elements for multiplication are the units, and a field is a commutative ring with $1 \neq 0$ in which each nonzero element is a unit.
[[Inverse semigroups|3M724K3B50]] weaken the axiom: each $a$ has a unique $b$ with $aba = a$ and $bab = b$, and they model partial symmetries.
In a [[quasigroup|ZJD31SPPFP]] the equations $ax = c$ and $ya = c$ have unique solutions, even without an identity element.
The Grothendieck construction adds formal inverses to a commutative monoid, and it builds $\mathbb{Z}$ from $(\mathbb{N}, +)$.
In a category, an invertible morphism is an isomorphism, and a category in which every morphism is invertible is a [[groupoid|FH3C0T643F]].
