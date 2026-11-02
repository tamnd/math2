---
tag: QF764XKBA3
kind: statement
role: theorem
name: Blakers–Massey theorem
msc: [55Q05, 55P40]
uses: [5W95QFHXPR, ZHHMDZWA7F, 1A943BWBQT]
about: [ZHHMDZWA7F]
sources:
  - url: https://en.wikipedia.org/wiki/Blakers%E2%80%93Massey_theorem
same_as:
  wikidata: Q4924632
  wikipedia: Blakers–Massey theorem
---

## Statement

Let $X$ be a [[CW complex|5W95QFHXPR]] that is the union of two subcomplexes $A$ and $B$ whose intersection $C = A \cap B$ is nonempty and connected.
Let $m, n \ge 0$, and assume that the pair $(A, C)$ is $m$-connected and the pair $(B, C)$ is $n$-connected.
Then, for a base point in $C$, the map $\pi_i(A, C) \to \pi_i(X, B)$ of [[relative homotopy groups|ZHHMDZWA7F]] induced by inclusion has the following properties:

1. it is an isomorphism for $i < m + n$;
2. it is surjective for $i = m + n$.

## Remarks

Here a pair $(Y, Z)$ is $k$-connected if every path component of $Y$ meets $Z$ and $\pi_i(Y, Z, z) = 0$ for $1 \le i \le k$ and all $z \in Z$, as for [[n-connected spaces|1A943BWBQT]].
The theorem is also called the homotopy excision theorem.
For homology, excision gives $H_i(A, C) \cong H_i(X, B)$ in all degrees; for homotopy groups excision holds only in the range above.
The proof reduces to the case where $A$ and $B$ are obtained from $C$ by attaching cells.
It then works cell by cell with a general position argument in the cubes $I^i$.
Applied to the two cones $A$ and $B$ that form the suspension of an $(n-1)$-connected complex, it gives the [[Freudenthal suspension theorem|7DM2KSS2DB]].

## Explanations

### L1 human

In homology, gluing two pieces together behaves predictably: what happens near the seam can be cut out.
For homotopy groups this fails in general, and new homotopy classes can appear after gluing.
The theorem says that the failure only starts in high dimensions.
The more connected the pieces are, the higher it starts.

### L2 human

The theorem is the reason homotopy theory becomes homology-like in the stable range.
It implies Freudenthal suspension, and it compares a cofibre sequence with a fibre sequence in a range of degrees.
A version for cubical diagrams of spaces, due to Goodwillie, is a basic tool in the calculus of functors.
