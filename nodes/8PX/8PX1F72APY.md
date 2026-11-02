---
tag: 8PX1F72APY
kind: definition
name: Symbolic dynamics
msc: [37B10]
defines: EWFWTSVY0B
uses: [A1XE59ZHNM, 5X6E97EMFR, AEXJNRBASV, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Symbolic_dynamics
---

## Definition

Let $\mathcal{A}$ be a finite alphabet and let $\sigma(x)_i = x_{i+1}$ be the shift map on $\mathcal{A}^{\Z}$.
A *symbolic dynamical system* is a pair $(X, \sigma_X)$ where $X \subseteq \mathcal{A}^{\Z}$ is a [[shift space|A1XE59ZHNM]] and $\sigma_X$ is the restriction of $\sigma$ to $X$.
One-sided versions use $\mathcal{A}^{\N}$.
*Symbolic dynamics* is the part of [[topological dynamics|5X6E97EMFR]] that studies symbolic dynamical systems and the maps between them that commute with the shifts.
It also studies codings: given a [[continuous map|0VGFHTM75Y]] $T \colon M \to M$ and a partition $M = P_0 \cup \cdots \cup P_{k-1}$, the *itinerary* of $x \in M$ is the sequence $(a_n)_{n \ge 0}$ with $T^n(x) \in P_{a_n}$.

## Remarks

The itinerary map $x \mapsto (a_n)$ turns $T$ into the shift: the itinerary of $T(x)$ is the shifted itinerary of $x$.
A coding is rarely continuous, since a connected space cannot be split into finitely many disjoint nonempty open pieces.
Instead one often has a continuous surjection $\pi$ from a shift space onto $M$ with $\pi \circ \sigma = T \circ \pi$, a [[semiconjugacy|AEXJNRBASV]] that sends a sequence to a point with that itinerary.
Example: for the doubling map $T(x) = 2x \bmod 1$ on $[0, 1)$ with $P_0 = [0, 1/2)$ and $P_1 = [1/2, 1)$, the itinerary of $x$ is its binary expansion $x = \sum_{n \ge 0} a_n 2^{-n-1}$ that does not end in all $1$s.
Indeed $T$ deletes the first binary digit, and the first digit is $0$ exactly when $x \in P_0$.
Here $\pi(a) = \sum_{n \ge 0} a_n 2^{-n-1}$ is a semiconjugacy from the one-sided full shift on $\set{0, 1}$ onto the circle $\R / \Z$.
Non-example: a coding with the single region $P_0 = M$ gives the constant itinerary $000\ldots$ for every point, so it records nothing about the dynamics.

## Explanations

### L1 human

Symbolic dynamics studies systems whose states are infinite words, moved by deleting or shifting letters, and uses them as codes for other systems.
