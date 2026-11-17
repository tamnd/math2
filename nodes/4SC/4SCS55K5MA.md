---
tag: 4SCS55K5MA
kind: example
name: The integers modulo the even integers
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0KYX2N69J0]
uses: [0BSCJA5G53, 0JPDTEDCFD, 03DEH43F4H, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Even and odd integers
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[additive group of integers|0BSCJA5G53]], and let $N = 2\mathbb{Z}$ be the subgroup of even integers.
The [[quotient group|0KYX2N69J0]] $\mathbb{Z}/2\mathbb{Z}$ has two elements: the even integers and the odd integers.

1. $N$ is normal, because each [[subgroup of an abelian group is normal|0JPDTEDCFD]].
2. Each integer is even or odd. So $N$ has exactly two [[cosets|03DEH43F4H]]: $0 + N$, the even integers, and $1 + N$, the odd integers.
3. The sum of two even integers is even, so $(0 + N) + (0 + N) = 0 + N$.
4. The sum of an even and an odd integer is odd, so $(0 + N) + (1 + N) = 1 + N$.
5. The sum of two odd integers is even, so $(1 + N) + (1 + N) = 0 + N$.
6. Thus $\mathbb{Z}/2\mathbb{Z}$ has identity $0 + N$, and $1 + N$ is its own inverse. It is the group of [[integers modulo $2$|03VFZ2WETT]].

## Remarks

The rules in steps 3 to 5 are the parity rules of school arithmetic.
They do not depend on the choice of the even or odd integers, and this is the well-definedness of the quotient.
The map $\mathbb{Z} \to \{1, -1\}$, $n \mapsto (-1)^n$, is a surjective homomorphism with kernel $2\mathbb{Z}$.
By the [[first isomorphism theorem|0CXXJNG5B6]], $\mathbb{Z}/2\mathbb{Z} \cong \{1, -1\}$ under multiplication.
This is the case $n = 2$ of [[the integers modulo n|0YJ3WRR9RY]].

## Explanations

### L1 human

Sort the integers into two piles: the even ones and the odd ones.
Add any number from one pile to any number from another pile.
The pile of the answer depends only on the two piles, not on the numbers.
So the two piles form a group with two elements: even plus even is even, even plus odd is odd, and odd plus odd is even.

### L2 human

The quotient group forgets everything about an integer except its parity.
To check that the addition of piles is well defined, take $a, a'$ in one coset and $b, b'$ in one coset.
Then $a' = a + 2s$ and $b' = b + 2t$ for some integers $s$ and $t$.
So $a' + b' = (a + b) + 2(s + t)$, and $a' + b'$ is in the coset of $a + b$.
A typical use is a parity argument.
For example, $n^2 + n$ is even for each integer $n$: in $\mathbb{Z}/2\mathbb{Z}$, both $0^2 + 0$ and $1^2 + 1$ equal $0$.
