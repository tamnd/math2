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

Take the [[Kripke model|NGHWZ9Y7ZV]] with these parts:
$$W = \{ 1, 2, 3 \}, \quad R = \{ (1, 2), (3, 3) \}, \quad V(p) = \{ 2 \}.$$
Let $\Sigma = \{ p, \square p \}$.
We identify worlds that agree on $p$ only, and we show that no relation on the quotient behaves like a [[filtration|6ZZSHAKG5F]].

First we compute $\square p$.
It is true at $1$, since the only successor $2$ has $p$.
It is false at $3$, since the only successor $3$ lacks $p$.
It is true at $2$, since $2$ has no successors.
So the worlds $1$ and $3$ agree on $p$, which is false at both, but they disagree on $\square p \in \Sigma$.

Now merge by $p$ only.
The classes are $X = \{ 1, 3 \}$ and $Y = \{ 2 \}$, with $p$ false at $X$ and true at $Y$.
Any relation that is to act like a filtration must contain the images of the arrows of $R$.
The arrow $(3, 3)$ gives the pair $(X, X)$, and $(1, 2)$ gives $(X, Y)$.
So $X$ sees $X$, where $p$ is false, and $\square p$ is false at $X$ in the quotient.
But $\square p$ is true at $1 \in X$.
So the truth value of $\square p$ at $1$ differs from its value at $[1] = X$, whatever further arrows we add.

## Remarks

### The correct quotient

A filtration must merge worlds that agree on all formulas of $\Sigma$, not only on the variables.
With agreement on $\Sigma$, the classes are $\{ 1 \}$, $\{ 2 \}$ and $\{ 3 \}$, since $1$ and $3$ differ on $\square p$.
The smallest filtration then has the arrows $[1] \to [2]$ and $[3] \to [3]$, so it is a copy of the model, and the [[filtration theorem|T99DK51S0W]] holds.
Check: $\square p$ is true at $[1]$ and false at $[3]$, as in the model.
The bound $2^{\lvert \Sigma \rvert}$ on the number of classes counts truth patterns on $\Sigma$, so it depends on this choice of equivalence.

### A variant that works

If we remove the loop $(3, 3)$, then $\square p$ becomes true at $3$, and the worlds $1$ and $3$ agree on all of $\Sigma$.
Then the two-class quotient with the single arrow $X \to Y$ is a filtration, and $\square p$ is true at $X$ as it is at $1$ and $3$.

### Watch out

A quotient by the variables alone keeps modal truth only in special cases, for instance when the merged worlds happen to be bisimilar.
In general it changes the truth of boxed formulas, as here.

## Explanations

### L1 human

A filtration merges worlds that look the same, to make a model smaller.
"Look the same" must cover every question we care about, including the questions with "necessarily".
Here worlds $1$ and $3$ both lack $p$, but only world $1$ has "necessarily $p$".
If we merge them, the merged world has to answer "necessarily $p$" with one value, and that value cannot be right for both.
So the merge breaks the answers for world $1$.

### L2 human

The typical use of this example is to check the definition of the equivalence in a filtration.
When you build a filtration, list the truth values of every formula of $\Sigma$, boxed ones included, before you merge anything.
In this model the list for $(p, \square p)$ is $(0, 1)$ at $1$, $(1, 1)$ at $2$ and $(0, 0)$ at $3$.
These are three different patterns, so the correct quotient has three classes, one more than the wrong quotient.
