---
tag: X51H6XKCDQ
kind: example
name: The group Z means the integers under addition
msc: ["00A35", "20A05"]
topics: [Z2WNQ1DNTX]
audience: ug1
instance_of: [JV68YRB5YZ]
uses: [JV68YRB5YZ, G5S1M9, 0C4JS9RF5M]
sources:
  - url: https://en.wikipedia.org/wiki/Abuse_of_notation
    locator: Suppression of parameters
---

## Example

A text says "the group $\mathbb{Z}$".
We expand the short form and check that only one expansion makes sense.

1. The symbol $\mathbb{Z}$ names the set $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ of [[integers|0C4JS9RF5M]]. A set alone is not a [[group|G5S1M9]], so the text must mean a set with an operation.
2. Try addition. The pair $(\mathbb{Z}, +)$ is a group: addition is associative, $0$ is the identity, and $-n$ is the inverse of $n$.
3. Try multiplication. The pair $(\mathbb{Z}, \cdot)$ is associative and has the identity $1$, but $2$ has no inverse, because $2m = 1$ has no integer solution $m$.
4. So $(\mathbb{Z}, \cdot)$ is not a group, and "the group $\mathbb{Z}$" can only mean $(\mathbb{Z}, +)$.
5. In the same way, "the ring $\mathbb{Z}$" means $(\mathbb{Z}, +, \cdot)$, and "$\mathbb{Z}$ is countable" refers to the set alone.

## Remarks

The example shows the abuse called suppression of parameters: one symbol names a set and each structure on it.
The abuse is safe here because only one standard operation on $\mathbb{Z}$ makes a group.
For a set with two group operations, the text must name the operation.
For example, $\mathbb{Q} \setminus \{0\}$ is a group under multiplication, and a text that also uses $(\mathbb{Q}, +)$ writes $\mathbb{Q}^{\times}$ for the multiplicative group.

## Explanations

### L1 human

The letter $\mathbb{Z}$ stands for all whole numbers, positive, negative and zero.
A group needs a way to combine two numbers, and a way to undo it.
With adding, we can always undo: $5 + (-5) = 0$.
With multiplying, we cannot undo $2$ inside the whole numbers, since $\tfrac{1}{2}$ is not a whole number.
So "the group $\mathbb{Z}$" must mean the whole numbers with adding.

### L2 human

We test the same short form on $\mathbb{Z}/6\mathbb{Z}$.

1. The pair $(\mathbb{Z}/6\mathbb{Z}, +)$ is a group with identity $0$ and inverse $6 - a$ of $a$.
2. The pair $(\mathbb{Z}/6\mathbb{Z}, \cdot)$ has identity $1$, but $0$ has no inverse, so it is not a group.
3. The set of classes with a multiplicative inverse is $\{1, 5\}$, since $1 \cdot 1 = 1$ and $5 \cdot 5 = 25 = 1$ in $\mathbb{Z}/6\mathbb{Z}$.
4. So "the group $\mathbb{Z}/6\mathbb{Z}$" means the additive group, and the multiplicative group is written $(\mathbb{Z}/6\mathbb{Z})^{\times} = \{1, 5\}$.

The typical use of this convention is in group theory, where "the group $\mathbb{Z}/n\mathbb{Z}$" is always the cyclic group of order $n$ under addition.
A trap: the notation $(\mathbb{Z}/n\mathbb{Z})^{\times}$ is a different group, and its order is not $n$.
