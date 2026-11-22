---
tag: 3AMPZ016SQ
kind: proof
name: Proof of the equivalent conditions for finite dimension
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: HW9HN5A5HJ
methods: [TFQ1845T84, 0NTF6DMVAP]
uses: [H75GS7QVPB, 08ZDRN6H41, AP9TD7QF51, 059THXBRBB, 018W3V3TCT]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
  - book: isbn:9783031410253
    locator: Section 2B
---

## Proof

We prove the cycle of implications 1 to 2, 2 to 3, 3 to 2, 2 to 4 and 4 to 1, which together show that all four conditions are equivalent.

1. (1 implies 2.) Let $w_1, \dots, w_n$ span $V$. If this list is dependent, the [[dependence lemma|H75GS7QVPB]] gives a vector in it that is a combination of the others, and removing that vector does not change the span.
2. We repeat step 1 as long as the list is dependent. The list gets shorter each time, so after at most $n$ removals it is independent, and it still spans $V$. So it is a finite basis.
3. (2 implies 3.) Let $b_1, \dots, b_N$ be a finite basis. It spans $V$, so the [[Steinitz exchange lemma|08ZDRN6H41]] shows that every independent family in $V$ has at most $N$ vectors.
4. (3 implies 2.) The empty family is independent, and by condition 3 the sizes of independent families are at most $N$. So we may choose an independent family $B$ whose size $k \le N$ is as large as possible.
5. For every $v \in V$, the family $B$ with $v$ added has $k + 1$ vectors, so it is dependent by the choice of $k$. Hence $B$ is a maximal independent family.
6. A maximal independent family is a basis, by [[the characterization of bases|AP9TD7QF51]]. So $B$ is a finite basis.
7. (2 implies 4.) Let $B = (b_1, \dots, b_n)$ be a finite basis. The coordinate map $v \mapsto [v]_B$ is a linear isomorphism $V \to F^n$, by the [[isomorphism with the coordinate space|059THXBRBB]].
8. (4 implies 1.) Let $\varphi \colon F^n \to V$ be a linear isomorphism, and let $v \in V$. Write $\varphi^{-1}(v) = \sum_i a_i e_i$ in the standard basis. Since $\varphi$ is linear,
$$v = \varphi\Bigl(\sum_{i=1}^{n} a_i e_i\Bigr) = \sum_{i=1}^{n} a_i \varphi(e_i).$$
9. So the $n$ vectors $\varphi(e_1), \dots, \varphi(e_n)$ span $V$, and $V$ is [[finite-dimensional|018W3V3TCT]].

## Idea

The proof moves between spanning lists and independent lists.
A finite spanning list shrinks to a basis when we throw out vectors that the others already build.
The exchange lemma bounds every independent list by the length of a spanning list.
In the other direction, an independent list of the largest possible length has no room for one more vector, so it already spans.
Coordinates then give the isomorphism with $F^n$, and an isomorphism carries the standard basis to a spanning list.

## Variants

The step from 3 to 2 can also be done by building a basis one vector at a time.
Start with the empty list, and while the list does not span $V$, add a vector outside its span; by the dependence lemma the list stays independent.
By condition 3 this stops after at most $N$ steps, and then the list is an independent spanning list, that is, a basis.
