---
tag: GF1TE1M8RN
kind: example
name: Almost all real numbers are irrational
msc: ["00A35", "28A05"]
topics: [Z2WNQ1DNTX]
audience: ug2
instance_of: [N1XSAXCQY3]
uses: [N1XSAXCQY3, 0NCJ5WXN6Z, 0DZXAXEJQ9, 01TQB88H4C, VQQM4Y550T, 0XGCZ4GDZ6, 0VQYCCQVJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_all
    locator: Meaning in measure theory
  - url: https://en.wikipedia.org/wiki/Null_set
    locator: lead section
---

## Example

We show that almost all real numbers are [[irrational|0DZXAXEJQ9]] in three senses of [[almost all|N1XSAXCQY3]]: the countable sense, the measure sense and the topological sense.
The set of exceptions is the set $\mathbb{Q}$ of [[rational numbers|0NCJ5WXN6Z]].

1. The set $\mathbb{Q}$ is [[countable|01TQB88H4C]].
   The map $\mathbb{Q} \to \mathbb{Z} \times \mathbb{Z}$ that sends $q$ to its lowest terms pair $(a, b)$ with $b > 0$ is injective, and $\mathbb{Z} \times \mathbb{Z}$ is countable.
   So the claim holds in the countable sense.
2. By step 1, we can list the rational numbers as $q_1, q_2, q_3, \ldots$.
   Fix $\varepsilon > 0$.
3. Around each $q_k$ put an open interval $I_k$ of length $\varepsilon / 2^k$.
   Then $\mathbb{Q} \subseteq \bigcup_k I_k$.
4. The total length of the intervals is a geometric series:
   $$\sum_{k=1}^{\infty} \frac{\varepsilon}{2^k} = \varepsilon \left( \frac{1}{2} + \frac{1}{4} + \cdots \right) = \varepsilon.$$
5. So $\mathbb{Q}$ is covered by intervals of total length at most $\varepsilon$, for every $\varepsilon > 0$.
   This is the definition of a set of [[measure zero|VQQM4Y550T]], so the claim holds in the measure sense.
6. A single point $\{q\}$ is closed and contains no open interval, so it is [[nowhere dense|0VQYCCQVJ5]].
   So $\mathbb{Q} = \bigcup_k \{q_k\}$ is a countable union of nowhere dense sets, which is a [[meager set|0XGCZ4GDZ6]].
   The claim holds in the topological sense: a generic real number is irrational.

## Remarks

The three senses agree here because the set of exceptions is countable.
The rationals are dense in $\mathbb{R}$, so "negligible" does not mean "far from most points".

Change the set of exceptions and the senses can split.
With the algebraic numbers in place of $\mathbb{Q}$, the same three steps work, because that set is also countable, so almost all real numbers are transcendental.
With the Cantor set, the senses still agree: the Cantor set is uncountable, but it has measure zero and is nowhere dense.
With the complement of the Liouville numbers, they disagree: that set has full measure, but it is meager.

## Explanations

### L1 human

Throw a dart at a ruler and look at the point it hits.
The fractions are everywhere on the ruler, but they take up no length at all.
You can cover all of them with tiny pieces of tape whose total length is as small as you like.
So the dart almost never hits a fraction, and we say that almost all real numbers are irrational.

### L2 human

We cover the rational numbers in $[0, 1]$ by intervals of total length at most $\tfrac{1}{100}$.
List them by increasing denominator:
$$q_1 = 0, \ q_2 = 1, \ q_3 = \tfrac{1}{2}, \ q_4 = \tfrac{1}{3}, \ q_5 = \tfrac{2}{3}, \ q_6 = \tfrac{1}{4}, \ q_7 = \tfrac{3}{4}, \ \ldots$$
Around $q_k$ put an interval of length $\tfrac{1}{100} \cdot 2^{-k}$, so the first has length $\tfrac{1}{200}$ and the second $\tfrac{1}{400}$.
The lengths add up to
$$\frac{1}{100} \left( \frac{1}{2} + \frac{1}{4} + \cdots \right) = \frac{1}{100}.$$
Since $\tfrac{1}{100}$ can be replaced by any $\varepsilon > 0$, the rationals in $[0, 1]$ have measure $0$, and the irrationals in $[0, 1]$ have measure $1 - 0 = 1$.

The typical use is a proof that a set is large because its complement is countable.
Watch out: the rationals and the irrationals are both dense, so no interval separates them, and the comparison is by measure or by category, not by position.
