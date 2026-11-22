---
tag: WW5X7DHHQ6
kind: example
name: A bilinear form that is not a polar form
msc: ["15A63"]
topics: [6TSCEW8QMK]
audience: ug1
not_instance_of:
  - target: 0HYFWKKY3C
    note: the form u1 v2 is not symmetric, and every polar form is symmetric
uses: [0HYFWKKY3C, 0P799D6AMN, 0744CN4MDA]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_form
    locator: Definitions
---

## Example

Let $B(u, v) = u_1 v_2$ on $\mathbb{R}^2$, for $u = (u_1, u_2)$ and $v = (v_1, v_2)$.
We show that $B$ is bilinear but is the polar form of no quadratic form.

1. $B$ is [[bilinear|0P799D6AMN]]: for fixed $v$ it is $v_2$ times the coordinate $u_1$, which is linear in $u$, and in the same way it is linear in $v$ for fixed $u$.
2. $B$ is not [[symmetric|0744CN4MDA]]: for $e_1 = (1, 0)$ and $e_2 = (0, 1)$ we get $B(e_1, e_2) = 1 \cdot 1 = 1$ and $B(e_2, e_1) = 0 \cdot 0 = 0$.
3. Every [[polar form|0HYFWKKY3C]] $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$ is symmetric, because $u + v = v + u$.
4. By steps 2 and 3, $B$ is not $b_Q$ for any quadratic form $Q$, and it is not $\tfrac{1}{2} b_Q$ either, since $\tfrac{1}{2} b_Q$ is symmetric too.

## Remarks

The form $B$ still produces a quadratic form, $Q(v) = B(v, v) = v_1 v_2$.
The polar form of this $Q$ is $b_Q(u, v) = u_1 v_2 + u_2 v_1$, and its half is the symmetric part $\tfrac{1}{2}\bigl(B(u, v) + B(v, u)\bigr)$ of $B$.
So the round trip from $B$ to $Q$ and back returns the symmetric part of $B$, not $B$ itself.
In matrices, $B$ has the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and $\tfrac{1}{2} b_Q$ has the matrix $\begin{pmatrix} 0 & 1/2 \\ 1/2 & 0 \end{pmatrix}$.

If you change $B$ to the symmetric form $u_1 v_2 + u_2 v_1$, it becomes a polar form: it is $b_Q$ for $Q = v_1 v_2$.
Every bilinear form that is not symmetric fails in the same way as $B$.

## Explanations

### L1 human

A polar form gives the same answer when you exchange its two inputs.
The form $u_1 v_2$ does not: with $u = (1, 0)$ and $v = (0, 1)$ it gives $1$ one way and $0$ the other way.
So it cannot be a polar form.

### L2 human

Here is the typical use: to get the matrix of a quadratic form from a bilinear form, first take the symmetric part.
The matrix $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ gives the correct values $x^{\mathsf{T}} A x = x_1 x_2$, but it is not the symmetric matrix of the form.
Watch out: the eigenvalues of $A$ say nothing about the form.
Both eigenvalues of $A$ are $0$, while the symmetric matrix has eigenvalues $\tfrac{1}{2}$ and $-\tfrac{1}{2}$, and these show that $x_1 x_2$ takes both signs.
