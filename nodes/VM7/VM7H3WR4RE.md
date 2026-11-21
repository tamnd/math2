---
tag: VM7H3WR4RE
kind: example
name: The trivial predimension gives Fraïssé limits
aliases: [trivial-predimension-fraisse-limit]
msc: ["03C15"]
topics: [ZS8X8KS54R]
audience: research
instance_of: [933BFNKPXF]
uses: [933BFNKPXF, HJVRBDQSGG, RMXR0FEF54, 00C0BR7D7H]
sources:
  - book: isbn:9780521587136
---

## Example

On finite [[graphs|00C0BR7D7H]], take the trivial predimension $\delta(A) = \lvert A \rvert$, which ignores edges.
We show that the [[Hrushovski amalgamation|933BFNKPXF]] for $\delta$ is the ordinary Fraïssé construction.

1. For $A \subseteq A' \subseteq B$, $\delta(A') = \lvert A' \rvert \ge \lvert A \rvert = \delta(A)$.
2. So $A \le B$ holds for every induced subgraph $A$ of $B$.
3. $\delta \ge 0$ always, so $\mathcal{K}_0$ is the class of all finite graphs.
4. Self-sufficient embeddings are all embeddings, so the generic is the [[Fraïssé limit|HJVRBDQSGG]] of the finite graphs.
5. That limit is the [[Rado graph|RMXR0FEF54]].

## Remarks

The example shows that Hrushovski amalgamation extends the Fraïssé construction.
The interesting cases come from a predimension that subtracts a count of relations, so that $\le$ is a proper restriction.
With $\delta(A) = 2 \lvert A \rvert - \lvert E(A) \rvert$, $\mathcal{K}_0$ is the class of graphs with at most $2 \lvert A \rvert$ edges on each subset $A$.

## Explanations

### L1 human

If every point counts as one unit of freedom and edges cost nothing, then no set ever loses freedom when it grows.
Every subset is self-sufficient, and the construction is the usual one.

### L2 human

We compare two predimensions on the triangle $K_3$.

1. Trivial: $\delta(K_3) = 3$, and every subset is self-sufficient.
2. Edge-counting: $\delta(K_3) = 3 - 3 = 0$, while $\delta$ of an edge is $1$. So an edge is not self-sufficient in $K_3$.

The typical use is as a sanity check on definitions.
A trap is to think the choice of $\delta$ does not matter; it changes the generic completely.
