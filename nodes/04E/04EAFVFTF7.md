---
tag: 04EAFVFTF7
kind: object
name: Circle group
msc: [22A05]
topics: [BAZT8JJ70S]
audience: ug1
instance_of: [082GHNPJ53]
uses: [071DDFVG4J, 09FTAET5Z4, 0FFXKTKKQC, 0FTH2E9TAS, 07GJV36896, 0CXXJNG5B6, 0CGYNDCWRR, 0DBWXQRXQJ]
sources:
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Circle_group
    locator: Isomorphisms and conventions
same_as:
  wikidata: Q105356493
  wikipedia: Circle group
---

## Description

The circle group is the set $\mathbb{T} = \{z \in \mathbb{C} : |z| = 1\}$ of the [[complex numbers|09FTAET5Z4]] of [[absolute value|0FFXKTKKQC]] $1$, with complex multiplication.
In the complex plane, $\mathbb{T}$ is the circle of radius $1$ about $0$.
We check that $\mathbb{T}$ is an [[abelian group|082GHNPJ53]].

1. Closure. For $z, w \in \mathbb{T}$, $|zw| = |z| \, |w| = 1 \cdot 1 = 1$. So $zw \in \mathbb{T}$.
2. Associativity. Multiplication of complex numbers is associative, so it is associative on the subset $\mathbb{T}$.
3. Identity. $|1| = 1$, so $1 \in \mathbb{T}$, and $1 \cdot z = z \cdot 1 = z$.
4. Inverses. For $z \in \mathbb{T}$, the [[complex conjugate|0FTH2E9TAS]] satisfies $z \bar{z} = |z|^2 = 1$. Also $|\bar{z}| = |z| = 1$. So $z^{-1} = \bar{z}$ is in $\mathbb{T}$.
5. Commutativity. Multiplication of complex numbers is commutative, so $zw = wz$.

