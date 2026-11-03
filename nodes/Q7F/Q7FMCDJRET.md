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

1. Let $a_1, \dots, a_n \in F^m$ be the columns of $A$, and write $x = (x_1, \dots, x_n)^T \in F^n$.
2. By the definition of the [[matrix–vector product|0CCQV3884B]], entry $i$ of $Ax$ is $\sum_j a_{ij} x_j$. So $Ax = x_1 a_1 + \cdots + x_n a_n$.
3. Entry $i$ of the equation $Ax = b$ is equation $i$ of the [[system|0JTRMBQ1SA]]. So the solutions of the system are the vectors $x \in F^n$ with $Ax = b$.
4. By steps 2 and 3, the system has a solution if and only if $b$ is a linear combination of $a_1, \dots, a_n$. This means $b \in \operatorname{Col}(A)$, the [[column space|0F0RPPJ2TT]] of $A$.
5. The columns of the [[augmented matrix|0YCDZ7N8VD]] $[A \mid b]$ are $a_1, \dots, a_n, b$. So $\operatorname{Col}(A) \subseteq \operatorname{Col}([A \mid b])$, since a [[span|0HR573CHNM]] can only grow when vectors are added.
6. Suppose a solution exists. By step 4, $b \in \operatorname{Col}(A)$. Then each combination of $a_1, \dots, a_n, b$ is a combination of $a_1, \dots, a_n$. So $\operatorname{Col}([A \mid b]) = \operatorname{Col}(A)$, and the two [[ranks|0EWQEYRVA8]] are equal.
7. Conversely, suppose $\rank A = \rank [A \mid b]$. The space $X = \operatorname{Col}([A \mid b])$ is spanned by $n + 1$ vectors, so it is finite-dimensional.
8. By step 5, $\operatorname{Col}(A)$ is a [[linear subspace|0EPTJA5QV4]] of $X$, and its dimension equals $\dim X$ by hypothesis. By [[a subspace of full dimension is the whole space|0WGAXEK99E]], $\operatorname{Col}(A) = X$.
9. Since $b \in X$, we get $b \in \operatorname{Col}(A)$, and the system has a solution by step 4. This proves the first claim.
10. Define $T \colon F^n \to F^m$ by $T(x) = Ax$. By [[distributivity|0RXD6EZYBK]], $A(x + y) = Ax + Ay$. Entry by entry, $A(cx) = c(Ax)$ for $c \in F$, because $F$ is commutative. So $T$ is a [[linear map|0NRYHJPQG2]].
11. By step 2, the image of $T$ is the set of all combinations of the columns, which is $\operatorname{Col}(A)$. So $\dim \im T = \rank A$.
12. The kernel of $T$ is the [[null space|0PQ2GGY1QV]] $N = \set{x \in F^n : Ax = 0}$. It is a linear subspace of $F^n$, since $A0 = 0$ and $T$ is linear.
13. By the [[rank–nullity theorem|0W4FSW1TVB]] and the [[dimension of the coordinate space|0QK7FPE6VE]], $\dim N = n - \rank A$.
14. Now suppose a solution $p \in F^n$ exists, so $Ap = b$. For $x \in F^n$, linearity gives $Ax - b = Ax - Ap = A(x - p)$.
15. So $x$ is a solution if and only if $x - p \in N$, that is, $x \in p + N$. The solution set is $p + N = \set{p + w : w \in N}$.
16. By step 15, the solution set is an [[affine subspace|0FBXFBZBH8]] of $F^n$ with direction $N$. Its [[dimension|05G2G0P224]] is $\dim N = n - \rank A$, by step 13.
17. For the last claim, assume a solution $p$ exists. By step 15, the solution is unique if and only if $N = \set{0}$.
18. If $N = \set{0}$, the empty family is a [[basis|0VTQTPQGAV]] of $N$, so $\dim N = 0$. If $\dim N = 0$, then $N$ has an empty basis, so $N$ is the span of the empty set, which is $\set{0}$.
19. So the solution is unique if and only if $\dim N = 0$. By step 13, this holds if and only if $\rank A = n$.

## Idea

The vector $Ax$ is a combination of the columns of $A$ with coefficients $x_1, \dots, x_n$. So the system is solvable exactly when $b$ lies in the column space, and then adding $b$ as a column does not raise the rank. Two solutions differ by a solution of $Ax = 0$, so the solution set is a translate of the null space, whose dimension comes from rank–nullity.
