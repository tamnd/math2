---
tag: DVEZQ8SP64
kind: example
name: A proper subspace of the same infinite dimension
msc: ["15A03"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [00YC1D652K]
uses: [0EPTJA5QV4, 05G2G0P224, 0JGZCDT5DN]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_(vector_space)
    locator: Facts
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Example

Let $F$ be a field and let $V = F[x]$ be the [[space of all polynomials|0JGZCDT5DN]] over $F$.
Let $W = x F[x]$ be the set of polynomials with no constant term:
$$W = \{p \in F[x] : p(0) = 0\} = \{a_1 x + a_2 x^2 + \dots + a_n x^n : n \ge 1, \ a_i \in F\}.$$
We check that $W$ is a proper [[subspace|0EPTJA5QV4]] of $V$ and that $W$ has the same dimension as $V$.

1. The zero polynomial has value $0$ at $0$, so $0 \in W$.
2. If $p(0) = 0$ and $q(0) = 0$, then $(p + q)(0) = p(0) + q(0) = 0 + 0 = 0$, so $p + q \in W$.
3. If $p(0) = 0$ and $c \in F$, then $(cp)(0) = c\,p(0) = c \cdot 0 = 0$, so $cp \in W$.
4. The constant polynomial $1$ has value $1 \ne 0$ at $0$, so $1 \notin W$ and $W \ne V$.
5. The monomials $1, x, x^2, \dots$ form a basis of $V$, so the [[dimension|05G2G0P224]] of $V$ is $\aleph_0$, the size of the natural numbers.
6. The monomials $x, x^2, x^3, \dots$ lie in $W$. They are independent, because they are part of the basis of step 5.
7. They span $W$: if $p = a_0 + a_1 x + \dots + a_n x^n$ has $p(0) = 0$, then $a_0 = p(0) = 0$, so $p = a_1 x + \dots + a_n x^n$.
8. So $x, x^2, x^3, \dots$ is a basis of $W$. It is indexed by the positive integers, a countably infinite set, so $\dim W = \aleph_0 = \dim V$.

## Remarks

The example shows that in infinite dimension a subspace can have the full dimension of the space and still be smaller.
In finite dimension this cannot happen: a [[subspace of full dimension is the whole space|0WGAXEK99E]].
The difference is the same as for sets, where the infinite set $\{0, 1, 2, \dots\}$ has the proper subset $\{1, 2, 3, \dots\}$ of the same size.

The two spaces are even isomorphic.
Multiplication by $x$ sends $p$ to $xp$, it is linear, and it is injective, since $xp = 0$ forces $p = 0$.
Its image is exactly $W$, because every $a_1 x + \dots + a_n x^n$ equals $x(a_1 + a_2 x + \dots + a_n x^{n - 1})$.
So $p \mapsto xp$ is an isomorphism $V \to W$, and it sends the basis $1, x, x^2, \dots$ of $V$ to the basis $x, x^2, x^3, \dots$ of $W$.

The same thing happens in the [[space of sequences|0GZB2SN0PH]] $F^{\mathbb{N}}$.
The sequences with first term $0$ form a proper subspace, and the right shift $(a_0, a_1, \dots) \mapsto (0, a_0, a_1, \dots)$ is an isomorphism onto it.
If we change $W$ to the polynomials with $p(0) = p'(0) = 0$, the same argument works with the basis $x^2, x^3, \dots$, so even a subspace of "codimension $2$" has full dimension.

## Explanations

### L1 human

In a finite-dimensional space, a subspace that has as many basis vectors as the whole space is the whole space.
With infinitely many basis vectors, this fails.
The polynomials with no constant term, such as $x + 3x^2$, form a smaller space, since the polynomial $1$ is missing.
But they still have infinitely many basis vectors $x, x^2, x^3, \dots$, one for each basis vector $1, x, x^2, \dots$ of all polynomials.

### L2 human

Match the two bases by the rule $x^k \mapsto x^{k + 1}$:
$$1 \mapsto x, \qquad x \mapsto x^2, \qquad x^2 \mapsto x^3, \qquad \dots$$
Every basis vector of $W$ appears exactly once on the right, so the two bases have the same size, and the dimensions agree.
Yet the vector $1$ of $V$ is not in $W$.
The lesson is that the rule "equal dimension forces equality" needs finite dimension, and a proof of it must use finiteness somewhere, as the proof for [[dimension of a subspace|0QW084460E]] does.
