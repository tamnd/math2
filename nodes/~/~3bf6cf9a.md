---
tag: ~3bf6cf9a
kind: example
name: Axiom 4 is true in a model whose frame is not transitive
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [NGHWZ9Y7ZV]
uses: [NGHWZ9Y7ZV, XBCYFDPS2F, 0GJZW9JFZQ, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Take the frame $\mathfrak{F} = (W, R)$ with
$$W = \set{1, 2, 3}, \quad R = \set{(1, 2), (2, 3)}.$$
We compare the truth of axiom $\mathrm{4}$, the formula $\square p \to \square\square p$, in two [[Kripke models|NGHWZ9Y7ZV]] on $\mathfrak{F}$.

1. The relation is not [[transitive|0GJZW9JFZQ]]: $1 R 2$ and $2 R 3$ hold, but $1 R 3$ fails.
2. The successor sets are $R[1] = \set{2}$, $R[2] = \set{3}$ and $R[3] = \varnothing$.
3. First model: $V(p) = W$. Then $p$ is true everywhere, so $\square p$ is true everywhere, and so is $\square\square p$.
4. So $\square p \to \square\square p$ is true at every world of the first model.
5. Second model: $V'(p) = \set{2} = R[1]$. Then $\square p$ is true at $1$, since the only successor $2$ has $p$.
6. $\square p$ is false at $2$, since the successor $3$ lacks $p$.
7. $\square\square p$ is false at $1$, since the successor $2$ makes $\square p$ false.
8. So axiom $\mathrm{4}$ fails at $1$ in the second model, and it is not valid on $\mathfrak{F}$.

## Remarks

The example shows the difference between truth in a model and validity on a frame.
Axiom $\mathrm{4}$ is valid on a frame exactly when the frame is transitive, by [[common modal axiom schemata|FDFQFWPM4X]].
This correspondence is about frames, and a single model can satisfy $\mathrm{4}$ on a frame that is not transitive.
The set of formulas true in the first model is not closed under uniform substitution.
Add a variable $q$ with $V(q) = \set{2}$ to the first model.
Then $\square p \to \square\square p$ is true in the model, but its substitution instance $\square q \to \square\square q$ fails at $1$, by steps 5 to 7.
The choice $V'(p) = R[1]$ is the general method: it makes $\square p$ true at $1$ with the smallest possible truth set.
If we add the pair $(1, 3)$, the frame becomes transitive, and $\mathrm{4}$ holds under every valuation.

## Explanations

### L1 human

Picture three stations on a line: from station 1 a train goes to station 2, and from station 2 a train goes to station 3.
There is no direct train from 1 to 3.
If every station has a flag, then every check of the form "all next stations have a flag" succeeds.
If only station 2 has a flag, then from station 1 all next stations have a flag, but two steps ahead there is none.
So the rule "one step implies two steps" can hold by luck, but it fails for some choice of flags.

### L2 human

1. Take the second model, $V'(p) = \set{2}$.
2. Compute $[\![ \square p ]\!] = \set{1, 3}$: world $1$ sees only $2$, and world $3$ has no successors.
3. Compute $[\![ \square\square p ]\!] = \set{2, 3}$: world $2$ sees only $3 \in [\![ \square p ]\!]$, and world $1$ sees $2 \notin [\![ \square p ]\!]$.
4. So $[\![ \square p \to \square\square p ]\!] = \set{2, 3}$, and the axiom fails exactly at $1$.

The typical use of this example is to test whether a frame validates a formula: try the valuation $V(p) = R[w]$ first.
A trap: one valuation that makes a formula true proves nothing about frame validity.
