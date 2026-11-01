---
tag: R7E5A4W6FJ
kind: statement
role: theorem
name: Ruzsa triangle inequality
msc: [11P70, 11B13]
uses: [XNBN31HQWB, 082GHNPJ53]
about: [XNBN31HQWB]
sources:
  - url: https://en.wikipedia.org/wiki/Ruzsa_triangle_inequality
same_as:
  wikidata: Q85798239
  wikipedia: Ruzsa triangle inequality
---

## Statement

Let $G$ be an [[abelian group|082GHNPJ53]], and let $A$, $B$ and $C$ be finite subsets of $G$.
Then the difference sets satisfy
$$\abs{A} \, \abs{B - C} \le \abs{A - B} \, \abs{A - C}.$$

## Remarks

The proof is an injection from $A \times (B - C)$ into $(A - B) \times (A - C)$.
For each $d \in B - C$, fix one pair $(b_d, c_d)$ with $d = b_d - c_d$.
Send $(a, d)$ to $(a - b_d, \ a - c_d)$.
The difference of the two coordinates is $d$, which recovers $b_d$ and $c_d$, and then $a$.
The name comes from the distance $d(A, B) = \log \big( \abs{A - B} / \sqrt{\abs{A}\abs{B}} \big)$ on nonempty finite sets.
The inequality is exactly $d(B, C) \le d(B, A) + d(A, C)$.
This $d$ is not a metric, since $d(A, A) > 0$ unless $A$ is a coset of a finite subgroup.
For example, with $A = B = C = \set{0, 1}$ in $\Z$, the inequality reads $2 \cdot 3 \le 3 \cdot 3$.

## Explanations

### L1 human

The size of a difference set measures how well two sets fit together under subtraction.
The inequality says that if $A$ fits well with $B$ and with $C$, then $B$ and $C$ fit well with each other.
It behaves like the triangle inequality for distances.

### L2 human

The Ruzsa triangle inequality is one of the first tools of [[additive combinatorics|3NM362A2JG]].
Together with the [[Plünnecke–Ruzsa inequality|EBEVWSRD2E]], it lets one pass between bounds on $A + A$, $A - A$ and longer sums.
The same injection proves a version in nonabelian groups, with products and inverses in place of sums and differences.
