---
tag: ~2e95cfaa
kind: proof
name: Proof of the structure theorem for solution sets of linear systems
proves: ~a01a76ca
methods: [0NTF6DMVAP, MKHVRNW68H]
uses: [0PDVQEP0ZC, 00YC1D652K, 0PYW26VNT6, 0W4FSW1TVB, 0EWQEYRVA8, E7SAHXQEVC]
sources:
  - book: isbn:9780321982384
    locator: Section 1.5
---

## Proof

We use that $A(x + y) = Ax + Ay$ and $A(cx) = c(Ax)$; both follow entrywise from the definition of the [[matrix-vector product|0PDVQEP0ZC]].

1. Part 2: $A(c_1 x_1 + c_2 x_2) = c_1 Ax_1 + c_2 Ax_2$, by the two rules.
2. This equals $c_1 b_1 + c_2 b_2$, by the hypotheses $Ax_1 = b_1$ and $Ax_2 = b_2$.
3. Part 1: $A0 = 0$, so $0 \in N$.
4. If $x_1, x_2 \in N$ and $c_1, c_2 \in F$, then $A(c_1 x_1 + c_2 x_2) = 0$, by part 2 with $b_1 = b_2 = 0$.
5. So $N$ is closed under linear combinations, and it is a [[linear subspace|00YC1D652K]].
6. Part 3, first inclusion: let $v \in N$. Then $A(p + v) = Ap + Av = b + 0 = b$, so $p + v \in S$.
7. Part 3, second inclusion: let $x \in S$, and put $v = x - p$.
8. Then $Av = Ax - Ap = b - b = 0$, by part 2 with $c_1 = 1$, $c_2 = -1$, so $v \in N$.
9. So $x = p + v \in p + N$, and steps 6 and 8 give $S = p + N$.
10. Part 4: if $S$ is not empty, choose $p \in S$; then $S = p + N$ with $N$ a subspace, by parts 1 and 3.
11. A set of the form $p + N$ with $N$ a subspace is an [[affine subspace|0PYW26VNT6]] with direction $N$, by definition.
12. Part 5: let $T \colon F^n \to F^m$ be the linear map $x \mapsto Ax$; its kernel is $N$.
13. Its image is the column space of $A$, by [[linear systems as vector equations|E7SAHXQEVC]].
14. The [[rank-nullity theorem|0W4FSW1TVB]] gives $\dim N = n - \dim \operatorname{Col}(A)$.
15. By [[the definition of rank|0EWQEYRVA8]], $\dim \operatorname{Col}(A) = \operatorname{rank} A$, so $\dim N = n - \operatorname{rank} A$.
16. The dimension of $p + N$ is $\dim N$, by definition, which finishes part 5.

## Idea

Two solutions of the same system differ by a solution of the homogeneous system, because $A$ is linear.

## Variants

Part 5 also follows without the rank-nullity theorem: by [[the lemma on systems in RREF|~e45eea91]], the vectors $v_1, \dots, v_k$ of the [[parametric form|~dc297165]] form a basis of $N$, and $k = n - r$ with $r$ the number of pivots.
Then $r = \operatorname{rank} A$, because the pivot columns of $A$ form a basis of its column space.
