---
tag: WXB40PTZNV
kind: proof
name: Proof of the finite dimension theorem by the Steinitz exchange lemma
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 0WK0Y8RH1M
methods: [0NTF6DMVAP, 0J0XBKG64S]
uses: [08ZDRN6H41, 0VTQTPQGAV, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/Steinitz_exchange_lemma
    locator: Statement
  - book: isbn:9783031410253
    locator: Section 2C
---

## Proof

We apply the exchange lemma twice, once in each direction, to two bases of $V$.
This proves part 1 of the theorem, and part 2 in the case where one of the two bases is finite.

1. Let $B = (b_1, \dots, b_n)$ be a finite basis of $V$, and let $C = (c_i)_{i \in I}$ be any basis of $V$.
2. Suppose, for a contradiction, that $I$ has more than $n$ elements, and choose $n + 1$ distinct indices $i_0, \dots, i_n \in I$.
3. A subfamily of an [[independent|0EVHJFTG9Z]] family is independent, so $c_{i_0}, \dots, c_{i_n}$ are independent. The vectors $b_1, \dots, b_n$ span $V$, because $B$ is a basis.
4. The [[Steinitz exchange lemma|08ZDRN6H41]] now gives $n + 1 \le n$, which is false. So $I$ is finite, with some number $m \le n$ of elements.
5. Number the basis $C$ as $c_1, \dots, c_m$. Since $C$ is a basis, it spans $V$, and since $B$ is a basis, it is independent.
6. The exchange lemma, with the independent list $B$ and the spanning list $C$, gives $n \le m$.
7. Steps 4 and 6 give $m = n$, so every basis of $V$ has exactly $n$ vectors.

## Idea

A basis has two properties at once: it is independent and it spans.
The exchange lemma says that an independent list is never longer than a spanning list.
Use the first basis as the spanning list and the second as the independent list, and then swap the roles.
Each size is at most the other, so the sizes are equal.
The only care needed is at the start, where the second basis might be infinite, and a finite piece of it already gives the contradiction.

## Variants

The [[proof by row reduction|2BVBSVQYMB]] replaces the exchange lemma by the fact that a homogeneous system with more unknowns than equations has a nonzero solution.
For two infinite bases, neither argument applies, and the [[proof by cardinal arithmetic|C6V1B2MC0X]] covers one basis by the finite supports of the other.
