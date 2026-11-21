---
tag: F30ZVR4AD5
kind: concept
name: Universal model
aliases: [universal-structure, kappa-universal-model]
msc: ["03C50"]
topics: [Z772KEC9BY]
audience: grad
uses: [983GZBQYT4, P3B1V182N4, CGH8C8EA9N, 0EBACQFAZW, RMTZ5J64FX]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 4
  - book: isbn:9780521587136
---

## Summary

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The structure $\mathcal{M}$ is *$\kappa$-universal* when every structure $\mathcal{N}$ [[elementarily equivalent|P3B1V182N4]] to $\mathcal{M}$ with $\abs{N} < \kappa$ has an [[elementary embedding|CGH8C8EA9N]] into $\mathcal{M}$.
It is *universal* when it is $\abs{M}^+$-universal, so that every model of its theory of size at most $\abs{M}$ embeds elementarily into it.
A universal model is a largest model of its size: it contains a copy of every other one.
[[Saturated models|RMTZ5J64FX]] are universal, and in the countable case saturation is the same as universality together with homogeneity.

## Motivation

Many classical structures contain copies of all structures of a kind.
The rational order contains a copy of every countable linear order, and an algebraically closed field of infinite transcendence degree $\kappa$ contains a copy of every algebraically closed field of the same characteristic and of size at most $\kappa$.
Universality asks for this property among the models of a complete theory, with elementary embeddings as the copies.

## Notation

Some authors write $\kappa$-universal for what is called $\kappa^+$-universal here, so that the bound on $\abs{N}$ is $\le \kappa$ instead of $< \kappa$.
The definition must be checked in each source.

## Remarks

### Examples

- The order $(\Q, <)$ is universal, since every countable dense order without endpoints is isomorphic to it; see [[the rational order is saturated|9H064SE6ZN]].
- An algebraically closed field of infinite transcendence degree $\kappa$ is universal; see [[saturated algebraically closed fields|QX6K7CWWNV]].
- Every $\kappa$-saturated structure is $\kappa^+$-universal, by the forth half of the proof of [[uniqueness of saturated models|DZ65A6X12W]].
- A [[special model|CBNPB0QZGQ]] is universal.

### Non-examples

- The field $\overline{\Q}$ is not universal, since $\Q(t)^{\mathrm{alg}}$ does not embed elementarily into it; see [[the algebraic numbers are not saturated|9JGR3GXPMK]].
- The order $(\Z, <)$ is not universal, since two copies of $\Z$ in a row do not embed elementarily into it; see [[the integer order is homogeneous but not saturated|YNSR6VMS8A]].

### Basic properties

- A $\kappa$-universal structure realizes every type over $\emptyset$ that is realized in some model of its theory of size less than $\kappa$.
- A countable structure is saturated exactly when it is homogeneous and universal; the proof is in the [[definition|J6ZSWZ0CC1]].
- So a countable complete theory with a countable universal model has only countably many types over $\emptyset$ in each number of variables, since a countable model realizes only countably many types.
- If $\mathcal{M}$ is $\kappa$-universal and $\mathcal{M} \preceq \mathcal{M}'$, then $\mathcal{M}'$ is $\kappa$-universal, since elementary embeddings compose.

### History

Morley and Vaught introduced universal models together with homogeneous and saturated models in their 1962 paper on homogeneous universal models.

### Common errors

- Using embeddings in place of elementary embeddings: $(\Q, <)$ embeds every countable linear order, but the elementary embeddings come only from models of the theory of dense orders.
- Expecting universal models in every size: for unstable theories their existence can depend on cardinal arithmetic, as for saturated models.

## Explanations

### L1 human

A universal model is one that contains a faithful copy of every other model of the same theory that is not larger.
The rational numbers are universal among countable dense orders: every such order is a copy of them.

### L2 human

We check that $(\Q, <)$ realizes the type over $\emptyset$ of every element of a countable dense order $D$ without endpoints.

1. By Cantor's theorem, $D \cong (\Q, <)$, so there is an elementary embedding $g : D \to \Q$.
2. An elementary embedding preserves every formula, so $g(d)$ has the same type as $d$.

The typical use is to move a configuration from an arbitrary model into one fixed universal model.
The trap is to use a structure that is only universal for embeddings: $(\Q, <)$ is universal for countable linear orders as an order, but $(\Z, <)$ does not embed into it elementarily, since the theories differ.

### L3 human

Universality and homogeneity are the two halves of saturation.
A universal model contains every small model, and a homogeneous model moves equivalent configurations onto each other.
Together they give the uniqueness of saturated models and the existence of a fixed universe, the [[monster model|EYTTQZ0E1S]].
For unstable theories, the existence of universal models of a given size can depend on set-theoretic hypotheses beyond the axioms of set theory.
