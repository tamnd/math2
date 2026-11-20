---
tag: E5W3RRSY5Z
kind: statement
role: theorem
name: Vaught's never-two theorem
aliases: [vaught-never-two-theorem, never-two-theorem]
msc: ["03C15", "03C35"]
topics: [6XEXRME4C1]
audience: grad
uses: [A22K1X8GKD, 655K8Y7VS8, W6XM5NVNRP, S8W40PYNHX, RMTZ5J64FX, 01TQB88H4C]
about: [A22K1X8GKD]
history:
  first_stated: "Robert Vaught, 1961"
sources:
  - url: https://en.wikipedia.org/wiki/Vaught_conjecture
  - book: isbn:9780387987606
  - book: isbn:9780521587136
---

## Statement

Let $T$ be a [[complete theory|655K8Y7VS8]] with infinite models in a countable signature.
Then $T$ does not have exactly two [[countable|01TQB88H4C]] models up to isomorphism.

The proof is [[here|94T8C8QJ8W]].

## Remarks

### Why each hypothesis is needed

- Completeness. Let $L = \set{P}$ with $P$ unary, and let $T$ say that there are infinitely many elements and that either every element is in $P$ or no element is. $T$ is not complete, and it has exactly two countable models.
- Countable signature. The proof uses the omitting types theorem and counts types; both steps need a countable signature.

### Consequences

- A complete theory with finitely many countable models, but more than one, is [[small|W6XM5NVNRP]], and its [[prime model|S8W40PYNHX]] and countable [[saturated model|RMTZ5J64FX]] are two different countable models.
- The proof shows that the countable saturated model of such a theory has a third model below it, so the number of countable models is $1$ or at least $3$.

### Converse

Every other finite number occurs.
[[Ehrenfeucht's theory|XT2D23G98S]] has exactly three countable models, and a version with $m$ colors has exactly $m + 2$.
So the possible finite numbers of countable models are $1, 3, 4, 5, \dots$

### Generalizations

The number of countable models of a complete countable theory is $1$, a finite number at least $3$, $\aleph_0$, $\aleph_1$ or $2^{\aleph_0}$.
[[Morley's theorem on countable models|JFG783DEG8]] rules out every infinite number strictly between $\aleph_1$ and $2^{\aleph_0}$.
The [[Vaught conjecture|YVBHE2SEE6]] asks whether $\aleph_1$ can be ruled out too.

## History

Robert Vaught proved the theorem in 1961, in his paper on denumerable models of complete theories.

## Explanations

### L1 human

Count the different countable worlds that a complete set of rules describes.
The count can be one, as for the rational order.
It can be three, four, or any larger finite number, or infinite.
Vaught's theorem says that it is never exactly two.
The reason is that two different countable worlds force a third one between them.

### L2 human

We see the third model in Ehrenfeucht's theory, where the prime model $M_0$ and the saturated model $M_s$ appear.

1. In $M_0$ the constants $c_0 < c_1 < \cdots$ are unbounded.
2. In $M_s$ they are bounded and have no least upper bound.
3. Naming one element $a$ above all constants gives a theory whose prime model is a third model: there $a$ is the least upper bound of the constants.

The typical use is a quick check: if a construction seems to give exactly two countable models, something is missing.
A trap is to apply the theorem to incomplete theories, where two is possible.
