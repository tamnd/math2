---
tag: JCMJDY59CH
kind: counterexample
name: The coordinate forms of an infinite basis do not span the dual space
msc: ["15A03", "15A04"]
topics: [9K7FFF26QR]
audience: ug2
uses: [0M856Q1AMZ, 0GZB2SN0PH, 0VTQTPQGAV, 0CRMGPAH83, 0DTY8B9HMS, 0R8X9XA83A]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_space
    locator: Infinite-dimensional case
  - url: https://en.wikipedia.org/wiki/Dual_basis
    locator: Existence and uniqueness
---

## Counterexample

In finite dimension the coordinate forms of a basis are a basis of the dual space, and this example shows that the spanning half fails for an infinite basis.
Let $F$ be a field and let $V = F^{(\mathbb{N})}$ be the [[space of sequences|0GZB2SN0PH]] $x = (x_0, x_1, \dots)$ in $F$ with only finitely many nonzero terms.
Let $e_k$ be the sequence with $1$ at place $k$ and $0$ elsewhere, so that $(e_k)_{k \in \mathbb{N}}$ is a [[basis|0VTQTPQGAV]] of $V$.
Let $e_k^* \in V^*$ be the coordinate form $e_k^*(x) = x_k$, so that $e_k^*(e_j) = \delta_{kj}$.
We show that the family $(e_k^*)$ is [[linearly independent|0CRMGPAH83]] but does not span the [[dual space|0M856Q1AMZ]] $V^*$.

1. For independence, let $S \subseteq \mathbb{N}$ be finite with $\sum_{k \in S} a_k e_k^* = 0$, and evaluate at $e_j$ for $j \in S$ to get $a_j = 0$.
2. Define $s \colon V \to F$ by $s(x) = \sum_k x_k$, which is a finite sum for each $x$ because $x$ has finitely many nonzero terms.
3. The map $s$ is linear, since $s(x + y) = \sum_k (x_k + y_k) = s(x) + s(y)$ and $s(cx) = c\, s(x)$.
4. For every $m \in \mathbb{N}$ we have $s(e_m) = 1$.
5. Suppose that $s$ lies in the [[span|0DTY8B9HMS]] of the $e_k^*$, so that $s = \sum_{k \in S} a_k e_k^*$ for a finite set $S$ and scalars $a_k$.
6. The set $\mathbb{N}$ is infinite and $S$ is finite, so there is an $m \in \mathbb{N}$ with $m \notin S$.
7. At this $m$ the right side gives $\sum_{k \in S} a_k e_k^*(e_m) = 0$, because $e_k^*(e_m) = 0$ for every $k \ne m$.
8. The left side gives $s(e_m) = 1$ by step 4, which is a contradiction, so $s$ is not in the span.
9. Hence $(e_k^*)$ is independent but not a basis of $V^*$.

## Remarks

### What the example shows

The finite sum $f = \sum_i f(b_i)\, b_i^*$ in the theorem on the [[dimension of the dual space|00889YD15K]] is the step that fails.
For $s$ it would be the sum $\sum_k s(e_k)\, e_k^* = \sum_k e_k^*$, which has infinitely many nonzero terms.
That sum makes sense pointwise, since each $x$ meets only finitely many of its terms, and it equals $s$.
But a span allows only finite combinations, so $s$ is outside it.
This is why the hypothesis of finite dimension in that theorem cannot be dropped.

### What the span is

A finite combination $\sum_{k \in S} a_k e_k^*$ vanishes at $e_k$ for every $k$ outside $S$.
So the span of the coordinate forms is exactly the set of forms $f$ with $f(e_k) = 0$ for all but finitely many $k$.
The theorem that [[linear maps are determined by a basis|0R8X9XA83A]] identifies $V^*$ with $F^{\mathbb{N}}$, all sequences, by $f \mapsto (f(e_0), f(e_1), \dots)$.
Under this identification the span is the small subspace $F^{(\mathbb{N})}$, and the form $s$ is the sequence $(1, 1, 1, \dots)$.
The example on [[the dual of the finitely supported sequences|GZ627X1S7Y]] works this out.

### Every infinite basis

Nothing here depends on sequences.
If $V$ has an infinite basis $B$, then the form that is $1$ on every element of $B$ exists by the same theorem on bases.
A finite combination of coordinate forms vanishes at some $b \in B$, while this form takes the value $1$ there.
So the coordinate forms of an infinite basis never span the dual.

## Explanations

### L1 human

Each coordinate form looks at only one place of a sequence.
A finite combination of them looks at only finitely many places, say places $0$ to $9$.
The form "add up all the terms" also looks at place $10$, and at every later place.
On the sequence with a single $1$ at place $10$, the combination gives $0$ and the sum gives $1$.
So the sum is not such a combination.

### L2 human

The method is general: to show that a form is not in a span, find one test vector on which every element of the span vanishes but the form does not.
Here the span consists of finite combinations, so each one ignores all places outside a finite set $S$.
For example, take $S = \{0, 1, 2\}$ and the combination $g = 2e_0^* - e_1^* + 5e_2^*$.
Test on $e_3$:
$$g(e_3) = 2 \cdot 0 - 0 + 5 \cdot 0 = 0, \qquad s(e_3) = 1.$$
So $g \ne s$, and the same test with a place outside $S$ works for every finite combination.
This is the typical way to see that the dual of an infinite-dimensional space is larger than the span of a dual family.
Watch out: the pointwise infinite sum $\sum_k e_k^*$ equals $s$, but that is not a linear combination.
