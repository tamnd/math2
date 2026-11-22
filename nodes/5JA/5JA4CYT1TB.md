---
tag: 5JA4CYT1TB
kind: concept
name: Algebra of endomorphisms
msc: ["15A04", "16S50"]
topics: [9080WQTZ3M]
audience: ug1
specializes: [3CTW1P4HBP]
uses: [0J7H0YBFDJ, 0X9MBPP2Z3, 3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Description
  - url: https://en.wikipedia.org/wiki/Endomorphism_ring
    locator: Examples
  - url: https://en.wikipedia.org/wiki/Linear_map
    locator: Endomorphisms and automorphisms
  - book: isbn:9780135367971
    locator: Section 3.2
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Summary

The linear maps from a space to itself can be added, scaled and composed, and with composition as the product they behave much like numbers.
Precisely, the [[endomorphisms|0J7H0YBFDJ]] of a vector space $V$ form an [[associative algebra|3CTW1P4HBP]] $\End(V)$, as in the [[formal description|0E3X2G1ZQB]].
Endomorphisms are added and scaled pointwise, as in the [[space of linear maps|0X9MBPP2Z3]], and they are multiplied by composition.
For $\dim V = n$, a basis identifies $\End(V)$ with the matrix algebra $M_n(F)$.

## Motivation

Endomorphisms can be added and composed, and these operations interact like those of numbers.
For example, $T^2 - 3T + 2\id = (T - \id)(T - 2\id)$ holds for every endomorphism $T$.
The algebra $\End(V)$ is the setting for polynomials in $T$, for eigenvalue theory and for normal forms.
It also explains why square matrices form a ring: they are the endomorphisms of $F^n$ written in a basis.

## Notation

The algebra is written $\End_F(V)$, $\End(V)$ or $L(V)$.
The product of $S$ and $T$ is $ST = S \circ T$, so $(ST)(v) = S(T(v))$.
The unit is $\id_V$, often written $I$ or $1$, and $T^0 = I$.

## Remarks

### Examples

In [[$\End(F^2)$|D7CQ3JQDE0]], which is $M_2(F)$ in the standard basis, two matrix units do not commute.
The algebra [[$\End(F)$|3AWAJSQR16]] is isomorphic to the field $F$ itself.
The endomorphisms of the polynomial space $F[x]$ form an infinite-dimensional algebra.
It contains the derivative $D$ and the multiplication $X$ by $x$, and they satisfy $DX - XD = \id$.

### What it is not

[[All maps $\R \to \R$ under composition|R1SP7B1F0V]] form a vector space, but composition does not distribute over sums from the left, so they do not form an algebra.
The space $M_{2 \times 3}(F)$ consists of linear maps, but it is not an algebra, since two $2 \times 3$ matrices cannot be multiplied.

### Properties

By the [[algebra theorem|7BDGQ1Q46E]], $\End(V)$ is an associative algebra with unit, and $\End(V) \cong M_n(F)$ for $\dim V = n$.
Its dimension is then $n^2$, by the [[dimension theorem|0Z9N1ER0W0]].
It is not commutative for $\dim V \ge 2$, and its center consists of the scalar maps $a \id_V$, by the [[center theorem|ZQPD85QCC8]].
Its units are the automorphisms, so its [[group of units|07C6ECNJET]] is $GL(V)$.
For $1 \le \dim V < \infty$, its only two-sided ideals are $\{0\}$ and $\End(V)$, so it is a [[simple ring|62M0NC3E2T]].
For infinite-dimensional $V$, the [[finite-rank operators|Z8FABSYQTS]] form a proper nonzero [[two-sided ideal|0CD87SFM2N]].

### History

Peano gave the modern definition of vector spaces and linear maps in 1888.
The [[matrix ring|AB2MD5CD13]] $M_n(F)$ is the coordinate form of the algebra $\End(V)$.
For abelian groups, the additive maps also form a ring with the same operations, called the endomorphism ring.

### Watch out

Do not assume that $ST = TS$: in $\End(\R^2)$, the rotation by $90°$ and the reflection in the $x$-axis do not commute.
Do not assume that $ST = 0$ forces $S = 0$ or $T = 0$, since $\End(V)$ has zero divisors for $\dim V \ge 2$.
For the same reason, $(S + T)^2$ is $S^2 + ST + TS + T^2$, not $S^2 + 2ST + T^2$.

### Try it

First, for $S(x, y) = (x, 0)$ and $T(x, y) = (0, x)$ on $\R^2$, compute $ST$ and $TS$.
We get $ST(x, y) = S(0, x) = (0, 0)$ and $TS(x, y) = T(x, 0) = (0, x)$, so $ST = 0$ while $TS = T \ne 0$.

Second, show that $T^2 - 3T + 2\id = (T - \id)(T - 2\id)$.
Expanding gives $T^2 - 2T - T + 2\id$, which is correct because $T$ commutes with $\id$.

## Explanations

### L1 human

The endomorphisms of a space can be added, scaled and composed.
Composition acts as multiplication, so the endomorphisms behave like numbers in many ways.
Two differences matter: the order of composition matters, and nonzero maps can compose to zero.

### L2 human

In a basis of $V$, the algebra $\End(V)$ becomes the algebra of $n \times n$ matrices.
Sums of maps become sums of matrices, and composites become products.
So matrix algebra is the computational form of $\End(V)$.
Watch out: rules of commutative algebra, such as $(S + T)^2 = S^2 + 2ST + T^2$, need $ST = TS$.

### L3 human

The algebra $\End(V)$ is the endomorphism ring of $V$ in the category of vector spaces over $F$, with an extra $F$-algebra structure.
Representations of a group or of an algebra $A$ on $V$ are homomorphisms $A \to \End(V)$.
For finite-dimensional $V \ne \{0\}$, the algebra $\End(V)$ is simple with center $F$, so it is a central simple algebra over $F$.
