---
tag: YVM74DY0WD
kind: proof
name: Proof that every vector space has a basis, by Zorn's lemma
msc: [15A03, "03E25"]
proves: 00MS9VMQ9Z
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We apply [[Zorn's lemma|04RXTQA5ZA]] to the linearly independent subsets of $V$. A subset is [[linearly independent|0EVHJFTG9Z]] when it is so as a family indexed by itself.

1. Let $P$ be the set of linearly independent subsets of $V$. Order $P$ by inclusion. This is a [[partial order|011C29Q1S1]].
2. The empty set is linearly independent, since it has no nontrivial linear combination. So $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $\emptyset \in P$ is an [[upper bound|0H5J02P8S9]] of $Q$.
4. Let $Q$ be nonempty, and let $M = \bigcup_{L \in Q} L$. Take distinct $v_1, \dots, v_k \in M$ and $a_1, \dots, a_k \in F$ with $a_1 v_1 + \cdots + a_k v_k = 0$.
5. If $k = 0$, there is nothing to show. Otherwise each $v_r$ lies in some $L_r \in Q$. The sets $L_1, \dots, L_k$ are totally ordered by inclusion, so one of them, say $L^*$, contains all the others.
6. Then $v_1, \dots, v_k \in L^*$, and $L^*$ is linearly independent. So $a_1 = \cdots = a_k = 0$.
7. By steps 4 to 6, $M$ is linearly independent, so $M \in P$. It contains each $L \in Q$, so it is an upper bound of $Q$.
8. By steps 2, 3 and 7, Zorn's lemma applies. So $P$ has a [[maximal element|0TZEEFTNCC]] $B$.
9. We show that $B$ spans $V$. Suppose that some $v \in V$ is not in $\operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. Then $v \notin B$.
10. Take distinct $b_1, \dots, b_k \in B$ and $a, a_1, \dots, a_k \in F$ with $av + a_1 b_1 + \cdots + a_k b_k = 0$.
11. If $a \ne 0$, then $v = -a^{-1}(a_1 b_1 + \cdots + a_k b_k) \in \operatorname{span}(B)$. This contradicts step 9, so $a = 0$.
12. Then $a_1 b_1 + \cdots + a_k b_k = 0$, so $a_1 = \cdots = a_k = 0$, because $B$ is linearly independent.
13. Each finite subset of $B \cup \set{v}$ has the form of step 10, possibly with the term $av$ absent. So $B \cup \set{v}$ is linearly independent, by steps 11 and 12.
14. Thus $B \cup \set{v} \in P$, and it is strictly larger than $B$. This contradicts the maximality of $B$.
15. So $\operatorname{span}(B) = V$, and $B$ is a [[spanning set|0BJKVF90Z6]] of $V$. Being also linearly independent, $B$ is a [[basis|0VTQTPQGAV]] of $V$.

## Idea

A basis is a linearly independent set that cannot be enlarged. Zorn's lemma gives such a maximal set, because the union of a chain of independent sets is still independent. If the maximal set missed a vector of $V$, adding that vector would keep it independent, which is impossible.
