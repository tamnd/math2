---
tag: V3FJMYC7Q1
kind: example
name: A binary tree has one more empty subtree than nodes
msc: ["00A35", "68P05", "05C05"]
topics: [EEH2F76CYQ]
audience: ug1
instance_of: [12MQ2NJ29A]
uses: [02A8EMC83C, 12MQ2NJ29A]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_induction
    locator: Well-ordering
---

## Example

We define [[binary trees|02A8EMC83C]] by two rules.
The empty tree $\varnothing$ is a binary tree, and if $L$ and $R$ are binary trees, then $\operatorname{node}(L, R)$ is a binary tree.
Let $n(t)$ be the number of nodes of $t$, and let $e(t)$ be the number of empty subtrees of $t$.
Both counts are defined by recursion on the tree:
$$n(\varnothing) = 0, \quad n(\operatorname{node}(L, R)) = n(L) + n(R) + 1, \qquad e(\varnothing) = 1, \quad e(\operatorname{node}(L, R)) = e(L) + e(R).$$
We prove that $e(t) = n(t) + 1$ for every binary tree $t$, by [[structural induction|12MQ2NJ29A]] on $t$.

1. Case $\varnothing$.
   The rules give $e(\varnothing) = 1$ and $n(\varnothing) + 1 = 0 + 1 = 1$, so the claim holds.
2. Case $\operatorname{node}(L, R)$.
   The induction hypotheses are $e(L) = n(L) + 1$ and $e(R) = n(R) + 1$, one for each part.
3. The rule for $e$ and the two hypotheses give
   $$e(\operatorname{node}(L, R)) = e(L) + e(R) = n(L) + n(R) + 2.$$
4. The rule for $n$ gives
   $$n(\operatorname{node}(L, R)) + 1 = n(L) + n(R) + 1 + 1 = n(L) + n(R) + 2.$$
5. Steps 3 and 4 have the same right side, so $e(\operatorname{node}(L, R)) = n(\operatorname{node}(L, R)) + 1$.
6. Both cases hold, so $e(t) = n(t) + 1$ for every binary tree $t$, by structural induction.

The small trees agree with the result.

| $t$ | $n(t)$ | $e(t)$ |
|---|---|---|
| $\varnothing$ | $0$ | $1$ |
| $\operatorname{node}(\varnothing, \varnothing)$ | $1$ | $2$ |
| $\operatorname{node}(\operatorname{node}(\varnothing, \varnothing), \varnothing)$ | $2$ | $3$ |
| $\operatorname{node}(\operatorname{node}(\varnothing, \varnothing), \operatorname{node}(\varnothing, \varnothing))$ | $3$ | $4$ |

## Remarks

The case for $\operatorname{node}(L, R)$ uses two hypotheses, one for each part, and it needs both.
With only the hypothesis for $L$, the term $e(R)$ in step 3 stays unknown and the step cannot finish.
This is the typical shape of a constructor with two parts.

The result has a second reading.
If we draw each empty subtree as a leaf, every tree becomes a full binary tree, in which each inner node has exactly two children.
Then the result says that a full binary tree has one more leaf than inner nodes.

A count gives the same answer without induction when $n(t) \ge 1$.
Each node has $2$ places for children, so there are $2n(t)$ places.
Each node except the root fills one place, and each empty subtree fills one place, so
$$2n(t) = (n(t) - 1) + e(t), \qquad \text{so} \qquad e(t) = n(t) + 1.$$
The induction proof is shorter to check, because each line applies one rule of a definition.

## Explanations

### L1 human

A binary tree is either empty, or it is a node with a left tree and a right tree below it.
In a drawing, each node has two places below it, and each place holds a node or nothing.
Count the places that hold nothing, and you find one more of them than there are nodes.
A single node has $2$ empty places and $1$ node.
Put two trees under a new node: the new node adds $1$ to the nodes, and the empty places of the two trees add up, so the rule "one more" stays true.

### L2 human

Let us follow the proof on $t = \operatorname{node}(\operatorname{node}(\varnothing, \varnothing), \varnothing)$, with $L = \operatorname{node}(\varnothing, \varnothing)$ and $R = \varnothing$.
For $R$ the base case gives $e(R) = 1 = n(R) + 1$.
For $L$ the step with two empty parts gives $e(L) = 1 + 1 = 2$ and $n(L) = 0 + 0 + 1 = 1$.
For $t$ itself the rules give
$$e(t) = e(L) + e(R) = 2 + 1 = 3, \qquad n(t) = n(L) + n(R) + 1 = 1 + 0 + 1 = 2.$$
Check: $3 = 2 + 1$, as the result says.
The proof works from the leaves up, in the same order in which the tree was built.
That is the typical use of the pattern: a relation between two counts that are both defined by recursion on the same structure.
