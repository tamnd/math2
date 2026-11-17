---
tag: GANHAKFNTA
kind: proof
name: Proof of the negation of an existential statement
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
proves: 05SZQKH75K
uses: [0T3DPBG981, 0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB]
methods: [0NTF6DMVAP]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Proof

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
We prove the two directions separately, with the rules of the quantifiers and of [[negation|0XR7A7RSXB]].
To prove $\neg \varphi$, we assume $\varphi$ and derive a contradiction; this is the definition of $\neg \varphi$ as "$\varphi$ implies a contradiction".

Direction 1: $\neg \exists x \, P(x) \to \forall x \, \neg P(x)$.

1. Assume $\neg \exists x \, P(x)$. Reason: hypothesis of the implication.
2. Let $b \in D$ be arbitrary. Reason: start of a proof of a universal statement.
3. Assume $P(b)$, to derive a contradiction. Reason: we want to prove $\neg P(b)$.
4. Then $\exists x \, P(x)$, with witness $b$. Reason: introduction of the [[existential quantifier|0JW2FHW7G3]].
5. Steps 1 and 4 give $\neg \exists x \, P(x)$ and $\exists x \, P(x)$, a contradiction.
6. So $\neg P(b)$. Reason: the assumption of step 3 led to a contradiction.
7. Since $b$ was arbitrary, $\forall x \, \neg P(x)$. Reason: introduction of the [[universal quantifier|0B88PQTJ66]].

Direction 2: $\forall x \, \neg P(x) \to \neg \exists x \, P(x)$.

8. Assume $\forall x \, \neg P(x)$. Reason: hypothesis of the implication.
9. Assume $\exists x \, P(x)$, to derive a contradiction. Reason: we want to prove $\neg \exists x \, P(x)$.
10. Choose $a \in D$ with $P(a)$. Reason: elimination of $\exists$ in step 9, with a new name $a$.
11. Then $\neg P(a)$. Reason: elimination of $\forall$ in step 8, applied to $a$.
12. Steps 10 and 11 give $P(a)$ and $\neg P(a)$, a contradiction.
13. So $\neg \exists x \, P(x)$. Reason: the assumption of step 9 led to a contradiction.

Conclusion.

14. By steps 1 to 7 and 8 to 13, each side implies the other, so $\neg \exists x \, P(x) \equiv \forall x \, \neg P(x)$. $\blacksquare$

Use of excluded middle: no step uses the [[law of excluded middle|0RYYK8PG4S]] or the [[double negation law|0NFAGWH84K]].
Each step is a rule of [[intuitionistic logic|Q11N8X99FK]], so the equivalence holds intuitionistically.

## Idea

Direction 1: if some $b$ had $P$, it would be a witness for $\exists x \, P(x)$, which is excluded, so every $b$ fails $P$.
Direction 2: a witness $a$ for $\exists x \, P(x)$ would contradict $\neg P(a)$.
Both directions only introduce or eliminate one quantifier and one negation, and no double negation is removed.

## Variants

1. A semantic proof with truth values: $\neg \exists x \, P(x)$ is true exactly when no $a \in D$ makes $P(a)$ true, exactly when every $P(a)$ is false, exactly when every $\neg P(a)$ is true, exactly when $\forall x \, \neg P(x)$ is true.
2. For a finite domain $\{a_1, \ldots, a_n\}$, the statement follows from [[De Morgan's law|09PKJKA6J0]] $\neg (p \lor q) \equiv \neg p \land \neg q$ by induction on $n$.
3. In Lean, where `Not` is defined as `a → False`, a proof of `not_exists` follows directions 1 and 2: each direction is a function that turns a witness into `False`.
