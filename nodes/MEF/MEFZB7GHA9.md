---
tag: MEFZB7GHA9
kind: proof
name: Proof that every linearly independent set extends to a basis, by Zorn's lemma
msc: [15A03]
proves: 0M4SXE5WW3
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We apply [[Zorn's lemma|04RXTQA5ZA]] to the linearly independent subsets of $V$ that contain $L$. A subset is [[linearly independent|0EVHJFTG9Z]] when it is so as a family indexed by itself.

1. Let $P$ be the set of linearly independent subsets $K \subseteq V$ with $L \subseteq K$. Inclusion is a [[partial order|011C29Q1S1]] on $P$.
2. By hypothesis, $L \in P$. So $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $L$ is an [[upper bound|0H5J02P8S9]] of $Q$ in $P$.
4. Let $Q$ be nonempty, and let $M = \bigcup_{K \in Q} K$. Then $L \subseteq M$. Take distinct $v_1, \dots, v_k \in M$ and $a_1, \dots, a_k \in F$ with $a_1 v_1 + \cdots + a_k v_k = 0$.
5. If $k = 0$, there is nothing to show. Otherwise each $v_r$ lies in some $K_r \in Q$. The sets $K_1, \dots, K_k$ are totally ordered by inclusion, so one of them, say $K^*$, contains all the others.
6. Then $v_1, \dots, v_k \in K^*$, and $K^*$ is linearly independent. So $a_1 = \cdots = a_k = 0$.
7. So $M$ is linearly independent, and $M \in P$. It contains each $K \in Q$, so it is an upper bound of $Q$.
8. By steps 2, 3 and 7, Zorn's lemma gives a [[maximal element|0TZEEFTNCC]] $B$ of $P$. So $B$ is linearly independent and $L \subseteq B$.
9. We show that $B$ spans $V$. Suppose that some $v \in V$ is not in $\operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. Then $v \notin B$.
10. Take distinct $b_1, \dots, b_k \in B$ and $a, a_1, \dots, a_k \in F$ with $av + a_1 b_1 + \cdots + a_k b_k = 0$.
11. If $a \ne 0$, then $v = -a^{-1}(a_1 b_1 + \cdots + a_k b_k) \in \operatorname{span}(B)$, a contradiction. So $a = 0$.
12. Then $a_1 b_1 + \cdots + a_k b_k = 0$, so all $a_r = 0$, because $B$ is linearly independent.
13. By steps 10 to 12, $B \cup \set{v}$ is linearly independent, and it contains $L$. So it lies in $P$ and is strictly larger than $B$. This contradicts the maximality of $B$.
14. So $B$ is a [[spanning set|0BJKVF90Z6]] of $V$. Being linearly independent, $B$ is a [[basis|0VTQTPQGAV]] of $V$ with $L \subseteq B$.

## Idea

Among the independent sets that contain $L$, Zorn's lemma gives one that cannot be enlarged. If it missed some vector of $V$ in its span, that vector could be added without losing independence. So the maximal set spans $V$, and it is a basis that contains $L$.
