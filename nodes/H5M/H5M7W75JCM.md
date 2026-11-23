---
tag: H5M7W75JCM
kind: proof
name: Proof that WKL0 is Π¹₁-conservative over RCA0
msc: ["03B30", "03F35"]
topics: [BY8AAFN7C5]
audience: research
proves: 8G2GVRXWG5
uses: [DNXCKXZZ08, K5YPW1NTHZ, WQ1ZE255SF, 484M0TZ1S7, 4A84VHDTHV]
methods: [0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
---

## Proof

We prove the contrapositive: from a countable model of $\mathsf{RCA}_0$ in which a $\Pi^1_1$ sentence fails, we build a model of $\mathsf{WKL}_0$ with the same numbers in which it still fails.
The proof cites one lemma from model theory without proof.

**Lemma E (cited).** For every countable model $(M, \mathcal{S})$ of [[RCA0|DNXCKXZZ08]] there is a family $\mathcal{S}' \supseteq \mathcal{S}$ of subsets of $M$ such that $(M, \mathcal{S}')$ is a model of [[WKL0|K5YPW1NTHZ]].

1. Let $\sigma = \forall X\, \theta(X)$ with $\theta$ arithmetical, and assume that $\mathsf{RCA}_0$ does not prove $\sigma$.
2. Then $\mathsf{RCA}_0 + \neg \sigma$ is consistent, so it has a model by [[Gödel's completeness theorem|WQ1ZE255SF]].
   The language $L_2$ is countable, so the [[Löwenheim-Skolem theorem|484M0TZ1S7]] gives a countable model $(M, \mathcal{S})$.
3. Since $\neg \sigma$ holds in $(M, \mathcal{S})$, there is a set $A \in \mathcal{S}$ with $(M, \mathcal{S}) \models \neg \theta(A)$.
4. Lemma E gives $\mathcal{S}' \supseteq \mathcal{S}$ with $(M, \mathcal{S}') \models \mathsf{WKL}_0$, and $A$ is still in $\mathcal{S}'$.
5. The formula $\neg \theta(A)$ has no set quantifiers, so its truth depends only on the numbers $M$, their operations and the set $A$.
   These are the same in $(M, \mathcal{S})$ and $(M, \mathcal{S}')$.
6. So $(M, \mathcal{S}') \models \neg \theta(A)$, and therefore $(M, \mathcal{S}') \models \neg \sigma$.
7. By the [[soundness theorem|4A84VHDTHV]], a theory with a model of $\neg \sigma$ does not prove $\sigma$, so $\mathsf{WKL}_0$ does not prove $\sigma$.
8. By contraposition, if $\mathsf{WKL}_0 \vdash \sigma$, then $\mathsf{RCA}_0 \vdash \sigma$.

## Idea

Adding sets to a model does not change the truth of a statement that talks only about numbers and one given set.
So it is enough to show that every countable model of the base theory can be enlarged, by new sets only, into a model of weak König's lemma.
That enlargement is Lemma E, and all the work sits there.
Its standard proof lists the infinite binary trees of the model, adds a path through one tree at a time, and takes the union of the resulting families.
The delicate point is that each new path must keep $\Sigma^0_1$ induction true in a model whose numbers may be nonstandard, and a forcing argument chooses the path so that this holds.

## Variants

For $\omega$-models the enlargement follows from the relativized low basis theorem, as in the [[ω-model of WKL0 in which every set is low|8B045KSKW5]]: there induction is automatic, because the numbers are standard.
That special case shows that every countable Turing ideal is contained in a countable $\omega$-model of $\mathsf{WKL}_0$, but it does not prove the theorem, which needs nonstandard models.
Proof-theoretic proofs avoid models altogether and transform a $\mathsf{WKL}_0$ derivation of a $\Pi^1_1$ sentence into an $\mathsf{RCA}_0$ derivation of the same sentence.
