---
tag: 0D9NDGE9KP
kind: statement
role: lemma
name: Uniqueness of identity and inverses
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
about: [G5S1M9, 07WYQPB8E3, 0ZNZH0EXFX]
uses: [G5S1M9, 07WYQPB8E3, 0ZNZH0EXFX, 0K8F7PVDMX]
formal:
  - system: lean4
    library: mathlib
    decl: eq_inv_of_mul_eq_one_right
    match: stronger
    adapter: Math2.Match.inv_unique
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
  - book: isbn:9780471433347
    locator: Section 1.1
  - book: isbn:9781305657960
    locator: Chapter 2
---

## Statement

Let $G$ be a [[group|G5S1M9]] with [[identity element|07WYQPB8E3]] $e$, and let $a, b \in G$.

1. The identity is unique. If $f \in G$ satisfies $fx = x$ for all $x \in G$, then $f = e$. If $f \in G$ satisfies $xf = x$ for all $x \in G$, then $f = e$.
2. [[Inverses|0ZNZH0EXFX]] are unique. If $ab = e$, then $b = a^{-1}$ and $a = b^{-1}$. In particular, each element of $G$ has exactly one inverse.
3. The inverse of the inverse is the element: $(a^{-1})^{-1} = a$.
4. The inverse of a product is the product of the inverses in the reverse order: $(ab)^{-1} = b^{-1} a^{-1}$.

## Remarks

### Why each hypothesis is needed

1. Associativity is needed for part 2. Let $M = \{e, a, b\}$ with the operation in which $e$ is an identity and $xy = e$ for all $x, y \in \{a, b\}$. Then $aa = e$ and $ab = e = ba$, so $a$ has the two different inverses $a$ and $b$. This operation is not associative: $(aa)b = eb = b$, but $a(ab) = ae = a$.
2. Inverses for all elements are needed for the one-equation test of part 2. In a [[monoid|0N6R902FG1]], one equation $ts = e$ does not make $s$ invertible. Let $M$ be the monoid of all functions $\mathbb{N} \to \mathbb{N}$ under composition, with $s(n) = n + 1$ and $t(n) = \max(n - 1, 0)$. Then $t \circ s$ is the identity function, but $s \circ t$ is not, because $s(t(0)) = 1$.

### Consequences

1. The notations $e$ and $a^{-1}$ are well defined, because there is only one identity and one inverse of each element.
2. For elements $a_1, \ldots, a_n$ of $G$, we have $(a_1 a_2 \cdots a_n)^{-1} = a_n^{-1} \cdots a_2^{-1} a_1^{-1}$. This follows from part 4 by induction on $n$.
3. The map $G \to G$, $x \mapsto x^{-1}$, is a bijection, and it is its own inverse map by part 3.
4. An element $a$ satisfies $a = a^{-1}$ if and only if $a^2 = e$. This follows from part 2 with $b = a$.
5. The group $G$ is [[abelian|082GHNPJ53]] if and only if $(ab)^{-1} = a^{-1} b^{-1}$ for all $a, b \in G$. If this law holds, part 4 gives $b^{-1} a^{-1} = a^{-1} b^{-1}$ for all $a, b$, and with $a^{-1}$ and $b^{-1}$ in place of $a$ and $b$, part 3 gives $ba = ab$. Conversely, if $G$ is abelian, then part 4 gives $(ab)^{-1} = b^{-1} a^{-1} = a^{-1} b^{-1}$.
6. In the [[symmetric group|0515A6D2Y1]] $S_3$, the law $(ab)^{-1} = a^{-1} b^{-1}$ fails. Take $a = (1\,2)$ and $b = (1\,3)$, with composition from right to left. Then $ab = (1\,3\,2)$, so $(ab)^{-1} = (1\,2\,3)$. But $a^{-1} b^{-1} = ab = (1\,3\,2)$, because each transposition is its own inverse.

### Converse

The converse of part 2 is the definition of the inverse: if $b = a^{-1}$, then $ab = e$ and $ba = e$.

### Generalizations

Parts 1 and 4 and the uniqueness in part 2 hold in each monoid, for the elements that have an inverse.
If $ba = e$ and $ac = e$ in a monoid, then $b = b(ac) = (ba)c = c$.
So the invertible elements of a monoid form a group, the group of [[units|0XVEZDE9J8]].

## Explanations

### L1 human

A group has only one element that does nothing.
Each element also has only one partner that undoes it.
So we can speak of the identity and of the inverse of an element.
To undo two steps, we undo the second step first and then the first step.
Think of putting on socks and then shoes: to undo this, you take off the shoes first and then the socks.
This is the rule $(ab)^{-1} = b^{-1} a^{-1}$.

### L2 human

The typical use of part 2 is a short test: to show that $b$ is the inverse of $a$, check one equation $ab = e$.
Here is a worked example in the nonzero residues modulo $7$ under multiplication, a group with identity $1$.

1. We look for the inverse of $3$.
2. We compute $3 \cdot 5 = 15 = 2 \cdot 7 + 1$, so $3 \cdot 5 = 1$ modulo $7$.
3. By part 2, $5 = 3^{-1}$, and also $3 = 5^{-1}$. We do not need to compute $5 \cdot 3$.
4. By part 4, the inverse of $3 \cdot 3 = 2$ is $3^{-1} \cdot 3^{-1} = 5 \cdot 5 = 25 = 4$ modulo $7$. Check: $2 \cdot 4 = 8 = 1$ modulo $7$.

A common error is to write $(ab)^{-1} = a^{-1} b^{-1}$.
This is correct only when $a$ and $b$ commute, and consequence 6 gives a failure in $S_3$.
A second trap is to use the one-equation test outside a group: in a monoid, $ts = e$ does not give $st = e$.

### L3 human

Part 1 is a fact about any [[binary operation|0M418FE7BB]]: a left identity $f$ and a right identity $e$ satisfy $f = fe = e$.
Part 2 holds in each monoid for invertible elements, so the inverse is a function on the group of units.
For this reason, the language of universal algebra can treat inversion as an operation $a \mapsto a^{-1}$ that is part of the structure.
Part 4 says that inversion is an [[isomorphism|08MG7H8JW5]] from $G$ to its [[opposite group|D33V8HE0KY]], since it reverses the order of products.
Part 3 says that this isomorphism is its own inverse.
