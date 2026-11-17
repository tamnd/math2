---
tag: FJF92WDREV
kind: example
name: The set of e, (1 2) and (1 3) is not the subgroup that they generate
msc: ["20A05", "20B30"]
topics: [BAVE5RN4EE]
audience: ug1
not_instance_of:
  - target: 0RP7VWQ0YN
    note: the set contains the generators and the identity, but it is not closed under products, and the generated subgroup is all of S3
uses: [0515A6D2Y1, 0RP7VWQ0YN, 0X1JXT47GA]
sources:
  - book: isbn:9780471433347
    locator: Section 2.4
---

## Example

Let $S_3$ be the [[symmetric group|0515A6D2Y1]] on $\{1, 2, 3\}$.
We compose from right to left: in $\sigma\tau$, we apply $\tau$ first.
Let $a = (1\,2)$, $c = (1\,3)$ and $T = \{e, a, c\}$.
The set $T$ contains $a$, $c$ and the identity, and it is closed under inverses, because $a^{-1} = a$ and $c^{-1} = c$.
We show that $T$ is not $\langle a, c \rangle$, the [[subgroup generated|0RP7VWQ0YN]] by $a$ and $c$.

1. $ac = (1\,2)(1\,3)$. Apply $(1\,3)$ first: $1 \mapsto 3 \mapsto 3$, $3 \mapsto 1 \mapsto 2$ and $2 \mapsto 2 \mapsto 1$. So $ac = (1\,3\,2)$.
2. $(1\,3\,2) \notin T$. So $T$ is not closed under products, and $T$ is not a [[subgroup|0X1JXT47GA]].
3. $ca = (1\,3)(1\,2)$. Apply $(1\,2)$ first: $1 \mapsto 2 \mapsto 2$, $2 \mapsto 1 \mapsto 3$ and $3 \mapsto 3 \mapsto 1$. So $ca = (1\,2\,3)$.
4. $a(1\,2\,3) = (1\,2)(1\,2\,3)$. Apply $(1\,2\,3)$ first: $1 \mapsto 2 \mapsto 1$, $2 \mapsto 3 \mapsto 3$ and $3 \mapsto 1 \mapsto 2$. So $a \cdot ca = (2\,3)$.
5. By steps 1, 3 and 4, the subgroup $\langle a, c \rangle$ contains $e$, $a$, $c$, $(1\,3\,2)$, $(1\,2\,3)$ and $(2\,3)$. These are all six elements of $S_3$.

So $\langle a, c \rangle = S_3$, and $T$ has only three of its six elements.

## Remarks

The example shows that the generated subgroup is more than the generators, their inverses and the identity.
It must also contain all products, and products of products.
The set $T$ passes two of the three subgroup conditions (identity and inverses), and it fails closure.
The same set appears in the [[subgroup criterion|05N4TQKPH0]] as the reason that the closure condition is needed.
The two transpositions $(1\,2)$ and $(1\,3)$ form a generating set of $S_3$.
In fact, any two different transpositions in $S_3$ generate $S_3$.

## Explanations

### L1 human

Take three cards in a row.
One move swaps the first two cards.
Another move swaps the first and the last card.
If we only allow "do nothing", the first move or the second move, we have three ways to shuffle.
But doing the first move after the second gives a new shuffle, which is not one of the three.
When we keep all the shuffles that we can reach, we get all six orders of the cards.

### L2 human

We compare $T$ with $\langle a, c \rangle$.

1. $T$ has $3$ elements and $\langle a, c \rangle = S_3$ has $6$ elements.
2. The missing elements are $ac = (1\,3\,2)$, $ca = (1\,2\,3)$ and $a \cdot ca = (2\,3)$.

The typical use is a warning: to find $\langle S \rangle$, keep taking products until the set is closed.

A trap: in a finite group, a set that contains the identity and is closed under inverses still need not be a subgroup.
Closure under products is the condition that usually fails.