So $\mathbb{T}$ is an abelian group, and it is a [[subgroup|0X1JXT47GA]] of the group $\mathbb{C} \setminus \{0\}$ under multiplication.
By [[Euler's formula|04R3CY41VJ]], each $z \in \mathbb{T}$ is $e^{i\theta} = \cos \theta + i \sin \theta$ for a real number $\theta$, an [[argument|070PFSYJJR]] of $z$.
Then $e^{i\theta} e^{i\varphi} = e^{i(\theta + \varphi)}$, so multiplication in $\mathbb{T}$ adds the angles.

## Remarks

### The isomorphism with R/Z

Let $p \colon (\mathbb{R}, +) \to \mathbb{T}$ be the map $p(t) = e^{2\pi i t}$, given by the [[complex exponential|07GJV36896]].

1. Homomorphism. $p(s + t) = e^{2\pi i s + 2\pi i t} = e^{2\pi i s} e^{2\pi i t} = p(s) p(t)$.
2. Onto. Each $z \in \mathbb{T}$ is $e^{i\theta}$ for a real $\theta$. Then $z = p(\theta / 2\pi)$.
3. Kernel. $p(t) = 1$ means $\cos 2\pi t = 1$ and $\sin 2\pi t = 0$. This holds exactly when $t \in \mathbb{Z}$.
4. Isomorphism. By the [[first isomorphism theorem|0CXXJNG5B6]], the map $t + \mathbb{Z} \mapsto e^{2\pi i t}$ is an isomorphism from the [[quotient group|0KYX2N69J0]] $\mathbb{R}/\mathbb{Z}$ to $\mathbb{T}$.

Thus $\mathbb{T}$ is the real line with each $t$ identified with $t + 1$, as in the [[circle as a quotient of the real line|0WH1GVBJNH]].

### The isomorphism with SO(2)

Let $\rho \colon \mathbb{T} \to \mathrm{SO}(2)$ send $z = a + bi$ to the matrix $\rho(z) = \begin{pmatrix} a & -b \\ b & a \end{pmatrix}$.
Here [[$\mathrm{SO}(2)$|0CGYNDCWRR]] is the group of real $2 \times 2$ matrices $M$ with $M^{\mathsf{T}} M = I$ and $\det M = 1$.

1. Values in $\mathrm{SO}(2)$. The columns $(a, b)$ and $(-b, a)$ have length $\sqrt{a^2 + b^2} = 1$ and dot product $-ab + ba = 0$. Also $\det \rho(z) = a^2 + b^2 = 1$.
2. Homomorphism. For $w = c + di$, we have $zw = (ac - bd) + (ad + bc)i$.
3. The matrix product is $\begin{pmatrix} a & -b \\ b & a \end{pmatrix} \begin{pmatrix} c & -d \\ d & c \end{pmatrix} = \begin{pmatrix} ac - bd & -(ad + bc) \\ ad + bc & ac - bd \end{pmatrix}$. This is $\rho(zw)$.
4. Injective. The first column of $\rho(z)$ is $(a, b)$, so $\rho(z)$ determines $z$.
5. Onto. Let $M \in \mathrm{SO}(2)$ have the first column $(a, b)$. This column has length $1$, so $a^2 + b^2 = 1$.
6. The second column has length $1$ and is perpendicular to $(a, b)$, so it is $(-b, a)$ or $(b, -a)$.
7. The second choice gives $\det M = -a^2 - b^2 = -1$. So the second column is $(-b, a)$, and $M = \rho(a + bi)$.

So $\rho$ is an isomorphism.
The matrix $\rho(e^{i\theta})$ is the [[rotation matrix|0B9QNFGTHM]] by the angle $\theta$.

### The torsion subgroup

An element $z \in \mathbb{T}$ has finite order exactly when $z^n = 1$ for some $n \geq 1$, that is, when $z$ is in the [[group of $n$th roots of unity|0WX11EA3F3]] $\mu_n$ for some $n$.
So the [[torsion subgroup|0DBWXQRXQJ]] of $\mathbb{T}$ is the union $\bigcup_{n \geq 1} \mu_n$.
Under the isomorphism with $\mathbb{R}/\mathbb{Z}$, $e^{2\pi i t}$ has finite order exactly when $nt \in \mathbb{Z}$ for some $n \geq 1$, that is, when $t$ is rational.
So the torsion subgroup corresponds to $\mathbb{Q}/\mathbb{Z}$.
For example, $e^{2\pi i \sqrt{2}}$ has infinite order, because $\sqrt{2}$ is irrational.

### A non-example

The circle $\{z \in \mathbb{C} : |z| = 2\}$ is not a group under multiplication: closure fails, because $|2 \cdot 2| = 4$.

## Explanations

### L1 human

The circle group is the circle of radius $1$ in the complex plane.
The product of two points of the circle is again a point of the circle.
If we describe each point by its angle, the product adds the two angles.
So the circle group is the group of all turns of a wheel about its centre.

### L2 human

We compute with the point $z = \frac{3}{5} + \frac{4}{5} i$.

1. $|z|^2 = \frac{9}{25} + \frac{16}{25} = 1$, so $z \in \mathbb{T}$.
2. The inverse is $\bar{z} = \frac{3}{5} - \frac{4}{5} i$. Check: $z \bar{z} = \frac{9}{25} + \frac{16}{25} = 1$.
3. The square is $z^2 = \frac{9 - 16}{25} + \frac{24}{25} i = -\frac{7}{25} + \frac{24}{25} i$, and $|z^2|^2 = \frac{49 + 576}{625} = 1$.
4. The matrix of $z$ is $\rho(z) = \begin{pmatrix} 3/5 & -4/5 \\ 4/5 & 3/5 \end{pmatrix}$, a rotation of the plane.

The typical use of $\mathbb{T}$ is to measure angles as a group, where adding $2\pi$ to an angle changes nothing.
A trap is to take the inverse $1/z$ for a general complex number $z$ to be $\bar{z}$: this holds only when $|z| = 1$.

### L3 human

The circle group is a compact [[Lie group|7JBRGCVJRB]] of dimension $1$, and each compact connected abelian Lie group is a product of copies of $\mathbb{T}$, a [[torus|03NM7DZXXC]].
The continuous homomorphisms $\mathbb{T} \to \mathbb{T}$ are the maps $z \mapsto z^n$ for $n \in \mathbb{Z}$.
So the [[Pontryagin dual|FMW57WNPDB]] of $\mathbb{T}$ is $\mathbb{Z}$, and the dual of $\mathbb{Z}$ is $\mathbb{T}$.
This duality is the base of [[Fourier series|G12KXDHPPS]]: a function on $\mathbb{T}$ is written as a sum of the characters $z \mapsto z^n$.
As an abstract group, without topology, $\mathbb{T}$ is divisible, and it is isomorphic to $(\mathbb{Q}/\mathbb{Z}) \oplus \mathbb{Q}^{(\mathfrak{c})}$, but this uses the axiom of choice.
