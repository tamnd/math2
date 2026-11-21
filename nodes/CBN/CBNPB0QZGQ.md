---
tag: CBNPB0QZGQ
kind: concept
name: Special model
aliases: [special-structure]
msc: ["03C50"]
topics: [Z772KEC9BY]
audience: research
uses: [983GZBQYT4, NHCRZ74JHH, RMTZ5J64FX, 0EBACQFAZW, 13ZV2F8JAR, GSQ833HAZT]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780521587136
  - book: isbn:9780387987606
---

## Summary

Let $T$ be a complete theory in a language $L$, and let $\lambda > \abs{L} + \aleph_0$ be a [[cardinal|0EBACQFAZW]].
A model $\mathcal{M}$ of $T$ of size $\lambda$ is *special* when it is the union of an [[elementary chain|NHCRZ74JHH]] $(\mathcal{M}_\mu)$, indexed by the cardinals $\mu$ with $\abs{L} + \aleph_0 \le \mu < \lambda$, in which each $\mathcal{M}_\mu$ is $\mu^+$-[[saturated|RMTZ5J64FX]].
Special models exist in every strong limit cardinal $\lambda > \abs{L}$ without further set-theoretic assumptions, and two special models of the same theory and size are isomorphic.
So they replace saturated models in proofs that would otherwise need the generalized continuum hypothesis.

## Motivation

Saturated models of size $\lambda$ need $\lambda^{<\lambda} = \lambda$ or stability, by [[existence of saturated models|GSQ833HAZT]].
A strong limit cardinal of countable cofinality, such as $\beth_\omega$, never satisfies $\lambda^{<\lambda} = \lambda$, yet each smaller cardinal $\mu$ is small enough that a $\mu^+$-saturated model of size less than $\lambda$ exists.
A special model glues these models together.
It keeps enough saturation along the chain to run the back-and-forth argument for uniqueness and universality.

## Notation

The chain $(\mathcal{M}_\mu)$ is called a *specializing chain*.
The cardinal $\lambda$ is a *strong limit* when $2^\mu < \lambda$ for every $\mu < \lambda$.

## Remarks

### Examples

- Every saturated model of size $\lambda > \abs{L} + \aleph_0$ is special, with the constant chain $\mathcal{M}_\mu = \mathcal{M}$.
- An algebraically closed field of uncountable transcendence degree $\kappa$ is special; see [[saturated algebraically closed fields|QX6K7CWWNV]].
- A dense linear order of size $\beth_\omega$ can be special without being saturated; see [[a special dense order that is not saturated|YTK20FB883]].

### Non-examples

- The order $(\R, <)$ is not special, since the first link of a chain would be an $\aleph_1$-saturated suborder of $\R$; see [[the real order is not special|TXSS2XTE2T]].
- A countable structure in a countable language is never special in this sense, since the definition needs $\lambda > \aleph_0$.

### Basic properties

- A special model of [[regular|13ZV2F8JAR]] size $\lambda$ is saturated, since each set of fewer than $\lambda$ elements lies in one link $\mathcal{M}_\mu$ with $\mu$ at least its size.
- Every complete $T$ with infinite models has a special model in every strong limit cardinal $\lambda > \abs{L}$; the links come from part 1 of [[existence of saturated models|GSQ833HAZT]], and their sizes stay below $\lambda$.
- Two special models of the same complete theory and the same size are isomorphic.
- A special model of size $\lambda$ is [[universal|F30ZVR4AD5]].
- If $\mathcal{M} \equiv \mathcal{N}$, then $\mathcal{M}$ and $\mathcal{N}$ have isomorphic elementary extensions: embed both into special models of the same strong limit size.

### History

Special models were introduced as a replacement for saturated models that needs no hypothesis on cardinal arithmetic beyond the existence of strong limit cardinals, which ZFC proves.

### Common errors

- Assuming that special models are saturated: in singular size they are not, by part 5 of [[existence of saturated models|GSQ833HAZT]].
- Indexing the chain by all ordinals below $\lambda$ instead of by cardinals: the saturation of a link is tied to its cardinal index.

## Explanations

### L1 human

A special model is built in layers.
Each layer is saturated for parameter sets up to its own cardinal, and the layers grow until they fill the whole model.
Special models play the role of saturated models in sizes where saturated models may not exist.

### L2 human

We check that a special model $\mathcal{M}$ of regular size $\lambda$ is saturated.

1. Let $A \subseteq M$ with $\abs{A} < \lambda$, and let $p \in S_1(A)$.
2. Each $a \in A$ lies in some link $\mathcal{M}_{\mu_a}$. Since $\lambda$ is regular and $\abs{A} < \lambda$, some cardinal $\mu < \lambda$ satisfies $\mu \ge \abs{A}$ and $\mu \ge \mu_a$ for all $a$.
3. Then $A \subseteq M_\mu$, and $p$ is a type over $A$ in $\mathcal{M}_\mu$, since $\mathcal{M}_\mu \preceq \mathcal{M}$.
4. The link $\mathcal{M}_\mu$ is $\mu^+$-saturated and $\abs{A} \le \mu$, so $p$ is realized in $\mathcal{M}_\mu$, hence in $\mathcal{M}$.

The trap is step 2 for singular $\lambda$: a set of size $\operatorname{cf}(\lambda)$ can meet cofinally many links.

### L3 human

Special models let arguments that would use saturated models, and hence the generalized continuum hypothesis, be carried out in ZFC alone.
The isomorphism of elementary extensions in the last basic property is a weak form of the [[Keisler-Shelah isomorphism theorem|A37HPCKCE2]], which gives isomorphic ultrapowers.
In stability theory and in work on [[Keisler's order|TD5D2G5PYP]], special models are one of the tools for working with large saturated-like models without extra axioms.
