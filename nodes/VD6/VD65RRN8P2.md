---
tag: VD65RRN8P2
kind: proof
name: Proof of the bijection principle
msc: [05A19]
proves: 0GV2573FP4
uses: [05099E1NMJ, 0SNQEF7Z53, 01VG2A0BHW, 01FPXMTBX1, 07EH4R3RVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Bijective_proof
    locator: lead section
---

## Proof

We compose bijections with the counting bijections in the definition of [[cardinality|05099E1NMJ]].

1. Let $n = |A|$. By definition, there is a [[bijection|0SNQEF7Z53]] $h : \set{1, \dots, n} \to A$.
2. Let $f : A \to B$ be a bijection. A composite of bijections is a bijection, since [[injections compose|01FPXMTBX1]] and [[surjections compose|07EH4R3RVQ]].
3. So $f \circ h : \set{1, \dots, n} \to B$ is a bijection. Thus $B$ has $n$ elements.
4. The number of elements of a finite set is unique, so $|B| = n = |A|$.
5. Conversely, let $|A| = |B| = n$. There are bijections $g : \set{1, \dots, n} \to A$ and $k : \set{1, \dots, n} \to B$.
6. A bijection [[has a two-sided inverse|01VG2A0BHW]], so $g^{-1} : A \to \set{1, \dots, n}$ exists and is a bijection.
7. By step 2, $k \circ g^{-1} : A \to B$ is a bijection. This proves the converse.

## Idea

Both directions pass through the standard set $\set{1, \dots, n}$.
A bijection with another set carries the numbering of one set over to the other.
