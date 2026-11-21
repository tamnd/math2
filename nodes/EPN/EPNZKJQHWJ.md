---
tag: EPNZKJQHWJ
kind: concept
name: Rigid structure
aliases: [rigid-model, rigidity-model-theory]
msc: ["03C50", "08A35"]
topics: [Z772KEC9BY]
audience: grad
uses: [983GZBQYT4, DSQ17TNW1C, 0K1SCPBNKJ, RMTZ5J64FX, DKAGC639W9]
sources:
  - url: https://en.wikipedia.org/wiki/Rigidity_(mathematics)
    locator: Examples
  - book: isbn:9780521587136
---

## Summary

An $L$-[[structure|983GZBQYT4]] $\mathcal{M}$ is *rigid* when its only [[automorphism|DSQ17TNW1C]] is the identity, so that its [[automorphism group|0K1SCPBNKJ]] is trivial.
The order $(\N, <)$, every well-order, the ring $\Z$ and the field $\R$ are rigid, while $(\Z, <)$ and the field $\C$ are not.
Rigidity is the opposite of homogeneity: in a rigid structure no two different tuples are in the same orbit, even when they have the same type.
No infinite [[saturated|RMTZ5J64FX]] structure is rigid, and every complete theory with infinite models has models that are not rigid.

## Motivation

The automorphisms of a structure are its symmetries, and many structures of everyday mathematics have none.
The real field has no automorphism except the identity, although its elements outside the real algebraic numbers cannot be named by formulas without parameters.
So rigidity and definability are different: rigidity says that every element is fixed by every symmetry, and definability says that a formula names it.
Comparing the two notions shows how far a structure is from the large saturated models, where they agree.

## Notation

The automorphism group is $\operatorname{Aut}(\mathcal{M})$, and $\mathcal{M}$ is rigid when $\operatorname{Aut}(\mathcal{M}) = \set{\mathrm{id}}$.
Some authors call a structure rigid when it has no nontrivial automorphisms and no nontrivial self-embeddings; this stronger notion is not used here.

## Remarks

### Examples

- The order $(\N, <)$ is rigid; see [[the natural number order is rigid|QKQMRRDC60]].
- The field $\R$ is rigid; see [[the real field is rigid|ND6BPSVNC7]].
- Every well-order is rigid: an automorphism $\sigma \ne \mathrm{id}$ has a least element $a$ with $\sigma(a) \ne a$, and both $\sigma(a) < a$ and $a < \sigma(a)$ lead to a contradiction with the leastness.
- The ring $\Z$ and the field $\Q$ are rigid, since an automorphism fixes $1$ and so every element built from $1$.

### Non-examples

- The order $(\Z, <)$ is not rigid, since $x \mapsto x + 1$ is an automorphism; see [[the integer order is homogeneous but not saturated|YNSR6VMS8A]].
- The field $\C$ is not rigid, since complex conjugation is an automorphism; see [[conjugate complex numbers|Y9XAHREJ8W]].

### Basic properties

- If every element of $\mathcal{M}$ is in $\operatorname{dcl}(\emptyset)$, then $\mathcal{M}$ is rigid, since automorphisms fix [[definable|DKAGC639W9]] elements. The converse fails for the field $\R$.
- An infinite saturated structure is not rigid: it realizes a type over $\emptyset$ that is not algebraic, this type has a second realization, and strong homogeneity gives an automorphism that exchanges them.
- Every complete theory with infinite models has a model with a nontrivial automorphism, built from a sequence of indiscernibles indexed by $(\Z, <)$ and moved by the shift.
- So rigidity is a property of a structure and not of its theory: $(\N, <)$ is rigid, and its nonstandard elementary extensions are not.

### History

Rigidity of classical structures, such as the real field, is a standard topic of algebra and model theory.
The use of indiscernible sequences to build models with many automorphisms goes back to Ehrenfeucht and Mostowski.

### Common errors

- Concluding that every element of a rigid structure is definable: in the field $\R$, the number $\pi$ is fixed by every automorphism, and it is not definable without parameters.
- Thinking that rigidity of a model is preserved by elementary extensions: saturated extensions are never rigid.

## Explanations

### L1 human

A structure is rigid when it has no symmetries except doing nothing.
The natural numbers with their order are rigid: $0$ is the least element and must stay in place, then $1$ must stay in place, and so on.
The integers with their order are not rigid, since shifting everything by one is a symmetry.

### L2 human

We show that the ordinal $\omega + \omega$ is rigid.

1. Let $\sigma$ be an automorphism and suppose $\sigma \ne \mathrm{id}$. Let $a$ be the least element with $\sigma(a) \ne a$.
2. If $\sigma(a) < a$, then $\sigma(\sigma(a)) = \sigma(a)$ by leastness, and injectivity of $\sigma$ gives $\sigma(a) = a$, a contradiction.
3. If $a < \sigma(a)$, then $a = \sigma(b)$ for some $b$, and $b \ne a$. If $b < a$, then $\sigma(b) = b \ne a$; if $a < b$, then $\sigma(a) < \sigma(b) = a$. Both contradict the assumptions.

The typical use is to recognize structures without symmetries.
The trap is to infer rigidity of a theory from one rigid model.

### L3 human

In a [[monster model|EYTTQZ0E1S]], an element is fixed by all automorphisms over a small set $A$ exactly when it is in $\operatorname{dcl}(A)$.
So the gap between rigidity and definability, as in the real field, disappears in saturated models.
Rigid structures and structures with prescribed automorphism groups are studied in combinatorics and in descriptive set theory as well.
