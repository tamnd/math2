---
tag: S5ET1HG2ZX
kind: statement
role: theorem
name: Erdős-Kaplansky theorem
aliases: [erdos-kaplansky-theorem]
msc: ["15A03", "15A04", "03E10"]
topics: [9K7FFF26QR]
audience: ug2
about: [07JBSZE0V4]
uses: [0M856Q1AMZ, 05G2G0P224, 00MS9VMQ9Z, 0QKPNZKNEA, 0WTEMGYV2C]
sources:
  - url: https://en.wikipedia.org/wiki/Erd%C5%91s%E2%80%93Kaplansky_theorem
    locator: Statement
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Infinite-dimensional case
same_as:
  wikipedia: Erdős–Kaplansky theorem
---

## Statement

The dual of an infinite-dimensional space is always strictly bigger than the space, and the theorem gives its dimension exactly.
Let $F$ be a field and let $V$ be an infinite-dimensional vector space over $F$.
Let $B$ be a basis of $V$, which exists by the theorem that [[every vector space has a basis|00MS9VMQ9Z]], so that $\dim V = \abs{B}$.
Then the [[dual space|0M856Q1AMZ]] $V^*$ has [[dimension|05G2G0P224]]
$$\dim V^* = \abs{F^B} = \abs{F}^{\dim V},$$
where $\abs{\cdot}$ is the [[cardinal number|0QKPNZKNEA]] of a set.
In particular, $\dim V^* > \dim V$, so $V^*$ is not isomorphic to $V$.

More generally, for every infinite set $I$, the space $F^I$ of all functions $I \to F$ satisfies $\dim F^I = \abs{F^I}$.

## Remarks

### A first computation

Take $F = \mathbb{Q}$ and $V = \mathbb{Q}^{(\mathbb{N})}$, the finitely supported rational sequences, with the countable basis $e_0, e_1, \dots$.
Then $\dim V = \aleph_0$, and a form on $V$ is any choice of values on the basis, so $V^* \cong \mathbb{Q}^{\mathbb{N}}$, all rational sequences.
The theorem gives
$$\dim V^* = \abs{\mathbb{Q}}^{\aleph_0} = \aleph_0^{\aleph_0} = 2^{\aleph_0},$$
the cardinal of the continuum.
So $V$ has a countable basis, but every basis of its dual is uncountable.
The same happens over the field $\mathbb{F}_2$ with two elements: the dual of a space of dimension $\aleph_0$ has dimension $2^{\aleph_0}$.
So a finite field does not save the isomorphism $V \cong V^*$.

### Why each hypothesis is needed

The space must be infinite-dimensional.
If $\dim V = n$ is finite, then $\dim V^* = n$ by the theorem on the [[dimension of the dual space|00889YD15K]].
For an infinite field $F$ the formula would instead give $\abs{F}^n = \abs{F}$, which is infinite, so it is false in finite dimension.
For infinite $I$ the general formula says the same: $\dim F^I = \abs{F^I}$ holds only for infinite $I$, while $\dim F^I = \abs{I}$ for finite $I$.

The [[proof|RE5HJ2154G]] uses the axiom of choice, both for the bases of $V$ and $V^*$ and for the rules of cardinal arithmetic.

### What it gives you

The theorem settles the question of whether $V \cong V^*$: it holds exactly when $V$ is finite-dimensional.
It also explains why the evaluation map $V \to V^{**}$ cannot be onto in infinite dimension.
Applying the theorem twice gives
$$\dim V^{**} > \dim V^* > \dim V,$$
so no linear map $V \to V^{**}$ is surjective.
This is a second proof of one half of the theorem on the [[double dual|0ZJM9D7NPS]].

### Watch out

The strict inequality is not a difference of one or two.
Already for $\dim V = \aleph_0$, the dual has dimension at least $2^{\aleph_0}$, and this cardinal is uncountable by [[Cantor's theorem|0WTEMGYV2C]].
Also, the theorem is about the algebraic dual, the space of all linear forms.
In analysis one often keeps only the continuous forms, and then the answer changes: for a real Hilbert space $H$, the continuous dual is isomorphic to $H$ by the Riesz representation theorem.

### Try it

First, find $\dim V^*$ when $V = \mathbb{R}^{(\mathbb{N})}$ over $\mathbb{R}$.
The theorem gives $\abs{\mathbb{R}}^{\aleph_0} = (2^{\aleph_0})^{\aleph_0} = 2^{\aleph_0 \cdot \aleph_0} = 2^{\aleph_0}$.

Second, find $\dim_{\mathbb{R}} \mathbb{R}^{\mathbb{R}}$, the space of all functions $\mathbb{R} \to \mathbb{R}$.
The general formula gives $\abs{\mathbb{R}^{\mathbb{R}}} = (2^{\aleph_0})^{2^{\aleph_0}} = 2^{2^{\aleph_0}}$, since $\aleph_0 \cdot 2^{\aleph_0} = 2^{\aleph_0}$.

## History

The theorem is named after Paul Erdős and Irving Kaplansky.

## Explanations

### L1 human

Some spaces need infinitely many basis vectors.
For such a space, the space of its linear forms is always bigger, even in the sense of infinite sizes.
For example, the sequences of rational numbers that end in zeros have a basis you can list as first, second, third, and so on.
Their linear forms correspond to all sequences of rational numbers, and those need a basis that cannot be listed in this way.
So in infinite dimension a space and its dual never match.

### L2 human

The proof compares the size of a space as a set with its dimension.
First, a form on $V$ is any choice of values on the basis $B$, so $V^*$ is in bijection with $F^B$ and has $\abs{F}^{\abs{B}}$ elements.
Second, an infinite-dimensional space $W$ is not much bigger than its basis: it has exactly $\max(\abs{F}, \dim W)$ elements.
Third, $\dim F^B \ge \abs{F}$, because the geometric sequences $(1, a, a^2, \dots)$ for $a \in F$ are independent by the Vandermonde determinant.
The second and third facts give $\abs{F^B} = \max(\abs{F}, \dim F^B) = \dim F^B$.
Finally, Cantor's theorem gives $\abs{F}^{\abs{B}} \ge 2^{\abs{B}} > \abs{B}$.
The typical use is to show that the duality theory of finite-dimensional spaces cannot hold unchanged in infinite dimension.

### L3 human

The theorem is one reason why functional analysis replaces the algebraic dual by the [[continuous dual|4A82S5FVRT]].
For a Hilbert space $H$, the continuous dual is identified with $H$ by the Riesz representation theorem, but the algebraic dual of an infinite-dimensional $H$ is much larger.
The formula $\dim F^I = \abs{F^I}$ also computes the dimension of many function spaces, such as $\dim_{\mathbb{R}} \mathbb{R}^{\mathbb{R}} = 2^{2^{\aleph_0}}$.
In the language of the [[dual space|07JBSZE0V4]], the theorem says that the finitely supported functions $F^{(B)} \cong V$ form a very small subspace of $F^B \cong V^*$.
