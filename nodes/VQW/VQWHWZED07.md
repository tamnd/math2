---
tag: VQWHWZED07
kind: proof
name: Proof of the correspondence between quadratic forms and symmetric bilinear forms
msc: ["15A63", "11E04"]
topics: [6TSCEW8QMK]
audience: ug1
proves: VN9AG8JKYT
methods: [0NTF6DMVAP]
uses: [0HZNE5QZDJ, 0744CN4MDA, 0P799D6AMN, 0P24YW565F]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
  - book: isbn:9780387728285
---

## Proof

We expand $B(u + v, u + v)$ by bilinearity, solve the result for $B(u, v)$, and then compare matrices.
Let $F$ be a field with $2 \ne 0$ in $F$, and let $V$ be a finite-dimensional vector space over $F$ with basis $(e_1, \dots, e_n)$.

1. Let $B$ be a [[symmetric bilinear form|0744CN4MDA]] on $V$ and let $Q_B(v) = B(v, v)$. For $a \in F$, bilinearity in each slot gives $Q_B(av) = B(av, av) = a^2 B(v, v) = a^2 Q_B(v)$.
2. For $u, v \in V$, bilinearity gives four terms, and symmetry joins the two middle ones:
$$B(u + v, u + v) = B(u, u) + B(u, v) + B(v, u) + B(v, v) = Q_B(u) + 2B(u, v) + Q_B(v).$$
3. So $Q_B(u + v) - Q_B(u) - Q_B(v) = 2B(u, v)$, which is bilinear. By steps 1 and 3 and [[the definition|0HZNE5QZDJ]], $Q_B$ is a quadratic form with polar form $2B$. This proves part 1.
4. Now let $Q$ be a quadratic form and $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$. The definition of a quadratic form says that $b_Q$ is [[bilinear|0P799D6AMN]], and $b_Q$ is symmetric because $u + v = v + u$.
5. Since $2 \ne 0$ in $F$, the element $\tfrac{1}{2}$ exists, so $B_Q = \tfrac{1}{2} b_Q$ is defined, and it is symmetric and bilinear. This is the first use of the hypothesis on the characteristic.
6. Taking $a = 2$ in the scaling rule gives $Q(2v) = 4Q(v)$, so
$$b_Q(v, v) = Q(2v) - Q(v) - Q(v) = 2Q(v).$$
7. Dividing by $2$ gives $B_Q(v, v) = Q(v)$, which proves part 2. In other words, $Q_{B_Q} = Q$ for every quadratic form $Q$.
8. Let $B$ be symmetric bilinear. Step 3 gives $b_{Q_B} = 2B$, so $B_{Q_B} = \tfrac{1}{2} \cdot 2B = B$.
9. Steps 7 and 8 say that the two maps are inverse to each other. So both are bijections, which proves part 3.
10. Let $A = (B_Q(e_i, e_j))$ be the [[matrix of B_Q|0P24YW565F]]; it is symmetric because $B_Q$ is symmetric. For $v = \sum_i x_i e_i$, bilinearity gives
$$Q(v) = B_Q(v, v) = \sum_{i, j} x_i x_j B_Q(e_i, e_j) = x^{\mathsf{T}} A x.$$
11. Let $A'$ be a symmetric matrix with $Q(\sum_i x_i e_i) = x^{\mathsf{T}} A' x$ for all $x$. Define $B'(\sum_i x_i e_i, \sum_j y_j e_j) = x^{\mathsf{T}} A' y$. Then $B'$ is bilinear, and it is symmetric because $x^{\mathsf{T}} A' y$ is a $1 \times 1$ matrix and equals its transpose $y^{\mathsf{T}} A'^{\mathsf{T}} x = y^{\mathsf{T}} A' x$.
12. By the choice of $A'$, $Q_{B'} = Q$. Step 8 applied to $B'$ gives $B' = B_{Q_{B'}} = B_Q$.
13. So $A'$ and $A$ are both the matrix of $B_Q$ in the basis $(e_i)$, and $A' = A$. This proves part 4.

## Idea

Going from $B$ to $Q$ means putting the same vector in both slots.
Going back uses the expansion $Q(u + v) = Q(u) + 2B(u, v) + Q(v)$, solved for $B(u, v)$.
Solving needs a division by $2$, and that is the only place where the characteristic matters.
Uniqueness of the matrix follows because a symmetric matrix defines a symmetric bilinear form, and that form is then forced to be $B_Q$.

## Variants

A second formula gives the same form: $B(u, v) = \tfrac{1}{4}\bigl(Q(u + v) - Q(u - v)\bigr)$.
It follows from step 2 applied to $u + v$ and to $u - v$, since the difference of the two expansions is $4B(u, v)$.
A proof in coordinates writes $Q = \sum_{i \le j} c_{ij} x_i x_j$ and reads off $a_{ii} = c_{ii}$ and $a_{ij} = a_{ji} = \tfrac{1}{2} c_{ij}$.
Uniqueness then follows by comparing the coefficients of $x_i^2$ and of $x_i x_j$ in $x^{\mathsf{T}} A x = \sum_i a_{ii} x_i^2 + \sum_{i < j} 2a_{ij} x_i x_j$.
