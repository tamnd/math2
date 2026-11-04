---
tag: PGAEBXP9WZ
kind: proof
name: Proof of the reduction of a higher-order equation to a first-order system
msc: [34A99]
proves: 0TH9CPW3VS
uses: [04SW7WECS8, 0P97V20RW7]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinary_differential_equation
    locator: Reduction to a first-order system
---

## Proof

1. By the definition of a [[solution|04SW7WECS8]] of the [[equation|0P97V20RW7]], $y : I \to \R$ solves $y^{(n)} = f\left(x, y, \dots, y^{(n-1)}\right)$ on $I$ when three things hold. The function $y$ is $n$ times differentiable on $I$. For each $x \in I$, the point $\left(x, y(x), \dots, y^{(n-1)}(x)\right)$ lies in $U$. For each $x \in I$, $y^{(n)}(x) = f\left(x, y(x), \dots, y^{(n-1)}(x)\right)$.
2. In the same way, $z = (z_1, \dots, z_n) : I \to \R^n$ solves the system on $I$ when three things hold. The function $z$ is differentiable on $I$. For each $x \in I$, $(x, z(x)) \in U$, and the $n$ equations of the system hold at $x$.
3. Let $y$ solve the equation on $I$, and set $z_k = y^{(k-1)}$ for $k = 1, \dots, n$. Since $k - 1 \le n - 1$, each $z_k$ is differentiable on $I$, with $z_k' = y^{(k)}$.
4. For $k = 1, \dots, n - 1$, this gives $z_k' = y^{(k)} = z_{k+1}$.
5. For $k = n$, step 1 gives $z_n' = y^{(n)} = f\left(x, y, \dots, y^{(n-1)}\right) = f(x, z_1, \dots, z_n)$ on $I$.
6. Also $(x, z(x)) = \left(x, y(x), \dots, y^{(n-1)}(x)\right) \in U$ for each $x \in I$. By step 2, $z$ solves the system on $I$.
7. Conversely, let $z$ solve the system on $I$, and set $y = z_1$. We show by induction on $k$ that $y$ is $k - 1$ times differentiable with $y^{(k-1)} = z_k$, for $k = 1, \dots, n$.
8. For $k = 1$ this is the definition $y = z_1$.
9. Let $1 \le k < n$ and assume $y^{(k-1)} = z_k$. The function $z_k$ is differentiable with $z_k' = z_{k+1}$. So $y^{(k-1)}$ is differentiable and $y^{(k)} = z_{k+1}$. This completes the induction.
10. In particular $y^{(n-1)} = z_n$, and $z_n$ is differentiable. So $y$ is $n$ times differentiable on $I$, and $y^{(n)} = z_n'$.
11. By the last equation of the system, $y^{(n)} = z_n' = f(x, z_1, \dots, z_n) = f\left(x, y, \dots, y^{(n-1)}\right)$ on $I$.
12. By steps 7 to 9, $\left(x, y(x), \dots, y^{(n-1)}(x)\right) = (x, z(x)) \in U$ for each $x \in I$. So $y$ solves the equation on $I$, and $z_k = y^{(k-1)}$ for $k = 1, \dots, n$.

## Idea

The new unknowns $z_k$ are names for the derivatives $y^{(k-1)}$. The first $n - 1$ equations of the system say exactly that each name is the derivative of the previous one. The last equation is the original equation, written in the new names.
