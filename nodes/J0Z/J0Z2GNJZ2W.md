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

A *β-model* is an $\omega$-model $(\N, \mathcal{S})$ of the language of [[second-order arithmetic|Y92NXGEQBD]] that is correct about every $\Sigma^1_1$ formula of the [[analytical hierarchy|M6JGF4TPM6]] with parameters from $\mathcal{S}$.
That is, such a formula is true in $(\N, \mathcal{S})$ if and only if it is true in the full model $(\N, \mathcal{P}(\N))$.
For $\omega$-models of $\mathsf{ACA}_0$, this is the same as being correct about which countable linear orders in $\mathcal{S}$ are [[well-orderings|01CGSJ0GNQ]].
The letter β comes from the French "bon ordre", which means well-ordering.

## Motivation

An $\omega$-model has the true natural numbers, so it is correct about every arithmetical formula.
It can still be wrong about formulas with set quantifiers, because it may lack the sets that witness them.
A β-model is the next level of correctness: it contains a witness for every true $\Sigma^1_1$ statement about its own sets.
The statements "$W$ is a well-ordering" and "this tree has no infinite path" are $\Pi^1_1$, so β-models judge them correctly.

## Remarks

### Examples

- The [[full model|CAA7K3VF59]] $(\N, \mathcal{P}(\N))$ is a β-model.
- A [[countable elementary substructure of the full model|MZXJDE7M7K]] is a countable β-model.

### Non-examples

- The [[computable sets|F5T3F7E0H1]] do not form a β-model. The Kleene tree is a computable infinite binary tree with a path, but with no computable path.
- The [[arithmetical sets|9KPCZ6NA32]] do not form a β-model. The $\Sigma^1_1$ sentence "the hierarchy of jumps along $\omega$ exists" is true, but it has no arithmetical witness, by the [[ω-th jump example|MF6AG57W3W]].

### Basic properties

- Every β-model is a model of [[ATR0|MKB74TX3Z8]].
  For an arithmetical formula $\varphi(n)$ with parameters in $\mathcal{S}$, the $\Sigma^1_1$ sentence $\exists Y\, \forall n\, (n \in Y \leftrightarrow \varphi(n))$ is true, so it has a witness in $\mathcal{S}$, and arithmetical comprehension holds.
  If $\mathcal{S}$ thinks that $W$ is a well-ordering, then $W$ is a true well-ordering, since "$W$ has a descending sequence" is $\Sigma^1_1$.
  Then the $\Sigma^1_1$ sentence "there is a hierarchy along $W$ for $\theta$" is true, so it has a witness in $\mathcal{S}$.
- Every β-model contains every [[hyperarithmetical|NS1HWGTD8E]] set, since every $\omega$-model of $\mathsf{ATR}_0$ does. The hyperarithmetical sets do not form a β-model, because they do not form a model of $\mathsf{ATR}_0$.
- $\Pi^1_1\text{-}\mathsf{CA}_0$ is equivalent over $\mathsf{ACA}_0$ to the statement that every set belongs to a countable coded β-model.

### History

Andrzej Mostowski introduced the notion of a β-model in 1959, as a strengthening of the notion of an $\omega$-model.

### Common errors

- An $\omega$-model of $\mathsf{ATR}_0$ need not be a β-model: it can contain a linear order that it thinks is a well-ordering, while a descending sequence exists outside the model.
- In set theory, the term β-model has a related meaning for models of set theory that are correct about well-foundedness.

## Explanations

### L1 human

A β-model is a family of sets that never makes a mistake about whether an order is a well-ordering.
Whenever some set with an arithmetical property exists, a set with that property is already in the family.

### L2 human

To show that a family $\mathcal{S}$ is not a β-model, one finds a true $\Sigma^1_1$ statement about a set in $\mathcal{S}$ with no witness in $\mathcal{S}$.
To build a countable β-model, one takes a countable elementary substructure of the full model.
β-models are the right tool for theorems about well-orderings, because in them the meaning of "well-ordering" is the true one.

### L3 human

A β-model is correct about $\Pi^1_1$ sentences too, by negation.
So if a theory has a β-model, then every $\Pi^1_1$ theorem of the theory is true.
The existence of countable coded β-models is the main tool for the study of $\Pi^1_1\text{-}\mathsf{CA}_0$ and stronger systems.
