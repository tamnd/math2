---
tag: WW5X7DHHQ6
kind: example
name: A bilinear form that is not a polar form
msc: [15A63]
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

Let $B(u, v) = u_1 v_2$ on $\R^2$, for $u = (u_1, u_2)$ and $v = (v_1, v_2)$.

1. $B$ is [[bilinear|0P799D6AMN]]: it is linear in $u$ for fixed $v$, and linear in $v$ for fixed $u$.
2. $B$ is not [[symmetric|0744CN4MDA]]: for $e_1 = (1, 0)$ and $e_2 = (0, 1)$, $B(e_1, e_2) = 1$ and $B(e_2, e_1) = 0$.
3. Every [[polar form|0HYFWKKY3C]] $b_Q(u, v) = Q(u + v) - Q(u) - Q(v)$ is symmetric, since $u + v = v + u$.
4. So $B$ is not the polar form $b_Q$ of any quadratic form $Q$.
5. $B$ is also not $\frac12 b_Q$ for any $Q$, since $\frac12 b_Q$ is symmetric too.

## Remarks

The form $B$ still defines a quadratic form: $Q(v) = B(v, v) = v_1 v_2$.
The polar form of this $Q$ is $b_Q(u, v) = u_1 v_2 + u_2 v_1$, and $\frac12 b_Q$ is the symmetric part $\frac12 (B(u, v) + B(v, u))$ of $B$.
So passing from $B$ to $Q$ and back gives the symmetric part of $B$, not $B$.
In matrices: $B$ has matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, and $\frac12 b_Q$ has matrix $\begin{pmatrix} 0 & \frac12 \\ \frac12 & 0 \end{pmatrix}$.

## Explanations

### L1 human

A polar form does not change when we exchange its two inputs.
The form $u_1 v_2$ does change: with $u = (1, 0)$ and $v = (0, 1)$ it gives $1$ one way and $0$ the other way.
So it cannot be a polar form.

### L2 human

The typical use: to find the matrix of a quadratic form from a bilinear form, first take the symmetric part.
A trap: the matrix $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ gives the correct values $x^T A x = x_1 x_2$, but it is not the symmetric matrix of the form.
Eigenvalues of this matrix tell nothing about the form; the symmetric matrix has eigenvalues $\frac12$ and $-\frac12$.
