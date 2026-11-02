---
tag: S9KDHJF5YV
kind: definition
name: Herglotz–Riesz kernel
msc: [31A10, 30C40]
defines: 1FSFX18D68
uses: [TCYSWCTYYM, 0NAHXR1FRH, 61WT6CE08W, 9ZBAX4ZPX0]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_harmonic_function
---

## Definition

Let $c \in \C$ and $R > 0$, and let $D = \set{z \in \C : \abs{z - c} < R}$.
For $\zeta$ on the circle $\abs{\zeta - c} = R$ and $z \in \C$ with $z \ne \zeta$, the *Herglotz–Riesz kernel* of $D$ is
$$H(\zeta, z) = \frac{(\zeta - c) + (z - c)}{(\zeta - c) - (z - c)} = \frac{\zeta + z - 2c}{\zeta - z}.$$

## Remarks

For fixed $\zeta$, the function $z \mapsto H(\zeta, z)$ is [[holomorphic|0NAHXR1FRH]] on $D$.
Its real part is the [[Poisson kernel|TCYSWCTYYM]]: with $a = \zeta - c$ and $b = z - c$,
$$\operatorname{Re} H(\zeta, z) = \operatorname{Re} \frac{(a + b)(\bar a - \bar b)}{\abs{a - b}^2} = \frac{R^2 - \abs{z - c}^2}{\abs{\zeta - z}^2},$$
because $b \bar a - a \bar b$ is purely imaginary.
Example: for the unit disc ($c = 0$, $R = 1$), $\zeta = 1$ and $z = 1/2$, one gets $H = 3$, and the Poisson kernel $(1 - 1/4)/(1/4)$ is also $3$.
Non-example: the Cauchy kernel $\zeta/(\zeta - z)$ is also holomorphic in $z$, but at $\zeta = 1$, $z = 1/2$ it equals $2$, so its real part is not the Poisson kernel.
For $c = 0$ the two kernels are related by $H(\zeta, z) = 2\zeta/(\zeta - z) - 1$.
If $u$ is harmonic on a neighbourhood of $\overline{D}$, the [[Schwarz integral formula|61WT6CE08W]] reads
$$u(z) + i v(z) = \frac{1}{2\pi} \int_0^{2\pi} H(c + R e^{i\theta}, z) \, u(c + R e^{i\theta}) \, d\theta,$$
where $v$ is the harmonic conjugate of $u$ on $D$ with $v(c) = 0$.
The same kernel appears in the [[Herglotz representation theorem|9ZBAX4ZPX0]].
Other names in use are Herglotz kernel and Schwarz kernel.
