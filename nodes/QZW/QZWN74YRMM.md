---
tag: QZWN74YRMM
kind: statement
role: proposition
name: Formula for the inverse
msc: ["03E20"]
sources:
  - wikipedia: en:14907@r1368588964
    locator: Inverse function, section Examples > Formula for the inverse
    note: adopted
    mention: wikipedia://en/14907#8I5T
    sections: [Statement]
inventory: [ZADBHJ84M0]
---

## Statement

Many functions given by algebraic formulas possess a formula for their inverse. This is because the inverse $f^{-1}$ of an invertible function $f\colon\mathbb{R}\to\mathbb{R}$ has an explicit description as

$$f^{-1}(y)=(\text{the unique element }x\in \mathbb{R}\text{ such that }f(x)=y).$$

This allows one to easily determine inverses of many functions that are given by algebraic formulas. For example, if $f$ is the function

$$f(x) = (2x + 8)^3$$

then to determine $f^{-1}(y)$ for a real number $y$, one must find the unique real number $x$ such that $(2x + 8)^{3} = y$. This equation can be solved:

$$\begin{aligned} y & = (2x+8)^3 \\ \sqrt[3]{y} & = 2x + 8 \\ \sqrt[3]{y} - 8 & = 2x \\ \dfrac{\sqrt[3]{y} - 8}{2} & = x . \end{aligned}$$

Thus the inverse function $f^{\,-1}$ is given by the formula

$$f^{-1}(y) = \frac{\sqrt[3]{y} - 8} 2.$$

Sometimes, the inverse of a function cannot be expressed by a closed-form formula. For example, if $f$ is the function

$$f(x) = x - \sin x ,$$

then $f$ is a bijection, and therefore possesses an inverse function $f^{\,-1}$. The formula for this inverse has an expression as an infinite sum:

$$f^{-1}(y) = \sum_{n=1}^\infty \frac{y^{n/3}}{n!} \lim_{ \theta \to 0} \left( \frac{\mathrm{d}^{\,n-1}}{\mathrm{d} \theta^{\,n-1}} \left( \frac \theta { \sqrt[3]{ \theta - \sin( \theta )} } \right)^n \right).$$
