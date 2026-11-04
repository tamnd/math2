---
tag: X4M1JAXJYY
kind: proof
name: Proof of the superposition principle
msc: [34A30]
proves: 0F2VBPXNP9
uses: [0EQZSAB9EC, 0PB7K8M7FG, 0M0TKFRX2A]
sources:
  - url: https://en.wikipedia.org/wiki/Superposition_principle
    locator: lead section
---

## Proof

1. Let $u = c_1 y_1 + c_2 y_2$. As solutions of the [[homogeneous linear equation|0EQZSAB9EC]], $y_1$ and $y_2$ are $n$ times differentiable on $I$, with $L y_1 = 0$ and $L y_2 = 0$.
2. We show by induction on $k$ that, for $0 \le k \le n$, $u$ is $k$ times differentiable on $I$ and $u^{(k)} = c_1 y_1^{(k)} + c_2 y_2^{(k)}$.
3. For $k = 0$ this is the definition of $u$.
4. Let $k < n$ and assume the claim for $k$. The functions $y_1^{(k)}$ and $y_2^{(k)}$ are differentiable, since $k < n$.
5. By [[linearity of differentiation|0M0TKFRX2A]], $u^{(k)} = c_1 y_1^{(k)} + c_2 y_2^{(k)}$ is differentiable with derivative $c_1 y_1^{(k+1)} + c_2 y_2^{(k+1)}$. This proves the claim for $k + 1$.
6. Write $a_n = 1$. By step 2, at each $x \in I$, $L u = \sum_{k=0}^{n} a_k \left(c_1 y_1^{(k)} + c_2 y_2^{(k)}\right) = c_1 L y_1 + c_2 L y_2$.
7. By step 1, this is $c_1 \cdot 0 + c_2 \cdot 0 = 0$. So $u$ is $n$ times differentiable and solves the [[linear equation|0PB7K8M7FG]] $L y = 0$ on $I$.

## Idea

Differentiation is linear, and $L$ is built from derivatives by multiplying with functions and adding. So $L$ is linear, and it maps a combination of solutions to the same combination of zeros.
