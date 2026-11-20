---
tag: 8GBH6BWXPZ
kind: statement
role: theorem
name: Characterization of complete theories
aliases: [complete-theory-iff-models-elementarily-equivalent]
msc: ["03C07", "03C35"]
topics: [AY09KYSW81]
audience: ug2
about: [655K8Y7VS8, P3B1V182N4]
uses: [655K8Y7VS8, P3B1V182N4, X9HV9C6X4F, 1HK0VYWTV7, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Complete_theory
    locator: Complete theories
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Statement

Let $T$ be a satisfiable $L$-theory, and let $\operatorname{Cn}(T) = \set{\sigma : T \models \sigma}$ be its set of [[consequences|1HK0VYWTV7]].
The following are equivalent.

1. $T$ is [[complete|655K8Y7VS8]]: for every $L$-sentence $\sigma$, $T \models \sigma$ or $T \models \neg\sigma$.
2. Any two [[models|MVCH6N9SNW]] of $T$ are [[elementarily equivalent|P3B1V182N4]].
3. There is an $L$-structure $\mathcal{M}$ with $\operatorname{Cn}(T) = \operatorname{Th}(\mathcal{M})$.
4. For every model $\mathcal{M}$ of $T$, $\operatorname{Cn}(T) = \operatorname{Th}(\mathcal{M})$.

## Remarks

### Why each hypothesis is needed

- Satisfiability is needed. The theory $T = \set{\exists x \, \neg(x = x)}$ has no models, so condition 2 and condition 4 hold vacuously, and $T \models \sigma$ for every $\sigma$, so condition 1 holds in the weak sense. But $\operatorname{Cn}(T)$ contains both $\sigma$ and $\neg\sigma$, and it is not the [[theory of any structure|X9HV9C6X4F]], so condition 3 fails.
- With the convention that complete theories must be satisfiable, as in Mathlib's `FirstOrder.Language.Theory.IsComplete`, the inconsistent theory is not complete, and the hypothesis is part of condition 1.

### Consequences

- For every structure $\mathcal{M}$, $\operatorname{Th}(\mathcal{M})$ is complete, by condition 3.
- To prove that $T$ is complete, it suffices to show that any two models of $T$ are elementarily equivalent; this is how the [[Łoś-Vaught test|ZR7Y5C235P]] works.
- If $T$ is complete and $\mathcal{M}, \mathcal{N} \models T$, then a sentence true in $\mathcal{M}$ is true in $\mathcal{N}$; so results transfer between all models.
- A complete theory with a computably enumerable set of axioms is decidable: enumerate the consequences until $\sigma$ or $\neg\sigma$ appears.

### Converse

The statement is an equivalence.
The stronger condition that all models of $T$ are isomorphic is sufficient for completeness but far from necessary; a first-order theory with an infinite model has models of every infinite cardinality $\ge \abs{L}$, so its models are never all isomorphic.

### Generalizations

- For a satisfiable theory $T$, the complete theories that contain $T$ are exactly the sets $\operatorname{Th}(\mathcal{M})$ for $\mathcal{M} \models T$, and each satisfiable theory has at least one complete extension.
- The same equivalence holds for theories with constants for parameters, such as the elementary diagram of a structure.

## History

The equivalence follows at once from the definitions and belongs to the basic material of the subject.
In 1954 Łoś and Vaught independently gave the categoricity test, which turns condition 2 into a practical method for proving completeness.

## Explanations

### L1 human

A theory is complete when it answers every question.
This is the same as saying that all its models look alike to first-order logic.
If two models disagreed on some statement, the theory could not decide that statement.

### L2 human

We apply the theorem to the theory $T$ of dense linear orders without endpoints.

1. $T$ is satisfiable, since $(\Q, <) \models T$.
2. Any two countable models of $T$ are isomorphic by Cantor's theorem, and every model of $T$ is elementarily equivalent to a countable one by the Löwenheim-Skolem theorem.
3. So any two models of $T$ are elementarily equivalent, and condition 2 holds.
4. By the theorem, $T$ is complete, and $\operatorname{Cn}(T) = \operatorname{Th}(\Q, <)$ by condition 4.

The typical use of the theorem is to prove completeness by comparing models.
A trap is to apply it to an unsatisfiable theory.

### L3 human

In terms of the Stone space $S_0(\emptyset)$ of complete theories, the satisfiable theories correspond to nonempty closed sets, and the complete theories are the points.
The theorem says that $T$ is complete exactly when its closed set is a single point, the common theory of all its models.
Methods to show that a closed set is a point include categoricity, quantifier elimination and back-and-forth systems; see the sub-areas on [[countable models|6XEXRME4C1]] and [[quantifier elimination|1A9JSC5YG8]].
