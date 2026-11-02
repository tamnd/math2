---
tag: 8BBSFVN1CS
kind: definition
name: Cauchy-type integral
msc: ["30E20", "45E05"]
defines: MGBKF52TQE
uses: [0HATW2VWAZ, 06ZGPYTWK8, 0NAHXR1FRH, 0DG10TVYPN]
sources:
  - url: https://en.wikipedia.org/wiki/Sokhotski%E2%80%93Plemelj_theorem
---

## Definition

Let $\Gamma$ be an oriented [[rectifiable curve|0HATW2VWAZ]] in $\C$, closed or not, and let $\varphi \colon \Gamma \to \C$ be continuous.
The *Cauchy-type integral* of $\varphi$ over $\Gamma$ is the function
$$\Phi(z) = \frac{1}{2\pi i} \int_\Gamma \frac{\varphi(\tau)}{\tau - z} \, d\tau, \quad z \in \C \setminus \Gamma,$$
where the integral is a [[contour integral|06ZGPYTWK8]].
The function $\varphi$ is its *density*.

## Remarks

The function $\Phi$ is [[holomorphic|0NAHXR1FRH]] on $\C \setminus \Gamma$, and $\Phi(z) \to 0$ as $z \to \infty$.
Example: let $\Gamma$ be the unit circle, oriented counterclockwise, and $\varphi(\tau) = \tau^{-1}$.
For $\abs{z} < 1$, the integrand $\frac{1}{\tau(\tau - z)} = \frac{1}{z} \left( \frac{1}{\tau - z} - \frac{1}{\tau} \right)$ gives $\Phi(z) = \frac{1}{z}(1 - 1) = 0$; for $\abs{z} > 1$ it gives $\Phi(z) = \frac{1}{z}(0 - 1) = -\frac{1}{z}$.
So the boundary values from inside and outside are $0$ and $-\tau^{-1}$, and their difference is $\varphi(\tau)$.
Non-example: for $z \in \Gamma$ the formula is not a convergent integral in general.
The reason is that $\frac{1}{\tau - z}$ is not integrable along $\Gamma$ near $\tau = z$.
On $\Gamma$ one uses instead the [[Cauchy principal value|0SYR10HD4R]], as in [[singular integral equations|E30EA6ETZ4]].
Let $\Gamma$ be a closed curve bounding a domain $D$, and let $\varphi$ be the boundary value of a function $F$ holomorphic on $D$ and continuous on its closure.
Then $\Phi = F$ on $D$ and $\Phi = 0$ outside $\overline{D}$, by [[Cauchy's integral formula|0DG10TVYPN]] and Cauchy's theorem.
The boundary values of $\Phi$ for Hölder continuous $\varphi$ are given by the [[Sokhotski–Plemelj formulae|DRT1E6WY6K]].
