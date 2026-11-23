---
tag: J0Z2GNJZ2W
kind: concept
name: Beta-model
msc: ["03B30", "03C62"]
topics: [BY8AAFN7C5]
audience: grad
uses: [Y92NXGEQBD, M6JGF4TPM6, 01CGSJ0GNQ, MKB74TX3Z8, NS1HWGTD8E]
sources:
  - url: https://en.wikipedia.org/wiki/Beta-model
    locator: In analysis
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: ω-models and β-models
same_as:
  wikidata: Q114901462
  wikipedia: Beta-model
inventory: [3VZR3CSYKY]
---

## Summary

There is a computable infinite binary tree with no computable path, so the computable sets miss a witness to the true statement "this tree has a path".
A *β-model* is an $\omega$-model that never misses a witness of this kind.
Precisely, an $\omega$-model $(\mathbb{N}, \mathcal{S})$ of the language of [[second-order arithmetic|Y92NXGEQBD]] is a β-model when, for every $\Sigma^1_1$ formula $\varphi$ of the [[analytical hierarchy|M6JGF4TPM6]] with parameters from $\mathcal{S}$:
$$(\mathbb{N}, \mathcal{S}) \models \varphi \iff (\mathbb{N}, \mathcal{P}(\mathbb{N})) \models \varphi.$$
For $\omega$-models of $\mathsf{ACA}_0$, this is the same as being correct about which countable linear orders in $\mathcal{S}$ are [[well-orderings|01CGSJ0GNQ]].

## Motivation

An $\omega$-model has the true natural numbers, so it is correct about every arithmetical formula.
It can still be wrong about formulas with set quantifiers, because it may lack the sets that witness them.
A β-model is the next level of correctness: it contains a witness for every true $\Sigma^1_1$ statement about its own sets.
The statements "$W$ is a well-ordering" and "this tree has no infinite path" are $\Pi^1_1$, so β-models judge them correctly.

## Notation

The name is also written "beta-model".
We write $\mathcal{P}(\mathbb{N})$ for the family of all subsets of $\mathbb{N}$, so $(\mathbb{N}, \mathcal{P}(\mathbb{N}))$ is the full model.
A *countable coded β-model* is a set $M$ whose columns $M_k = \{ n : (n, k) \in M \}$ form the family $\mathcal{S}$ of a β-model.

## Remarks

### The computable sets miss a path

Let $T$ be a computable infinite binary tree with no computable path, such as a [[separation tree|7W9EG02T79]] for two computably inseparable sets.
The sentence "there is a $Y$ that is a path through $T$" is $\Sigma^1_1$ with a computable parameter.
It is true in the full model, by weak König's lemma, but false in the $\omega$-model of the [[computable sets|F5T3F7E0H1]].
So the computable sets do not form a β-model.

### The arithmetical sets miss a hierarchy

The [[arithmetical sets|9KPCZ6NA32]] contain a path through every infinite computable tree that is finitely branching.
They still fail to be a β-model.
The $\Sigma^1_1$ sentence "the hierarchy of jumps along $\omega$ exists" is true, but it has no arithmetical witness, by the [[ω-th jump example|MF6AG57W3W]].

### Countable β-models exist

The [[full model|CAA7K3VF59]] is a β-model.
A [[countable elementary substructure of the full model|MZXJDE7M7K]] is a countable β-model, by the Löwenheim-Skolem theorem.
Such a model is not given effectively: it must contain a witness for each true $\Sigma^1_1$ sentence about its own sets.

### Every β-model satisfies ATR0

Let $(\mathbb{N}, \mathcal{S})$ be a β-model.
For an arithmetical $\varphi(n)$ with parameters in $\mathcal{S}$, the $\Sigma^1_1$ sentence $\exists Y\, \forall n\, (n \in Y \leftrightarrow \varphi(n))$ is true, so it has a witness in $\mathcal{S}$.
So arithmetical comprehension holds.
If $\mathcal{S}$ takes $W$ for a well-ordering, then $W$ is a true well-ordering, since "$W$ has a descending sequence" is $\Sigma^1_1$.
The $\Sigma^1_1$ sentence "there is a hierarchy along $W$ for $\theta$" is then true, so it has a witness in $\mathcal{S}$, and [[ATR0|MKB74TX3Z8]] holds.

### Relation to other systems

Every β-model contains every [[hyperarithmetical|NS1HWGTD8E]] set, since every $\omega$-model of $\mathsf{ATR}_0$ does.
The hyperarithmetical sets do not form a β-model, because they do not form a model of $\mathsf{ATR}_0$.
Over $\mathsf{ACA}_0$, [[Π¹₁-CA0|T21WETAHN5]] is equivalent to the statement that every set belongs to a countable coded β-model.

### Watch out

An $\omega$-model of $\mathsf{ATR}_0$ need not be a β-model.
It can contain a linear order that it takes for a well-ordering, while a descending sequence exists outside the model.
In set theory, the term β-model has a related meaning: a model of set theory that is correct about well-foundedness.

### History

Andrzej Mostowski introduced the notion of a β-model, as a strengthening of the notion of an $\omega$-model.

### Try it

First, is every β-model a model of $\mathsf{ACA}_0$?
Yes: as shown above, each instance of arithmetical comprehension is a true $\Sigma^1_1$ sentence, so it has a witness in the model.

Second, if a theory has a β-model, must its $\Pi^1_1$ theorems be true?
Yes: a β-model is correct about $\Pi^1_1$ sentences too, by negation, so each $\Pi^1_1$ theorem true in it is true in the full model.

## Explanations

### L1 human

A β-model is a family of sets that never makes a mistake about whether an order is a well-ordering.
Whenever some set with an arithmetical property exists, a set with that property is already in the family.
The computable sets fail this test, because some computable tree has a path but no computable path.

### L2 human

To show that a family $\mathcal{S}$ is not a β-model, find a true $\Sigma^1_1$ statement about a set in $\mathcal{S}$ with no witness in $\mathcal{S}$.
To build a countable β-model, take a countable elementary substructure of the full model.
β-models are the right tool for theorems about well-orderings, because in them the meaning of "well-ordering" is the true one.

### L3 human

A β-model is correct about $\Pi^1_1$ sentences too, by negation.
So if a theory has a β-model, then every $\Pi^1_1$ theorem of the theory is true.
The existence of countable coded β-models is the main tool for the study of $\Pi^1_1\text{-}\mathsf{CA}_0$ and stronger systems.
