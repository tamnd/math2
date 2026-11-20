---
tag: ~ddda0a28
kind: statement
role: theorem
name: Prime models are the countable atomic models
aliases: [prime-iff-countable-atomic, uniqueness-of-prime-models]
msc: ["03C50", "03C15"]
topics: [6XEXRME4C1]
audience: grad
uses: [~fbef995e, S8W40PYNHX, 655K8Y7VS8, 9V71Q3SD1G, 6F2DB4HTJR, XTNYY0WRQ5]
about: [~fbef995e, S8W40PYNHX]
sources:
  - url: https://en.wikipedia.org/wiki/Prime_model
    locator: Relationship with saturated models
  - book: isbn:9780387987606
---

## Statement

Let $T$ be a [[complete theory|655K8Y7VS8]] with infinite models in a countable signature $L$.

1. A model $M$ of $T$ is a [[prime model|S8W40PYNHX]] if and only if $M$ is countable and [[atomic|~fbef995e]].
2. Any two countable atomic models of $T$ are isomorphic.
3. In particular, if $T$ has a prime model, it is unique up to isomorphism.

The proof is [[here|~b067529e]].

## Remarks

### Why each hypothesis is needed

- Countable signature. Let $L$ have constants $c_\alpha$ for $\alpha < \omega_1$, and let $T$ say that the $c_\alpha$ are pairwise distinct and that there are infinitely many elements. The model whose elements are exactly the constants is prime, and it is uncountable.
- Countable model. In the theory of dense linear orders without endpoints, $(\R, <)$ is atomic but not prime; see [[this example|~309e2d86]].
- Completeness of $T$ is part of the definitions: isolation and elementary embeddings into all models both need a fixed complete theory.

### Consequences

- The field of [[algebraic numbers|~5820c59d]] is the prime model of $\mathrm{ACF}_0$, and $(\Q, <)$ is the prime model of the theory of dense linear orders.
- A theory with no isolated $n$-type for some $n$, such as the theory of [[independent unary predicates|~a949e251]], has no atomic model, and so no prime model.
- If $T$ is $\aleph_0$-categorical, its countable model is atomic and prime.

### Converse

Clause 2 does not extend to all countable models.
If any two countable models of $T$ are isomorphic, then $T$ is $\aleph_0$-categorical, which is a strong extra condition.
In general $T$ has countable models that are not atomic, such as $\Z + \Z$ for the theory of $(\Z, <)$.

### Generalizations

The back-and-forth in the proof also shows that a countable atomic model $M$ is homogeneous: if two tuples of $M$ have the same type, an automorphism of $M$ maps one to the other.
In an $\omega$-stable theory, every set $A$ inside a model has a prime model over $A$, and it is unique up to isomorphism over $A$.

## History

This theorem is one of the basic results on countable models of complete theories, together with the existence theorem for [[atomic models|~24829d6c]] and [[Vaught's never-two theorem|~ea319e25]].

## Explanations

### L1 human

A prime model is a smallest model, one that fits inside every other model of the theory.
The theorem says what such a model looks like: it is countable, and every finite list of its elements is described by one formula.
It also says that there is at most one such model.
So when a theory has a smallest model, that model is unique.

### L2 human

We apply clause 1 to the theory of an infinite set in the empty signature.

1. In a model, the type of a tuple is fixed by which entries are equal, and this is said by one formula. So every model is atomic.
2. The countable models are the countably infinite sets, all atomic.
3. By clause 1, a countably infinite set is prime: it embeds elementarily into every infinite set.

The typical use is to prove that a given countable model is prime by checking that each tuple is isolated.
A trap is to apply clause 1 to an uncountable model; atomic models of large size are usually not prime.

### L3 human

The proof of clause 2 is the back-and-forth method with the complete formulas in place of order patterns.
