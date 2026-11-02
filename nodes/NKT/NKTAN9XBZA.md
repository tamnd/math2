---
tag: NKTAN9XBZA
kind: statement
role: lemma
name: Douglas' lemma
msc: [47A05, 47A62]
uses: [HM2HHE3J51, 6HSJBJ8TTQ, 77020CY5ZW, 3JY5HNFRMF]
about: [HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Douglas%27_lemma
same_as:
  wikidata: Q5301141
  wikipedia: Douglas' lemma
---

## Statement

Let $H_1$, $H_2$ and $H$ be [[Hilbert spaces|HM2HHE3J51]], and let $A \colon H_1 \to H$ and $B \colon H_2 \to H$ be bounded linear operators.
The following are equivalent.

1. The range of $A$ is contained in the range of $B$.
2. There is $\lambda \ge 0$ with $AA^* \le \lambda^2 BB^*$, that is, $\norm{A^* x} \le \lambda \norm{B^* x}$ for all $x \in H$.
3. There is a bounded linear operator $C \colon H_1 \to H_2$ with $A = BC$.

Here $A^*$ and $B^*$ are the [[Hilbert space adjoints|6HSJBJ8TTQ]], and $\le$ is the order given by [[positive operators|77020CY5ZW]].
Moreover, if these hold, there is a unique $C$ with $A = BC$ whose range lies in the closure of the range of $B^*$.
It satisfies $\ker C = \ker A$ and $\norm{C}^2 = \inf \set{\mu \ge 0 : AA^* \le \mu BB^*}$.

## Remarks

Proof idea: (3) implies (1) at once, and (3) implies (2) because $AA^* = BCC^*B^* \le \norm{C}^2 BB^*$.
For (2) implies (3), the map $B^* x \mapsto A^* x$ is well defined and bounded by $\lambda$ on the range of $B^*$.
Extend it to the closure, set it to $0$ on the orthogonal complement, and let $C$ be the adjoint of the result.
For (1) implies (3), define $Cx$ as the unique $y \perp \ker B$ with $By = Ax$, and use the closed graph theorem to see that $C$ is bounded.

Example: on $\ell^2$ let $B$ be the diagonal operator with entries $1/n$ and $A$ the diagonal operator with entries $1/n^2$.
Then $A = BC$ with $C$ diagonal with entries $1/n$, and indeed $AA^* \le BB^*$ since $1/n^4 \le 1/n^2$.

## Explanations

### L1 human

The lemma relates three ways in which one operator can be smaller than another.
The range of $A$ fits inside the range of $B$ exactly when $A$ factors through $B$, and exactly when $AA^*$ is dominated by a multiple of $BB^*$.
It turns a question about ranges, which are often not closed, into an inequality between positive operators.

### L2 human

Douglas' lemma is a standard tool for factorization and for range inclusion questions.
For example, with $B = (AA^*)^{1/2}$, the [[square root|3JY5HNFRMF]] of $AA^*$, condition 2 holds in both directions, so $A$ and $(AA^*)^{1/2}$ have the same range.
It is used in dilation theory, in the theory of de Branges spaces, and in the study of operator equations $A = BX$.
