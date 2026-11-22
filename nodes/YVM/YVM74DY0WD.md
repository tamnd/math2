---
tag: YVM74DY0WD
kind: proof
name: Proof that every vector space has a basis, by Zorn's lemma
msc: ["15A03", "03E25"]
topics: [MVH97H8B2J]
audience: ug1
proves: 00MS9VMQ9Z
methods: [JZQVJ9XT63, 0J0XBKG64S]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, 0HR573CHNM, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Proof that every vector space has a basis
---

## Proof

We use [[Zorn's lemma|04RXTQA5ZA]] to get an independent set that cannot be enlarged, and we show that such a set spans $V$.
A subset of $V$ is [[linearly independent|0EVHJFTG9Z]] when every finite linear relation among distinct elements of it has all coefficients $0$.

1. Let $P$ be the set of linearly independent subsets of $V$, with the [[partial order|011C29Q1S1]] given by inclusion.
2. The empty set is linearly independent, because it has no nontrivial linear relation. So $P$ is nonempty.
3. Let $Q \subseteq P$ be a [[chain|0GP9ASVQ1X]]. If $Q$ is empty, then $\emptyset$ is an [[upper bound|0H5J02P8S9]] of $Q$ in $P$. So let $Q$ be nonempty, and let $M$ be the union of the members of $Q$.
4. We show that $M$ is independent. Take distinct $v_1, \dots, v_k \in M$, with $k \ge 1$, and scalars with $a_1 v_1 + \dots + a_k v_k = 0$.
5. Each $v_r$ lies in some member $L_r$ of $Q$. These finitely many sets are totally ordered by inclusion, because $Q$ is a chain, so one of them, call it $L^*$, contains all the others.
6. So $v_1, \dots, v_k$ lie in the independent set $L^*$, and $a_1 = \dots = a_k = 0$. Hence $M \in P$, and $M$ is an upper bound of $Q$.
7. By steps 2 to 6, every chain in $P$ has an upper bound in $P$. So Zorn's lemma gives a [[maximal element|0TZEEFTNCC]] $B$ of $P$.
8. We show that $B$ spans $V$. Suppose not, and let $v \in V$ lie outside $\operatorname{span}(B)$, the [[linear span|0HR573CHNM]] of $B$. In particular $v \notin B$.
9. Take distinct $b_1, \dots, b_k \in B$ and scalars with $a v + a_1 b_1 + \dots + a_k b_k = 0$. If $a \ne 0$, then $v = -a^{-1}(a_1 b_1 + \dots + a_k b_k) \in \operatorname{span}(B)$, which contradicts step 8. So $a = 0$.
10. Then $a_1 b_1 + \dots + a_k b_k = 0$, and all $a_r = 0$ because $B$ is independent.
11. Every finite relation among distinct elements of $B \cup \{v\}$ has the form of step 9, with the term $a v$ possibly absent. By steps 9 and 10, all its coefficients are $0$, so $B \cup \{v\}$ is independent.
12. So $B \cup \{v\} \in P$, and it is strictly larger than $B$. This contradicts the maximality of $B$.
13. Hence $\operatorname{span}(B) = V$, and $B$ is a [[spanning set|0BJKVF90Z6]] of $V$. Since $B$ is also independent, it is a [[basis|0VTQTPQGAV]] of $V$.

## Idea

A basis is the same as an independent set that cannot be enlarged: if some vector were outside its span, we could add that vector and stay independent.
So it is enough to find a maximal independent set.
Zorn's lemma finds one, because the union of a chain of independent sets is independent: a relation uses finitely many vectors, and those already lie in a single member of the chain.
The step that divides by $a \ne 0$ is where we use that $F$ is a field.

## Variants

With a well-ordering of $V$ in place of Zorn's lemma, run through $V$ in order and keep each vector that lies outside the span of the vectors kept so far, by transfinite recursion.
The kept vectors are independent, because in any relation the latest of them is outside the span of the earlier ones, and every vector of $V$ is either kept or in the span of earlier kept vectors.
This is how Hamel built a basis of $\mathbb{R}$ over $\mathbb{Q}$.
The same argument with sets between $L$ and $S$ proves the extension theorem, as in [[its proof by Zorn's lemma|MEFZB7GHA9]], and that theorem contains this theorem as the case $L = \emptyset$ and $S = V$.
