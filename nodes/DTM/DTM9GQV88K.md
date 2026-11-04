---
tag: DTM9GQV88K
kind: proof
name: Proof of the negation of a universal statement
msc: [03B10]
proves: 0P3A06QNDP
uses: [0T3DPBG981, 0B88PQTJ66, 0JW2FHW7G3, 0XR7A7RSXB]
sources:
  - url: https://richardhammack.github.io/BookOfProof/
---

## Proof

We show that the two propositions have the same truth value for each set $X$ and each [[predicate|0T3DPBG981]] $P$ on $X$.

1. Let $X$ be a set and let $P(x)$ be a predicate on $X$. For each $a \in X$, the proposition $P(a)$ is true or false.
2. By the definition of [[negation|0XR7A7RSXB]], $\neg \bigl( \forall x \in X, \, P(x) \bigr)$ is true exactly when $\forall x \in X, \, P(x)$ is false.
3. By the definition of the [[universal quantifier|0B88PQTJ66]], $\forall x \in X, \, P(x)$ is false exactly when it is not the case that $P(a)$ is true for each $a \in X$.
4. This means that there is some $a \in X$ for which $P(a)$ is not true. By step 1, such a $P(a)$ is false.
5. By the definition of negation, $P(a)$ is false exactly when $\neg P(a)$ is true.
6. By steps 2 to 5, $\neg \bigl( \forall x \in X, \, P(x) \bigr)$ is true exactly when $\neg P(a)$ is true for at least one $a \in X$.
7. By the definition of the [[existential quantifier|0JW2FHW7G3]], this is exactly when $\exists x \in X, \, \neg P(x)$ is true.
8. So the two propositions are true in the same cases, and false in the same cases. Hence $\neg \bigl( \forall x \in X, \, P(x) \bigr) \equiv \exists x \in X, \, \neg P(x)$.

## Idea

"Not everything has the property" means "at least one thing fails to have it". The proof unfolds the meaning of the universal quantifier and of negation. Classical logic enters in steps 3 and 4: "not all are true" becomes "some one is false".
