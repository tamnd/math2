---
tag: Q7FMCDJRET
kind: proof
name: Proof of the Rouché–Capelli theorem
msc: [15A06]
proves: 0HV1SKWPMS
uses: [0JTRMBQ1SA, 0YCDZ7N8VD, 0EWQEYRVA8, 0F0RPPJ2TT, 0CCQV3884B, 0RXD6EZYBK, 0NRYHJPQG2, 0PQ2GGY1QV, 0EPTJA5QV4, 0HR573CHNM, 0FBXFBZBH8, 0W4FSW1TVB, 0QK7FPE6VE, 0WGAXEK99E, 0VTQTPQGAV, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_linear_equations
    locator: Relation to nonhomogeneous systems
---

## Proof

The proof uses these facts about rank and dimension.
The rank of a matrix is the dimension of its column space, by [[the definition of rank|0EWQEYRVA8]].
A subspace of a finite-dimensional space with the same dimension is the whole space, by [[the subspace theorem|0WGAXEK99E]].
The [[rank-nullity theorem|0W4FSW1TVB]] holds, and $\dim F^n = n$ by [[the dimension of the coordinate space|0QK7FPE6VE]].

1. Let $a_1, \dots, a_n \in F^m$ be the columns of $A$, and write $x = (x_1, \dots, x_n)^T \in F^n$.
2. By the definition of the [[matrix-vector product|0CCQV3884B]], entry $i$ of $Ax$ is $\sum_j a_{ij} x_j$.
3. So $Ax = x_1 a_1 + \cdots + x_n a_n$, by comparing entries.
4. Entry $i$ of the equation $Ax = b$ is equation $i$ of the [[system|0JTRMBQ1SA]].
5. So the solutions of the system are the vectors $x \in F^n$ with $Ax = b$.
6. By steps 3 and 5, the system has a solution if and only if $b$ is a linear combination of $a_1, \dots, a_n$.
7. That means $b \in \operatorname{Col}(A)$, the [[column space|0F0RPPJ2TT]] of $A$.
8. The columns of the [[augmented matrix|0YCDZ7N8VD]] $[A \mid b]$ are $a_1, \dots, a_n, b$.
9. So $\operatorname{Col}(A) \subseteq \operatorname{Col}([A \mid b])$, since a [[span|0HR573CHNM]] can only grow when vectors are added.
10. Suppose that a solution exists; then $b \in \operatorname{Col}(A)$, by step 7.
11. Then each combination of $a_1, \dots, a_n, b$ is a combination of $a_1, \dots, a_n$.
12. So $\operatorname{Col}([A \mid b]) = \operatorname{Col}(A)$, and the two [[ranks|0EWQEYRVA8]] are equal.
13. Conversely, suppose that $\rank A = \rank [A \mid b]$, and put $X = \operatorname{Col}([A \mid b])$.
14. The space $X$ is spanned by $n + 1$ vectors, so it is finite-dimensional.
15. By step 9, $\operatorname{Col}(A)$ is a [[linear subspace|0EPTJA5QV4]] of $X$, and its dimension is $\dim X$ by hypothesis.
16. So $\operatorname{Col}(A) = X$, by [[the subspace theorem|0WGAXEK99E]].
17. Since $b \in X$, we get $b \in \operatorname{Col}(A)$, and the system has a solution by step 7.
18. This proves the first claim.
19. Define $T \colon F^n \to F^m$ by $T(x) = Ax$.
20. By [[distributivity|0RXD6EZYBK]], $A(x + y) = Ax + Ay$.
21. Entry by entry, $A(cx) = c(Ax)$ for $c \in F$, because $F$ is commutative.
22. So $T$ is a [[linear map|0NRYHJPQG2]].
23. By step 3, the image of $T$ is the set of all combinations of the columns, which is $\operatorname{Col}(A)$.
24. So $\dim \im T = \rank A$.
25. The kernel of $T$ is the [[null space|0PQ2GGY1QV]] $N = \set{x \in F^n : Ax = 0}$, a linear subspace of $F^n$.
26. By the [[rank-nullity theorem|0W4FSW1TVB]] and [[the dimension of the coordinate space|0QK7FPE6VE]], $\dim N = n - \rank A$.
27. Now suppose that a solution $p \in F^n$ exists, so $Ap = b$.
28. For $x \in F^n$, linearity gives $Ax - b = Ax - Ap = A(x - p)$.
29. So $x$ is a solution if and only if $x - p \in N$, that is, $x \in p + N$.
30. So the solution set is $p + N = \set{p + w : w \in N}$.
31. This set is an [[affine subspace|0FBXFBZBH8]] of $F^n$ with direction $N$.
32. Its [[dimension|05G2G0P224]] is $\dim N = n - \rank A$, by step 26.
33. For the last claim, assume that a solution $p$ exists.
34. By step 30, the solution is unique if and only if $N = \set{0}$.
35. If $N = \set{0}$, the empty family is a [[basis|0VTQTPQGAV]] of $N$, so $\dim N = 0$.
36. If $\dim N = 0$, then $N$ is the span of the empty set, which is $\set{0}$.
37. So the solution is unique if and only if $\dim N = 0$.
38. By step 26, this holds if and only if $\rank A = n$.

## Idea

The vector $Ax$ is a combination of the columns of $A$ with coefficients $x_1, \dots, x_n$.
So the system is solvable exactly when $b$ lies in the column space, and then adding $b$ as a column does not raise the rank.
Two solutions differ by a solution of $Ax = 0$, so the solution set is a translate of the null space.
The dimension of the null space comes from the rank-nullity theorem.

## Variants

A proof by row reduction, without the rank-nullity theorem, is [[the proof of the Rouché-Capelli theorem by row reduction|~403d5028]].
It counts pivots in the reduced row echelon form instead of dimensions.
