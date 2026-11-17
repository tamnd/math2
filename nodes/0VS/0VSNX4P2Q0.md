---
tag: 0VSNX4P2Q0
kind: statement
role: lemma
name: Cancellation laws
aliases: [cancellation-law]
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
about: [G5S1M9]
uses: [G5S1M9, 0ZNZH0EXFX, 0K8F7PVDMX]
sources:
  - url: https://en.wikipedia.org/wiki/Cancellation_property
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Group_(mathematics)
    locator: Division
  - book: isbn:9781305657960
    locator: Chapter 2
---

## Statement

Let $G$ be a [[group|G5S1M9]] with identity $e$.

1. Left cancellation: for all $a, b, c \in G$, if $ab = ac$, then $b = c$.
2. Right cancellation: for all $a, b, c \in G$, if $ba = ca$, then $b = c$.
3. Unique solutions: for all $a, b \in G$, the equation $ax = b$ has exactly one solution $x \in G$, namely $x = a^{-1} b$. The equation $ya = b$ has exactly one solution $y \in G$, namely $y = b a^{-1}$.

## Remarks

### Why each hypothesis is needed

1. Inverses are needed. The integers under multiplication form a [[monoid|0N6R902FG1]] in which $0$ has no [[inverse|0ZNZH0EXFX]]. There, $0 \cdot 1 = 0 \cdot 2$ but $1 \neq 2$. Also $0 \cdot x = 1$ has no solution, and $0 \cdot x = 0$ has infinitely many solutions.
2. The inverse must be on the correct side. In the monoid of all functions $\mathbb{N} \to \mathbb{N}$ under composition, let $s(n) = n + 1$ and $t(n) = \max(n - 1, 0)$, so $t \circ s$ is the identity function. Then $s$ can be cancelled on the left, because $s \circ f = s \circ g$ implies $f = t \circ s \circ f = t \circ s \circ g = g$. But $s$ cannot be cancelled on the right: $\mathrm{id} \circ s = s = (s \circ t) \circ s$, and $\mathrm{id} \neq s \circ t$ because $s(t(0)) = 1$.
3. The factor must be on the same side. From $ab = ca$ we cannot conclude $b = c$. In the [[symmetric group|0515A6D2Y1]] $S_3$, with composition from right to left, let $a = (1\,2)$, $b = (1\,3)$ and $c = (2\,3)$. Then $ab = (1\,3\,2) = ca$, but $b \neq c$.

### Consequences

1. For fixed $a \in G$, the map $G \to G$, $x \mapsto ax$, is a bijection, by part 3. The same holds for $x \mapsto xa$.
2. In the [[Cayley table|0YB2NRP0T5]] of a finite group, each element occurs exactly one time in each row and exactly one time in each column. This follows from consequence 1.
3. The identity is the only element $a$ of $G$ with $aa = a$. Indeed, $aa = a = ae$ gives $a = e$ by left cancellation.
4. Consequence 1 is the first step of [[Cayley's theorem|0151VYVX27]], which represents each element $a$ by the permutation $x \mapsto ax$ of $G$.

### Converse

The converse of parts 1 and 2 is false: a structure with both cancellation laws need not be a group.
The natural numbers under addition satisfy both laws, but [[they are not a group|R68D2P175Z]].
The converse of part 3 is true: a nonempty set with an associative operation in which each equation $ax = b$ and $ya = b$ has a solution is a group.
For a finite nonempty set with an associative operation, both cancellation laws are enough to make it a group.
The reason is that an injective map from a finite set to itself is a bijection, so the equations of part 3 have solutions.

### Generalizations

In each monoid, an element with a two-sided inverse can be cancelled on both sides, by the same proof.
A monoid in which all elements can be cancelled is a cancellative monoid.
Each commutative cancellative monoid, such as $(\mathbb{N}, +)$, lies inside a group, as $\mathbb{N}$ lies inside $\mathbb{Z}$.

## Explanations

### L1 human

In a group, you can remove the same element from both sides of an equation, if it stands on the same side in both products.
This works because each element has an inverse that undoes it.
For the same reason, an equation such as $ax = b$ has exactly one answer.
Take care with the side: $ab = ca$ does not give $b = c$ in general.

### L2 human

The typical use is to solve an equation in a group, or to show that two elements are equal.
Here is a worked example in $S_3$, with composition from right to left.

1. Let $a = (1\,2)$ and $b = (1\,2\,3)$. We solve $ax = b$.
2. By part 3, the only solution is $x = a^{-1} b = (1\,2)(1\,2\,3)$, because $(1\,2)$ is its own inverse.
3. We compute $(1\,2)(1\,2\,3)$. The point $1$ goes to $2$ and then to $1$. The point $2$ goes to $3$ and then stays at $3$. The point $3$ goes to $1$ and then to $2$. So $x = (2\,3)$.
4. Check: $(1\,2)(2\,3)$ sends $1$ to $2$, $2$ to $3$ and $3$ to $1$, so it is $(1\,2\,3) = b$.
5. The other equation $ya = b$ has the solution $y = b a^{-1} = (1\,2\,3)(1\,2) = (1\,3)$, which is different from $x$.

A common error is to cancel across sides, as in remark 3 of the first list.
A second trap is to cancel in a monoid: in $(\mathbb{Z}, \cdot)$, the element $0$ cannot be cancelled.

### L3 human

Part 3 says that a group is a [[quasigroup|ZJD31SPPFP]]: left and right division are possible and unique.
A group is the same thing as an associative quasigroup with at least one element.
The bijections $x \mapsto ax$ give the [[left regular action|PR8C073VWY]] of $G$ on itself.
For rings, cancellation of nonzero elements characterizes the [[integral domains|0QVD7WBFGN]] among the nonzero commutative rings, even though nonzero elements need not have inverses.
