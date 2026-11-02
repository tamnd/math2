---
tag: 1PFE27B2MG
kind: statement
role: theorem
name: Birkhoff–Grothendieck theorem
msc: [14F06, 14H60]
uses: [ZT9A6JK8QF, P4DZM975BV, V93Y0XYPZD]
about: [P4DZM975BV]
sources:
  - url: https://en.wikipedia.org/wiki/Birkhoff–Grothendieck_theorem
same_as:
  wikidata: Q4916483
  wikipedia: Birkhoff–Grothendieck theorem
---

## Statement

Let $k$ be a field and let $\mathcal{E}$ be a [[vector bundle|P4DZM975BV]] (a locally free sheaf) of rank $r \ge 1$ on the [[projective line|ZT9A6JK8QF]] $\mathbb{P}^1_k$.
Then there are integers $a_1 \ge a_2 \ge \dots \ge a_r$ such that
$$\mathcal{E} \cong \mathcal{O}(a_1) \oplus \mathcal{O}(a_2) \oplus \dots \oplus \mathcal{O}(a_r),$$
where $\mathcal{O}(a)$ is the $a$-th power of [[Serre's twisting sheaf|V93Y0XYPZD]].
The integers $a_1, \dots, a_r$ are uniquely determined by $\mathcal{E}$.

## Remarks

The idea of the proof: induct on $r$.
Choose the largest $a$ with $H^0(\mathcal{E}(-a)) \ne 0$; a section of $\mathcal{E}(-a)$ gives a subbundle $\mathcal{O}(a) \subseteq \mathcal{E}$ whose quotient is a vector bundle of rank $r - 1$, which splits by induction as $\bigoplus \mathcal{O}(b_i)$.
The maximality of $a$ forces $b_i \le a$, so the extension class lies in $\bigoplus H^1(\mathbb{P}^1, \mathcal{O}(a - b_i)) = 0$ and the sequence splits.
Uniqueness follows from the dimensions $h^0(\mathcal{E}(n))$ for all $n$.

Example: the tangent bundle of $\mathbb{P}^1_k$ is $\mathcal{O}(2)$.
The bundles $\mathcal{O}(1) \oplus \mathcal{O}(1)$ and $\mathcal{O} \oplus \mathcal{O}(2)$ both have rank $2$ and degree $2$, but they are not isomorphic.
Indeed, after twisting by $\mathcal{O}(-2)$, the first has no nonzero global sections and the second has a one-dimensional space of them.

The statement fails on other curves and in higher dimension.
On an elliptic curve there are indecomposable vector bundles of rank $2$, and the tangent bundle of $\mathbb{P}^2$ is not a direct sum of line bundles.

## Explanations

### L1 human

On the projective line, every vector bundle breaks into a sum of line bundles, and line bundles there are classified by one integer, the degree.
So a vector bundle on $\mathbb{P}^1$ is described by a finite list of integers.
This makes $\mathbb{P}^1$ the simplest possible base for vector bundles.

### L2 human

The integers $a_i$ are called the splitting type of $\mathcal{E}$.
The theorem is used to study vector bundles on $\mathbb{P}^n$ by restricting them to lines, where they split, and seeing how the splitting type varies.
In the analytic setting it says that every holomorphic vector bundle on the Riemann sphere is a sum of line bundles.
This is equivalent to a factorization theorem for matrices of functions on a circle.
