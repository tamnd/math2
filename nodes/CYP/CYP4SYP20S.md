---
tag: CYP4SYP20S
kind: example
name: Collapsing worlds that disagree on Σ does not give a filtration
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: 6ZZSHAKG5F
    note: the quotient identifies worlds that differ on a formula of Σ, so the filtration lemma fails
uses: [6ZZSHAKG5F, T99DK51S0W, NGHWZ9Y7ZV]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the [[Kripke model|NGHWZ9Y7ZV]] with
$$W = \set{1, 2, 3}, \quad R = \set{(1, 2), (3, 3)}, \quad V(p) = \set{2},$$
and $\Sigma = \set{p, \square p}$.
We identify worlds that agree on $p$ only, and show that no relation on the quotient behaves like a [[filtration|6ZZSHAKG5F]].

1. $\square p$ is true at $1$, since the only successor $2$ has $p$.
2. $\square p$ is false at $3$, since the only successor $3$ lacks $p$.
3. $\square p$ is true at $2$, since $2$ has no successors.
4. The worlds $1$ and $3$ agree on $p$, which is false at both, but they disagree on $\square p \in \Sigma$.
5. Identify by $p$ only: the classes are $X = \set{1, 3}$ and $Y = \set{2}$, with $p$ false at $X$ and true at $Y$.
6. A filtration must contain the images of the arrows of $R$. The arrow $(3, 3)$ gives the pair $(X, X)$, and $(1, 2)$ gives $(X, Y)$.
7. So $X$ sees $X$, where $p$ is false, and $\square p$ is false at $X$ in the quotient.
8. But $\square p$ is true at $1 \in X$, by step 1. So the truth of $\square p$ at $1$ and at $[1] = X$ differ.
9. So no relation on these classes that contains the images of $R$ satisfies the filtration lemma for $\square p$.

## Remarks

The example shows that the quotient in a filtration must be taken by agreement on all formulas of $\Sigma$, not only on the variables.
With agreement on $\Sigma$, the classes are $\set{1}$, $\set{2}$ and $\set{3}$, since $1$ and $3$ differ on $\square p$.
Then the smallest filtration is a copy of $\mathfrak{M}$, and the [[filtration theorem|T99DK51S0W]] holds.
The bound $2^{|\Sigma|}$ on the number of classes depends on this choice of equivalence.
If we remove the loop $(3, 3)$, then $\square p$ is true at $3$, and the worlds $1$ and $3$ agree on $\Sigma$.
Then the two-class quotient becomes a filtration.

## Explanations

### L1 human

A filtration merges worlds that look the same, to make a model smaller.
"Look the same" must include every question we care about, also the questions with "necessarily".
Here worlds $1$ and $3$ both lack $p$, but only world $1$ has "necessarily $p$".
If we merge them, the merged world has to answer "necessarily $p$" with one value, and it cannot be right for both.
So the merge breaks the answers for world $1$.

### L2 human

1. Compute the correct filtration through $\Sigma$ with the classes $\set{1}$, $\set{2}$, $\set{3}$.
2. The smallest filtration has the arrows $[1] \to [2]$ and $[3] \to [3]$.
3. $\square p$ is true at $[1]$ and false at $[3]$, as in the model.
4. So the correct quotient here has 3 classes, one more than the wrong quotient.

The typical use of this example is to check the definition of the equivalence in a filtration.
A trap: a quotient by the variables alone is a bisimulation quotient only in special cases; in general it changes modal truth.
