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

A textbook says "every subgroup of the group $\mathbb{Z}$ is cyclic".
The phrase "the group $\mathbb{Z}$" names a set where a group should be, so it is an [[abuse of notation|JV68YRB5YZ]].
We expand the short form and check that only one expansion makes sense.

1. The symbol $\mathbb{Z}$ names the set $\{\ldots, -2, -1, 0, 1, 2, \ldots\}$ of [[integers|0C4JS9RF5M]].
   A set alone is not a [[group|G5S1M9]], so the text must mean the set with an operation.
2. Try addition.
   The pair $(\mathbb{Z}, +)$ is a group: addition is associative, $0$ is the identity, and $-n$ is the inverse of $n$, since $n + (-n) = 0$.
3. Try multiplication.
   The pair $(\mathbb{Z}, \cdot)$ is associative and has the identity $1$, but $2$ has no inverse, because $2m = 1$ has no integer solution $m$.
4. So $(\mathbb{Z}, \cdot)$ is not a group, and "the group $\mathbb{Z}$" can only mean $(\mathbb{Z}, +)$.
5. In the same way, "the ring $\mathbb{Z}$" means $(\mathbb{Z}, +, \cdot)$, and "$\mathbb{Z}$ is countable" refers to the set alone.

## Remarks

One symbol names a set and each structure on it, and the sentence tells the reader which one is meant.
This shortcut is called suppression of parameters.
It is safe here because only one standard operation on $\mathbb{Z}$ makes a group.

On a set with two group operations the text must name the operation.
The set $\mathbb{Q} \setminus \{0\}$ is a group under multiplication, and $\mathbb{Q}$ is a group under addition.
A text that uses both writes $\mathbb{Q}^{\times}$ for the multiplicative group and keeps $\mathbb{Q}$ for the additive one.

## Explanations

### L1 human

The letter $\mathbb{Z}$ stands for all whole numbers, positive, negative and zero.
A group needs a way to combine two numbers and a way to undo it.
With adding, we can always undo: $5 + (-5) = 0$.
With multiplying, we cannot undo $2$ inside the whole numbers, since $\tfrac{1}{2}$ is not a whole number.
So "the group $\mathbb{Z}$" must mean the whole numbers with adding.

### L2 human

Test the same short form on "the group $\mathbb{Z}/6\mathbb{Z}$".
The pair $(\mathbb{Z}/6\mathbb{Z}, +)$ is a group with identity $0$, and the inverse of $a$ is $6 - a$.
The pair $(\mathbb{Z}/6\mathbb{Z}, \cdot)$ has identity $1$, but $0$ has no inverse, so it is not a group.
The classes that do have a multiplicative inverse are $1$ and $5$, since
$$1 \cdot 1 = 1, \qquad 5 \cdot 5 = 25 = 4 \cdot 6 + 1 = 1 \ \text{in } \mathbb{Z}/6\mathbb{Z}.$$
So "the group $\mathbb{Z}/6\mathbb{Z}$" is the additive group, and the multiplicative group is written $(\mathbb{Z}/6\mathbb{Z})^{\times} = \{1, 5\}$.
In group theory "the group $\mathbb{Z}/n\mathbb{Z}$" always means the cyclic group of order $n$ under addition.
Watch out: $(\mathbb{Z}/n\mathbb{Z})^{\times}$ is a different group, and its order is not $n$; for $n = 6$ it has $2$ elements.
