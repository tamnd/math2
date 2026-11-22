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

Let $V = \mathbb{R}$, viewed as a vector space over the field $\mathbb{Q}$: we add real numbers as usual, and we multiply them only by rational scalars.
The vector space axioms hold, because each of them is a rule of arithmetic in $\mathbb{R}$ applied to scalars in $\mathbb{Q} \subseteq \mathbb{R}$.
By the theorem that [[every vector space has a basis|00MS9VMQ9Z]], $V$ has a [[basis|0VTQTPQGAV]] $B$, which is called a *Hamel basis*.
So every real $x$ is, in exactly one way, a finite sum $x = q_1 b_1 + \dots + q_k b_k$ with $q_i \in \mathbb{Q}$ and distinct $b_i \in B$.
We check three facts about $B$.

First, the numbers $1$, $\sqrt{2}$ and $\sqrt{3}$ are independent over $\mathbb{Q}$, so some Hamel basis contains all three.

1. Let $a, b, c \in \mathbb{Q}$ with $a + b\sqrt{2} + c\sqrt{3} = 0$. Move $a$ to the other side and square:
$$2b^2 + 3c^2 + 2bc\sqrt{6} = a^2.$$
2. If $bc \ne 0$, this gives $\sqrt{6} = \dfrac{a^2 - 2b^2 - 3c^2}{2bc} \in \mathbb{Q}$, but $\sqrt{6}$ is irrational. So $b = 0$ or $c = 0$.
3. If $c = 0$, then $a + b\sqrt{2} = 0$, and $b \ne 0$ would make $\sqrt{2} = -a/b$ rational. So $b = 0$, and then $a = 0$.
4. If $b = 0$, the same argument with $\sqrt{3}$ gives $c = 0$ and $a = 0$.
5. So only the trivial relation exists, and the [[extension theorem|0M4SXE5WW3]] puts $1$, $\sqrt{2}$ and $\sqrt{3}$ into a Hamel basis.

Second, $B$ is uncountable.

1. Suppose $B$ were countable. Each real number is determined by a finite list of pairs $(q_i, b_i)$ in $\mathbb{Q} \times B$.
2. The set $\mathbb{Q} \times B$ is countable, and a countable set has only countably many finite lists. So $\mathbb{R}$ would be countable.
3. This contradicts Cantor's theorem that $\mathbb{R}$ is uncountable, so $B$ is uncountable.

Third, the [[dimension|05G2G0P224]] of $\mathbb{R}$ over $\mathbb{Q}$ is $2^{\aleph_0}$, the cardinality of $\mathbb{R}$.

1. Since $B \subseteq \mathbb{R}$, we have $\abs{B} \le 2^{\aleph_0}$.
2. The set $B$ is infinite, so $\abs{\mathbb{Q} \times B} = \aleph_0 \cdot \abs{B} = \abs{B}$, and the set of finite lists from $\mathbb{Q} \times B$ also has cardinality $\abs{B}$.
3. Every real is the value of such a list, so $2^{\aleph_0} \le \abs{B}$.
4. By steps 1 and 3 and the [[Schröder-Bernstein theorem|0A9V6RKQG6]], $\abs{B} = 2^{\aleph_0}$.

## Remarks

### No basis can be written down

The proof of existence uses the axiom of choice, and this is not a weakness of the proof.
It is consistent with Zermelo-Fraenkel set theory without choice that $\mathbb{R}$ has no basis over $\mathbb{Q}$, so no explicit description of a Hamel basis can exist.
What we can do is test small families, as with $1, \sqrt{2}, \sqrt{3}$ above.
The same method shows that $1$ and $\pi$ are independent over $\mathbb{Q}$, because $\pi$ is irrational.

### What changes with the field

Over the field $\mathbb{R}$ itself, the space $\mathbb{R}$ has dimension $1$, and $\{1\}$ is a basis.
So the size of a basis depends on the scalars: the set is the same, but $\dim_\mathbb{R} \mathbb{R} = 1$ while $\dim_\mathbb{Q} \mathbb{R} = 2^{\aleph_0}$.
A Hamel basis also gives [[discontinuous additive functions|FFTNS66XG6]], which are $\mathbb{Q}$-linear maps from $\mathbb{R}$ to $\mathbb{R}$ that are not $\mathbb{R}$-linear.

### Hamel bases and Schauder bases

"Hamel basis" means a basis in the sense of linear algebra, with finite sums only.
In analysis one also uses a [[Schauder basis|RZT4WMH4SG]], which allows convergent infinite sums.
In the sequence space $\ell^2$, the unit vectors $e_1, e_2, \dots$ form a Schauder basis, but not a Hamel basis.
Their span is the set of sequences with finitely many nonzero entries, and it misses the sequence $(1, \tfrac12, \tfrac13, \dots)$, which lies in $\ell^2$ because $\sum 1/n^2$ converges.
By the Baire category theorem, an infinite-dimensional Banach space never has a countable Hamel basis.

## Explanations

### L1 human

Think of the real numbers as a space in which you may only stretch by fractions.
Then $\sqrt{2}$ is a new direction, because no fraction times $1$ equals $\sqrt{2}$.
So is $\sqrt{3}$, and so is $\pi$, and there are far more new directions than whole numbers.
A Hamel basis is a full set of such directions.
It exists, but nobody can list it.

### L2 human

Here is the counting argument in a smaller setting.
Suppose a space over $\mathbb{Q}$ has a basis with $3$ elements $b_1, b_2, b_3$.
Each vector is $q_1 b_1 + q_2 b_2 + q_3 b_3$, so the space is in bijection with $\mathbb{Q}^3$, which is countable.
The same is true for any finite or countable basis, since a countable union of countable sets of finite combinations is countable.
Since $\mathbb{R}$ is uncountable, a Hamel basis must be uncountable, and the cardinal arithmetic above pins its size to $2^{\aleph_0}$.
Watch out: the space $\mathbb{R}$ over $\mathbb{Q}$ is very different from $\mathbb{R}$ over $\mathbb{R}$, even though the set and the addition are the same.
