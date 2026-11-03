---
tag: 3F1K8BHAHB
kind: definition
name: Dennis–Stein symbol
msc: [19C20, 19C99]
defines: A575FYBCCY
uses: [0310REJJY8, 590VZSQ83X, W7T56A6YF8, 07C6ECNJET]
sources:
  - url: https://en.wikipedia.org/wiki/Steinberg_symbol
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] with identity, and let $St(R)$ be its [[Steinberg group|590VZSQ83X]], with generators $x_{ij}(r)$.
For a [[unit|07C6ECNJET]] $u$ of $R$, set $w_{12}(u) = x_{12}(u) \, x_{21}(-u^{-1}) \, x_{12}(u)$ and $h_{12}(u) = w_{12}(u) \, w_{12}(-1)$.
Let $a, b \in R$ be such that $u = 1 + ab$ is a unit.
The *Dennis–Stein symbol* of $a$ and $b$ is
$$\langle a, b \rangle = x_{21}(-b u^{-1}) \, x_{12}(a) \, x_{21}(b) \, x_{12}(-u^{-1} a) \, h_{12}(u)^{-1} \in St(R).$$

## Remarks

The element $\langle a, b \rangle$ lies in [[K2|W7T56A6YF8]] of $R$.
Check, with $2 \times 2$ blocks: the image of $h_{12}(u)$ is $\operatorname{diag}(u, u^{-1})$, since the image of $w_{12}(u)$ is $\begin{pmatrix} 0 & u \\ -u^{-1} & 0 \end{pmatrix}$.
Also $x_{12}(a) \, x_{21}(b) \mapsto \begin{pmatrix} u & a \\ b & 1 \end{pmatrix}$, and multiplying on the left by the image of $x_{21}(-bu^{-1})$ and on the right by the image of $x_{12}(-u^{-1}a)$ gives $\operatorname{diag}(u, u^{-1})$.
So the image of $\langle a, b \rangle$ is the identity matrix.

Example: in $R = k[\varepsilon]/(\varepsilon^2)$ over a field $k$, the symbol $\langle \varepsilon, b \rangle$ is defined for every $b \in R$, because $1 + \varepsilon b$ is a unit with inverse $1 - \varepsilon b$.

Non-example: in $R = \Z$, the pair $a = b = 1$ gives $1 + ab = 2$, which is not a unit of $\Z$, so $\langle 1, 1 \rangle$ is not defined.

Dennis–Stein symbols are used to describe $K_2$ of rings with many non-units, such as local rings and rings with nilpotent ideals.
