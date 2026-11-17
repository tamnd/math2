---
tag: 0VVPQNVM8S
kind: statement
role: proposition
name: Order of a power
msc: [20A05]
topics: [BAZT8JJ70S]
audience: ug1
about: [0WE2NHZJ7B]
uses: [0WE2NHZJ7B, 0F5QC101Q7, 0C8WYW4KYQ, YJRBCWQV6B]
sources:
  - url: https://en.wikipedia.org/wiki/Order_(group_theory)
    locator: Order and structure
---

## Statement

Let $G$ be a [[group|G5S1M9]] with identity element $e$.

1. Let $g \in G$ be an element of finite [[order|0WE2NHZJ7B]] $n$, and let $k$ be an integer. Then the order of $g^k$ is $n / \gcd(n, k)$, where $\gcd$ is the [[greatest common divisor|0C8WYW4KYQ]].
2. Let $g, h \in G$ be [[commuting elements|YJRBCWQV6B]], that is, $gh = hg$. Let $g$ have finite order $m$ and $h$ have finite order $n$, with $\gcd(m, n) = 1$. Then $gh$ has order $mn$.

## Remarks

In part 1, $\gcd(n, 0) = n$, so $g^0 = e$ has order $n / n = 1$.
In part 1, $g^k$ has order $n$ if and only if $\gcd(n, k) = 1$.
For example, if $g$ has order $12$, then $g^8$ has order $12 / \gcd(12, 8) = 12 / 4 = 3$.

### Why each hypothesis is needed

1. In part 1 the order of $g$ must be finite. In $(\mathbb{Z}, +)$ the element $1$ has infinite order, and each multiple $k \cdot 1$ with $k \neq 0$ also has infinite order.
2. In part 2 the elements must commute. In the [[symmetric group|0515A6D2Y1]] $S_3$, with composition from right to left, $(1\,2)$ has order $2$ and $(1\,2\,3)$ has order $3$. Their product $(1\,2)(1\,2\,3) = (2\,3)$ has order $2$, not $6$. The two elements do not commute, because $(1\,2\,3)(1\,2) = (1\,3)$.
3. In part 2 the orders must be coprime. Let $g$ have order $n \geq 2$, and let $h = g^{-1}$. Then $g$ and $h$ commute and both have order $n$, by [[the order of an inverse|0PMT9YJZVW]]. But $gh = e$ has order $1$, not $n^2$.
4. In part 2 the orders must be finite. In $(\mathbb{Z}, +)$ the elements $1$ and $-1$ commute and have infinite order, but their sum $0$ has order $1$.

### Consequences

1. Let $G = \langle g \rangle$ be a [[cyclic group|0KVGH0J5B3]] of order $n$. By part 1, $g^k$ generates $G$ if and only if $\gcd(n, k) = 1$. So $G$ has exactly $\varphi(n)$ generators, where $\varphi$ is [[Euler's totient function|0DAMHCT17R]].
2. For each positive divisor $d$ of $n$, the element $g^{n/d}$ has order $n / \gcd(n, n/d) = n / (n/d) = d$. So a cyclic group of order $n$ has an element of each order $d$ that divides $n$.
3. In the [[direct product|00HF4RJ5QN]] $\mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$ with $\gcd(m, n) = 1$, the elements $(1, 0)$ and $(0, 1)$ commute and have orders $m$ and $n$. By part 2, their sum $(1, 1)$ has order $mn$, so the product is cyclic.

### Converse

The converse of part 2 is true for commuting elements of finite order.
Let $gh = hg$ with orders $m$ and $n$, and let $l = \operatorname{lcm}(m, n)$ be the [[least common multiple|007NPQX34K]].
Then $(gh)^l = g^l h^l = e$, so the order of $gh$ divides $l$, by [[the divisibility criterion|0F5QC101Q7]].
Since $l \cdot \gcd(m, n) = mn$, the number $l$ equals $mn$ only when $\gcd(m, n) = 1$.
So when $gh$ has order $mn$, the orders $m$ and $n$ are coprime.

### Generalizations

1. Let $g$ and $h$ commute, have finite orders $m$ and $n$, and satisfy $\langle g \rangle \cap \langle h \rangle = \{e\}$. Then $gh$ has order $\operatorname{lcm}(m, n)$. The proof is the proof of part 2, with the trivial intersection in place of the coprime orders.
2. In an [[abelian group|082GHNPJ53]], if there are elements of finite orders $m$ and $n$, there is an element of order $\operatorname{lcm}(m, n)$. One chooses coprime divisors $m'$ of $m$ and $n'$ of $n$ with $m' n' = \operatorname{lcm}(m, n)$, and applies part 2 to $g^{m/m'}$ and $h^{n/n'}$.

## Explanations

### L1 human

A power of an element comes back to the identity sooner than the element, or at the same time.
Suppose that $g$ has order $12$.
Then $g^8$ is back at the identity after $s$ steps exactly when $8s$ is a multiple of $12$.
This first happens at $s = 3$, because $8 \cdot 3 = 24$, while $8$ and $16$ are not multiples of $12$.
So $g^8$ has order $3$.

### L2 human

We work in $\mathbb{Z}/12\mathbb{Z}$ with addition, where $1$ has order $12$ and the element $k$ is the $k$th multiple of $1$.

1. By part 1, the element $8$ has order $12 / \gcd(12, 8) = 12 / 4 = 3$.
2. Check: the multiples of $8$ modulo $12$ are $8$, $16 \equiv 4$ and $24 \equiv 0$.
3. The element $4$ has order $12 / 4 = 3$, and the element $3$ has order $12 / 3 = 4$.
4. The group is abelian, so $4$ and $3$ commute, and $\gcd(3, 4) = 1$. By part 2, $4 + 3 = 7$ has order $3 \cdot 4 = 12$.
5. Check with part 1: $\gcd(12, 7) = 1$, so $7$ has order $12$.

The typical use of part 1 is to list the generators of a cyclic group: here they are $1, 5, 7, 11$.
The typical use of part 2 is to build an element of large order from elements of small orders.
A trap is to apply part 2 to elements that do not commute, as the example in $S_3$ shows.

### L3 human

Part 1 says that the subgroup $\langle g^k \rangle$ of the cyclic group $\langle g \rangle$ of order $n$ has order $n / \gcd(n, k)$.
In fact $\langle g^k \rangle = \langle g^{\gcd(n, k)} \rangle$, and the subgroups of a cyclic group of order $n$ correspond to the positive divisors of $n$.
Part 2 is the group form of the [[Chinese remainder theorem|0FNN9B4W64]]: for coprime $m$ and $n$, $\mathbb{Z}/mn\mathbb{Z} \cong \mathbb{Z}/m\mathbb{Z} \times \mathbb{Z}/n\mathbb{Z}$.
Generalization 2 shows that in a finite abelian group the [[exponent|0ZDW0H0VX4]] of the group is the order of some element.
This fails for groups that are not abelian: $S_3$ has exponent $6$, but no element of order $6$.
The later sub-areas on cyclic groups and on finite abelian groups use both parts in each step.
