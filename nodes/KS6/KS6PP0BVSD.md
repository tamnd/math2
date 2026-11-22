---
tag: KS6PP0BVSD
kind: proof
name: Proof that every spanning set contains a basis, by Zorn's lemma
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 06MRNP4BNT
methods: [JZQVJ9XT63, 0J0XBKG64S]
uses: [0VTQTPQGAV, 0BJKVF90Z6, 0EVHJFTG9Z, 0HR573CHNM, 0EPTJA5QV4, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We take a largest independent subset of $S$, which [[Zorn's lemma|04RXTQA5ZA]] provides, and show that it spans $V$.
A subset of $V$ is [[linearly independent|0EVHJFTG9Z]] when every finite linear relation among distinct elements of it has all coefficients $0$.

1. Let $P$ be the set of linearly independent subsets of $S$, with the [[partial order|011C29Q1S1]] given by inclusion.
2. The empty set is linearly independent and is a subset of $S$, so $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $\emptyset$ is an [[upper bound|0H5J02P8S9]] of $Q$ in $P$. So let $Q$ be nonempty, and let $M$ be the union of all members of $Q$. Then $M \subseteq S$.
4. We show that $M$ is independent. Take distinct $v_1, \dots, v_k \in M$, with $k \ge 1$, and scalars with $a_1 v_1 + \dots + a_k v_k = 0$.
5. Each $v_r$ lies in some member $L_r$ of $Q$. These finitely many sets are totally ordered by inclusion, because $Q$ is a chain, so one of them, call it $L^*$, contains all the others.
6. So $v_1, \dots, v_k$ all lie in $L^*$, which is independent. Hence $a_1 = \dots = a_k = 0$, and $M$ is independent.
7. By steps 3 to 6, $M \in P$, and $M$ contains every member of $Q$. So every chain in $P$ has an upper bound in $P$.
8. By steps 2 and 7, Zorn's lemma gives a [[maximal element|0TZEEFTNCC]] $B$ of $P$. So $B \subseteq S$, and $B$ is linearly independent.
9. We claim that $S \subseteq \operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. Suppose not, and let $s \in S$ with $s \notin \operatorname{span}(B)$. In particular $s \notin B$.
10. Take distinct $b_1, \dots, b_k \in B$ and scalars with $a s + a_1 b_1 + \dots + a_k b_k = 0$. If $a \ne 0$, then $s = -a^{-1}(a_1 b_1 + \dots + a_k b_k)$ lies in $\operatorname{span}(B)$, which contradicts step 9. So $a = 0$.
11. Then $a_1 b_1 + \dots + a_k b_k = 0$, and all $a_r = 0$ because $B$ is independent. Every finite relation among distinct elements of $B \cup \{s\}$ has this form, so $B \cup \{s\}$ is independent.
12. The set $B \cup \{s\}$ lies in $S$, so it belongs to $P$, and it is strictly larger than $B$. This contradicts the maximality of $B$, so the claim of step 9 holds.
13. The span of $B$ is a [[linear subspace|0EPTJA5QV4]] of $V$ that contains $S$, so it contains every linear combination of elements of $S$. Since $S$ is a [[spanning set|0BJKVF90Z6]], this gives $V = \operatorname{span}(S) \subseteq \operatorname{span}(B)$.
14. So $B \subseteq S$ is linearly independent and spans $V$, which means that $B$ is a [[basis|0VTQTPQGAV]] of $V$ contained in $S$.

## Idea

Among the independent subsets of $S$, take one that cannot grow inside $S$.
Zorn's lemma supplies such a set, because a union of a chain of independent sets is again independent: any finite relation already lives in one member of the chain.
If some vector of $S$ were outside the span of this set, we could add that vector and keep independence, which the maximality forbids.
So the set spans everything that $S$ spans, and that is $V$.

## Variants

For a finite set $S$ there is a [[proof by removal|GJKC4QQWAW]] that uses induction in place of Zorn's lemma.
The same argument with the extra condition $L \subseteq K$ on the members $K$ of $P$ proves the [[extension theorem|0M4SXE5WW3]], and with $S = V$ it proves that [[every vector space has a basis|00MS9VMQ9Z]].
One can also replace Zorn's lemma by a well-ordering of $S$: run through $S$ in that order and keep each vector that lies outside the span of the vectors kept so far.
