---
tag: CA0AYVS1XD
kind: proof
name: Proof of the minimum-norm solution theorem
msc: [15A06, 15A09]
topics: [8GQVME4SZZ]
audience: ug1
proves: QM2Y84VDX8
uses: [GQF2KG1R1N, 0SP7P0G7KQ, 0BVTDM872V, 0Q8HZTJC7G, 0EWQEYRVA8, 0TZAG60ZYT, 0F0RPPJ2TT, ACDFDABVQK, 0PSRCMCM5X, 0EX045E2BP]
methods: [0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Moore%E2%80%93Penrose_inverse
    locator: Minimum norm solution to a linear system
---

## Proof

We split each solution into a row space part and a null space part, and then we find the row space part by a formula.
Write $W = \operatorname{Col}(A^*) \subseteq \mathbb{K}^n$ and $N = \operatorname{Nul}(A)$.

1. By the [[orthogonality of the fundamental subspaces|GQF2KG1R1N]], $N = W^\perp$, so every vector of $W$ is orthogonal to every vector of $N$.
2. Fix one solution $x$ of $Ax = b$. By the [[orthogonal decomposition|0SP7P0G7KQ]] of $\mathbb{K}^n$ into $W \oplus W^\perp$, we can write $x = x_0 + z$ with $x_0 \in W$ and $z \in N$.
3. Then $A x_0 = A x - A z = b - 0 = b$, so $x_0$ is a solution that lies in $W$.
4. If $x_0'$ is a second solution in $W$, then $A(x_0 - x_0') = 0$, so $x_0 - x_0'$ lies in $W \cap N = W \cap W^\perp = \{0\}$.
5. Hence $x_0$ is the only solution in $W$, which proves part 2.
6. A vector $x$ is a solution if and only if $A(x - x_0) = 0$, that is, if and only if $x = x_0 + z$ with $z \in N$.
7. For such $x$, step 1 gives $x_0 \perp z$, so the [[Pythagorean theorem|0BVTDM872V]] gives $\norm{x}^2 = \norm{x_0}^2 + \norm{z}^2$, which proves part 3.
8. By step 7, $\norm{x} \ge \norm{x_0}$ for every solution, with equality only when $\norm{z} = 0$, that is, when $x = x_0$; this proves part 1.
9. For a solution $x = x_0 + z$ we have $x_0 \in W$ and $x - x_0 = z \in W^\perp$, so $x_0$ is the [[orthogonal projection|0Q8HZTJC7G]] of $x$ onto $W$ by its definition; this proves part 4.
10. Now let $\rank A = m$. Since [[row rank equals column rank|0TZAG60ZYT]], the [[column space|0F0RPPJ2TT]] has dimension $m$, so it is all of $\mathbb{K}^m$, and $Ax = b$ has a solution for every $b$.
11. Let $y \in \mathbb{K}^m$ with $A A^* y = 0$. Then
$$\norm{A^* y}^2 = (A^* y)^* (A^* y) = y^* (A A^* y) = 0,$$
so $A^* y = 0$.
12. The orthogonality of the fundamental subspaces also gives $\operatorname{Nul}(A^*) = \operatorname{Col}(A)^\perp = (\mathbb{K}^m)^\perp = \{0\}$, so $y = 0$.
13. So the square matrix $A A^*$ has null space $\{0\}$, and it is invertible by the [[invertible matrix theorem|ACDFDABVQK]].
14. Put $x_1 = A^* (A A^*)^{-1} b$. Then $A x_1 = (A A^*)(A A^*)^{-1} b = b$, so $x_1$ is a solution.
15. Also $x_1 = A^* y_1$ with $y_1 = (A A^*)^{-1} b$, so $x_1 \in W$, and step 5 gives $x_1 = x_0$; this proves part 5.
16. For part 6, put $B = A^* (A A^*)^{-1}$. The matrix $A A^*$ is self-adjoint, so its inverse is self-adjoint too:
$$\big( (A A^*)^{-1} \big)^* = \big( (A A^*)^* \big)^{-1} = (A A^*)^{-1}.$$
17. We check the four conditions of the [[Moore-Penrose inverse|0PSRCMCM5X]]. First, $A B = A A^* (A A^*)^{-1} = I_m$, so $A B A = A$ and $(A B)^* = I_m = A B$.
18. Next, $B A B = B (A B) = B I_m = B$.
19. Last, $B A = A^* (A A^*)^{-1} A$, and step 16 gives $(B A)^* = A^* \big( (A A^*)^{-1} \big)^* A = B A$.
20. So $B$ satisfies the four conditions, and the uniqueness of the Moore-Penrose inverse gives $B = A^+$; with step 15, $x_0 = A^+ b$, which proves part 6.

## Idea

The solution set is a copy of the null space moved away from the origin, and the null space is orthogonal to the row space $\operatorname{Col}(A^*)$.
So every solution splits into a row space part, which is the same for all solutions, and a null space part, which only adds length.
The shortest solution is the row space part alone.
To find it, we look for a solution of the form $x = A^* y$, since those are exactly the vectors of the row space, and then $Ax = b$ becomes the square system $A A^* y = b$.

## Variants

Over $\R$ one can use Lagrange multipliers: minimize $\norm{x}^2$ subject to $Ax = b$.
The condition $2x = A^{\mathsf{T}} \lambda$ says that $x$ lies in the row space.
Substituting into $Ax = b$ gives $A A^{\mathsf{T}} \lambda = 2b$, and this leads to the same formula $x = A^{\mathsf{T}} (A A^{\mathsf{T}})^{-1} b$.
This route finds the candidate quickly, but it needs a separate argument that the critical point is a minimum, and the Pythagorean identity of step 7 supplies that argument.
