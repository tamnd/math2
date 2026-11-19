---
tag: JP8876HAAR
kind: proof
name: Proof of the undecidability of monadic IQC by reduction from classical logic
msc: ["03B20", "03B25", "03D35"]
topics: [38EQ20GR7M]
audience: research
proves: 744RW1KZJ9
uses: [VA6BNNY2YC, MW0RVDRFTA]
methods: [0J0XBKG64S]
sources:
  - arxiv: 2505.00524v1
    locator: Abstract
---

## Proof

The proof is a reduction, and it cites two lemmas without proof.

1. Let $B$ be the set of classical first-order sentences whose only nonlogical symbol is one binary predicate $R$, without equality.
2. Lemma A, cited: the set of sentences in $B$ that are classically valid is undecidable. This is a refinement of [[Church's theorem|VA6BNNY2YC]].
3. Lemma B, cited: there is a computable map $\tau$ from $B$ to monadic formulas such that $\varphi$ is classically valid if and only if $\mathsf{IQC} \vdash \tau(\varphi)$.
4. The idea of Lemma B is that a Kripke model with growing domains can code a binary relation in unary predicates. A pair $(a, b)$ is in the relation when a later world gives $a$ and $b$ prescribed unary properties together.
5. Lemma B is the only part of the proof that uses intuitionistic semantics. We do not prove it here.
6. Suppose, for a contradiction, that an algorithm $\mathcal{A}$ decides whether $\mathsf{IQC}$ proves a monadic formula.
7. For $\varphi \in B$, compute $\tau(\varphi)$ and run $\mathcal{A}$ on it.
8. By step 3, the answer is "yes" exactly when $\varphi$ is classically valid.
9. So this procedure decides classical validity on $B$. This contradicts Lemma A.
10. Hence no algorithm decides monadic $\mathsf{IQC}$.

## Idea

Classical logic with a binary predicate is undecidable, while classical monadic logic is decidable.
In intuitionistic logic, the order of worlds supplies extra structure.
Unary predicates evaluated at later worlds can then simulate a binary relation.
So a decision method for monadic $\mathsf{IQC}$ would decide classical logic with a binary predicate.

## Variants

1. Recent proofs use tiling problems, and they show that the monadic theorems of $\mathsf{IQC}$ and the monadic formulas valid on finite frames are recursively inseparable.
2. Similar codings give undecidability for monadic fragments of many modal predicate logics with expanding domains.
