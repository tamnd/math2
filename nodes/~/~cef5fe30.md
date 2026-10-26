---
tag: ~cef5fe30
kind: counterexample
name: A continuous nowhere differentiable function
msc: [26A27]
uses: [~2034293f, ~323bbdf8, ~0f274b29]
sources:
  - url: https://en.wikipedia.org/wiki/Weierstrass_function_(nowhere-differentiable_function)
    locator: Construction
---

## Counterexample

Let $\varphi \colon \mathbb{R} \to \mathbb{R}$ be the zigzag function with $\varphi(x) = |x|$ for $-1 \le x \le 1$ and $\varphi(x + 2) = \varphi(x)$ for all $x$.
Define
$$f(x) = \sum_{n=0}^{\infty} \Big( \frac{3}{4} \Big)^n \varphi(4^n x).$$
The function $f$ is continuous on $\mathbb{R}$, but it is not [[differentiable|~0f274b29]] at any point.

## Remarks

Since $0 \le \varphi \le 1$, the [[M-test|~2034293f]] with $M_n = (3/4)^n$ and the [[continuity of uniform sums|~323bbdf8]] give continuity.
Fix $x$. For each $m$, choose $\delta_m = \pm \frac{1}{2} 4^{-m}$ so that no integer lies strictly between $4^m x$ and $4^m (x + \delta_m)$.
Then $\Big| \frac{f(x + \delta_m) - f(x)}{\delta_m} \Big| \ge \frac{3^m + 1}{2}$. This tends to infinity while $\delta_m \to 0$, so $f'(x)$ does not exist.
This function replaces the cosine in the [[Weierstrass function|~c4cfb464]] by a piecewise linear zigzag.

## Explanations

### L1 human

Each term adds smaller and steeper zigzags to the graph.
The sum is continuous, but its graph has a corner at every scale near every point.
