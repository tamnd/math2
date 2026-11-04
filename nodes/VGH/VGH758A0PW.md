---
tag: VGH758A0PW
kind: proof
name: Proof of the chain rule for Jacobian matrices
msc: [26B10]
proves: 03GGQEAG9S
uses: [0EAAS2EHDR, 0YF0VXKXGB, 0A6PMR20N4, 05AXG3QRKR, 0YYMY95FWS, 05Q1B7MH0M]
sources:
  - url: https://www.jirka.org/ra/realanal2.pdf
    locator: Proposition 8.3.9
---

## Proof

We show that a Jacobian matrix is the matrix of the derivative, and then we use that matrices multiply like compositions.

1. Let $p, q \ge 1$, let $V \subseteq \mathbb{R}^p$ be open, let $\sigma \colon V \to \mathbb{R}^q$, and let $c \in V$. Suppose that $\sigma$ is differentiable at $c$. Let $e_1, \dots, e_p$ be the standard basis of $\mathbb{R}^p$.
2. Since [[the derivative gives the directional derivatives|0A6PMR20N4]], $\big(\sigma(c + t e_j) - \sigma(c)\big) / t \to D\sigma(c)(e_j)$ as $t \to 0$, for each $j$.
3. For each $v \in \mathbb{R}^q$, the entry $v_i$ satisfies $|v_i| \le \|v\|$. So the $i$-th entries in step 2 converge as well: $\big(\sigma_i(c + t e_j) - \sigma_i(c)\big) / t \to \big(D\sigma(c)(e_j)\big)_i$.
4. By the definition of the [[partial derivative|05AXG3QRKR]], step 3 says that $\partial \sigma_i / \partial x_j (c)$ exists and equals $\big(D\sigma(c)(e_j)\big)_i$.
5. So the [[Jacobian matrix|0YF0VXKXGB]] $J_\sigma(c)$ is defined. Its column $j$ is the vector $D\sigma(c)(e_j)$. Thus $J_\sigma(c)$ is the [[matrix|0YYMY95FWS]] of $D\sigma(c)$ in the standard bases.
6. Now let $U$, $W$, $g$, $f$ and $a$ be as in the statement. By the [[chain rule in several variables|0EAAS2EHDR]], $f \circ g$ is differentiable at $a$, and $D(f \circ g)(a) = Df(g(a)) \circ Dg(a)$.
7. By step 5 applied to $f \circ g$ at $a$, to $f$ at $g(a)$ and to $g$ at $a$, the three Jacobian matrices are defined. They are the matrices of $D(f \circ g)(a)$, $Df(g(a))$ and $Dg(a)$ in the standard bases.
8. Since the [[matrix of a composition is the product of the matrices|05Q1B7MH0M]], step 6 gives $J_{f \circ g}(a) = J_f(g(a)) \, J_g(a)$.
9. Here $J_f(g(a))$ is a $k \times m$ matrix and $J_g(a)$ is an $m \times n$ matrix. Indeed $f$ maps $W \subseteq \mathbb{R}^m$ into $\mathbb{R}^k$, and $g$ maps $U \subseteq \mathbb{R}^n$ into $\mathbb{R}^m$.

## Idea

The Jacobian matrix of a differentiable map is the matrix of its derivative, because the partial derivatives are the values of the derivative on the basis vectors. The chain rule says that the derivative of a composition is a composition of linear maps. Matrices of linear maps multiply in the same order as the maps compose.
