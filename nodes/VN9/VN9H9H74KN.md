---
tag: VN9H9H74KN
kind: example
name: The odd integers are not a subgroup of the integers
msc: ["20A05"]
topics: [BAVE5RN4EE]
audience: ug1
not_instance_of:
  - target: 0X1JXT47GA
    note: the set does not contain 0 and is not closed under addition
uses: [0X1JXT47GA, 0BSCJA5G53]
sources:
  - url: https://en.wikipedia.org/wiki/Subgroup
    locator: Basic properties of subgroups
  - book: isbn:9781305657960
    locator: Chapter 3
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[additive group of integers|0BSCJA5G53]], with identity $0$.
Let $O = \{2k + 1 : k \in \mathbb{Z}\} = \{\ldots, -3, -1, 1, 3, \ldots\}$ be the set of odd integers.
We check the three conditions of a [[subgroup|0X1JXT47GA]] one by one.

1. Identity: if $0 = 2k + 1$ for an integer $k$, then $k = -\tfrac{1}{2}$, which is not an integer. So $0 \notin O$, and the first condition fails.
2. Closure: $1 \in O$, but $1 + 1 = 2 = 2 \cdot 1$ is even. More generally, $(2k + 1) + (2l + 1) = 2(k + l + 1)$ is even for all $k, l$. So the sum of two odd integers is never odd, and the second condition fails.
3. Inverses: $-(2k + 1) = 2(-k - 1) + 1$ is odd. So the third condition holds.

Thus $O$ is not a subgroup of $\mathbb{Z}$, because conditions 1 and 2 fail.

## Remarks

The example shows that one true condition (here, closure under inverses) does not make a subgroup.
For a subgroup $H$ and an integer $a$, the coset $a + H$ is the set $\{a + h : h \in H\}$.
The odd integers are a coset of the even integers: $O = 1 + 2\mathbb{Z}$.
A coset $a + H$ of a subgroup $H$ is a subgroup only when $a \in H$, and then $a + H = H$.
For $n \geq 2$, the same proof shows that the set $1 + n\mathbb{Z}$ of integers $\equiv 1 \pmod n$ is not a subgroup of $(\mathbb{Z}, +)$: it does not contain $0$.
Under multiplication, the odd integers behave in a different way: the product of two odd integers is odd.
But $(\mathbb{Z} \setminus \{0\}, \cdot)$ is not a group, because $2$ has no multiplicative inverse in $\mathbb{Z}$, so this does not give a subgroup either.

## Explanations

### L1 human

Odd numbers are the numbers $1, 3, 5, \ldots$ and $-1, -3, -5, \ldots$.
For a subgroup of the integers under addition, zero must be in the set, and sums must stay in the set.
Zero is not odd.
Also, two odd numbers add to an even number, for example $3 + 5 = 8$.
So the odd numbers fail two of the three tests, and they are not a subgroup.

### L2 human

We compare the odd integers with the even integers, which do form a subgroup.

1. The even integers $2\mathbb{Z}$ contain $0 = 2 \cdot 0$.
2. For even integers, $2k + 2l = 2(k + l)$ is even, and $-2k = 2(-k)$ is even.
3. For odd integers, $0$ is missing and $(2k+1) + (2l+1) = 2(k + l + 1)$ is even.

The typical use of this non-example is a quick test.
Before a long check, look for the identity: a set without the identity is never a subgroup.

A trap: a set can fail to be a subgroup and still be closed under inverses, as $O$ is.
Each of the three conditions needs its own check.
