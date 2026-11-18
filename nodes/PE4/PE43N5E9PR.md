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

This page gives the structure of Buss's proof step by step.
The cited lemma is Buss's lemma that the counting formulas below have polynomial-size Frege proofs of their basic properties; its proof is in Buss's paper of 1987.
By [[Reckhow's theorem|YAHHWZ7XRH]], we may fix any Frege system with the connectives $\neg, \land, \lor$.

1. *Counting formulas.* For bits $y_1, \dots, y_k$, define formulas $\mathrm{Count}(y_1, \dots, y_k)$ that compute the binary representation of $y_1 + \cdots + y_k$, with $\lceil \log_2(k+1) \rceil$ output bits. They are built by *carry-save addition*: three numbers are reduced to two numbers in one layer of constant depth, and $O(\log k)$ layers reduce $k$ numbers to two, which are added at the end. The resulting formulas have depth $O(\log k)$ and size polynomial in $k$.
2. *Formulas for comparison.* For two binary numbers given by formulas, there are formulas of polynomial size for $a = b$ and $a \le b$.
3. *Cited lemma (Buss).* Frege proves, in size polynomial in $k$, the basic properties of these formulas: the sum of a sequence does not depend on the order of the terms; the sum of a sequence is the sum of the sums of its blocks; changing one term from $0$ to $1$ adds $1$; a sum of $k$ terms each at most $1$ is at most $k$.
4. *Row sums.* For pigeon $i$, let $r_i = \sum_j x_{ij}$, given by counting formulas. From the pigeon clause $P_i$, Frege derives $r_i \ge 1$ in polynomial size, by step 3.
5. *Column sums.* For hole $j$, let $c_j = \sum_i x_{ij}$. From the hole clauses $H_{i i' j}$, Frege derives $c_j \le 1$: if two pigeons sat in hole $j$, a hole clause would fail.
6. *Total from the rows.* By steps 3 and 4, Frege derives $\sum_i r_i \ge n + 1$, since there are $n + 1$ rows and each sum is at least $1$.
7. *Total from the columns.* By steps 3 and 5, Frege derives $\sum_j c_j \le n$.
8. *Double counting.* Both totals are the sum of all $n(n+1)$ variables $x_{ij}$, in two orders. Step 3 gives a polynomial-size Frege proof of $\sum_i r_i = \sum_j c_j$.
9. *Contradiction.* Steps 6, 7 and 8 give $n + 1 \le n$, which is false for the fixed binary numbers $n$ and $n + 1$; Frege refutes it in polynomial size.
10. *Size.* Each step uses formulas of size polynomial in $n$ and a polynomial number of lines. So the whole derivation of a contradiction from $\mathrm{PHP}^{n+1}_n$, and hence the proof of $\neg \mathrm{PHP}^{n+1}_n$, has polynomial size. $\blacksquare$

## Idea

The pigeonhole principle is double counting: the total number of (pigeon, hole) pairs is at least $n + 1$ by rows and at most $n$ by columns.
Frege systems can express sums of many bits as formulas of logarithmic depth, and they can prove the laws of addition for these formulas in polynomial size.
So the counting argument becomes a polynomial-size Frege proof.

## Variants

- *Extended Frege.* Cook and Reckhow's proof of 1979 works by induction on $n$. From a map of $n + 1$ pigeons into $n$ holes, extension variables define a map of $n$ pigeons into $n - 1$ holes, and $n$ rounds reach the case $n = 1$.
- *Bounded depth.* The counting formulas need depth growing with $n$. Bounded-depth Frege cannot count in this way, and [[Ajtai's theorem|Q0ERK64J78]] shows that no other method works either.
- *Cutting planes.* In [[cutting planes|40KJ0VKNG7]], lines are linear inequalities, and the sums are written directly; so the same double counting works without counting formulas.
