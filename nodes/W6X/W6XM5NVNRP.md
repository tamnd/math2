---
tag: W6XM5NVNRP
kind: concept
name: Small theory
aliases: [small-theory, theory-with-countably-many-types]
msc: ["03C15", "03C50"]
topics: [6XEXRME4C1]
audience: grad
uses: [9V71Q3SD1G, 655K8Y7VS8, ZV38HA5PAQ, 01TQB88H4C]
sources:
  - book: isbn:9780387987606
  - book: isbn:9780521587136
---

## Summary

Let $T$ be a [[complete theory|655K8Y7VS8]] with infinite models in a countable signature.
$T$ is *small* if for every $n$ it has only [[countably|01TQB88H4C]] many complete $n$-[[types|9V71Q3SD1G]] over the empty set.
Small theories are the ones with a countable saturated model, and every small theory also has a prime model.
A theory that is not small has $2^{\aleph_0}$ countable models, so smallness is the first dividing line in counting countable models.

## Motivation

A countable model realizes only countably many $n$-types, since it has only countably many $n$-tuples.
So a theory with uncountably many types needs many countable models to realize them all.
A countable model that realizes every type, and more, every type over finite sets, is a saturated model.
Smallness is exactly the condition under which such a model exists.

## Notation

Write $S_n(T)$ for the set of complete $n$-types of $T$; it is the [[Stone space|ZV38HA5PAQ]] of the algebra of formulas in $n$ variables modulo $T$.
So $T$ is small when $\abs{S_n(T)} \le \aleph_0$ for all $n$.
Some books state the condition without a name, as "$T$ has countably many types".

## Remarks

### Examples

- Every $\aleph_0$-categorical theory, which has only finitely many $n$-types for each $n$.
- The theory $\mathrm{ACF}_0$; see [[this example|DKE21EBN3M]].
- The theory of $(\Z, <)$, in which an $n$-type is fixed by the order of the points and the finite distances between them; see [[this example|91WRBX69MB]].
- [[Ehrenfeucht's theory|XT2D23G98S]] with exactly three countable models.

### Non-examples

- The theory of [[independent unary predicates|9MV9VG8G67]], with $2^{\aleph_0}$ complete $1$-types.
- The theory of $(\N, 0, 1, +, \cdot, <)$: for each set $X$ of primes there is a type saying that $x$ is divisible by the primes in $X$ and by no others.

### Basic properties

- $T$ is small if and only if it has a countable saturated model; see [[this theorem|7GN6XF590M]].
- A small theory has a prime model; see [[this theorem|MXVGKQ783S]].
- If $T$ is small, then $T$ with finitely many new constants naming a tuple is small. A $k$-type over a tuple $\bar c$ corresponds to an $(m + k)$-type of $T$, where $m$ is the length of $\bar c$.
- So a small theory has a prime model over every finite tuple $\bar a$ of every model, and a countable saturated model of $\operatorname{Th}(M, \bar a)$.
- If $T$ is not small, then some $S_n(T)$ is uncountable. It is a compact metrizable space, so it has $2^{\aleph_0}$ points, and $T$ has $2^{\aleph_0}$ countable models.
- An $\omega$-stable theory, one with countably many types over each countable set, is small.

### History

The condition of countably many types appears in the first studies of countable models of complete theories, through its link with countable saturated models and [[Vaught's never-two theorem|E5W3RRSY5Z]].

### Common errors

- Small is weaker than $\omega$-stable. The theory of dense linear orders is small, but over $\Q$ it has $2^{\aleph_0}$ types, one for each cut.
- A small theory can still have $2^{\aleph_0}$ countable models; the theory of $(\Z, <)$ does.
- Smallness counts types over the empty set, or equivalently over finite sets, not over countable sets.

## Explanations

### L1 human

A type is a complete description of how a few elements can behave.
A theory is small when there are only countably many such descriptions for each number of elements.
Then one countable model can contain an example of every description, and the theory has a richest countable model.

### L2 human

We show that a theory that is not small has $2^{\aleph_0}$ countable models, assuming $\abs{S_n(T)} = 2^{\aleph_0}$ for some $n$.

1. Each countable model realizes at most $\aleph_0$ types in $S_n(T)$, one for each $n$-tuple.
2. Each type is realized in some countable model, by the Löwenheim-Skolem theorem.
3. So the countable models together realize $2^{\aleph_0}$ types, and at least $2^{\aleph_0}$ models are needed.
4. There are at most $2^{\aleph_0}$ countable models up to isomorphism in a countable signature, so the number is exactly $2^{\aleph_0}$.

The typical use is the first case split in counting countable models: either $T$ is small, or it has the maximum number.
A trap is to skip the topology: an uncountable $S_n(T)$ has size $2^{\aleph_0}$ because it is a closed subset of the Cantor space, even without the continuum hypothesis.

### L3 human

In descriptive set theory terms, $S_n(T)$ is a compact Polish space, and an uncountable Polish space contains a perfect set.
[[Morley's theorem on countable models|JFG783DEG8]] extends this kind of argument from types to whole models.
