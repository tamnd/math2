---
tag: RMTZ5J64FX
kind: concept
name: Saturated model
msc: ["03C50"]
topics: [Z772KEC9BY]
audience: grad
uses: [9V71Q3SD1G, 983GZBQYT4, 0EBACQFAZW, 0G0ASKNA6Z, P3B1V182N4]
sources:
  - url: https://en.wikipedia.org/wiki/Saturated_model
    locator: Definition
  - book: isbn:9780387987606
    locator: Chapter 4
  - book: isbn:9780521587136
same_as:
  wikidata: Q1473532
  wikipedia: Saturated model
---

## Summary

Let $\mathcal{M}$ be an $L$-[[structure|983GZBQYT4]] with domain $M$, and let $\kappa$ be an infinite [[cardinal|0EBACQFAZW]].
The structure $\mathcal{M}$ is *$\kappa$-saturated* when, for every $A \subseteq M$ with $\abs{A} < \kappa$, every complete $1$-[[type|9V71Q3SD1G]] over $A$ is realized in $\mathcal{M}$.
It is *saturated* when it is infinite and $\abs{M}$-saturated, where $\abs{M}$ is the [[cardinality|0G0ASKNA6Z]] of $M$.
So a saturated model realizes every type over every parameter set smaller than itself.
Saturated models of the same theory and size are isomorphic, they contain a copy of every smaller model, and they serve as the large universes in which model theory works.

## Motivation

The rational order has a property that the integer order lacks: every consistent wish over finitely many points, such as "between $1/3$ and $1/2$", is met by some element.
Cantor's back-and-forth proof that countable dense orders are isomorphic uses only this property.
Saturation asks for the same property over every parameter set smaller than the model.
In algebraic geometry, Weil worked in a universal domain, an algebraically closed field of infinite transcendence degree, for the same reason: every configuration that can exist already exists inside it.
Saturated models are the model-theoretic form of this idea.

## Notation

One writes $\kappa$-saturated, and $\omega$-saturated for $\aleph_0$-saturated.
The word "saturated" alone means $\abs{M}$-saturated.
For $\aleph_1$-saturation in nonstandard analysis one also says countable saturation.

## Remarks

### Examples

- The order $(\Q, <)$ is saturated, since each type over a finite set asks for a point in an open interval; see [[the rational order is saturated|9H064SE6ZN]].
- An algebraically closed field of transcendence degree $\kappa$ over its prime field is saturated when $\kappa$ is infinite; see [[saturated algebraically closed fields|QX6K7CWWNV]].
- The [[Rado graph|RMXR0FEF54]] is a countable saturated graph.
- For a countable language, every ultrapower $\mathcal{M}^{\N}/\mathcal{U}$ by a nonprincipal ultrafilter is $\aleph_1$-saturated; see [[saturation of ultraproducts|DYXQP8WS63]].

### Non-examples

- The field $\overline{\Q}$ of algebraic numbers is not $\aleph_0$-saturated, since it omits the transcendental type; see [[the algebraic numbers are not saturated|9JGR3GXPMK]].
- The order $(\Z, <)$ is not $\aleph_0$-saturated, since no element lies at an infinite distance from $0$; see [[the integer order is homogeneous but not saturated|YNSR6VMS8A]].
- The order $(\R, <)$ is $\aleph_0$-saturated but not saturated: it has size $2^{\aleph_0}$ and omits the type of an element just above $0$ over the countable set $\Q$.

### Basic properties

- A $\kappa$-saturated structure realizes every complete or partial $n$-type over fewer than $\kappa$ parameters, for every $n$, by realizing one variable at a time.
- If $\lambda < \kappa$, then $\kappa$-saturated implies $\lambda$-saturated.
- No infinite structure is $\abs{M}^+$-saturated, since the type $\set{x \ne m : m \in M}$ over $M$ is not realized.
- Two saturated models of the same complete theory and the same size are isomorphic; see [[uniqueness of saturated models|DZ65A6X12W]].
- A saturated model is [[universal|F30ZVR4AD5]] and [[strongly homogeneous|4NJS7W57VK]].
- Every structure has a $\kappa^+$-saturated elementary extension, but saturated models need set-theoretic or stability hypotheses; see [[existence of saturated models|GSQ833HAZT]].
- A complete theory with infinite models in a countable signature has a countable saturated model if and only if it is small; see [[countable saturated models of small theories|7GN6XF590M]].

### History

Morley and Vaught introduced saturated models in 1962, in their paper on homogeneous universal models.
They showed that saturated models of the same complete theory and the same size are isomorphic.

### Common errors

- Asking for types over all of $M$: no infinite structure realizes all of them.
- Assuming that every theory has a saturated model in every infinite cardinal: for unstable theories this depends on cardinal arithmetic.
- Confusing $\aleph_0$-saturated with countable and saturated: $(\R, <)$ is $\aleph_0$-saturated, and it is not countable.

## Explanations

### L1 human

A saturated model has no gaps that its own language can describe with a few of its elements.
If a description of an element mentions fewer elements than the model has, and the description is consistent, then such an element already exists in the model.
For example, the rational numbers with their order are saturated.
Given finitely many rationals, a consistent wish such as "between $1/3$ and $1/2$" or "larger than all of them" is met by some rational number.
The integers with their order are not saturated: no integer is "larger than $0$, with infinitely many integers between it and $0$".

### L2 human

We show that $(\R, <)$ is not saturated.

1. The real line has size $2^{\aleph_0} > \aleph_0 = \abs{\Q}$, so saturation would require all types over $\Q$ to be realized.
2. The set $p(x) = \set{0 < x} \cup \set{x < q : q \in \Q, \, q > 0}$ is finitely satisfiable in $\R$: finitely many conditions allow $x$ to be half the smallest $q$.
3. A real $r$ with $0 < r$ has a rational $q$ with $0 < q < r$, so $r$ fails $x < q$, and no real realizes $p$.

The typical use of saturation is to find elements by compactness inside one fixed model.
The trap is to forget the size bound on the parameters: the type over $\Q$ above has countably many parameters, and $\R$ is only $\aleph_0$-saturated.

### L3 human

Saturated models are the model-theoretic counterpart of injective or universal objects: every small model embeds in them, and every small partial elementary map extends to an automorphism.
In stability theory one works inside a [[monster model|EYTTQZ0E1S]], a very saturated model of the theory, so that types become orbits and definable sets become classes.
In nonstandard analysis, $\aleph_1$-saturation gives the countable saturation principle; see [[nonstandard analysis|T28ZZJRDJ6]].
Saturation of ultrapowers leads to [[Keisler's order|TD5D2G5PYP]], which compares theories by how hard their ultrapowers are to saturate.
