---
tag: HZ7A7B2ERA
kind: statement
role: theorem
name: A complete axiomatizable theory is decidable
aliases: [complete-recursively-axiomatizable-theories-are-decidable]
msc: ["03B25"]
topics: [E4AVTNWE9E]
audience: ug2
about: [HWC687ES0Q, 655K8Y7VS8]
uses: [HWC687ES0Q, 655K8Y7VS8, 92SWXST1ZM, PPGD5KW8JC, WQ1ZE255SF]
sources:
  - url: https://en.wikipedia.org/wiki/Decidability_(logic)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Complete_theory
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Undecidability
---

## Statement

Let $L$ be a signature with a computable coding of its symbols, so that the set of $L$-sentences is computable.
Let $A$ be a computable set of $L$-sentences, and let $T = \operatorname{Cn}(A) = \set{\sigma : A \models \sigma}$.
Assume that $T$ is [[complete|655K8Y7VS8]]: $T$ has a model, and for every $L$-sentence $\sigma$, $\sigma \in T$ or $\neg \sigma \in T$.
Then $T$ is a [[decidable theory|HWC687ES0Q]].

The same holds when $A$ is only [[computably enumerable|TN9G24VABN]], since then $T$ also has a computable set of axioms, by Craig's trick.

## Remarks

### Why each hypothesis is needed

- Completeness is needed. In a signature with one binary relation symbol, $A = \emptyset$ is computable, and $\operatorname{Cn}(\emptyset)$, the set of valid sentences, is undecidable by [[Church's theorem|VA6BNNY2YC]]. This theory is not complete: it contains neither $\exists x \, R(x, x)$ nor its negation.
- A computable or computably enumerable set of axioms is needed. True arithmetic $\operatorname{Th}(\N, 0, S, +, \cdot)$ is complete, because it is the theory of one structure, but it is not decidable, because it is a consistent extension of the [[essentially undecidable|9JDDFN8PT7]] theory $\mathsf{Q}$.
- The condition that $T$ has a model is not needed for the conclusion. If $A$ has no model, then $T$ is the set of all sentences, which is decidable. The proof uses this condition only to show that the answer "no" is correct.

### Consequences

1. The theory of infinite sets, the theory of dense linear orders without endpoints, [[Presburger arithmetic|4W0E9G7PPV]] and the theory of algebraically closed fields of a fixed characteristic are decidable, since each is complete and has a computable set of axioms.
2. True arithmetic has no computably enumerable set of axioms, because it is complete and undecidable. This is a form of [[Gödel's first incompleteness theorem|X9WYNYE29C]].
3. To prove that a theory with a computable set of axioms is decidable, it suffices to prove that it is complete. Model theory gives many tools for this, such as the [[Łoś-Vaught test|ZR7Y5C235P]] and quantifier elimination.

### Converse

The converse is false: a decidable theory need not be complete.
In a signature with one unary relation symbol $P$, the set of valid sentences is decidable, by the [[finite model property of monadic logic|AS0NHQMAKA]].
It is not complete, because it contains neither $\exists x \, P(x)$ nor $\neg \exists x \, P(x)$.
The other half of the converse is true: a decidable theory $T$ is axiomatized by the computable set $T$ itself.

### Generalizations

The proof shows more: a complete theory $T = \operatorname{Cn}(A)$ is computable relative to $A$, for every set of axioms $A$.
For an incomplete theory, the same search decides the sentences that $T$ settles, but it runs forever on the other sentences.

## Explanations

### L1 human

Imagine a complete rule book: for each statement, either the statement or its opposite follows from the rules.
A computer can list, one after another, everything that follows from the rules.
To judge a statement, the computer waits until the statement or its opposite appears in the list.
Completeness guarantees that one of the two appears after finite time, so the computer always gives an answer.

### L2 human

We follow the algorithm on the theory $T$ of dense linear orders without endpoints and the sentence $\sigma = \exists x \, \exists y \, (x < y)$.

1. The axioms of $T$ are finitely many: strict linear order, density $\forall x \, \forall y \, (x < y \to \exists z \, (x < z \wedge z < y))$, no least element, no greatest element, and at least two elements.
2. $T$ is complete, by the Łoś-Vaught test and Cantor's theorem that all countable dense linear orders without endpoints are isomorphic.
3. The algorithm lists all formal proofs from these axioms. One short proof takes $x$ arbitrary and uses "no greatest element" to get $y$ with $x < y$.
4. That proof ends with $\sigma$, so the algorithm stops and answers "yes".
5. For $\neg \sigma$, the same proof appears in the list, and the algorithm answers "no".

The typical use of the theorem is the chain "axioms, completeness, decidability".
A trap is to believe that the algorithm is fast: it may search through very many proofs before it stops.

### L3 human

The theorem is the effective content of the equation "complete and axiomatizable implies $\Delta^0_1$": a $\Sigma^0_1$ set whose complement, inside the sentences, is the image of the set under the computable map $\sigma \mapsto \neg \sigma$ is computable.
It turns model-theoretic completeness proofs, by categoricity or by quantifier elimination, into decision procedures, but it gives no bound on running time.
In the other direction, it is the reason why the undecidability results of [[essential undecidability|9JDDFN8PT7]] imply incompleteness: a consistent, complete, axiomatizable extension of $\mathsf{Q}$ would be decidable.
