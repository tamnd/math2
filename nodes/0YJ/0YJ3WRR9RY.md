---
tag: 0YJ3WRR9RY
kind: example
name: Integers modulo n as a quotient group
msc: ["20K01"]
topics: [E1506A5A55]
audience: ug1
instance_of: [0KYX2N69J0]
illustrates: [0CXXJNG5B6]
uses: [0BSCJA5G53, 0SRATCFF1W, 0JPDTEDCFD, 03DEH43F4H, 0CHQKZFK5S, 0KVGH0J5B3]
sources:
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Integer modular arithmetic
  - url: https://en.wikipedia.org/wiki/Quotient_group
    locator: Remainders of integer division
---

## Example

Let $n$ be a positive integer, and let $n\mathbb{Z} = \{nk : k \in \mathbb{Z}\}$ be the multiples of $n$ in the [[additive group of integers|0BSCJA5G53]].
The [[quotient group|0KYX2N69J0]] $\mathbb{Z}/n\mathbb{Z}$ is the group of integers modulo $n$, with $n$ elements.

1. $n\mathbb{Z}$ is a subgroup of $\mathbb{Z}$; by [[subgroups of the integers|0SRATCFF1W]], every subgroup of $\mathbb{Z}$ has this form.
2. $n\mathbb{Z}$ is normal, because $\mathbb{Z}$ is abelian and every [[subgroup of an abelian group is normal|0JPDTEDCFD]].
3. Two [[cosets|03DEH43F4H]] are equal, $a + n\mathbb{Z} = b + n\mathbb{Z}$, if and only if $a - b \in n\mathbb{Z}$, that is, $n$ divides $a - b$.
4. By the [[division algorithm|0CHQKZFK5S]], each integer $a$ is $qn + r$ with $0 \le r < n$. So $a + n\mathbb{Z} = r + n\mathbb{Z}$.
5. Two different remainders $r, r'$ in $\{0, 1, \ldots, n-1\}$ give different cosets, because $0 < |r - r'| < n$, so $n$ does not divide $r - r'$.
6. By steps 4 and 5, the cosets are exactly $0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n-1) + n\mathbb{Z}$. So $\mathbb{Z}/n\mathbb{Z}$ has $n$ elements.
7. The sum is $(a + n\mathbb{Z}) + (b + n\mathbb{Z}) = (a + b) + n\mathbb{Z}$. In terms of remainders, this is addition followed by reduction modulo $n$.
8. The map $\pi \colon \mathbb{Z} \to \mathbb{Z}/n\mathbb{Z}$, $a \mapsto a + n\mathbb{Z}$, is a surjective homomorphism with kernel $n\mathbb{Z}$.

## Remarks

$\mathbb{Z}/n\mathbb{Z}$ is a [[cyclic group|0KVGH0J5B3]] of order $n$ with generator $1 + n\mathbb{Z}$.
For $n = 2$, the two cosets are the even and the odd integers ([[the integers modulo the even integers|4SCS55K5MA]]).
For $n = 1$, the quotient $\mathbb{Z}/\mathbb{Z}$ is the trivial group.
For $n = 0$, the subgroup $0\mathbb{Z}$ is $\{0\}$, and $\mathbb{Z}/\{0\}$ is isomorphic to $\mathbb{Z}$.
By the [[correspondence theorem|0S9ZVZ34MD]], the subgroups of $\mathbb{Z}/n\mathbb{Z}$ correspond to the subgroups $d\mathbb{Z}$ that contain $n\mathbb{Z}$, that is, to the positive divisors $d$ of $n$.
Each homomorphism from $\mathbb{Z}$ onto a cyclic group of order $n$ has kernel $n\mathbb{Z}$, so the [[first isomorphism theorem|0CXXJNG5B6]] shows that each cyclic group of order $n$ is isomorphic to $\mathbb{Z}/n\mathbb{Z}$.

## Explanations

### L1 human

Two integers are in the same coset of $n\mathbb{Z}$ when their difference is a multiple of $n$.
So the quotient group keeps only the remainder on division by $n$.
Adding cosets is the same as adding remainders and reducing modulo $n$.
For $n = 12$ this is the arithmetic of a clock: $9 + 5 = 14$, and $14$ has remainder $2$, so $9 + 5 = 2$ in $\mathbb{Z}/12\mathbb{Z}$.

### L2 human

We work out $\mathbb{Z}/4\mathbb{Z}$.
The cosets are $\bar 0 = \{\ldots, -4, 0, 4, 8, \ldots\}$, $\bar 1 = \{\ldots, -3, 1, 5, 9, \ldots\}$, $\bar 2 = \{\ldots, -2, 2, 6, 10, \ldots\}$ and $\bar 3 = \{\ldots, -1, 3, 7, 11, \ldots\}$.
To compute $\bar 3 + \bar 2$, take any representatives, for example $7$ and $-2$.
Their sum $5$ lies in $\bar 1$, so $\bar 3 + \bar 2 = \bar 1$.
Other representatives give the same coset: $3 + 2 = 5$ and $-1 + 10 = 9$, and both $5$ and $9$ lie in $\bar 1$.
The element $\bar 1$ has order $4$, and $\bar 2$ has order $2$.
The quotient group $\mathbb{Z}/n\mathbb{Z}$ is the standard model of a cyclic group of order $n$.
A trap is to think that $\mathbb{Z}/n\mathbb{Z}$ is a subgroup of $\mathbb{Z}$.
The set $\{0, 1, \ldots, n-1\}$ is not closed under the addition of $\mathbb{Z}$, and $\mathbb{Z}$ has no nonzero element of finite order.
