---
tag: 07JBSZE0V4
kind: concept
name: Dual space
msc: ["15A04"]
topics: [9K7FFF26QR]
audience: ug1
specializes: [000AYPA9AJ]
uses: [07YQ1C78G0, 0X9MBPP2Z3, 000AYPA9AJ]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Algebraic dual space
  - book: isbn:9783031410253
    locator: Section 3F
  - book: isbn:9780134860244
    locator: Section 2.6
  - book: isbn:9780387728285
    locator: Chapter 3
same_as:
  wikidata: Q752487
  wikipedia: Dual space
inventory: [X25E8AQW7R]
---

## Summary

The linear ways of measuring the vectors of a space can be added and scaled, so they form a vector space of their own, the dual space.
It is the second space that sits next to every vector space, and much of linear algebra reads best as a conversation between the two.
Let $F$ be a field and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
The *dual space* of $V$ is the set of all [[linear forms|07YQ1C78G0]] on $V$,
$$V^* = \Hom_F(V, F),$$
with the pointwise operations $(f + g)(v) = f(v) + g(v)$ and $(af)(v) = a f(v)$ for $f, g \in V^*$, $a \in F$ and $v \in V$.
It is a vector space over $F$, because it is the case $W = F$ of the [[space of linear maps|0X9MBPP2Z3]] $\Hom(V, W)$.
The [[formal definition|0M856Q1AMZ]] states it.

## Motivation

We often know a vector only through numbers that we measure on it: its coordinates, its component along a direction, or the left side of a linear equation evaluated at it.
Each such measurement is a linear form, and two measurements can be added or scaled to give a third.
So the measurements form a vector space, and the dual space is the name of that space.

The dual space turns statements about $V$ into statements about a second space.
A subspace of $V$ can be described by the forms that vanish on it, which is the idea of the [[annihilator|0ASHNYF7AG]] and of describing a plane by its equations.
A linear map $V \to W$ gives a [[dual map|0AZ5ARP287]] $W^* \to V^*$ that goes the other way, and in coordinates this is the transpose of a matrix.
In physics, a gradient is most naturally a covector, an element of a dual space, and in functional analysis the dual space is the main tool for studying spaces of functions.

## Notation

Books write $V^*$, $V'$, $V^\vee$, $\Hom(V, F)$ or $\mathcal{L}(V, F)$.
The elements are called linear forms, linear functionals, dual vectors or covectors.
The value of $f \in V^*$ at $v \in V$ is written $f(v)$ or $\langle f, v \rangle$, and the bracket here is a pairing between two different spaces, not an inner product.
In functional analysis, $V'$ or $V^*$ often means the [[continuous dual|4A82S5FVRT]], which is a smaller space.
Mathlib writes `Module.Dual F V`.

## Remarks

### A first look at the dual of the plane

On $\R^2$, every linear form has the shape $f(x, y) = ax + by$, because $f(x, y) = x f(1, 0) + y f(0, 1)$.
So a form is fixed by the two numbers $a = f(1, 0)$ and $b = f(0, 1)$.
Add the forms $2x + y$ and $x - 3y$ and scale the result by $2$:
$$2\big((2x + y) + (x - 3y)\big) = 6x - 4y.$$
The operations on forms are the operations on the pairs $(a, b)$, so $(\R^2)^*$ is again a plane.
In general the [[row vectors|EGJXHX96R9]] of length $n$ act on columns by $x \mapsto cx$, and this gives every linear form on $F^n$.

### More duals worked out

The space $M_n(F)$ of square matrices has a dual that is again $M_n(F)$, through the [[trace pairing|4F7GWKTQ1H]] $A \mapsto (X \mapsto \tr(AX))$.
For example, the form $X \mapsto x_{11} + 2x_{12}$ on $M_2(F)$ is $\tr(AX)$ for $A = \begin{pmatrix} 1 & 0 \\ 2 & 0 \end{pmatrix}$.

The space $F^{(\N)}$ of sequences with finitely many nonzero terms has a much larger dual.
A form on it may take any value $c_k$ on the $k$-th unit sequence, so its [[dual is the space of all sequences|GZ627X1S7Y]] $F^{\N}$.
The form with $c = (1, 1, 1, \dots)$ adds up the terms, and at $(2, 0, 5, 0, \dots)$ it gives $2 + 5 = 7$.

Two small cases complete the picture.
The dual of the zero space is zero, since the only map $\{0\} \to F$ sends $0$ to $0$.
The dual of $F$ itself is a copy of $F$, since each form on $F$ is $x \mapsto cx$ with $c = f(1)$.

### What the dual is not

The functions $g(x, y) = ax + by + c$ on $\R^2$ form a vector space, but it is [[not the dual space|FWNY6EYBC3]].
The constant function $1$ belongs to it, and it fails $f(0) = 0$, which every linear form satisfies.
That space has dimension $3$, one more than the dual.
The space of all functions $\R^2 \to \R$ is not the dual either, because it contains $h(x, y) = xy$, which is not additive.
For example, $h(1, 1) = 1$, but $h(2, 2) = 4$, which is not $h(1, 1) + h(1, 1) = 2$.

### How big the dual is

