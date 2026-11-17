---
tag: M9QVG263VV
kind: example
name: The shift n ↦ n + 1 on ℕ has a left inverse but no inverse
msc: [08A02, 20M20]
topics: [BAZT8JJ70S]
audience: school
instance_of: [05SG20AMXH]
not_instance_of:
  - target: 0ZNZH0EXFX
    note: s has the left inverse t with t(n) = n - 1 for n ≥ 1 and t(0) = 0, but s ∘ u is never the identity, because s(u(0)) ≥ 1
uses: [0MWKJ44V5A, 0THBK9V825, 0PSKT5W817, 09NWETVTNY, 01RVCMSN5N]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_element
    locator: Definitions and basic properties
---

## Example

Let $\mathbb{N} = \{0, 1, 2, \ldots\}$ be the [[natural numbers|0MWKJ44V5A]], and let $M$ be the set of all functions $\mathbb{N} \to \mathbb{N}$ with [[composition|0THBK9V825]].
The identity element of $M$ is the [[identity function|0PSKT5W817]] $\mathrm{id}$.
Let $s \in M$ be the shift $s(n) = n + 1$.

1. Define $t \in M$ by $t(0) = 0$ and $t(n) = n - 1$ for $n \geq 1$. For each $n \in \mathbb{N}$, $s(n) = n + 1 \geq 1$, so $t(s(n)) = (n + 1) - 1 = n$. Thus $t \circ s = \mathrm{id}$, and $t$ is a left inverse of $s$.
2. The left inverse is not unique. Define $t'$ by $t'(0) = 5$ and $t'(n) = n - 1$ for $n \geq 1$. Step 1 never uses the value at $0$, so $t' \circ s = \mathrm{id}$ as well, and $t' \neq t$.
3. The element $s$ has no right inverse. Let $u \in M$. Then $(s \circ u)(0) = u(0) + 1 \geq 1$, so $(s \circ u)(0) \neq 0 = \mathrm{id}(0)$. Thus $s \circ u \neq \mathrm{id}$.
4. An inverse must be a right inverse, so by step 3, $s$ has no [[inverse|0ZNZH0EXFX]] in $M$.
5. The element $t$ has the right inverse $s$, by step 1. It has no left inverse: $t(0) = t(1) = 0$, so for each $v \in M$, $(v \circ t)(1) = v(0) = (v \circ t)(0)$, and $v \circ t \neq \mathrm{id}$.

## Remarks

The function $s$ is [[injective|09NWETVTNY]] but not [[surjective|01RVCMSN5N]], because $0$ is not a value of $s$.
For functions, injective maps have left inverses and surjective maps have right inverses, so the example is typical.
Step 2 does not contradict the uniqueness of inverses: the rule $b = c$ for a left inverse $b$ and a right inverse $c$ of the same element needs a right inverse, and $s$ has none.
The example needs an infinite set.
In a finite monoid, a left inverse is always a two-sided inverse.
For a finite set $X$, an injective function $X \to X$ is also surjective, so a function with a left inverse is a bijection.

## Explanations

### L1 human

Think of a hotel with rooms $0, 1, 2, \ldots$ and one guest in each room.
The shift $s$ moves each guest one room up.
The map $t$ moves each guest one room down, and keeps the guest of room $0$ in room $0$.
If we move up and then down, each guest is back in the old room.
If we move down and then up, the guests of rooms $0$ and $1$ both end in room $1$, so we do not come back.
A plan that ends with the move up always leaves room $0$ empty, so it never brings each guest back.

### L2 human

A one-sided inverse of a function shows itself in the equation $g \circ f = \mathrm{id}$: it says that $g$ undoes $f$, but not that $f$ undoes $g$.
To show that no right inverse exists, find a point that is not a value of $s$; here it is $0$.
The typical use of this example is to show that a one-sided inverse is not enough in a general monoid.
In a group, one side is enough, because each element also has an inverse on the other side.
A trap is to use finite sets for intuition, where one side is enough.
