---
tag: 0CKGBEJX6B
kind: statement
role: theorem
name: Finite subgroups of the multiplicative group of a field are cyclic
msc: ["12E20", "20K01"]
topics: [BAVE5RN4EE]
audience: ug2
about: [0KVGH0J5B3, 04C5ZBG1WT]
uses: [04C5ZBG1WT, 07C6ECNJET, 0X1JXT47GA, 0KVGH0J5B3, 0KJVQV3E0F, 0MC0AQZSHE]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Multiplicative structure
---

## Statement

Let $K$ be a [[field|04C5ZBG1WT]], and let $K^\times = K \setminus \{0\}$ be its multiplicative group, the [[group of units|07C6ECNJET]] of $K$.
Let $G$ be a finite [[subgroup|0X1JXT47GA]] of $K^\times$, of order $n$.
Then $G$ is [[cyclic|0KVGH0J5B3]].
In addition, $G$ is the set of all roots of $x^n - 1$ in $K$.

## Remarks

### Why each hypothesis is needed

1. Commutativity of $K$ is needed. In the [[quaternions|0GE4DVQKR8]], a [[division ring|0EA5BTA0CX]] that is not a field, the [[quaternion group|0NRJGW864D]] $Q_8 = \{\pm 1, \pm i, \pm j, \pm k\}$ is a finite subgroup of the nonzero elements. It has order $8$, and each element has order at most $4$, so it is not cyclic. Here the polynomial $x^2 + 1$ has the six roots $\pm i, \pm j, \pm k$ in $Q_8$, more than its degree $2$.
2. The absence of zero divisors is needed. The units of the ring $\mathbb{Z}/8\mathbb{Z}$ form the group $\{1, 3, 5, 7\}$ of order $4$, and each of its elements satisfies $x^2 = 1$. So the group is not cyclic, and $x^2 - 1$ has four roots in $\mathbb{Z}/8\mathbb{Z}$.
3. Finiteness of $G$ is needed. The group $\mathbb{Q}^\times$ is not cyclic: a generator $g$ would give $2 = g^a$ and $3 = g^b$ for integers $a, b$, and then $2^b = 3^a$. By unique factorization in $\mathbb{Q}^\times$, this forces $a = b = 0$, and then $2 = g^0 = 1$, which is false.

### Consequences

1. [[The multiplicative group of a finite field is cyclic|0EBZ3G455G]]. If $K$ is a [[finite field|0ZXZ82FTX2]] with $q$ elements, then $K^\times$ is cyclic of order $q - 1$. A generator is a [[primitive element|00QSK85Y2X]] of $K$.
2. The [[primitive root theorem|0E0DNQK22P]] for a prime $p$: the group $(\mathbb{Z}/p\mathbb{Z})^\times$ is cyclic of order $p - 1$. For example, $3$ generates $(\mathbb{Z}/7\mathbb{Z})^\times$, because its powers are $3, 2, 6, 4, 5, 1$.
3. The finite subgroups of $\mathbb{C}^\times$ are the groups $\mu_n = \{z \in \mathbb{C} : z^n = 1\}$ of $n$-th [[roots of unity|0YV2CKP2AV]], one for each $n \geq 1$.
4. The finite subgroups of $\mathbb{R}^\times$ are $\{1\}$ and $\{1, -1\}$, because the only real roots of unity are $1$ and $-1$.
5. For each $n$, the group $K^\times$ has at most one subgroup of order $n$, namely the set of roots of $x^n - 1$, when this set has $n$ elements.

### Converse

Every finite cyclic group is a subgroup of the multiplicative group of some field: $\mathbb{Z}/n\mathbb{Z}$ is isomorphic to $\mu_n \subseteq \mathbb{C}^\times$.
But a fixed field contains only some of them.
For example, $\mathbb{R}^\times$ has no subgroup of order $3$.

### Generalizations

1. The theorem holds for an integral domain $R$ in place of $K$. The group $R^\times$ is a subgroup of the multiplicative group of the field of fractions of $R$.
2. In a division ring $D$ of characteristic $p > 0$, every finite subgroup $G$ of $D^\times$ is cyclic. The set of sums of elements of $G$ with coefficients in $\mathbb{F}_p$ is a finite subring of $D$ without zero divisors, so it is a division ring. By [[Wedderburn's little theorem|0RRNVX1VKA]] it is a field, and the theorem applies.
3. A finite group $G$ of order $n$ in which, for each $d \mid n$, at most $d$ elements satisfy $x^d = e$, is cyclic. The [[counting proof|E2JV6XNN5F]] uses only this property.

## Explanations

### L1 human

In ordinary arithmetic, the equation $x^2 = 1$ has only two solutions, $1$ and $-1$.
In the same way, in any field, $x^d = 1$ has at most $d$ solutions.
The theorem says that this limit forces a finite group of nonzero numbers to be very simple.
Such a group is made from the powers of one element.
For example, the four complex numbers $1, i, -1, -i$ form a group under multiplication, and they are the powers of $i$.

### L2 human

We find a generator of $\mathbb{F}_{11}^\times$, which is cyclic of order $10$ by the theorem.

1. The order of each element divides $10$, so it is $1, 2, 5$ or $10$.
2. An element $a$ has order $10$ exactly when $a^2 \neq 1$ and $a^5 \neq 1$.
3. Try $a = 2$. Then $2^2 = 4 \neq 1$ and $2^5 = 32 = 2 \cdot 11 + 10 \equiv 10 \pmod{11}$. So $2^5 \neq 1$.
4. So $2$ has order $10$, and $\mathbb{F}_{11}^\times = \langle 2 \rangle$.

The typical use is a structure fact: in a finite field there is a generator $g$, so every nonzero element is a power of $g$.
This turns multiplication into addition of exponents modulo $q - 1$.

A trap: the theorem gives a generator, but it does not say how to find one.
There is no known formula for a generator of $\mathbb{F}_p^\times$, and in practice we test candidates as above.

### L3 human

The theorem is a statement about the polynomial ring $K[x]$: the bound on the number of roots holds because $K[x]$ is an integral domain with a division algorithm.
There are two standard proofs.
The [[exponent proof|A2VZWSBS4B]] shows that $\exp(G) = |G|$ and uses [[the theorem on exponent and order|0MC0AQZSHE]].
The [[counting proof|E2JV6XNN5F]] counts the elements of each order with Euler's totient function.

For a finite field $\mathbb{F}_q$, the theorem identifies $\mathbb{F}_q^\times$ with $\mathbb{Z}/(q-1)\mathbb{Z}$, but the isomorphism depends on a choice of generator.
Computing this isomorphism, the [[discrete logarithm|0HJHYMGN3C]] problem, is believed to be hard for large $q$, and this is the basis of the [[Diffie-Hellman key exchange|01TKKESHSB]].
For an infinite field, the torsion subgroup of $K^\times$ is the group of all roots of unity in $K$, and it is [[locally cyclic|RXWA8TF2RM]]: every finitely generated subgroup of it is finite and so cyclic.
