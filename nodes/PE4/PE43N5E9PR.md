---
tag: PE43N5E9PR
kind: proof
name: Proof structure of Buss's theorem by counting formulas
msc: ["03F20"]
topics: [CBAF7J051K]
audience: research
proves: VRX23FZV21
uses: [J2BAR09TPF, RJ571F7FF0, YAHHWZ7XRH]
methods: [0NTF6DMVAP, 1KVSS0KRZA]
sources:
  - url: https://en.wikipedia.org/wiki/Frege_system
    locator: lead section
---

## Proof

We write the double count of pigeon-hole pairs with formulas for binary sums, and we use a cited lemma that Frege proves the laws of these sums in polynomial size.
The cited lemma is due to Buss, and its proof is in his paper of 1987.
By [[Reckhow's theorem|YAHHWZ7XRH]], we may fix any [[Frege system|J2BAR09TPF]] over the connectives $\neg, \land, \lor$.
Let $x_{ij}$ say that pigeon $i$ sits in hole $j$, for $1 \le i \le n + 1$ and $1 \le j \le n$.

1. *Counting formulas.*
   For bits $y_1, \dots, y_k$, there are formulas $\mathrm{Count}(y_1, \dots, y_k)$ that compute the binary form of $y_1 + \dots + y_k$, with $\lceil \log_2 (k + 1) \rceil$ output bits.
   They use carry-save addition, which turns three binary numbers into two with formulas of constant depth.
   After $O(\log k)$ such layers two numbers remain, and one more addition finishes, so the formulas have depth $O(\log k)$ and size polynomial in $k$.
2. *Comparison formulas.*
   For two binary numbers given by formulas, there are formulas of polynomial size for $a = b$ and for $a \le b$.
3. *Cited lemma (Buss).*
   Frege proves, in size polynomial in $k$, the basic laws of these formulas.
   A sum does not depend on the order of its terms, a sum equals the sum of the sums of its blocks, and a sum of $k$ terms, each at most $1$, is at most $k$.
4. *Row sums.*
   For pigeon $i$, let $r_i = \sum_j x_{ij}$, written with counting formulas.
   From the pigeon clause $\{x_{i1}, \dots, x_{in}\}$, Frege derives $r_i \ge 1$ in polynomial size, by step 3.
5. *Column sums.*
   For hole $j$, let $c_j = \sum_i x_{ij}$.
   From the hole clauses $\{\neg x_{ij}, \neg x_{i'j}\}$, Frege derives $c_j \le 1$, since two true terms in column $j$ would falsify a hole clause.
6. *Total by rows.*
   By steps 3 and 4, Frege derives $\sum_i r_i \ge n + 1$, because there are $n + 1$ rows and each sum is at least $1$.
7. *Total by columns.*
   By steps 3 and 5, Frege derives $\sum_j c_j \le n$, because there are $n$ columns and each sum is at most $1$.
8. *Double counting.*
   Both totals are the sum of the same $n(n + 1)$ variables in two orders, so step 3 gives a polynomial-size Frege proof of $\sum_i r_i = \sum_j c_j$.
9. *Contradiction.*
   Steps 6, 7 and 8 give $n + 1 \le n$ for the fixed binary numerals $n$ and $n + 1$.
   This is a false comparison of constants, and Frege refutes it in polynomial size.
10. *Size.*
    Each step uses formulas of size polynomial in $n$ and a polynomial number of lines.
    So the derivation of a contradiction from $\mathrm{PHP}^{n+1}_n$, and with it the proof of $\neg \mathrm{PHP}^{n+1}_n$, has polynomial size.

$\blacksquare$

## Idea

The pigeonhole principle is a double count: the number of (pigeon, hole) pairs is at least $n + 1$ by rows and at most $n$ by columns.
A Frege line can be any formula, so it can hold a sum of many bits as a formula of logarithmic depth.
Buss's lemma says that the laws of addition for these formulas have short Frege proofs.
With that lemma in hand, the schoolbook argument becomes a polynomial-size Frege proof line by line.

## Variants

Cook and Reckhow's extended Frege proof of 1979 works by induction on $n$ instead.
From a map of $n + 1$ pigeons into $n$ holes, extension variables define a map of $n$ pigeons into $n - 1$ holes, and $n - 1$ such rounds reach $2$ pigeons and $1$ hole, which is refuted directly.
The counting formulas of Buss need depth that grows with $n$, so bounded-depth Frege cannot count in this way, and [[Ajtai's theorem|Q0ERK64J78]] shows that no other method works there either.
In [[cutting planes|40KJ0VKNG7]] the lines are linear inequalities, so the sums are written directly and the same double count works without counting formulas.
