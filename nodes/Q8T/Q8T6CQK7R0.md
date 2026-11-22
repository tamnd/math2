---
tag: Q8T6CQK7R0
kind: proof
name: Proof that a basis is a maximal independent and a minimal spanning set
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: AP9TD7QF51
methods: [TFQ1845T84, 0J0XBKG64S]
uses: [0VTQTPQGAV, 0EVHJFTG9Z, 0BJKVF90Z6, H75GS7QVPB]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Properties
  - book: isbn:9780134860244
    locator: Section 1.7
---

## Proof

We prove that condition 1 implies each of conditions 2 and 3, and that each of them implies condition 1.
Every step uses only finite combinations, and the facts we use are those of the [[linear dependence lemma|H75GS7QVPB]], proved here in the form we need.

1. (1 implies 2) Let $B$ be a [[basis|0VTQTPQGAV]], and let $v \in V \setminus B$. Since $B$ [[spans|0BJKVF90Z6]] $V$, there are distinct $b_1, \dots, b_k \in B$ and scalars $a_j$ with $v = a_1 b_1 + \dots + a_k b_k$.
2. Then $1 \cdot v - a_1 b_1 - \dots - a_k b_k = 0$ is a relation among distinct vectors of $B \cup \{v\}$, since $v \notin B$, and the coefficient of $v$ is $1 \ne 0$. So $B \cup \{v\}$ is [[linearly dependent|0EVHJFTG9Z]]. Since $B$ is independent, $B$ is a maximal independent set.
3. (2 implies 1) Let $B$ be a maximal independent set. Suppose, for a contradiction, that some $v \in V$ is not in the span of $B$. Then $v \notin B$.
4. Let $c v + c_1 b_1 + \dots + c_k b_k = 0$ with distinct $b_j \in B$. If $c \ne 0$, then $v = -c^{-1}(c_1 b_1 + \dots + c_k b_k)$ lies in the span of $B$, which is false. So $c = 0$.
5. Then $c_1 b_1 + \dots + c_k b_k = 0$, and the independence of $B$ gives $c_j = 0$ for all $j$. So $B \cup \{v\}$ is independent, which contradicts maximality. Hence $B$ spans $V$, and $B$ is a basis.
6. (1 implies 3) Let $B$ be a basis, and let $b \in B$. Suppose, for a contradiction, that $B \setminus \{b\}$ spans $V$. Then $b = a_1 b_1 + \dots + a_k b_k$ with distinct $b_j \in B \setminus \{b\}$.
7. So $1 \cdot b - a_1 b_1 - \dots - a_k b_k = 0$ is a nontrivial relation among distinct vectors of $B$, which contradicts the independence of $B$. Hence $B$ is a minimal spanning set.
8. (3 implies 1) Let $B$ be a minimal spanning set. Suppose, for a contradiction, that $B$ is dependent, so $c_1 b_1 + \dots + c_k b_k = 0$ with distinct $b_j \in B$ and some $c_m \ne 0$.
9. Dividing by $c_m$, which is possible because $F$ is a field, gives $b_m = -c_m^{-1} \sum_{j \ne m} c_j b_j$. So $b_m$ lies in the span $W$ of $B \setminus \{b_m\}$.
10. The subspace $W$ then contains every vector of $B$, so it contains the span of $B$, which is $V$. So $B \setminus \{b_m\}$ spans $V$, which contradicts minimality. Hence $B$ is independent, and $B$ is a basis.

## Idea

Two moves drive the proof.
A vector outside the span can always be added to an independent set without creating a relation, and a vector inside the span of the others can always be removed from a spanning set without losing anything.
So an independent set that cannot grow already spans, and a spanning set that cannot shrink is already independent.
The only place where the field matters is step 9, where we divide by a nonzero coefficient.

## Variants

A shorter write-up quotes the linear dependence lemma instead of proving its parts again.
Steps 1, 2, 6, 7, 8, 9 and 10 use the fact that a set is dependent exactly when one of its vectors lies in the span of the others, and that removing such a vector does not change the span.
Steps 3 to 5 use the fact that adding a vector outside the span of an independent set keeps it independent.
With these two facts quoted, each of the four implications takes one or two lines.
