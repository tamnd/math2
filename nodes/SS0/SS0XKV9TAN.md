---
tag: SS0XKV9TAN
kind: proof
name: Proof that an independent set extends to a basis, in finite dimension
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
proves: 0M4SXE5WW3
methods: [0ASJVEFA9J, X5HG1RNWQX]
uses: [H75GS7QVPB, 08ZDRN6H41, 0VTQTPQGAV, 0BJKVF90Z6]
sources:
  - book: isbn:9783031410253
    locator: Section 2B
---

## Proof

We add vectors of $S$ that lie outside the current span, one at a time, and the Steinitz bound makes the process stop.
This proof covers a space $V$ that has a finite spanning list $w_1, \dots, w_m$, and the [[proof by Zorn's lemma|MEFZB7GHA9]] covers the general case.

1. Every finite subset of $L$ is an independent list, so by the [[Steinitz exchange lemma|08ZDRN6H41]] it has at most $m$ elements. Hence $L$ is finite and $\abs{L} \le m$.
2. Part 1 follows from part 2. Indeed, $S = L \cup \{w_1, \dots, w_m\}$ contains a spanning list, so it [[spans|0BJKVF90Z6]] $V$, and it contains $L$.
3. For part 2, let $S \supseteq L$ span $V$. We use induction on $d = m - \abs{L}$, which is at least $0$ by step 1, and we assume part 2 for every independent set $L' \subseteq S$ with $m - \abs{L'} < d$.
4. First case: every $s \in S$ lies in $\operatorname{span}(L)$. A span is a subspace, so $\operatorname{span}(L)$ contains every combination of elements of $S$, and $V = \operatorname{span}(S) \subseteq \operatorname{span}(L)$.
5. In the first case $L$ is independent and spans $V$, so $B = L$ is a [[basis|0VTQTPQGAV]] with $L \subseteq B \subseteq S$.
6. Second case: some $s \in S$ is not in $\operatorname{span}(L)$. By the [[linear dependence lemma|H75GS7QVPB]], adding a vector outside the span keeps independence, so $L' = L \cup \{s\}$ is independent.
7. In the second case $L \subseteq L' \subseteq S$ and $m - \abs{L'} = d - 1$, which is at least $0$ by step 1 applied to $L'$. By the induction hypothesis there is a basis $B$ with $L' \subseteq B \subseteq S$, and then $L \subseteq B \subseteq S$.

## Idea

Start from $L$ and look through $S$ for a vector that the current set cannot build.
If there is none, the current set already spans and is a basis.
If there is one, add it, and the set stays independent.
The Steinitz lemma says that an independent set never has more than $m$ vectors, so we can add at most $m - \abs{L}$ times, and the process must end at a basis.

## Variants

In $F^n$ we can do the whole search by row reduction.
Put the vectors of $L$ first and then the vectors of $S$ as the columns of a matrix.
The pivot columns of this matrix form a basis, and they include all the columns of $L$, because the columns of $L$ are independent and so each of them gets a pivot.
