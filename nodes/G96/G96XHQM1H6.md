---
tag: G96XHQM1H6
kind: example
name: Multiplication of complex numbers is commutative
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
instance_of: [099E72KTF8]
uses: [09FTAET5Z4, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: lead section
---

## Example

A [[complex number|09FTAET5Z4]] has the form $a + bi$ with $a, b \in \mathbb{R}$, where $i^2 = -1$.
The product is defined by $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$.
We check that this multiplication is [[commutative|099E72KTF8]].
Let $a, b, c, d \in \mathbb{R}$.

1. By the definition, $(a + bi)(c + di) = (ac - bd) + (ad + bc)i$.
2. By the definition with the roles of the two factors exchanged, $(c + di)(a + bi) = (ca - db) + (cb + da)i$.
3. Multiplication and addition of [[real numbers|08J2M1JYAG]] are commutative, so $ca = ac$, $db = bd$ and $cb + da = ad + bc$.
4. By steps 1 to 3, the two products have the same real part and the same imaginary part, so they are equal.

A numerical check with $1 + 2i$ and $3 + i$:

5. $(1 + 2i)(3 + i) = (3 - 2) + (1 + 6)i = 1 + 7i$.
6. $(3 + i)(1 + 2i) = (3 - 2) + (6 + 1)i = 1 + 7i$.

## Remarks

The proof uses only the commutativity of addition and multiplication of real numbers.
Multiplication of complex numbers is also associative, and the nonzero complex numbers form an abelian group under multiplication.
The complex numbers $\cos\theta + i\sin\theta$ of absolute value $1$ act on the plane as rotations about the origin, so this example also explains why [[rotations of the plane commute|AX0JXCRNJB]].
For the quaternions, a larger number system with $i^2 = j^2 = k^2 = ijk = -1$, the same kind of definition gives a multiplication that is not commutative: $ij = k$, but $ji = -k$.

## Explanations

### L1 human

Complex numbers are multiplied with the usual rules of algebra and the extra rule $i \cdot i = -1$.
If we multiply in the other order, each part of the computation is a product or a sum of real numbers in the other order.
For real numbers the order does not matter, so for complex numbers it does not matter either.

### L2 human

To prove that an operation given by a formula is commutative, write out $x \ast y$ and $y \ast x$ and compare the parts.
Here the two formulas differ only by the order inside products and sums of real numbers.
A trap is to expect the same for every number system: the quaternions have a similar formula, but their multiplication is not commutative.
