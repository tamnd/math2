---
tag: XT227BYP7B
kind: statement
role: theorem
name: Vaught's two-cardinal theorem
aliases: [vaught-two-cardinal-theorem, vaughts-two-cardinal-theorem, two-cardinal-theorem]
msc: ["03C55", "03C50"]
topics: [W9CHA4PD9H]
audience: grad
about: [92SWXST1ZM]
uses: [92SWXST1ZM, WDVVEYD6AT, 01TQB88H4C, 0G0ASKNA6Z, 8WZF9SBP39, 484M0TZ1S7, 4NJS7W57VK, Z92S2GVCX9]
history:
  notes: "Robert Vaught proved the theorem with Vaughtian pairs and countable homogeneous models."
sources:
  - book: isbn:9780387987606
  - book: isbn:9780486488219
    locator: Chapter 7
---

## Statement

Let $L$ be a [[countable|01TQB88H4C]] [[signature|WDVVEYD6AT]] with a unary relation symbol $P$, and let $T$ be an $L$-[[theory|92SWXST1ZM]].
For cardinals $\kappa$ and $\lambda$, a *$(\kappa, \lambda)$-model* of $T$ is a model $\mathcal{M} \models T$ with $\abs{M} = \kappa$ and $\abs{P^{\mathcal{M}}} = \lambda$.

If $T$ has a $(\kappa, \lambda)$-model for some cardinals $\kappa > \lambda \ge \aleph_0$, then $T$ has an $(\aleph_1, \aleph_0)$-model.

The proof uses *Vaughtian pairs*: a pair $\mathcal{N} \preceq \mathcal{M}$ of models of $T$ with $\mathcal{N} \ne \mathcal{M}$, $P^{\mathcal{N}} = P^{\mathcal{M}}$ and $P^{\mathcal{M}}$ infinite, where $\preceq$ is the [[elementary substructure|8WZF9SBP39]] relation.
The proof is in [[the proof of Vaught's two-cardinal theorem|BKSPVH8B35]].

## Remarks

### Why each hypothesis is needed

- $\kappa > \lambda$: the theory $\set{\forall x \, P(x)}$ with infinite models has $(\kappa, \kappa)$-models for every infinite $\kappa$, and no $(\aleph_1, \aleph_0)$-model.
- $\lambda$ infinite: the theory "$P$ has exactly one element, and the universe is infinite" has $(\kappa, 1)$-models, and in no model is $P$ infinite.
- $L$ countable: add constants $c_\alpha$ for $\alpha < \omega_1$, with the axioms $P(c_\alpha)$ and $c_\alpha \ne c_\beta$ for $\alpha \ne \beta$. This theory has an $(\aleph_2, \aleph_1)$-model, and in each model $P$ is uncountable.

### Consequences

- The same holds for a formula $\varphi(x)$ in place of $P$: add a new predicate $P$ with the axiom $\forall x \, (P(x) \leftrightarrow \varphi(x))$.
- If $T$ has a model in which $P$ is infinite and smaller than the model, then $T$ has a Vaughtian pair, and conversely.
- A theory with a Vaughtian pair is not $\aleph_1$-categorical. It has an $(\aleph_1, \aleph_0)$-model, and compactness with the Löwenheim-Skolem theorem gives an $(\aleph_1, \aleph_1)$-model.
- This exclusion of Vaughtian pairs is a step in the Baldwin-Lachlan proof of [[Morley's categoricity theorem|V7N84P60SJ]].

### Converse

The weak converse is true and empty: an $(\aleph_1, \aleph_0)$-model is a $(\kappa, \lambda)$-model with $\kappa > \lambda \ge \aleph_0$.
The strong converse, that an $(\aleph_1, \aleph_0)$-model gives $(\kappa, \lambda)$-models for all $\kappa > \lambda \ge \aleph_0$, is false.
Let $L = \set{P, E}$, and let $T$ say that elements outside $P$ are determined by their $E$-predecessors in $P$.
Then $T$ has an $(\aleph_1, \aleph_0)$-model, with $P = \N$ and $\aleph_1$ subsets of $\N$ outside $P$.
But a model with $\abs{P} = \lambda$ has at most $\lambda + 2^\lambda$ elements, so $T$ has no $(\kappa, \aleph_0)$-model for $\kappa > 2^{\aleph_0}$.

### Generalizations

[[Chang's two-cardinal theorem|4STP69KESQ]] gives $(\kappa^+, \kappa)$-models from an $(\aleph_1, \aleph_0)$-model, for regular $\kappa$ under the generalized continuum hypothesis.
Transfers between other gaps, such as from $(\aleph_2, \aleph_0)$-models to $(\aleph_3, \aleph_1)$-models, are the gap-$n$ problems discussed there.

## History

Robert Vaught proved the theorem, with the method of Vaughtian pairs and countable homogeneous models.
The notion of a Vaughtian pair now has a central role in the study of categoricity.

## Explanations

### L1 human

Imagine a theory with a small part, called $P$, inside a model.
Suppose that some model is much larger than its small part, for example the small part has as many elements as the natural numbers and the model has as many as the real numbers.
The theorem says that there is then a model whose small part is still the size of the natural numbers, and whose whole size is the next possible size.
So a gap between the two sizes, of any width, can be moved down to the smallest gap.

### L2 human

We find a Vaughtian pair in a concrete $(2^{\aleph_0}, \aleph_0)$-model, which is the first step of the proof.

1. Let $L = \set{P, E}$, and let $\mathcal{M}$ have universe $\N \cup \mathcal{P}(\N)$, with $P = \N$ and $n E X$ when $n \in X$.
2. By the downward [[Löwenheim-Skolem theorem|484M0TZ1S7]], some countable $\mathcal{N} \preceq \mathcal{M}$ contains $\N$.
3. Then $P^{\mathcal{N}} = P^{\mathcal{M}} \cap N = \N$, which is infinite.
4. The model $\mathcal{N}$ is countable and $\mathcal{M}$ is not, so $\mathcal{N} \ne \mathcal{M}$, and $(\mathcal{M}, \mathcal{N})$ is a Vaughtian pair.

The typical use is to show that a theory with a Vaughtian pair has an $(\aleph_1, \aleph_0)$-model, and so is not $\aleph_1$-categorical.
The trap is to apply the theorem to a definable set that is finite: the hypothesis $\lambda \ge \aleph_0$ is needed.

### L3 human

The theorem is a Löwenheim-Skolem theorem for pairs of cardinals: a two-cardinal property of a countable theory moves down to the smallest gap $(\aleph_1, \aleph_0)$.
The proof shows that the gap is a property of a countable configuration, a Vaughtian pair of countable homogeneous models with the same types, which then repeats along $\omega_1$.
Moving up is harder, and it needs set theory: [[Chang's theorem|4STP69KESQ]] uses saturated models and the generalized continuum hypothesis, and the general gap problems are independent of ZFC.
Vaughtian pairs return in the analysis of [[uncountably categorical theories|V7N84P60SJ]], where their absence controls the size of definable sets.
