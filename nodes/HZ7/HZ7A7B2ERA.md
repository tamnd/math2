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

If a theory has a computable list of axioms and settles every sentence one way or the other, then a program decides it.
For example, the theory of dense linear orders without endpoints has six axioms and is complete, so it is decidable.

Let $L$ be a signature with a computable coding of its symbols, so that the set of $L$-sentences is computable.
Let $A$ be a computable set of $L$-sentences, and let $T = \operatorname{Cn}(A) = \{ \sigma : A \models \sigma \}$.
Assume that $T$ is [[complete|655K8Y7VS8]]: $T$ has a model, and for every $L$-sentence $\sigma$, $\sigma \in T$ or $\neg \sigma \in T$.
Then $T$ is a [[decidable theory|HWC687ES0Q]].

The same holds when $A$ is only [[computably enumerable|TN9G24VABN]], since then $T$ also has a computable set of axioms, by Craig's trick.
The [[proof by proof search|44T8BZG75G]] gives the algorithm.

## Remarks

### Why completeness is needed

Drop completeness, and the conclusion fails.
In a signature with one binary relation symbol, $A = \emptyset$ is computable, and $\operatorname{Cn}(\emptyset)$, the set of valid sentences, is undecidable by [[Church's theorem|VA6BNNY2YC]].
This theory is not complete, because it contains neither $\exists x \, R(x, x)$ nor its negation.

### Why the axioms must be computable

Drop the condition on the axioms, and the conclusion fails again.
True arithmetic $\operatorname{Th}(\mathbb{N}, 0, S, +, \cdot)$ is complete, because it is the theory of one structure.
It is not decidable, because it is a consistent extension of the [[essentially undecidable|9JDDFN8PT7]] theory $\mathsf{Q}$.
So its axioms cannot be listed by any program.

The condition that $T$ has a model is not needed for the conclusion.
If $A$ has no model, then $T$ is the set of all sentences, which is decidable.
The proof uses the model only to show that the answer "no" is correct.

### What it gives you

The theory of infinite sets, the theory of dense linear orders without endpoints, [[Presburger arithmetic|4W0E9G7PPV]] and the theory of algebraically closed fields of a fixed characteristic are decidable.
Each of them is complete and has a computable set of axioms.
So to show that a theory with computable axioms is decidable, it is enough to show that it is complete.
Model theory gives many tools for this, such as the [[Łoś-Vaught test|ZR7Y5C235P]] and quantifier elimination.

Read backwards, the theorem gives a form of [[Gödel's first incompleteness theorem|X9WYNYE29C]].
True arithmetic is complete and undecidable, so it has no computably enumerable set of axioms.

### The converse

The converse is false: a decidable theory need not be complete.
In a signature with one unary relation symbol $P$, the set of valid sentences is decidable, by the [[finite model property of monadic logic|AS0NHQMAKA]].
It is not complete, because it contains neither $\exists x \, P(x)$ nor $\neg \exists x \, P(x)$.
The other half of the converse is true: a decidable theory $T$ is axiomatized by the computable set $T$ itself.

### Generalizations

The proof shows more: a complete theory $T = \operatorname{Cn}(A)$ with a model is computable relative to $A$, for every set of axioms $A$.
For an incomplete theory, the same search decides the sentences that $T$ settles, but it runs forever on the other sentences.

### Watch out

The algorithm is not fast.
It may search through very many proofs before it stops, and the proof gives no bound on the time.
For dense linear orders, [[quantifier elimination|7FDDXV3JK7]] gives a much more direct procedure.

## Explanations

### L1 human

Imagine a complete rule book: for each statement, either the statement or its opposite follows from the rules.
A computer can list, one after another, everything that follows from the rules.
To judge a statement, the computer waits until the statement or its opposite appears in the list.
Completeness guarantees that one of the two appears after finite time, so the computer always gives an answer.

### L2 human

We follow the algorithm on the theory $T$ of dense linear orders without endpoints and the sentence $\sigma = \exists x \, \exists y \, (x < y)$.
The axioms of $T$ are finitely many: strict linear order, density, no least element, no greatest element, and at least two elements.
$T$ is complete, by the Łoś-Vaught test and Cantor's theorem that all countable dense linear orders without endpoints are isomorphic.

The algorithm lists all formal proofs from these axioms.
One short proof takes some element $x$, which exists because domains are nonempty, and uses "no greatest element" to get $y$ with $x < y$.
That proof ends with $\sigma$, so on input $\sigma$ the algorithm stops and answers "yes".
On input $\neg \sigma$, the algorithm looks for a proof of $\neg \sigma$ or of $\neg \neg \sigma$.
Adding a few lines to the proof of $\sigma$ gives a proof of $\neg \neg \sigma$, so the algorithm answers "no".

The typical use of the theorem is the chain "axioms, completeness, decidability".

### L3 human

The theorem is the effective content of the slogan "complete and axiomatizable implies $\Delta^0_1$".
The theory $T$ is $\Sigma^0_1$, and its complement inside the sentences is $\{ \sigma : \neg \sigma \in T \}$, the preimage of $T$ under the computable map $\sigma \mapsto \neg \sigma$.
So the complement is $\Sigma^0_1$ too, and a set that is $\Sigma^0_1$ with a $\Sigma^0_1$ complement is computable.

The theorem turns completeness proofs from model theory, by categoricity or by quantifier elimination, into decision procedures.
In the other direction, it is the reason why the results on [[essential undecidability|9JDDFN8PT7]] imply incompleteness: a consistent, complete, axiomatizable extension of $\mathsf{Q}$ would be decidable.
