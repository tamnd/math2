---
tag: YR6HCMABTE
kind: concept
name: Model complete theory
aliases: [model-complete-theory, model-completeness]
msc: ["03C10"]
topics: [1A9JSC5YG8]
audience: grad
uses: [92SWXST1ZM, MVCH6N9SNW, 676H7EGTKJ, 8WZF9SBP39, SCRB74SWQN, CGH8C8EA9N, 7FDDXV3JK7]
sources:
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Model_complete_theory
    locator: Sufficient condition for completeness of model-complete theories
  - book: isbn:9780387987606
    locator: Chapter 3
  - book: isbn:9780521587136
same_as:
  wikidata: Q6888319
  wikipedia: Model complete theory
---

## Summary

A [[theory|92SWXST1ZM]] $T$ is *model complete* when for all [[models|MVCH6N9SNW]] $M$ and $N$ of $T$ with $M$ a [[substructure|676H7EGTKJ]] of $N$, $M$ is an [[elementary substructure|8WZF9SBP39]] of $N$.
Equivalently, every [[embedding|SCRB74SWQN]] between models of $T$ is [[elementary|CGH8C8EA9N]], and by [[Robinson's test|QHEADWYQ64]], every formula is equivalent modulo $T$ to an existential formula.
The formal page is [[this definition|ERVV6RWNNX]].
Model completeness is weaker than [[quantifier elimination|7FDDXV3JK7]], and it is the property that the [[model companion|68GG7QKN7C]] of a theory must have.

## Motivation

In algebra one often embeds a structure into a larger one to solve an equation, and then asks whether a solution already existed in the smaller one.
For algebraically closed fields $K \subseteq F$, a system of polynomial equations over $K$ with a solution in $F$ has a solution in $K$.
This is a form of Hilbert's Nullstellensatz, and it says that $K$ is existentially closed in $F$.
Model completeness asks for this transfer for every first-order formula and every inclusion of models.
The definition uses only embeddings, so it is often easier to check than quantifier elimination.

## Notation

Some authors write "model-complete" with a hyphen.
For an inclusion $M \subseteq N$, the notation $M \preceq N$ means that $M$ is an elementary substructure of $N$.
The notation $M \preceq_1 N$ means that existential formulas with parameters in $M$ that hold in $N$ already hold in $M$; then $M$ is [[existentially closed|6M98MCW575]] in $N$.

## Remarks

### Examples

- Every theory with quantifier elimination is model complete, for example [[dense linear orders without endpoints|E52RM0KX94]].
- The theory of [[algebraically closed fields|61VW0F3R83]] is model complete in the ring signature.
- The theory of [[real closed fields in the ring signature|G3GGANFA7C]] is model complete, but it has no quantifier elimination in that signature.
- The theory of [[differentially closed fields|KPCN3KHG50]] of characteristic $0$ is model complete in the signature of differential rings.
- Presburger arithmetic in the signature $\set{0, 1, +, -, <}$ is model complete, since the divisibility predicates have existential definitions.

### Non-examples

- The theory of [[the additive group of the integers|HMXD4AM0Y9]]: the even integers form a submodel in which $2$ is not divisible by $2$.
- Dense linear orders with endpoints: $[0, 1] \cap \Q \subseteq [0, 2] \cap \Q$, and $1$ is the greatest element only in the smaller model.
- The theory of fields: $\Q \subseteq \C$, and $\exists y \, (y \cdot y = 1 + 1)$ holds only in $\C$.

### Basic properties

- [[Robinson's test|QHEADWYQ64]]: $T$ is model complete if and only if $M \preceq_1 N$ for all models $M \subseteq N$, if and only if every formula is equivalent to an existential formula, if and only if every formula is equivalent to a universal formula.
- If $T$ is model complete and has a model that embeds into every model of $T$, then $T$ is complete. So the real algebraic numbers make the theory of real closed fields complete.
- More generally, a model complete theory with the joint embedding property is complete: two models embed into a third one, elementarily.
- The union of a chain of models of a model complete theory is an elementary chain, so it is a model. So a model complete theory is [[inductive|G8TRE2KSRV]].
- A theory has at most one model complete extension with the same universal consequences; this is the [[uniqueness of the model companion|68GG7QKN7C]].

### History

Abraham Robinson introduced model completeness in the 1950s.
The test for model completeness that bears his name comes from this work.
Robinson also defined the model completion of a theory, a stronger form of the later notion of model companion.

### Common errors

- Confusing model complete with complete. The theory of algebraically closed fields is model complete, but $\mathbb{C}$ and the algebraic closure of $\mathbb{F}_2$ are not elementarily equivalent.
- Confusing model completeness with quantifier elimination. Real closed fields in the ring signature are model complete without quantifier elimination.
- Forgetting the signature. Dense linear orders with endpoints become model complete when constants for the endpoints are added, since then a submodel must contain the endpoints of the larger model.

## Explanations

### L1 human

Imagine two models of a theory, one inside the other.
The theory is model complete when the inner model gives the same answer as the outer one to every question about its own elements.
For example, the real algebraic numbers sit inside the real numbers.
The question "is there a number whose square is $2$" has the answer yes in both.
Model completeness says that this agreement holds for every question, not only for this one.

### L2 human

We check that dense linear orders with endpoints are not model complete.

1. Let $M = [0, 1] \cap \Q$ and $N = [0, 2] \cap \Q$, both with the usual order.
2. Both are dense linear orders with a least and a greatest element, so both are models.
3. The order of $M$ is the restriction of the order of $N$, so $M$ is a substructure of $N$.
4. Let $\varphi(x)$ be $\forall y \, (y < x \vee y = x)$, which says that $x$ is the greatest element.
5. In $M$, $\varphi(1)$ is true. In $N$, $\varphi(1)$ is false, since $3/2 > 1$.

The typical use of model completeness is to show that a solution in a large model gives a solution in a small one.
A trap is to test only inclusions between isomorphic models, or only one inclusion: the definition asks for every inclusion of models.

### L3 human

Model completeness is the existential part of quantifier elimination.
Robinson's test says that it suffices to check that each model is existentially closed in each larger model.
For a theory $T_0$ and its class of [[existentially closed models|6M98MCW575]], the question is whether this class is elementary; when it is, its theory is the model companion of $T_0$, and it is model complete.
This explains the examples: algebraically closed fields for fields, real closed fields for formally real fields, differentially closed fields for differential fields.

The property depends on the signature, like quantifier elimination, but less strongly.
In geometric terms, model completeness says that the definable sets are projections of quantifier-free definable sets, and that their complements are also such projections.
In the later theory, a theory with quantifier elimination is the model completion of its universal part, and [[Robinson forcing|2TYY0ZP7YQ]] gives a forcing companion for every inductive theory, which equals the model companion when that exists.
