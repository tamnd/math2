---
tag: WBJWGYGSNQ
kind: example
name: Parallel or is not stable
msc: ["03F52", "68Q55"]
topics: [98QF5J4W16]
audience: research
instance_of: [WSGZ5HGK1X]
uses: [6RQPAH8SBK, B2R55XVZMC]
sources:
  - url: https://en.wikipedia.org/wiki/Coherent_space
    locator: Stable functions
  - book: isbn:9780521371810
    note: Girard, Lafont and Taylor, Proofs and Types
---

## Example

We use the spaces $\mathbf{Bool}$ and $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ of the [[flat space example|B2R55XVZMC]].
The *parallel or* $P$ from $\mathbf{Bool} \mathbin{\&} \mathbf{Bool}$ to $\mathbf{Bool}$ answers "true" as soon as one argument is true.

1. $P(c) = \set{t}$ if $t_1 \in c$ or $t_2 \in c$.
2. $P(c) = \set{f}$ if $f_1 \in c$ and $f_2 \in c$.
3. $P(c) = \emptyset$ in all other cases.

Cases 1 and 2 exclude each other, since a clique with $f_1$ and $f_2$ contains neither $t_1$ nor $t_2$.
$P$ is monotone and continuous, but it is not [[stable|6RQPAH8SBK]].

1. Take $c = \set{t_1}$ and $c' = \set{t_2}$.
2. $c \cup c' = \set{t_1, t_2}$ is a clique, since tokens from different parts cohere.
3. $P(c) \cap P(c') = \set{t} \cap \set{t} = \set{t}$.
4. $P(c \cap c') = P(\emptyset) = \emptyset$.
5. So $P(c \cap c') \neq P(c) \cap P(c')$, and the condition of stability fails.

## Remarks

The output $t$ on the input $\set{t_1, t_2}$ has two minimal inputs, $\set{t_1}$ and $\set{t_2}$, and they cohere.
A stable function allows several minimal inputs for one output only if they do not cohere.
So the semantics of coherence spaces has no point for parallel or, and it models only sequential computation of this kind.

## Explanations

### L1 human

Parallel or asks both questions at the same time.
It says "true" as soon as either answer is "true".
So the answer "true" has two different reasons, and no one of them is the smallest; a stable function does not allow that.

### L2 human

We compare parallel or with the left-sequential or $L$, where $L(c) = \set{t}$ if $t_1 \in c$, $L(c) = \set{t}$ if $f_1, t_2 \in c$, and $L(c) = \set{f}$ if $f_1, f_2 \in c$.

1. The minimal inputs of $L$ for $t$ are $\set{t_1}$ and $\set{f_1, t_2}$, which do not cohere, since $t_1$ and $f_1$ do not.
2. So for each clique only one of them applies, and the argument of stability goes through.
3. For $P$, the minimal inputs $\set{t_1}$ and $\set{t_2}$ cohere, and the argument breaks.
4. On $\set{t_2}$ alone, $L$ gives $\emptyset$ but $P$ gives $\set{t}$.

The typical use of this example is to show that stability excludes some continuous functions.
A trap: $P$ is monotone and continuous, so it is a correct function in Scott's sense; only the extra condition of stability rules it out.
