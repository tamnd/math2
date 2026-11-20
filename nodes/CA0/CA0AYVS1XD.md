---
tag: CA0AYVS1XD
kind: proof
name: Proof of the minimum-norm solution theorem
msc: [15A06, 15A09]
topics: [8GQVME4SZZ]
audience: ug1
proves: QM2Y84VDX8
uses: [GQF2KG1R1N, 0BVTDM872V, 0Q8HZTJC7G, 0EWQEYRVA8, 0TZAG60ZYT, 0F0RPPJ2TT, ACDFDABVQK, 0PSRCMCM5X, 0EX045E2BP]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
    locator: Minimum norm solution to a linear system
---

## Proof

Write $W = \operatorname{Col}(A^*) \subseteq \mathbb{K}^n$ and $N = \operatorname{Nul}(A)$.

1. By part 2 of the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]], $N = W^\perp$. So every $w \in W$ is orthogonal to every $z \in N$.
2. By part 5 of the same theorem, $Ax = b$ has exactly one solution $x_0 \in W$, and the set of all solutions is $x_0 + N$.
3. Let $x = x_0 + z$ be any solution, with $z \in N$. By step 1, $x_0 \perp z$, so the [[Pythagorean theorem|0BVTDM872V]] gives $\norm{x}^2 = \norm{x_0}^2 + \norm{z}^2$. This proves part 2.
4. By step 3, $\norm{x} \ge \norm{x_0}$, with equality if and only if $\norm{z} = 0$, that is, $x = x_0$. So $x_0$ is the unique solution of smallest norm. This proves part 1.
5. Part 3: for a solution $x = x_0 + z$, we have $x_0 \in W$ and $x - x_0 = z \in N = W^\perp$. By the definition of the [[orthogonal projection|0Q8HZTJC7G]], $x_0$ is the projection of $x$ onto $W$.
6. Part 4: let $\rank A = m$. By [[row rank equals column rank|0TZAG60ZYT]], $\dim \operatorname{Col}(A) = m$, so the [[column space|0F0RPPJ2TT]] is all of $\mathbb{K}^m$. Hence $Ax = b$ has a solution for every $b$.
7. Let $y \in \mathbb{K}^m$ with $A A^* y = 0$. Then $\norm{A^* y}^2 = (A^* y)^* (A^* y) = y^* (A A^* y) = 0$, so $A^* y = 0$.
8. By part 1 of the fundamental subspaces theorem, $\operatorname{Nul}(A^*) = \operatorname{Col}(A)^\perp = (\mathbb{K}^m)^\perp = \set{0}$. So $y = 0$ by step 7.
9. The square matrix $A A^*$ has null space $\set{0}$, so it is invertible by the [[invertible matrix theorem|ACDFDABVQK]].
10. Put $x_1 = A^* (A A^*)^{-1} b$. Then $A x_1 = (A A^*) (A A^*)^{-1} b = b$, so $x_1$ is a solution.
11. $x_1 = A^* y_1$ with $y_1 = (A A^*)^{-1} b$, so $x_1 \in W$. By the uniqueness in step 2, $x_1 = x_0$. This proves part 4.
12. Part 5: let $B = A^* (A A^*)^{-1}$. The matrix $A A^*$ is self-adjoint, so its inverse is self-adjoint too, because $((A A^*)^{-1})^* = ((A A^*)^*)^{-1} = (A A^*)^{-1}$.
13. We check the four conditions of the [[Moore-Penrose inverse|0PSRCMCM5X]]. First, $A B = A A^* (A A^*)^{-1} = I_m$. So $A B A = A$, and $(A B)^* = I_m = A B$.
14. $B A B = B (A B) = B I_m = B$.
15. $B A = A^* (A A^*)^{-1} A$, and $(B A)^* = A^* ((A A^*)^{-1})^* A = A^* (A A^*)^{-1} A = B A$ by step 12.
16. So $B$ satisfies the four conditions, and by the uniqueness in the definition, $B = A^+$. With step 11, $x_0 = A^+ b$. This proves part 5.

## Idea

The solution set is a translate of the null space, and the null space is orthogonal to $\operatorname{Col}(A^*)$.
So every solution splits into a part in $\operatorname{Col}(A^*)$, which is the same for all solutions, and a part in the null space, which only adds length.
The formula comes from looking for the solution in the form $x = A^* y$, which forces $A A^* y = b$.

## Variants

By Lagrange multipliers: minimize $\norm{x}^2$ subject to $Ax = b$ over $\R$.
The condition $2x = A^{\mathsf{T}} \lambda$ says that $x$ lies in the row space, and then $A A^{\mathsf{T}} \lambda = 2b$ gives the same formula.
