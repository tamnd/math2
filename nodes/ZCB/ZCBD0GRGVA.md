---
tag: ZCBD0GRGVA
kind: example
name: Hamel basis of the real numbers over the rationals
aliases: [hamel-basis]
msc: ["15A03", "03E25"]
topics: [MVH97H8B2J]
audience: ug1
instance_of: [0KCQ9Y3QKA]
uses: [0VTQTPQGAV, 00MS9VMQ9Z, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Basis_(linear_algebra)
    locator: Related notions
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal arithmetic
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Example

Let $V = \R$, as a vector space over the field $\Q$.
The vector space axioms hold, because they are field axioms of $\R$ for scalars in $\Q \subseteq \R$.
By the [[existence of a basis|00MS9VMQ9Z]], $V$ has a [[basis|0VTQTPQGAV]] $B$, called a Hamel basis.
So each real $x$ is a unique finite sum $x = q_1 b_1 + \cdots + q_k b_k$ with $q_i \in \Q$ and $b_i \in B$.

Check that $1$ and $\sqrt{2}$ are independent over $\Q$:

1. Let $a, b \in \Q$ with $a \cdot 1 + b \sqrt{2} = 0$.
2. If $b \ne 0$, then $\sqrt{2} = -a / b \in \Q$, but $\sqrt{2}$ is irrational. So $b = 0$.
3. Then $a = 0$. So the family $(1, \sqrt{2})$ is independent, and some Hamel basis contains both, by [[the extension theorem|0M4SXE5WW3]].

Check that $\dim_\Q \R = 2^{\aleph_0}$, the cardinality of $\R$:

1. $B \subseteq \R$, so $\abs{B} \le 2^{\aleph_0}$.
2. Suppose $B$ is countable. A real number is fixed by a finite list of pairs $(q_i, b_i) \in \Q \times B$.
3. The set $\Q \times B$ is countable, and the set of finite lists from a countable set is countable. So $\R$ is countable, which is false.
4. So $B$ is infinite, and the finite lists from $\Q \times B$ form a set of cardinality $\abs{B} \cdot \aleph_0 = \abs{B}$, by the cardinal fact $\kappa \cdot \aleph_0 = \kappa$ for infinite $\kappa$.
5. Each real is the value of such a list, so $2^{\aleph_0} \le \abs{B}$.
6. By steps 1 and 5 and the [[Schröder-Bernstein theorem|0A9V6RKQG6]], $\abs{B} = 2^{\aleph_0}$.

## Remarks

No Hamel basis of $\R$ over $\Q$ can be written down; over ZF alone, its existence is not provable.
A Hamel basis gives discontinuous additive functions; see [[this example|FFTNS66XG6]].
The word "Hamel basis" means an algebraic basis, with finite sums only.
A [[Schauder basis|RZT4WMH4SG]] of a Banach space allows convergent infinite sums: $e_1, e_2, \dots$ is a Schauder basis of $\ell^2$, but not a Hamel basis.
Its span is the space of finite sequences, which fails to contain $(1, 1/2, 1/3, \dots) \in \ell^2$.
An infinite-dimensional Banach space has no countable Hamel basis, by the Baire category theorem.

## Explanations

### L1 human

The real numbers form a vector space over the rationals.
Its basis is enormous: it has as many elements as $\R$ itself.
We know that it exists, but no one can list its elements.

### L2 human

To find vectors of a Hamel basis, look for reals that are independent over $\Q$.
Example: $1, \sqrt{2}, \sqrt{3}$ are independent over $\Q$.
The proof squares the relation $b \sqrt{2} + c \sqrt{3} = -a$ and uses that $\sqrt{6}$ is irrational.
But no countable list is enough, because countably many vectors span only a countable subset of $\R$.
