---
tag: 6V2ENEMAS8
kind: example
name: Finite order-preserving maps of the rational order are partial elementary
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
instance_of: [XTNYY0WRQ5]
uses: [XTNYY0WRQ5, XY6CJMDY5M, NDTJ2E895C, 2W4S2H4VYA]
sources:
  - url: https://en.wikipedia.org/wiki/Dense_order
    locator: lead section
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Example

Let $L = \set{<}$ and $\mathcal{M} = \mathcal{N} = (\Q, <)$.
Let $a_1 < a_2 < \dots < a_n$ and $b_1 < b_2 < \dots < b_n$ be rationals, with $n \ge 1$, and let $f(a_i) = b_i$.
We check that $f \colon \set{a_1, \dots, a_n} \to \Q$ is a [[partial elementary map|XTNYY0WRQ5]].

1. Define $\sigma \colon \Q \to \Q$ by $\sigma(x) = x + (b_1 - a_1)$ for $x \le a_1$, and $\sigma(x) = x + (b_n - a_n)$ for $x \ge a_n$.
2. For $a_i \le x \le a_{i+1}$, let $\sigma(x) = b_i + \frac{b_{i+1} - b_i}{a_{i+1} - a_i} (x - a_i)$, the increasing affine map of $[a_i, a_{i+1}]$ onto $[b_i, b_{i+1}]$.
3. The pieces agree at the points $a_i$, where both give $b_i$. So $\sigma$ is well defined, and $\sigma(a_i) = b_i$ for each $i$.
4. Each piece is increasing, and the pieces map the intervals $(-\infty, a_1]$, $[a_i, a_{i+1}]$, $[a_n, \infty)$ onto $(-\infty, b_1]$, $[b_i, b_{i+1}]$, $[b_n, \infty)$. So $\sigma$ is an increasing bijection of $\R$.
5. All coefficients are rational, so $\sigma$ and its inverse map rationals to rationals. So $\sigma$ restricts to an [[automorphism|XY6CJMDY5M]] of $(\Q, <)$.
6. Let $\varphi(x_1, \dots, x_k)$ be a formula and $c_1, \dots, c_k$ elements of $\set{a_1, \dots, a_n}$. [[Automorphisms preserve formulas|NDTJ2E895C]], so $\Q \models \varphi(\bar c)$ iff $\Q \models \varphi(\sigma(\bar c))$.
7. $\sigma(\bar c) = f(\bar c)$ by step 3. So $f$ is partial elementary.

## Remarks

The example shows that in $(\Q, <)$ the partial elementary maps with finite domain are exactly the order-preserving maps; the converse holds because $x < y$ is a formula.
So a type of a finite tuple in $(\Q, <)$ is fixed by the order relations among its entries.
The same argument works in $(\R, <)$, with real coefficients.
It fails in $(\Z, <)$, whose only automorphisms are the translations; see [[this non-example|5MN48ESK0F]].
Every [[dense linear order|2W4S2H4VYA]] without endpoints has the same property, because its theory has quantifier elimination, but the proof by automorphisms needs a model with many automorphisms, such as $\Q$ or $\R$.
For infinite domains the claim also holds, because a formula mentions only finitely many elements.

## Explanations

### L1 human

Take two lists of rational numbers in increasing order, of the same length, for example $0, 1, 3$ and $5, 6, 10$.
Match them in order: $0$ with $5$, $1$ with $6$, $3$ with $10$.
We can stretch and slide the number line, piece by piece, so that $0$ lands on $5$, $1$ on $6$ and $3$ on $10$, and the order is kept.
Such a stretch changes no statement about the order, so any statement about $0, 1, 3$ holds exactly when the same statement holds about $5, 6, 10$.

### L2 human

We compute $\sigma$ for $a = (0, 1, 3)$ and $b = (5, 6, 10)$.

1. For $x \le 0$: $\sigma(x) = x + 5$.
2. For $0 \le x \le 1$: $\sigma(x) = 5 + x$.
3. For $1 \le x \le 3$: $\sigma(x) = 6 + \frac{4}{2}(x - 1) = 2x + 4$.
4. For $x \ge 3$: $\sigma(x) = x + 7$.
5. Check: $\sigma(1) = 6$ from steps 2 and 3, and $\sigma(3) = 10$ from steps 3 and 4. The midpoint $2$ of $1$ and $3$ goes to $8$, the midpoint of $6$ and $10$.

The typical use is the back-and-forth proof that countable dense linear orders without endpoints are isomorphic, where each finite stage is such a map.
A trap is to think that the maps must be affine; any order-preserving finite map is partial elementary, and the affine pieces are only a tool for the proof.
