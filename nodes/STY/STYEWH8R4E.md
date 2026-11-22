---
tag: STYEWH8R4E
kind: statement
role: lemma
name: Linear maps preserve zero, negatives and linear combinations
msc: ["15A04"]
topics: [9080WQTZ3M]
audience: ug1
about: [0NRYHJPQG2]
uses: [0RJF668P1T, 0V8F3E48E6]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Definition and first consequences
  - book: isbn:9780134860244
    locator: Section 2.1
---

## Statement

The lemma says that a linear map carries the zero vector, negatives and every finite linear combination over to the target space.
Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0RJF668P1T]].
Then the following hold.

1. $T(0) = 0$, where the first $0$ is the zero vector of $V$ and the second is the zero vector of $W$.
2. $T(-v) = -T(v)$ for each $v \in V$.
3. For each integer $k \ge 1$, all $v_1, \dots, v_k \in V$ and all $a_1, \dots, a_k \in F$, the [[linear combination|0V8F3E48E6]] is preserved:
$$T(a_1 v_1 + \dots + a_k v_k) = a_1 T(v_1) + \dots + a_k T(v_k).$$

Moreover, a function $T \colon V \to W$ is linear if and only if $T(au + v) = a\,T(u) + T(v)$ for all $u, v \in V$ and $a \in F$.

## Remarks

### What each part needs

Parts 1 and 2 use only additivity, as the [[proof|NQ6EK4PT1G]] shows.
Homogeneity alone also gives part 1, since $T(0) = T(0 \cdot 0) = 0 \cdot T(0) = 0$.

Part 3 needs both conditions.
The map $(x, y) \mapsto \sqrt[3]{x^3 + y^3}$ from $\R^2$ to $\R$ is homogeneous, but it sends $(1, 0) + (0, 1)$ to $\sqrt[3]{2}$, not to $1 + 1 = 2$.
Complex conjugation on $\C$ is additive, but it sends $i \cdot 1$ to $-i$, not to $i \cdot \bar 1 = i$, so part 3 fails for it with $k = 1$ and $a_1 = i$.

### What it gives you

Part 1 is the quickest test of non-linearity: a [[translation|DTCM6N02A9]] by $w_0 \ne 0$ sends $0$ to $w_0$, so it is not linear.
Part 3 says that a linear map is fixed by its values on a [[spanning set|088RYKAWK9]].
For example, if $T \colon \R^2 \to \R^2$ is linear with $T(1, 0) = (2, 1)$ and $T(0, 1) = (0, 3)$, then
$$T(4, -2) = 4\,(2, 1) - 2\,(0, 3) = (8, \; 4 - 6) = (8, -2),$$
and part 2 then gives $T(-4, 2) = (-8, 2)$.
This is the first half of the theorem that a [[linear map is determined by a basis|0R8X9XA83A]].
Part 3 also shows that the image of a [[subspace|00YC1D652K]] is closed under linear combinations, so it is again a subspace.

### The converse

The converse of part 1 is false.
The [[squaring map|RMC0D67M01]] $x \mapsto x^2$ on $\R$ sends $0$ to $0$, but it is not linear.
The converse of part 3 is true: if part 3 holds for $k = 2$, then the case $a_1 = a_2 = 1$ is additivity, and the case $a_2 = 0$ is homogeneity.

## Explanations

### L1 human

A linear map always sends the zero vector to the zero vector.
It sends the opposite of a vector to the opposite of its image.
If a vector is built from other vectors by scaling and adding, its image is built from their images in the same way.
For example, if $T(v_1) = 5$ and $T(v_2) = 1$, then $T(2v_1 + 3v_2) = 2 \cdot 5 + 3 \cdot 1 = 13$.

### L2 human

Here is a typical use: a linear map $T \colon \R^3 \to \R$ has $T(1, 0, 0) = 2$, $T(0, 1, 0) = -1$ and $T(0, 0, 1) = 4$, and we want $T(3, 5, -1)$.
Write the vector as a combination of the three given ones, $(3, 5, -1) = 3(1, 0, 0) + 5(0, 1, 0) - (0, 0, 1)$.
Part 3 moves $T$ inside the combination:
$$T(3, 5, -1) = 3 \cdot 2 + 5 \cdot (-1) - 4 = -3.$$
So three values were enough to compute $T$ everywhere.
Watch out: a map with $T(0) = 0$ can still fail to be linear, so part 1 only ever rules maps out.

### L3 human

Part 3 says that a linear map is a homomorphism for all finite linear combinations, and finite combinations are all the structure that a vector space has.
Infinite sums need a topology, and a map preserves them only when it is continuous, which is the setting of [[continuous linear maps|03TM135G0N]].
The single condition $T(au + v) = a\,T(u) + T(v)$ is the usual form of the definition in proofs and in proof assistants, because one check covers both conditions.
