---
tag: 0CC56MJ4FG
kind: definition
name: Harmonic conjugate
msc: [31A05]
defines: 050F2FMTKF
uses: [0DG0Z72CQD, 031BG625Y3]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_conjugate
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Harmonic_conjugate
    locator: Examples
---

## Definition

Let $U \subseteq \mathbb{C}$ be an open set, and identify $\mathbb{C}$ with $\mathbb{R}^2$ by $x + iy \leftrightarrow (x, y)$.
Let $u : U \to \mathbb{R}$ be a harmonic function: $u$ is twice continuously differentiable and $u_{xx} + u_{yy} = 0$ on $U$.
A harmonic conjugate of $u$ is a function $v : U \to \mathbb{R}$ such that the function $f = u + iv$ is [[holomorphic|0DG0Z72CQD]] on $U$.

## Remarks

For example, $v = 2xy$ is a harmonic conjugate of $u = x^2 - y^2$ on $\mathbb{C}$, because $u + iv = z^2$.
If $U$ is a [[domain|097KNJFJ7V]], two harmonic conjugates of $u$ differ by a real constant.
If $v$ is a harmonic conjugate of $u$, then $-u$ is a harmonic conjugate of $v$, because $v - iu = -i(u + iv)$ is holomorphic.
On a disc, each harmonic function has a harmonic conjugate. On $\mathbb{C} \setminus \{0\}$, the harmonic function $\log |z|$ has none.

## Explanations

### L1 human

The [[real part of a holomorphic function is harmonic|031BG625Y3]]. A harmonic conjugate goes the other way: it starts with a harmonic function $u$ and finds the missing imaginary part $v$.
For $u = x$, the conjugate is $v = y$, because $x + iy = z$ is holomorphic.