In finite dimension the dual has the same size as the space.
If $b_1, \dots, b_n$ is a basis of $V$, the [[dual basis|0ZD2CF6ZS0]] of coordinate forms is a basis of $V^*$, so $\dim V^* = \dim V$ by the theorem on the [[dimension of the dual space|00889YD15K]].
More generally, a form is fixed by its values on a basis $B$, and these values are free, so $f \mapsto (f(b))_{b \in B}$ is an isomorphism $V^* \to F^B$ by the [[theorem on bases|0R8X9XA83A]].

In infinite dimension this isomorphism shows that the dual is larger.
The space $V$ is made of finite combinations of basis vectors, while $V^*$ allows any family of values.
The [[Erdős-Kaplansky theorem|S5ET1HG2ZX]] makes this exact, and it gives $\dim V^* > \dim V$ whenever $\dim V$ is infinite.

### The rules you can use

Each linear map $f \colon V \to W$ has a [[dual map|0AZ5ARP287]] $f^* \colon W^* \to V^*$, given by $f^*(\varphi) = \varphi \circ f$, and $(g \circ f)^* = f^* \circ g^*$.
Each subspace $U$ of $V$ has an [[annihilator|0ASHNYF7AG]] $U^0 \subseteq V^*$, and in finite dimension $\dim U + \dim U^0 = \dim V$.
The evaluation map $V \to V^{**}$, $v \mapsto (f \mapsto f(v))$, is always injective, and it is an isomorphism exactly when $V$ is finite-dimensional, by the theorem on the [[double dual|0ZJM9D7NPS]].

### Watch out

A common mistake is to treat $V^*$ as the same space as $V$.
In finite dimension the two are isomorphic, but every isomorphism needs a choice, such as a basis.
For example, the basis $(1, 1), (1, 2)$ of $\R^2$ sends $(1, 1)$ to the form $2x - y$, while the standard basis sends it to $x + y$; the [[basis-dependent isomorphism|A3CP855PNV]] works this out.
In infinite dimension there is no isomorphism at all, and the coordinate forms of a basis are independent but [[do not span the dual|JCMJDY59CH]].

### History

In the absolute differential calculus of Ricci and Levi-Civita, published in 1900, the covariant components of a tensor carry lower indices, and they behave like elements of a dual space.
In 1907 Riesz and Fréchet showed, independently, that each continuous linear form on the space of square-integrable functions is given by an inner product with one fixed function.

### Try it

First, write the form $f(x, y, z) = \int_0^1 (x + yt + zt^2)\,dt$ on $\R^3$ as $ax + by + cz$.
Integrating gives $x + \tfrac{1}{2} y + \tfrac{1}{3} z$, so $(a, b, c) = (1, \tfrac{1}{2}, \tfrac{1}{3})$.

Second, is $g(x, y) = |x| + |y|$ in $(\R^2)^*$?
No, since $g(1, 0) = 1$ but $g(-1, 0) = 1 \ne -g(1, 0)$, so $g$ does not respect scaling by $-1$.

## Explanations

### L1 human

The dual space of a space of vectors is the space of all linear "measuring rules" on those vectors.
On the plane, the rule "three times the first coordinate plus the second" is one element of the dual space.
Two rules can be added: the rule $x$ plus the rule $y$ is the rule $x + y$.
A rule can be scaled: $5$ times the rule $x$ is the rule $5x$.
So the measuring rules form a space, and on the plane this space is again two-dimensional, since each rule is fixed by two numbers.

### L2 human

Let us find a basis of the dual of $P_1(\R)$, the polynomials $a + bx$, and write one form in it.
A form $f$ is fixed by its values $f(1)$ and $f(x)$, because $1, x$ is a basis.
So let $\varphi_0(a + bx) = a$ and $\varphi_1(a + bx) = b$, and then every form is
$$f = f(1)\, \varphi_0 + f(x)\, \varphi_1.$$
The two forms are independent, since $\varphi_0$ is $1$ at $1$ and $0$ at $x$, and $\varphi_1$ is the other way round.

Now take the integral $f(p) = \int_0^2 p(t)\,dt$.
It gives $f(1) = 2$ and $f(x) = \tfrac{1}{2} \cdot 2^2 = 2$, so $f = 2\varphi_0 + 2\varphi_1$.
Check on $p = 3 + x$:
$$\int_0^2 (3 + t)\,dt = 6 + 2 = 8 \qquad\text{and}\qquad 2 \cdot 3 + 2 \cdot 1 = 8.$$
This is the typical use of the dual space: a form that looks complicated, such as an integral, becomes a short list of numbers once a basis is fixed.

### L3 human

The dual space is the contravariant functor $\Hom(-, F)$ applied to $V$, and the [[dual map|0AZ5ARP287]] is its action on maps.
It turns direct sums into products, $(\bigoplus_i V_i)^* \cong \prod_i V_i^*$, which explains why duals of infinite-dimensional spaces are so large.
When $V$ is finite-dimensional, $V^* \otimes W \cong \Hom(V, W)$, and the [[tensor product|0BF2DE2SYK]] together with the dual space produces all of multilinear algebra.
A [[nondegenerate bilinear form|01NHFZF2SK]] on a finite-dimensional space is the same as an isomorphism $V \to V^*$, and for an inner product this is the [[Riesz representation|04GYPXDXNH]].
In functional analysis the [[continuous dual space|4A82S5FVRT]] replaces $V^*$, and it keeps the good duality properties for Banach and Hilbert spaces.
