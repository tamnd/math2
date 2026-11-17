---
tag: E0R6P2FMCM
kind: proof
name: Proof of the pigeonhole principle
msc: ["05A05"]
topics: [GB14W4SYPK]
audience: school
proves: 0HGVCWQGY3
uses: [05099E1NMJ, 0PVG1CRAJN, 0SNQEF7Z53, 0Q3F20XB0A, 01FPXMTBX1, 07EH4R3RVQ, 03QC59M99B]
methods: [0J0XBKG64S]
sources:
  - url: https://proofwiki.org/wiki/Pigeonhole_Principle
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
---

## Proof

Let $A$ and $B$ be finite sets with $|A| > |B|$, and let $f : A \to B$ be a function.
We argue by [[contradiction|0J0XBKG64S]].

1. Suppose that $f$ is [[injective|0PVG1CRAJN]]. Let $C = f(A) = \set{f(a) : a \in A}$ be the [[image|0Q3F20XB0A]] of $A$ under $f$.
2. We view $f$ as a map from $A$ to $C$. It is injective by step 1. It is surjective, because each element of $C$ is $f(a)$ for some $a \in A$, by the definition of $C$.
3. So $f : A \to C$ is a [[bijection|0SNQEF7Z53]].
4. Let $m = |A|$. By the definition of [[cardinality|05099E1NMJ]], there is a bijection $h : \set{1, \dots, m} \to A$.
5. The composite $f \circ h : \set{1, \dots, m} \to C$ is injective, because [[injections compose|01FPXMTBX1]]. It is surjective, because [[surjections compose|07EH4R3RVQ]].
6. So $f \circ h$ is a bijection from $\set{1, \dots, m}$ to $C$. By the definition of cardinality, $C$ is finite and $|C| = m = |A|$.
7. The set $C$ is a subset of the finite set $B$. By the [[complement principle|03QC59M99B]], $|B \setminus C| = |B| - |C|$.
8. By steps 6 and 7, $|B \setminus C| = |B| - |A|$.
9. The left side is the number of elements of a set, so it is at least $0$. The right side is negative, because $|A| > |B|$ by hypothesis.
10. Steps 8 and 9 contradict each other. So the assumption of step 1 is false, and $f$ is not injective.
11. By the definition of an injective function, there are elements $a \neq a'$ of $A$ with $f(a) = f(a')$. This is the conclusion of the [[pigeonhole principle|0HGVCWQGY3]].

## Idea

An injective map copies $A$ onto its image, a subset of $B$ with exactly $|A|$ elements.
A subset of $B$ cannot have more elements than $B$.
So an injective map from $A$ to $B$ cannot exist when $|A| > |B|$.
The hypothesis $|A| > |B|$ is used only in step 9.

## Variants

- A proof by fibres: the sets $f^{-1}(b)$ for $b \in B$ are pairwise disjoint and cover $A$. If each had at most one element, the [[rule of sum|0EE2V3CHFK]] would give $|A| \le |B|$. This is the case $n = 1$ of the [[proof of the generalized principle|V64DJESEA6]].
- A proof by [[induction|0ASJVEFA9J]] on $|B|$: for $|B| = 0$ there is no map from a non-empty set to $B$. For the step, remove one box $b$; if $f^{-1}(b)$ has two elements we are done, and otherwise the other boxes receive at least $|A| - 1 > |B| - 1$ objects.
- In Lean with Mathlib, the statement follows from the fact that an injective map on a finite set does not increase the number of elements.
