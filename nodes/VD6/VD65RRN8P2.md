---
tag: VD65RRN8P2
kind: proof
name: Proof of the bijection principle
msc: ["05A19"]
topics: [GB14W4SYPK]
audience: ug1
proves: 0GV2573FP4
uses: [05099E1NMJ, 0SNQEF7Z53, 01VG2A0BHW, 01FPXMTBX1, 07EH4R3RVQ]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Bijective_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Cardinality
    locator: Finite cardinals
---

## Proof

We give a [[direct proof|0NTF6DMVAP]] of each direction, by composing with the numberings $\{1, \dots, n\} \to A$ that the definition of [[cardinality|05099E1NMJ]] provides.
Let $A$ and $B$ be finite sets.

First direction: a bijection gives equal sizes.

1. Let $n = |A|$.
   By the definition of cardinality, there is a [[bijection|0SNQEF7Z53]] $h : \{1, \dots, n\} \to A$.
2. Let $f : A \to B$ be a bijection.
3. The composite $f \circ h : \{1, \dots, n\} \to B$ is injective, because [[injections compose|01FPXMTBX1]].
   It is surjective, because [[surjections compose|07EH4R3RVQ]].
4. So $f \circ h$ is a bijection from $\{1, \dots, n\}$ to $B$, and by the definition of cardinality, $B$ has $n$ elements.
5. The cardinality of a finite set is well defined, so $|B| = n = |A|$.

Second direction: equal sizes give a bijection.

6. Let $|A| = |B| = n$.
   By the definition of cardinality, there are bijections $g : \{1, \dots, n\} \to A$ and $k : \{1, \dots, n\} \to B$.
7. A bijection [[has a two-sided inverse|01VG2A0BHW]], so $g^{-1} : A \to \{1, \dots, n\}$ exists.
   It is a bijection, because its inverse is $g$.
8. By the reasoning of step 3, applied to $g^{-1}$ and $k$, the composite $k \circ g^{-1} : A \to B$ is a bijection.
9. So there is a bijection from $A$ to $B$.
   Together with step 5, this proves that $|A| = |B|$ if and only if there is a bijection $A \to B$.

## Idea

Both directions pass through the standard set $\{1, \dots, n\}$.
A bijection carries a numbering of one set over to the other set.
In the second direction, the bijection $k \circ g^{-1}$ sends the element with number $i$ in $A$ to the element with number $i$ in $B$, like matching two queues of people place by place.

## Variants

The first direction also has a proof by induction on $|A|$.
Remove an element $a$ from $A$ and its image $f(a)$ from $B$.
The restriction of $f$ is a bijection $A \setminus \{a\} \to B \setminus \{f(a)\}$, and the induction hypothesis gives equal sizes for the smaller sets, so $|A| = |B|$.

The first direction also follows from two inequalities.
An injection $A \to B$ gives $|A| \le |B|$, and the injection $f^{-1} : B \to A$ gives $|B| \le |A|$.

In Lean with Mathlib, the first direction is `Fintype.card_congr`, which takes an equivalence of finite types.
