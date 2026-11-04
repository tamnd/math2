---
tag: DYSCY9R157
kind: proof
name: Proof of the complement principle
msc: [05A05]
proves: 03QC59M99B
uses: [05099E1NMJ, 0SNQEF7Z53, 0EE2V3CHFK, 0W4RPA8QH3]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Cardinality_of_Complement
---

## Proof

We first show that every subset of a finite set is finite, by induction on the size. Then we apply the [[rule of sum|0EE2V3CHFK]].

1. Claim: for each natural number $n$, every subset of a set with $n$ elements is finite. We argue by induction on $n$.
2. For $n = 0$, the only set with $0$ elements is $\varnothing$. Its only subset is $\varnothing$, which is finite.
3. Suppose the claim holds for $n$. Let $V$ have $n + 1$ elements, with a [[bijection|0SNQEF7Z53]] $g : \set{1, \dots, n+1} \to V$. Let $B \subseteq V$.
4. Put $v = g(n+1)$ and $V' = V \setminus \set{v}$. The restriction of $g$ to $\set{1, \dots, n}$ is a bijection onto $V'$, so $V'$ has $n$ elements.
5. The set $B \setminus \set{v}$ is a subset of $V'$. By the induction hypothesis it is finite.
6. If $v \notin B$, then $B = B \setminus \set{v}$ is finite.
7. If $v \in B$, then $B$ is the union of the [[disjoint|0W4RPA8QH3]] finite sets $B \setminus \set{v}$ and $\set{v}$. By the rule of sum, $B$ is finite. This proves the claim.
8. Now let $U$ be finite and $A \subseteq U$. By the claim, $A$ and $A^c = U \setminus A$ are finite.
9. Every element of $U$ is in $A$ or in $A^c$, and no element is in both. So $U$ is the disjoint union of $A$ and $A^c$.
10. By the rule of sum, $|U| = |A| + |A^c|$. Hence $|A^c| = |U| - |A|$.

## Idea

The set $U$ splits into the part inside $A$ and the part outside $A$, with no overlap.
So the two sizes add up to $|U|$, and the size of the outside part is a difference.
The only extra work is to check that both parts are finite.
