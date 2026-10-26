---
tag: ~da31dd1b
kind: statement
role: proposition
name: Derivative of a map into R^n by components
msc: [26B05]
uses: [~9740fd2d, ~e1757e04, ~e325b0fe]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_derivative
    locator: Finite dimensions
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, let $f = (f_1, \dots, f_m) \colon U \to \mathbb{R}^m$, let $a \in U$, and let $L \colon \mathbb{R}^n \to \mathbb{R}^m$ be linear with components $L_1, \dots, L_m$.
Then $f$ is [[differentiable|~9740fd2d]] at $a$ with $Df(a) = L$ if and only if, for each $j \in \{1, \dots, m\}$, the component $f_j$ is differentiable at $a$ with $Df_j(a) = L_j$.

## Remarks

So you can differentiate a vector-valued map one component at a time. The derivative of $f_j$ is row $j$ of the [[Jacobian matrix|~e325b0fe]] of $f$.
The proof compares norms: each $|v_j| \le \|v\|$, and $\|v\| \le \sqrt{m} \max_j |v_j|$, for $v \in \mathbb{R}^m$.
This is the case of [[a map into a product|~e1757e04]] with $m$ factors equal to $\mathbb{R}$.

## Explanations

### L1 human

The map $f(t) = (\cos t, \sin t)$ has the derivative $h \mapsto (-h \sin t, \, h \cos t)$ at $t$.
You get it by differentiating $\cos t$ and $\sin t$ separately.
