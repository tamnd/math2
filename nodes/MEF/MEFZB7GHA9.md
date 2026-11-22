---
tag: MEFZB7GHA9
kind: proof
name: Proof that every linearly independent set extends to a basis, by Zorn's lemma
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 0M4SXE5WW3
methods: [JZQVJ9XT63, 0J0XBKG64S]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We prove part 2 by taking, with [[Zorn's lemma|04RXTQA5ZA]], an independent set between $L$ and $S$ that cannot grow, and we get part 1 by putting $S = V$.
A subset of $V$ is [[linearly independent|0EVHJFTG9Z]] when every finite linear relation among distinct elements of it has all coefficients $0$.

1. Let $S \subseteq V$ span $V$ with $L \subseteq S$. Let $P$ be the set of linearly independent sets $K$ with $L \subseteq K \subseteq S$, with the [[partial order|011C29Q1S1]] given by inclusion.
2. By hypothesis $L \in P$, so $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $L$ is an [[upper bound|0H5J02P8S9]] of $Q$ in $P$. So let $Q$ be nonempty, and let $M$ be the union of the members of $Q$. Then $L \subseteq M \subseteq S$.
4. We show that $M$ is independent. Take distinct $v_1, \dots, v_k \in M$, with $k \ge 1$, and scalars with $a_1 v_1 + \dots + a_k v_k = 0$.
5. Each $v_r$ lies in some member $K_r$ of $Q$. These finitely many sets are totally ordered by inclusion, because $Q$ is a chain, so one of them, call it $K^*$, contains all the others.
6. So $v_1, \dots, v_k$ lie in the independent set $K^*$, and $a_1 = \dots = a_k = 0$. Hence $M \in P$, and $M$ is an upper bound of $Q$.
7. By steps 2 to 6, every chain in $P$ has an upper bound in $P$. So Zorn's lemma gives a [[maximal element|0TZEEFTNCC]] $B$ of $P$, and $B$ is independent with $L \subseteq B \subseteq S$.
8. We claim that $S \subseteq \operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. Suppose not, and let $s \in S$ with $s \notin \operatorname{span}(B)$. In particular $s \notin B$.
9. Take distinct $b_1, \dots, b_k \in B$ and scalars with $a s + a_1 b_1 + \dots + a_k b_k = 0$. If $a \ne 0$, then $s = -a^{-1}(a_1 b_1 + \dots + a_k b_k) \in \operatorname{span}(B)$, a contradiction. So $a = 0$.
10. Then $a_1 b_1 + \dots + a_k b_k = 0$, and all $a_r = 0$ because $B$ is independent. Every finite relation among distinct elements of $B \cup \{s\}$ has this form, so $B \cup \{s\}$ is independent.
11. Also $L \subseteq B \cup \{s\} \subseteq S$, so $B \cup \{s\} \in P$, and it is strictly larger than $B$. This contradicts the maximality of $B$, so $S \subseteq \operatorname{span}(B)$.
12. The span of $B$ is a subspace that contains $S$, so it contains $\operatorname{span}(S) = V$. Hence $B$ is a [[spanning set|0BJKVF90Z6]] of $V$, and $B$ is a [[basis|0VTQTPQGAV]] with $L \subseteq B \subseteq S$. This proves part 2.
13. For part 1, the set $S = V$ spans $V$ and contains $L$, so part 2 gives a basis $B$ with $L \subseteq B$.

## Idea

Look at all independent sets that lie between $L$ and $S$.
A union of a chain of such sets is again one of them, because a finite relation only involves finitely many vectors, and those already sit in one member of the chain.
So Zorn's lemma gives a set that cannot grow.
If it failed to build some vector of $S$, that vector could be added, so it builds all of $S$ and hence all of $V$.

## Variants

When $V$ has a finite spanning set, the [[proof by adding vectors|SS0XKV9TAN]] gives the same result with induction in place of Zorn's lemma.
With $L = \emptyset$ the argument is the proof that [[every spanning set contains a basis|KS6PP0BVSD]], and with $L = \emptyset$ and $S = V$ it is the proof that [[every vector space has a basis|YVM74DY0WD]].
