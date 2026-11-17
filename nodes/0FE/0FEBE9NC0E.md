---
tag: 0FEBE9NC0E
kind: statement
role: theorem
name: A subgroup of smallest prime index is normal
msc: ["20D60"]
topics: [E1506A5A55]
audience: ug2
about: [0CB0DX5BVV, 0DTXBQPA2S]
uses: [0X1JXT47GA, 0DTXBQPA2S, 0CB0DX5BVV, 0B85S2V2DR]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 4.2
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], and let $p$ be the smallest prime number that divides the [[order|0B85S2V2DR]] $|G|$.
Let $H$ be a [[subgroup|0X1JXT47GA]] of $G$ of [[index|0DTXBQPA2S]] $p$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

The proof lets $G$ act on the $p$ left cosets of $H$ by left multiplication.
This gives a homomorphism $\rho \colon G \to S_p$ whose kernel $K$ is a normal subgroup of $G$ inside $H$.
The index $[G : K]$ divides $p!$ and has no prime factor less than $p$, so it is $p$, and $K = H$.

### Why each hypothesis is needed

- The prime $p$ must be the smallest prime divisor of $|G|$. In $S_3$, with composition from right to left, $H = \{e, (1\,2)\}$ has index $3$, and $3$ is a prime divisor of $6$, but not the smallest one. $H$ is not normal ([[a subgroup of order two in S3 is not normal|XD0WBC1MWB]]).
- The index must be the prime $p$ itself, not a power of $p$. In the [[dihedral group|0JZ27DMJ5D]] $D_4$ of order $8$, let $s$ be a reflection. The subgroup $\{e, s\}$ has index $4 = 2^2$, and it is not normal, because a rotation by a quarter turn conjugates $s$ into a different reflection.
- The group must be finite, so that $p$ is defined. For index $2$, finiteness is not needed ([[subgroups of index two are normal|0V547YQRMV]]).

### Consequences

- For $p = 2$: in a finite group of even order, each subgroup of index $2$ is normal.
- Let $|G| = 75 = 3 \cdot 5^2$. The smallest prime divisor is $3$, so each subgroup of order $25$ has index $3$ and is normal.
- Let $|G| = pq$ with primes $p < q$. Then each subgroup of order $q$ has index $p$, so it is normal. So $G$ is not [[simple|0YMYMNQ0QZ]], because a subgroup of order $q$ exists by [[Cauchy's theorem|0JM7PA288B]].
- In a group of odd order, each subgroup of index $3$ is normal, because the smallest prime divisor of an odd order divisible by $3$ is $3$.

### Converse

The converse is false.
A normal subgroup of prime index $q$ need not have $q$ equal to the smallest prime divisor of $|G|$.
In the cyclic group $\mathbb{Z}/6\mathbb{Z}$, the subgroup $\{0, 3\}$ has index $3$, and it is normal because the group is abelian, but the smallest prime divisor of $6$ is $2$.

### Generalizations

- The proof gives a more general fact. If $H$ has index $n$ in $G$, then the kernel of the action on the cosets is a normal subgroup $K \le H$, and $[G : K]$ divides $n!$. This $K$ is the [[normal core|0GETX79CJN]] of $H$.
- So a finite group with a subgroup of index $n > 1$ and order not dividing $n!$ is not simple.

## History

The theorem is a standard result of the theory of finite groups, and it contains the case of index $2$.
Its proof by the action on cosets is a typical use of group actions.

## Explanations

### L1 human

A subgroup of index $2$ is always normal.
This theorem shows that index $2$ is a special case of a larger rule.
Find the smallest prime that divides the order of the group.
If a subgroup has exactly this prime as its index, then it is normal.
For a group of order $15$, this prime is $3$, so a subgroup of order $5$ is normal.

### L2 human

To use the theorem, compute two numbers: the smallest prime $p$ that divides $|G|$, and the index $[G : H]$.
If they are equal, then $H$ is normal.

1. Let $|G| = 75 = 3 \cdot 5^2$ and $|H| = 25$.
2. The smallest prime that divides $75$ is $3$.
3. $[G : H] = 75 / 25 = 3$.
4. So $H$ is normal in $G$, without any information about the elements of $G$.

A common error is to drop the word "smallest".
In $S_3$, the subgroup $\{e, (1\,2)\}$ has prime index $3$, but $2$ is the smallest prime divisor of $6$, and the subgroup is not normal.
Another common error is to use a power of $p$ as the index; the example in $D_4$ above shows that this fails.

### L3 human

The theorem is a statement about the homomorphism $\rho \colon G \to S_p$ from the action on cosets.
Its image has order dividing both $|G|$ and $p!$, and this forces the image to have order $p$.
The same method gives the bound of the generalization: a simple group with a subgroup of index $n > 1$ embeds in $S_n$.
For example, a simple group of order $60$ has no subgroup of index $2$, $3$ or $4$, because $60$ does not divide $2!$, $3!$ or $4!$.
The orbit version of the proof, in [[the proof of this theorem|CARDX0G5Z0]], uses only the action of $H$ on the cosets and the orbit-stabiliser theorem.
