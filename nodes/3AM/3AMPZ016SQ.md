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

We prove 1 implies 2, 2 implies 3, 3 implies 2, 2 implies 4, and 4 implies 1.

1. (1 implies 2) Let $w_1, \dots, w_n$ span $V$. If the list is dependent, then by parts 1 and 2 of the [[dependence lemma|H75GS7QVPB]], we can remove one vector and keep the span.
2. Repeat step 1. The list gets shorter at each step, so after at most $n$ steps it is independent, and it still spans $V$. So it is a finite basis.
3. (2 implies 3) Let $b_1, \dots, b_N$ be a basis. It spans $V$, so by the [[Steinitz exchange lemma|08ZDRN6H41]], each independent family has at most $N$ vectors.
4. (3 implies 2) The empty family is independent, so some independent family exists. The sizes of independent families are bounded by $N$, so choose an independent family $B$ of largest size $k \le N$.
5. For $v \in V$ not in $B$, the family $B$ with $v$ added has $k + 1$ vectors, so it is dependent, by the choice of $k$. So $B$ is a maximal independent set.
6. By [[the characterization of bases|AP9TD7QF51]], $B$ is a basis, and it is finite.
7. (2 implies 4) For a finite basis $B = (b_1, \dots, b_n)$, the coordinate map $v \mapsto [v]_B$ is an isomorphism $V \to F^n$, by [[isomorphism with the coordinate space|059THXBRBB]].
8. (4 implies 1) Let $\varphi \colon F^n \to V$ be an isomorphism. For $v \in V$, write $\varphi^{-1}(v) = \sum_i a_i e_i$. Then $v = \sum_i a_i \varphi(e_i)$, by linearity.
9. So $\varphi(e_1), \dots, \varphi(e_n)$ is a finite spanning set, and $V$ is [[finite-dimensional|018W3V3TCT]].

## Idea

Shrinking a finite spanning list gives a finite basis, and the Steinitz lemma bounds independent lists by its size.
An independent list of largest size cannot be extended, so it is a basis.
