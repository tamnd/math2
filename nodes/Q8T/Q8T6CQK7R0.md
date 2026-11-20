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

We use the [[dependence lemma|H75GS7QVPB]], which holds for infinite sets because each relation involves finitely many vectors.

1. (1 implies 2) Let $B$ be a basis, and let $v \in V \setminus B$. Since $B$ spans, $v \in \operatorname{span}(B)$.
2. So $v$ is a combination of the other vectors of $B \cup \set{v}$, and $B \cup \set{v}$ is dependent by part 3 of the dependence lemma. Also $B$ is independent, so $B$ is maximal.
3. (2 implies 1) Let $B$ be maximal independent. We show that $B$ spans. Suppose, for a contradiction, that some $v \in V$ is not in $\operatorname{span}(B)$.
4. Then $v \notin B$, and by part 4 of the dependence lemma, $B \cup \set{v}$ is independent. This contradicts maximality. So $B$ spans and is a basis.
5. (1 implies 3) Let $B$ be a basis, and let $b \in B$. Suppose, for a contradiction, that $B \setminus \set{b}$ spans $V$.
6. Then $b$ is a combination of $B \setminus \set{b}$, so $B$ is dependent by part 3 of the dependence lemma. This contradicts independence of $B$. So $B$ is minimal spanning.
7. (3 implies 1) Let $B$ be minimal spanning. Suppose, for a contradiction, that $B$ is dependent.
8. By part 3 of the dependence lemma, some $b \in B$ is a combination of finitely many vectors of $B \setminus \set{b}$, so $b \in \operatorname{span}(B \setminus \set{b})$.
9. By part 2 of the dependence lemma, $\operatorname{span}(B \setminus \set{b}) = \operatorname{span}(B) = V$. This contradicts minimality. So $B$ is independent and is a basis.

## Idea

A vector outside the span can always be added to an independent set, and a redundant vector can always be removed from a spanning set.
So an independent set that cannot grow spans, and a spanning set that cannot shrink is independent.
