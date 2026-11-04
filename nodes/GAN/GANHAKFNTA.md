---
tag: GANHAKFNTA
kind: proof
name: Proof of the negation of an existential statement
msc: [03B10]
proves: 05SZQKH75K
uses: [0T3DPBG981, 0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
---

## Proof

We show that the two propositions have the same truth value for each set $X$ and each [[predicate|0T3DPBG981]] $P$ on $X$.

1. Let $X$ be a set and let $P(x)$ be a predicate on $X$. For each $a \in X$, the proposition $P(a)$ is true or false.
2. By the definition of [[negation|0XR7A7RSXB]], $\neg \bigl( \exists x \in X, \, P(x) \bigr)$ is true exactly when $\exists x \in X, \, P(x)$ is false.
3. By the definition of the [[existential quantifier|0JW2FHW7G3]], $\exists x \in X, \, P(x)$ is false exactly when there is no $a \in X$ for which $P(a)$ is true.
4. There is no such $a$ exactly when, for each $a \in X$, $P(a)$ is not true. By step 1, this means that $P(a)$ is false for each $a \in X$.
5. By the definition of negation, $P(a)$ is false exactly when $\neg P(a)$ is true. So step 4 says that $\neg P(a)$ is true for each $a \in X$.
6. By the definition of the [[universal quantifier|0B88PQTJ66]], this is exactly when $\forall x \in X, \, \neg P(x)$ is true.
7. By steps 2 to 6, the two propositions are true in the same cases, and false in the same cases. Hence $\neg \bigl( \exists x \in X, \, P(x) \bigr) \equiv \forall x \in X, \, \neg P(x)$.

## Idea

"Nothing has the property" means "each thing fails to have it". The proof unfolds the meaning of the existential quantifier and of negation, one definition at a time.
