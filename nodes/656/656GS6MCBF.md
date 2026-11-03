---
tag: 656GS6MCBF
kind: definition
name: Linear system
msc: [93C05, 93A10]
defines: 21FN2KSTJZ
uses: [000AYPA9AJ, 0NRYHJPQG2, ZPDTVZQN5K]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_system
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $\mathcal{T}$ be $\R$ (continuous time) or $\Z$ (discrete time).
Let $\mathcal{U}$ and $\mathcal{Y}$ be [[vector spaces|000AYPA9AJ]] over $\mathbb{K}$ of functions on $\mathcal{T}$, the input signals and the output signals.
A *system* is a map $H \colon \mathcal{U} \to \mathcal{Y}$ that sends each input $u$ to its output $Hu$.
The system is *linear* if
$$H(a u_1 + b u_2) = a \, H u_1 + b \, H u_2$$
for all $u_1, u_2 \in \mathcal{U}$ and all $a, b \in \mathbb{K}$, that is, if $H$ is a [[linear map|0NRYHJPQG2]].

## Remarks

Example: the delay $(Hu)(t) = u(t - 1)$ on real signals over $\R$ is linear, since $(a u_1 + b u_2)(t - 1) = a u_1(t - 1) + b u_2(t - 1)$.
Non-example: $(Hu)(t) = u(t) + 1$ is not linear, since $H0$ is the constant $1$, while a linear map sends $0$ to $0$.
A [[control system|ZPDTVZQN5K]] in state-space form $x' = A(t) x + B(t) u$, $y = C(t) x + D(t) u$, with matrix functions $A, B, C, D$, is called a linear system.
With the initial state $x(t_0) = 0$, its input-output map is linear in the sense above.
With a nonzero initial state, the output is the sum of a fixed free response and a linear function of the input.
