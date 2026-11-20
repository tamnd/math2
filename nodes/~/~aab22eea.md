---
tag: ~aab22eea
kind: example
name: Groups form a basic elementary class in two signatures
msc: ["03C52", "20A05"]
topics: [AY09KYSW81]
audience: ug2
instance_of: [MEC3ZMC4F1, ~8205aea8]
uses: [MEC3ZMC4F1, ~8205aea8, G5S1M9, CBKC2DMXEQ, 676H7EGTKJ, ~ad0fa7f2]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: Examples
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Example

We check that the class of [[groups|G5S1M9]] is a basic [[elementary class|MEC3ZMC4F1]] in each of the signatures $L_1 = \set{\cdot, {}^{-1}, e}$ and $L_2 = \set{\cdot}$, so that the theory of groups is [[finitely axiomatizable|~8205aea8]] in both.

1. In $L_1$, let $\gamma_1$ be the conjunction of $\forall x \, \forall y \, \forall z \, ((x \cdot y) \cdot z = x \cdot (y \cdot z))$, $\forall x \, (x \cdot e = x \land e \cdot x = x)$ and $\forall x \, (x \cdot x^{-1} = e \land x^{-1} \cdot x = e)$. Its models are exactly the groups with their inverse map and identity.
2. In $L_2$, let $\gamma_2$ be the conjunction of associativity and $\exists u \, (\forall x \, (x \cdot u = x \land u \cdot x = x) \land \forall x \, \exists y \, (x \cdot y = u \land y \cdot x = u))$. Its models are exactly the sets with a binary operation that make a group.
3. Each model of $\gamma_2$ has a unique identity and unique inverses, so it has exactly one expansion to a model of $\gamma_1$. Conversely, the [[reduct|~ad0fa7f2]] to $L_2$ of a model of $\gamma_1$ is a model of $\gamma_2$.
4. So both classes are basic elementary, and they correspond to each other by reducts and expansions.

## Remarks

The choice of signature changes the [[substructures|676H7EGTKJ]].
In $L_1$ every substructure of a group is a subgroup, because $\gamma_1$ is a universal sentence.
In $L_2$ the set $\N$ is a substructure of $(\Z, +)$ that is not a group, because $\gamma_2$ is not universal.
The two presentations are compared in more detail in [[this example|CBKC2DMXEQ]].
Abelian groups, rings, fields, linear orders and dense linear orders without endpoints are further basic elementary classes in their usual signatures.

## Explanations

### L1 human

A group is a set with a multiplication that is associative, has an identity element and has inverses.
These three rules are a short, finite list of axioms.
We can treat the identity and the inverse as part of the structure, or we can say "there exists an identity" inside the axioms.
Both ways give a finite list.

### L2 human

We check that $(\Z, +)$ satisfies $\gamma_2$, reading $\cdot$ as $+$.

1. Addition of integers is associative.
2. Take $u = 0$: $x + 0 = x$ and $0 + x = x$ for every integer $x$.
3. For each $x$, take $y = -x$: $x + (-x) = 0 = (-x) + x$.

The typical use of the example is as a model for finite axiomatizations of algebraic classes.
A trap is to think that the class depends only on the axioms; it depends also on the signature, as the substructures show.
