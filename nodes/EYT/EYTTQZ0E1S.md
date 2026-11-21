---
tag: EYTTQZ0E1S
kind: concept
name: Monster model
aliases: [monster-model-convention, universal-domain]
msc: ["03C50", "03C45"]
topics: [Z772KEC9BY]
audience: grad
uses: [655K8Y7VS8, RMTZ5J64FX, 4NJS7W57VK, F30ZVR4AD5, 0EBACQFAZW, NW4DREQ5DQ, DSQ17TNW1C]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: Motivation
  - book: isbn:9780387987606
    locator: Chapter 4
---

## Summary

Let $T$ be a [[complete|655K8Y7VS8]] theory with infinite models in a language $L$.
A *monster model* of $T$ is a model $\mathbb{M}$ that is $\bar{\kappa}$-[[saturated|RMTZ5J64FX]] and strongly $\bar{\kappa}$-[[homogeneous|4NJS7W57VK]] for a [[cardinal|0EBACQFAZW]] $\bar{\kappa}$ larger than every set that a given argument needs.
A set of size less than $\bar{\kappa}$ is *small*.
By convention, every model of $T$ under discussion is a small elementary substructure of $\mathbb{M}$, every parameter set is small, and every type over a small set is realized in $\mathbb{M}$.
The monster model is the fixed universe of stability theory, in which types over small sets are orbits of automorphisms.

## Motivation

Proofs in model theory pass to elementary extensions again and again: to realize a type, to extend a map, to find an automorphism.
Keeping track of all these extensions is tedious.
A monster model does all of them at once: every small model sits inside it, every type over a small set is realized in it, and every small partial elementary map extends to an automorphism of it.
Algebraic geometers made the same choice when they worked in one universal domain, a large algebraically closed field.

## Notation

The monster model is written $\mathbb{M}$, $\mathfrak{C}$ or $\mathfrak{M}$, and $\bar{\kappa}$ is its saturation.
One writes $\models \varphi(\bar{a})$ for $\mathbb{M} \models \varphi(\bar{a})$, and $\operatorname{Aut}(\mathbb{M}/A)$ for the automorphisms that fix a small set $A$ pointwise.

## Remarks

### Examples

- For algebraically closed fields of characteristic $p$, a saturated algebraically closed field of large transcendence degree is a monster model; see [[a monster model of algebraically closed fields|PQZD703FGC]].
- For dense linear orders, a saturated dense order of inaccessible size is a monster model; see [[a monster model of dense linear orders|PPZTWMEFTQ]].
- The field $\C$ is a monster model of $\mathrm{ACF}_0$ for countable parameter sets, since it is saturated of size $2^{\aleph_0}$; see [[saturated algebraically closed fields|QX6K7CWWNV]].

### Non-examples

- The order $(\R, <)$ is not $\aleph_1$-saturated, so it cannot serve as a monster model for countable parameter sets; see [[the real order is not special|TXSS2XTE2T]].
- The order $(\Q, <)$ is saturated, but its small sets are the finite sets, and no model of the theory is small. So it does not contain the models under discussion.

### Basic properties

- $\abs{\mathbb{M}} \ge \bar{\kappa}$, since the type $\set{x \ne a : a \in A}$ over a small set $A$ is realized.
- Every model of $T$ of size less than $\bar{\kappa}$ is isomorphic to an elementary substructure of $\mathbb{M}$, since $\bar{\kappa}$-saturated models are $\bar{\kappa}$-[[universal|F30ZVR4AD5]].
- For small $A$, two tuples have the same type over $A$ exactly when an automorphism over $A$ maps one to the other; see [[types as orbits|7WH24MZZQ8]].
- For small $A$, a definable set is definable over $A$ exactly when every [[automorphism|DSQ17TNW1C]] over $A$ maps it onto itself.
- If $\bar{\kappa}$ is an [[inaccessible cardinal|NW4DREQ5DQ]] larger than $\abs{L}$, then a saturated model of size $\bar{\kappa}$ exists and is a monster model, by [[existence of saturated models|GSQ833HAZT]] and [[uniqueness of saturated models|DZ65A6X12W]].
- In ZFC alone, for every cardinal $\kappa$, $T$ has a $\kappa$-saturated and strongly $\kappa$-homogeneous model, which is enough for each fixed argument.

### History

The convention of working inside one large saturated model became standard in stability theory.
It continues the universal domains of algebraic geometry.

### Common errors

- Treating $\mathbb{M}$ itself as small: the type $\set{x \ne a : a \in \mathbb{M}}$ is not realized in $\mathbb{M}$.
- Assuming that a saturated model of size $\bar{\kappa}$ exists for every $\bar{\kappa}$: for unstable theories this depends on cardinal arithmetic, and the ZFC version uses $\bar{\kappa}$-saturated, strongly $\bar{\kappa}$-homogeneous models instead.

## Explanations

### L1 human

The monster model is one very large model of a theory that contains all the smaller models one cares about.
Inside it, any element that could exist does exist, and any two configurations that look the same are moved onto each other by a symmetry.
Model theorists fix it once and then work inside it, as geometers work inside one large field.

### L2 human

We show that in $\mathbb{M}$ an element $b \notin \operatorname{acl}(A)$ has infinitely many images under $\operatorname{Aut}(\mathbb{M}/A)$, for small $A$.

1. Every formula of $\operatorname{tp}(b/A)$ has infinitely many solutions, since $b \notin \operatorname{acl}(A)$.
2. For distinct realizations $b_1, \dots, b_k$ of $\operatorname{tp}(b/A)$, the set $\operatorname{tp}(b/A) \cup \set{x \ne b_i : i \le k}$ is finitely satisfiable, by step 1.
3. It is a set of formulas over the small set $A \cup \set{b_1, \dots, b_k}$, so a new realization exists in $\mathbb{M}$.
4. Each realization is the image of $b$ under an automorphism over $A$, by strong homogeneity.

The typical use is to turn compactness arguments into statements about automorphisms.
The trap is to apply such arguments to a set that is not small.

### L3 human

The monster model hides the set theory of saturated models behind a convention.
Results proved inside $\mathbb{M}$ for small sets do not depend on the choice of $\mathbb{M}$, since any two monster models of large enough saturation contain isomorphic copies of the small configurations.
Galois theory of definable sets, forking and stable groups are all developed inside $\mathbb{M}$; see [[algebraic and definable closure|DKAGC639W9]] and [[stable theory|T7JW5QY6KR]].
