---
tag: M15HYQH7KP
kind: example
name: The complex algebra of a two-point frame
msc: ["03G05", "03B45"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [3H85NSFWHK]
uses: [JCP47TNBSD, NGHWZ9Y7ZV, YHGXV3SQDP]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_algebra
    locator: lead section
  - book: isbn:9780521527149
    locator: Chapter 5
---

## Example

Let $W = \set{0, 1}$ and let the [[accessibility relation|YHGXV3SQDP]] be $R = \set{(0, 1)}$.
The complex algebra has the four subsets of $W$, with $\Box X = \set{w : \text{every } R\text{-successor of } w \text{ is in } X}$.
The point $1$ has no successor, so $1 \in \Box X$ for every $X$.
The point $0$ has the single successor $1$, so $0 \in \Box X$ iff $1 \in X$.

| $X$ | $\emptyset$ | $\set{0}$ | $\set{1}$ | $W$ |
|---|---|---|---|---|
| $\Box X$ | $\set{1}$ | $\set{1}$ | $W$ | $W$ |
| $\Diamond X$ | $\emptyset$ | $\emptyset$ | $\set{0}$ | $\set{0}$ |

Here $\Diamond X = \neg \Box \neg X$, the set of points with a successor in $X$.

## Remarks

1. $\Box W = W$, and $\Box$ preserves meets in all six pairs; so this is a [[modal algebra|JCP47TNBSD]].
2. The axiom $\Box p \to p$ fails: $\Box \emptyset = \set{1} \not\subseteq \emptyset$.
   This matches the frame, since the point $1$ is not reflexive.
3. The axiom $\Box p \to \Box \Box p$ holds: $\Box X \subseteq \Box \Box X$ in all four columns.
   This matches the frame, since $R$ is transitive.

## Explanations

### L1 human

There are two worlds, and world $0$ can see world $1$.
World $1$ sees nothing.
"Necessarily $X$" holds at a world when $X$ holds at every world it sees.
At world $1$ this is always true, because it sees no world at all.

### L2 human

1. Compute $\Box \set{0}$: world $0$ sees $1 \notin \set{0}$, so $0 \notin \Box \set{0}$; world $1$ is in it. So $\Box \set{0} = \set{1}$.
2. Compute $\Box \Box \set{0} = \Box \set{1} = W$.
3. So $\Box \set{0} \subseteq \Box \Box \set{0}$, as transitivity predicts.
4. Compute $\Diamond \set{1} = \neg \Box \set{0} = \set{0}$.

The typical use: a finite frame gives a finite modal algebra, so one can test axioms by hand.
The trap: $\Box \emptyset$ need not be empty; it is the set of dead-end worlds.
