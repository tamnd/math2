---
tag: 3AWAJSQR16
kind: example
name: The endomorphisms of a field as a one-dimensional space
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
instance_of: [5JA4CYT1TB]
uses: [0E3X2G1ZQB, 0RJF668P1T, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
---

## Example

On a line, every linear map is multiplication by a number, so the endomorphisms of a line are just the numbers again.
Let $F$ be a field, viewed as a vector space over itself of dimension $1$, and consider the [[algebra of endomorphisms|0E3X2G1ZQB]] $\End(F)$.
For $a \in F$, let $m_a \colon F \to F$ be multiplication by $a$, so $m_a(x) = ax$.

1. Each $m_a$ is [[linear|0RJF668P1T]], since $m_a(x + y) = ax + ay$ and $m_a(cx) = c\,(ax)$, using that $F$ is commutative.
2. Each linear $T \colon F \to F$ equals $m_a$ with $a = T(1)$, since $T(x) = T(x \cdot 1) = x\,T(1) = ax$.
3. The scalar $a$ is unique, since $m_a(1) = a$, so $a \mapsto m_a$ is a bijection $F \to \End(F)$.
4. Sums and multiples match, since $m_a + m_b = m_{a+b}$ and $c\,m_a = m_{ca}$.
5. Products match, since $(m_a m_b)(x) = a(bx) = (ab)x$, so $m_a m_b = m_{ab}$, and also $m_1 = \id_F$.
6. So $a \mapsto m_a$ is an algebra isomorphism $F \cong \End(F)$, and $\End(F)$ is commutative.

Check: over $\R$, $m_2 m_3 = m_6$, and both sides send $5$ to $30$.

## Remarks

Step 2 is the [[theorem on bases|0R8X9XA83A]] for the basis $(1)$ of $F$, and in matrix terms it says $\End(F) \cong M_1(F) = F$.
The automorphisms are the maps $m_a$ with $a \ne 0$, so $GL(F) \cong F^\times$.
The same holds for every one-dimensional space $V$, where $a \mapsto a \id_V$ is an isomorphism $F \cong \End(V)$.
If we change the dimension to $2$ or more, the algebra $\End(V)$ is no longer commutative.

## Explanations

### L1 human

A linear map from the number line to itself is multiplication by a fixed number.
Adding or composing such maps adds or multiplies the numbers.
So the endomorphisms of a line behave exactly like the numbers.

### L2 human

The example is the case $n = 1$ of $\End(V) \cong M_n(F)$.
Apart from $V = \{0\}$, it is the only case in which $\End(V)$ is commutative.
Watch out: nonlinear maps such as $x \mapsto x^2$ send $F$ to itself, but they are not endomorphisms of the vector space $F$.
