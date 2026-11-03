---
tag: KS6PP0BVSD
kind: proof
name: Proof that every spanning set contains a basis, by Zorn's lemma
msc: [15A03]
proves: 06MRNP4BNT
uses: [0VTQTPQGAV, 0BJKVF90Z6, 0EVHJFTG9Z, 0HR573CHNM, 0EPTJA5QV4, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We apply [[Zorn's lemma|04RXTQA5ZA]] to the linearly independent subsets of $S$. A subset is [[linearly independent|0EVHJFTG9Z]] when it is so as a family indexed by itself.

1. Let $P$ be the set of linearly independent subsets of $S$, with the [[partial order|011C29Q1S1]] given by inclusion.
2. The empty set is linearly independent and lies in $S$. So $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $\emptyset$ is an [[upper bound|0H5J02P8S9]] of $Q$ in $P$.
4. Let $Q$ be nonempty, and let $M = \bigcup_{L \in Q} L$. Then $M \subseteq S$. Take distinct $v_1, \dots, v_k \in M$ and $a_1, \dots, a_k \in F$ with $a_1 v_1 + \cdots + a_k v_k = 0$.
5. If $k = 0$, there is nothing to show. Otherwise each $v_r$ lies in some $L_r \in Q$. The sets $L_1, \dots, L_k$ are totally ordered by inclusion, so one of them, say $L^*$, contains all the others.
6. Then $v_1, \dots, v_k \in L^*$, and $L^*$ is linearly independent. So $a_1 = \cdots = a_k = 0$.
7. So $M$ is linearly independent, and $M \in P$. It contains each $L \in Q$, so it is an upper bound of $Q$.
8. By steps 2, 3 and 7, Zorn's lemma gives a [[maximal element|0TZEEFTNCC]] $B$ of $P$. So $B \subseteq S$ and $B$ is linearly independent.
9. We claim that $S \subseteq \operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. Suppose that some $s \in S$ is not in $\operatorname{span}(B)$. Then $s \notin B$.
10. Take distinct $b_1, \dots, b_k \in B$ and $a, a_1, \dots, a_k \in F$ with $as + a_1 b_1 + \cdots + a_k b_k = 0$.
11. If $a \ne 0$, then $s = -a^{-1}(a_1 b_1 + \cdots + a_k b_k) \in \operatorname{span}(B)$, a contradiction. So $a = 0$.
12. Then $a_1 b_1 + \cdots + a_k b_k = 0$, so all $a_r = 0$, because $B$ is linearly independent.
13. By steps 10 to 12, $B \cup \set{s}$ is linearly independent. It lies in $S$, so it is in $P$, and it is strictly larger than $B$. This contradicts the maximality of $B$.
14. So $S \subseteq \operatorname{span}(B)$. The span of $B$ is a [[linear subspace|0EPTJA5QV4]] of $V$, so it contains every linear combination of vectors of $S$.
15. Hence $V = \operatorname{span}(S) \subseteq \operatorname{span}(B) \subseteq V$, since $S$ is a [[spanning set|0BJKVF90Z6]]. So $B$ spans $V$.
16. Thus $B \subseteq S$ is linearly independent and spans $V$. So $B$ is a [[basis|0VTQTPQGAV]] of $V$.

## Idea

Take an independent subset of $S$ that cannot be enlarged inside $S$; Zorn's lemma provides one. Every vector of $S$ is then a combination of this subset, or else it could be added. So the subset spans everything that $S$ spans, which is $V$.
