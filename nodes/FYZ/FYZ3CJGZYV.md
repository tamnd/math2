---
tag: FYZ3CJGZYV
kind: statement
role: theorem
name: Lindström's theorem
msc: [03C95, 03B10]
uses: [086QKPF0A6, 1NR3HAWG9D, 484M0TZ1S7, 983GZBQYT4, DKFGQTRYZE]
about: [086QKPF0A6]
sources:
  - url: https://en.wikipedia.org/wiki/Lindström's_theorem
same_as:
  wikidata: Q2379128
  wikipedia: Lindström's theorem
---

## Statement

Let $\mathcal{L}$ be a regular abstract logic that extends [[first-order logic|086QKPF0A6]].
Regular means that $\mathcal{L}$ is closed under the Boolean connectives, existential quantification, renaming of symbols and relativization.
Suppose that $\mathcal{L}$ has the following two properties.

1. Compactness: a set of $\mathcal{L}$-sentences has a model whenever each of its finite subsets has a model.
2. Downward Löwenheim–Skolem property: each $\mathcal{L}$-sentence with an infinite model has a countable model.

Then each $\mathcal{L}$-sentence is equivalent to a first-order [[sentence|DKFGQTRYZE]], that is, it has the same models.

## Remarks

The proof argues by contradiction with Ehrenfeucht–Fraïssé games.
If an $\mathcal{L}$-sentence $\varphi$ is not first-order, then for each $n$ there are [[structures|983GZBQYT4]] $\mathcal{A}_n \models \varphi$ and $\mathcal{B}_n \models \neg\varphi$ that satisfy the same first-order sentences of quantifier depth $n$.
Compactness and the Löwenheim–Skolem property, applied to an $\mathcal{L}$-sentence coding these pairs and partial isomorphisms between them, give countable $\mathcal{A} \models \varphi$ and $\mathcal{B} \models \neg\varphi$ with a back-and-forth system.
Then $\mathcal{A} \cong \mathcal{B}$, which contradicts $\mathcal{A} \models \varphi$ and $\mathcal{B} \models \neg\varphi$.

Example: second-order logic is a regular extension of first-order logic that is not equivalent to it.
By the theorem, it must lack the [[compactness theorem|1NR3HAWG9D]] or the [[Löwenheim–Skolem theorem|484M0TZ1S7]]; in fact it lacks both.
The infinitary logic $L_{\omega_1\omega}$ has the Löwenheim–Skolem property, so it must fail compactness, and it does.

## Explanations

### L1 human

First-order logic has two famous properties: compactness and the Löwenheim–Skolem property.
Lindström's theorem says that no stronger logic keeps both.
So these two properties characterise first-order logic among all reasonable logics.

### L2 human

The theorem, proved by Per Lindström in 1969, founded abstract model theory, which compares logics by their properties.
It explains why first-order logic is the default logic of model theory: any gain in expressive power costs compactness or the Löwenheim–Skolem theorem.
