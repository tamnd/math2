---
tag: 08FDFEF8D1
kind: statement
role: theorem
name: Z/m × Z/n is cyclic iff gcd(m, n) = 1
msc: ["20K01", "11A07"]
topics: [BAVE5RN4EE]
audience: ug1
about: [0KVGH0J5B3, 00HF4RJ5QN]
uses: [0KVGH0J5B3, 00HF4RJ5QN, 0WE2NHZJ7B, 0C8WYW4KYQ, 007NPQX34K, 0VZ48N083F, 03VFZ2WETT, 08MG7H8JW5, 0FNN9B4W64]
sources:
  - url: https://en.wikipedia.org/wiki/Cyclic_group
    locator: Additional properties
  - url: https://en.wikipedia.org/wiki/Chinese_remainder_theorem
    locator: Statement
  - book: isbn:9781305657960
    locator: Chapter 8
---

## Statement

Let $m$ and $n$ be positive integers.
Let $G = \langle g \rangle$ and $H = \langle h \rangle$ be [[cyclic groups|0KVGH0J5B3]] of orders $m$ and $n$.
Let $G \times H$ be their [[direct product|00HF4RJ5QN]], with the operation $(x, y)(x', y') = (xx', yy')$.
Write $\Z/k$ for the [[integers modulo k|03VFZ2WETT]] under addition.

1. (Element orders.) The [[order|0WE2NHZJ7B]] of each element of $G \times H$ divides $\operatorname{lcm}(m, n)$, the [[least common multiple|007NPQX34K]]. The element $(g, h)$ has order exactly $\operatorname{lcm}(m, n)$.
2. (Criterion.) The group $G \times H$ is cyclic if and only if $\gcd(m, n) = 1$, that is, $m$ and $n$ are [[coprime|0VZ48N083F]]. In that case, $(g, h)$ is a generator. In particular, $\Z/m \times \Z/n$ is cyclic if and only if $\gcd(m, n) = 1$.
3. (Chinese remainder theorem.) The map $f \colon \Z/mn \to \Z/m \times \Z/n$, $f(k \bmod mn) = (k \bmod m, k \bmod n)$, is a well-defined homomorphism. If $\gcd(m, n) = 1$, then $f$ is an [[isomorphism|08MG7H8JW5]].

## Remarks

### Why each hypothesis is needed

1. The orders must be coprime. In $\Z/2 \times \Z/6$, the largest order of an element is $\operatorname{lcm}(2, 6) = 6$, but the group has $12$ elements. So it is not cyclic.
2. The two factors must be cyclic. The [[Klein four-group|0PMRQJVTME]] $V$ and $\Z/3$ have the coprime orders $4$ and $3$. But $V \times \Z/3$ contains a copy of $V$, which is not cyclic. Since [[subgroups of cyclic groups are cyclic|0KB1ND7XDS]], the group $V \times \Z/3$ is not cyclic.
3. The orders must be finite. For $n \geq 2$, the group $\Z \times \Z/n$ is not cyclic. The element $(0, 1)$ has finite order $n$, but an infinite cyclic group has no element of finite order other than the identity.

### Consequences

1. $\Z/6 \cong \Z/2 \times \Z/3$ and $\Z/12 \cong \Z/3 \times \Z/4$. For example, $f(7) = (1, 3)$ and $f(5) = (2, 1)$ for $\Z/12 \to \Z/3 \times \Z/4$.
2. $\Z/4 \times \Z/6 \cong \Z/2 \times \Z/12$. Indeed, $\Z/6 \cong \Z/2 \times \Z/3$ and $\Z/4 \times \Z/3 \cong \Z/12$.
3. By induction, if $n_1, \ldots, n_r$ are pairwise coprime, then $\Z/n_1 \times \cdots \times \Z/n_r$ is cyclic of order $n_1 \cdots n_r$. So $\Z/n$ is a product of cyclic groups of prime power order, one for each prime factor of $n$.
4. The map $f$ also respects multiplication. So for coprime $m, n$, the units of $\Z/mn$ match the pairs of units, and the totient function is [[multiplicative|0FSJA9M43W]]: $\varphi(mn) = \varphi(m)\varphi(n)$.

### Converse

Part 2 is an equivalence.
For the map $f$ of part 3, the converse also holds: if $f$ is an isomorphism, then $\gcd(m, n) = 1$.
The reason: if $\gcd(m, n) > 1$, then $L = \operatorname{lcm}(m, n) < mn$, and $f(L) = (0, 0)$, so $f$ is not injective.
For example, with $m = n = 2$, we get $f(2 \bmod 4) = (0, 0)$.

### Generalizations

1. The [[Chinese remainder theorem|0FNN9B4W64]] for $r$ pairwise coprime moduli gives $\Z/(n_1 \cdots n_r) \cong \Z/n_1 \times \cdots \times \Z/n_r$.
2. A finite abelian group is cyclic if and only if its [[exponent|0ZDW0H0VX4]] equals its order. This is the [[exponent criterion for cyclic groups|0MC0AQZSHE]], and part 1 is the case of two cyclic factors.
3. In a commutative ring $R$, if two ideals $I$ and $J$ satisfy $I + J = R$, then $R/(I \cap J) \cong R/I \times R/J$. Part 3 is the case $R = \Z$, $I = m\Z$, $J = n\Z$.

## Explanations

### L1 human

Think of two clocks, one with $3$ hours and one with $4$ hours.
Both clocks start at $0$, and at each tick both hands move forward by $1$.
The pair of positions comes back to $(0, 0)$ only after $12$ ticks, because $12$ is the first number that both $3$ and $4$ divide.
On the way, the pair visits all $3 \cdot 4 = 12$ possible positions.
So one tick of both clocks generates everything, and the pair of clocks behaves like one clock with $12$ hours.
With clocks of $2$ and $6$ hours, the pair comes back after $6$ ticks, so it misses half of the $12$ positions.

### L2 human

We check that $\Z/3 \times \Z/4$ is cyclic, and we compute the isomorphism $f$.

1. The gcd is $\gcd(3, 4) = 1$, and $\operatorname{lcm}(3, 4) = 12$.
2. The element $(1, 1)$ has order $12$, by part 1. The group has $3 \cdot 4 = 12$ elements, so $(1, 1)$ generates it.
3. The map $f$ sends $k$ to $(k \bmod 3, k \bmod 4)$. For $k = 0, 1, \ldots, 11$ the images are $(0,0), (1,1), (2,2), (0,3), (1,0), (2,1), (0,2), (1,3), (2,0), (0,1), (1,2), (2,3)$.
4. These $12$ pairs are distinct, so $f$ is a bijection. It is a homomorphism, so it is an isomorphism.

The typical use is to split $\Z/n$ into simpler pieces, or to join two cyclic groups into one.
A trap: $\Z/2 \times \Z/2$ is not $\Z/4$.
Both groups have $4$ elements, but every element of $\Z/2 \times \Z/2$ has order at most $2$.

### L3 human

The direct product is the categorical product of groups, and $\Z/m \times \Z/n$ is cyclic exactly when it is a quotient of $\Z$.
Part 1 says that the exponent of $\Z/m \times \Z/n$ is $\operatorname{lcm}(m, n)$, and the product is cyclic exactly when the exponent reaches the order $mn$.

The isomorphism $\Z/mn \cong \Z/m \times \Z/n$ is also a ring isomorphism.
It is the start of the structure theory of finite abelian groups.
In that theory, every finite abelian group is a product of cyclic groups of prime power order.
The same idea gives the decomposition of a module over a [[principal ideal domain|0CMD0BCH8T]] into primary parts.
