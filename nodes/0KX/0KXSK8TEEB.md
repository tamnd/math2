---
tag: 0KXSK8TEEB
kind: statement
role: theorem
name: Continuous partial derivatives imply differentiability
msc: [26B05]
uses: [09EGC6F8PT, 0135XZZQ8M]
sources:
  - url: https://en.wikipedia.org/wiki/Differentiable_function
    locator: Differentiability in higher dimensions
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Finite dimensions
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f \colon U \to \mathbb{R}^m$, and let $a \in U$.
Suppose that each [[partial derivative|09EGC6F8PT]] $\partial f_j / \partial x_i$ exists at each point of $U$, for $1 \le i \le n$ and $1 \le j \le m$, and that each of them is continuous at $a$.
Then $f$ is [[differentiable|0135XZZQ8M]] at $a$.

## Remarks

If the partial derivatives exist on $U$ and are continuous on all of $U$, then $f$ is differentiable on $U$, and $Df$ is continuous. So $f$ is of class $C^1$ on $U$.
The converse is false. The function $f(x) = \|x\|^2 \sin(1/\|x\|)$ for $x \ne 0$, with $f(0) = 0$, is differentiable on $\mathbb{R}^n$, but its partial derivatives are not continuous at $0$.
Without continuity, the existence of the partial derivatives is not enough, see [[this counterexample|0TNZC55X3J]].

## Explanations

### L1 human

The partial derivatives give a candidate for the derivative: the matrix of all $\partial f_j / \partial x_i$ at $a$.
Continuity of the partial derivatives near $a$ is what makes this candidate a good linear approximation in all directions, and not only along the axes.
In practice, this theorem is how you check differentiability: compute the partial derivatives and see that they are continuous.
