---
tag: N64R1MGDBN
kind: topic
name: Back-and-forth methods and Ehrenfeucht-Fraïssé games
msc: ["03C07", "03C75"]
topics: [F3AXVABC35]
---

## Summary

This topic is a part of [[model theory|F3AXVABC35]].
It studies when two structures look alike, by building matchings of finitely many elements that can always be extended in both directions.
For countable structures the [[back-and-forth method|~61b06888]] turns such matchings into an isomorphism.
In general they form a [[back-and-forth system|~95b1c1d3]], which is exactly agreement on the infinitary logic $L_{\infty\omega}$, by [[Karp's theorem|~ca02717b]].
With a bound of $n$ steps one gets the [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]], which matches agreement on first-order sentences of [[quantifier rank|~e5a7f04b]] at most $n$.
The games are the standard way to prove that a property is not first-order definable, also on finite structures.

## Remarks

### Reading order

1. [[Back-and-forth method|~61b06888]]: Cantor's zig-zag proof that countable dense orders without endpoints are isomorphic.
2. [[Back-and-forth system|~95b1c1d3]]: the extension properties alone, for structures of any size.
3. [[Quantifier rank|~e5a7f04b]]: the depth of nested quantifiers, which measures first-order sentences.
4. [[Ehrenfeucht-Fraïssé game|2RE7YAZK8R]]: Spoiler and Duplicator play $n$ rounds on two structures.
5. [[Ehrenfeucht-Fraïssé theorem|~9f527b73]]: Duplicator wins $n$ rounds exactly when the structures agree up to rank $n$.
6. [[Games on finite linear orders|~992acee7]]: orders with at least $2^n - 1$ elements agree up to rank $n$.
7. [[Karp's theorem|~ca02717b]]: back-and-forth systems match the infinitary logic $L_{\infty\omega}$.
8. [[Non-definability proofs by games|~51a6b3d5]]: how to show that even size, connectivity or Hamiltonicity is not first-order.

### Prerequisites

- [[Basic notions of model theory|AY09KYSW81]]: structures, isomorphisms, elementary equivalence and elementary embeddings.
- [[Structures, satisfaction and truth|NJDME6F845]]: formulas, sentences and the satisfaction relation.
- [[Completeness, compactness and interpolation|FBWW4J1XWG]]: the compactness theorem, used for comparison with the game method.
