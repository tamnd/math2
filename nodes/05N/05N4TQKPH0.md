---
tag: 05N4TQKPH0
kind: statement
role: theorem
name: Subgroup criterion
aliases: [one-step-subgroup-test]
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
about: [0X1JXT47GA]
uses: [G5S1M9, 0X1JXT47GA, 0D9NDGE9KP, 00DRK90Z6K]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Subgroup tests
  - book: isbn:9781305657960
    locator: Chapter 3
  - book: isbn:9780471433347
    locator: Section 2.1
---

## Statement

Let $G$ be a [[group|G5S1M9]] with identity $e$, and let $H$ be a subset of $G$.

1. (One-step test.) $H$ is a [[subgroup|0X1JXT47GA]] of $G$ if and only if $H \neq \emptyset$ and $ab^{-1} \in H$ for all $a, b \in H$.
2. (Two-step test.) $H$ is a subgroup of $G$ if and only if $H \neq \emptyset$, $ab \in H$ for all $a, b \in H$, and $a^{-1} \in H$ for all $a \in H$.
3. (Finite test.) Suppose that $H$ is finite and $H \neq \emptyset$. Then $H$ is a subgroup of $G$ if and only if $ab \in H$ for all $a, b \in H$.

In additive notation, the condition of the one-step test is $a - b \in H$ for all $a, b \in H$.

## Remarks

### Why each hypothesis is needed

1. The condition $H \neq \emptyset$ is needed in each test. The empty set satisfies all the closure conditions, because there are no elements to check, but it does not contain $e$.
2. Finiteness is needed in the finite test. The set $\mathbb{N} = \{0, 1, 2, \ldots\}$ is a nonempty subset of $(\mathbb{Z}, +)$ that is closed under addition, but $-1 \notin \mathbb{N}$, so it is not a subgroup.
3. The inverse condition is needed in the two-step test for the same reason: $\mathbb{N}$ satisfies the other two conditions.
4. The closure condition is needed in the two-step test. In the [[symmetric group|0515A6D2Y1]] $S_3$, the set $\{e, (1\,2), (1\,3)\}$ is nonempty and closed under inverses, but $(1\,2)(1\,3) = (1\,3\,2)$ is not in it.

### Why the finite proof does not extend

The proof of the finite test takes $a \in H$ and looks at the powers $a, a^2, a^3, \ldots$, which all lie in $H$ by closure.
Because $H$ is finite, two of these powers are equal, and this gives $a^{-1}$ as a positive power of $a$.
In $\mathbb{N} \subseteq \mathbb{Z}$, the multiples $1, 2, 3, \ldots$ of $1$ are all distinct, so no repetition occurs and the argument gives nothing.
Some school texts define a subgroup as a subset that is closed under the operation.
That definition agrees with the correct one only for finite subsets.

### Consequences

1. The subgroups $n\mathbb{Z}$ of $\mathbb{Z}$, the special linear group in the general linear group and many other examples follow from one check of $ab^{-1} \in H$.
2. The [[intersection of subgroups|0ZTGMDNVTB]] is a subgroup: the one-step test passes in each subgroup, so it passes in the intersection.
3. In a finite group, a nonempty subset closed under the operation is a subgroup. For example, the set of even permutations in $S_n$ is a subgroup, because the product of two even permutations is even.

### Converse

Each test is an equivalence, so the converse of each direction holds.
The direction "subgroup implies the conditions" follows from the definition of a subgroup.

### Generalizations

The finite test holds under a weaker hypothesis: it is enough that each element of $H$ has finite [[order|0WE2NHZJ7B]] in $G$.
The proof is the same, because it uses only that some positive power of $a$ equals $e$.
For a monoid, the analogue of the two-step test defines a submonoid: a subset that contains the identity and is closed under products.

## Explanations

### L1 human

To test whether a part of a group is a subgroup, we can use one check instead of three.
Take any two elements $a$ and $b$ of the part.
Combine $a$ with the inverse of $b$.
If the result is always in the part, and the part is not empty, then the part is a subgroup.
For example, take the multiples of $5$ in the integers under addition.
The difference of two multiples of $5$ is a multiple of $5$, for example $20 - 35 = -15$.
So the multiples of $5$ form a subgroup.

### L2 human

We use the one-step test to show that $H = \{x \in \mathbb{R}^\times : x > 0\}$ is a subgroup of $(\mathbb{R}^\times, \cdot)$.

1. $H$ is not empty, because $1 \in H$.
2. Let $a, b \in H$. Then $a > 0$ and $b > 0$, so $b^{-1} = 1/b > 0$.
3. The product of two positive numbers is positive, so $ab^{-1} = a/b > 0$.
4. So $ab^{-1} \in H$, and the one-step test gives $H \leq \mathbb{R}^\times$.

The typical use is a short proof that a set given by a property is a subgroup.
For a finite set, the finite test is often faster: for example, $\{1, -1, i, -i\}$ is closed under multiplication, so it is a subgroup of $\mathbb{C}^\times$.

A trap: the finite test applied to an infinite set.
The set $\{x \in \mathbb{R}^\times : x \geq 1\}$ is closed under multiplication, but $2^{-1} = \tfrac{1}{2}$ is not in it.

### L3 human

The one-step test shows that a subgroup is the same as a nonempty subset closed under the single binary operation $(a, b) \mapsto ab^{-1}$.
This operation is the basis of the theory of heaps and torsors, where a group without a chosen identity is described by $(a, b, c) \mapsto ab^{-1}c$.

The finite test is a special case of a general fact: in a finite monoid, each element has a power that is idempotent.
In a group the only idempotent is $e$, so a finite nonempty subset of a group that is closed under products is a subgroup.
The same fact for compact topological groups says that a nonempty closed subsemigroup of a compact group is a subgroup.
The test is used in every later sub-area, from [[cyclic subgroups|08ABT85339]] to kernels of homomorphisms and Sylow subgroups.
