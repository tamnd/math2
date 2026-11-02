---
tag: SV6A17MEYZ
kind: definition
name: Lelong class
msc: [32U35, 32U15]
defines: X4ZHQG9995
uses: [FF2P7ER3QT]
sources:
  - url: https://en.wikipedia.org/wiki/Plurisubharmonic_function
---

## Definition

Let $n \ge 1$ and let $\abs{z}$ be the Euclidean norm on $\C^n$.
The *Lelong class* $\mathcal{L} = \mathcal{L}(\C^n)$ is the set of [[plurisubharmonic functions|FF2P7ER3QT]] $u$ on $\C^n$ for which there is a constant $C_u \in \R$ with
$$u(z) \le \log(1 + \abs{z}) + C_u \quad \text{for all } z \in \C^n .$$
The subclass $\mathcal{L}^+$ consists of the $u \in \mathcal{L}$ for which there is also a constant $c_u \in \R$ with $u(z) \ge \log(1 + \abs{z}) + c_u$ for all $z \in \C^n$.

## Remarks

Example: let $p$ be a polynomial on $\C^n$ of degree $d \ge 1$ and $u = \frac{1}{d} \log\abs{p}$.
Then $u$ is plurisubharmonic, and $\abs{p(z)} \le M (1 + \abs{z})^d$ for some $M > 0$, so $u(z) \le \log(1 + \abs{z}) + \frac{1}{d} \log M$; hence $u \in \mathcal{L}$.
It is not in $\mathcal{L}^+$ when $p$ has a zero, since $u = -\infty$ there.
The function $\log(1 + \abs{z}^2)/2$ is in $\mathcal{L}^+$.
Non-example: $u(z) = \abs{z_1}$ is plurisubharmonic, but $\abs{z_1} - \log(1 + \abs{z})$ is unbounded above, so $u \notin \mathcal{L}$.
For $n = 1$, the logarithmic potentials $\int \log\abs{z - w} \, d\mu(w)$ for compactly supported probability measures $\mu$ are in $\mathcal{L}$.
Some authors write $\log^+\abs{z} = \max(\log\abs{z}, 0)$ in place of $\log(1 + \abs{z})$; the class is the same, since the two functions differ by a bounded amount.
