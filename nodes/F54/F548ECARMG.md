---
tag: F548ECARMG
kind: definition
name: Transformation optics
msc: [78A25, 78A48]
defines: HBCRG5V2BD
uses: [9BWWD4QK8Y, 0KZZ70ZHXP, 047NDTEPCV, F768YN0P2V, 5MJQ5J5H8Z]
sources:
  - url: https://en.wikipedia.org/wiki/Transformation_optics
---

## Definition

Let $\Omega$ and $\Omega'$ be open subsets of $\R^3$, and let $F \colon \Omega \to \Omega'$ be an orientation-preserving smooth [[diffeomorphism|0KZZ70ZHXP]].
Let $A(x) = DF(x)$ be its [[Jacobian matrix|047NDTEPCV]].
Let a linear medium on $\Omega$ have [[permittivity|F768YN0P2V]] $\varepsilon(x)$ and [[permeability|5MJQ5J5H8Z]] $\mu(x)$, given by symmetric positive definite $3 \times 3$ matrices.
The *transformed medium* on $\Omega'$ has, at $y = F(x)$,
$$\varepsilon'(y) = \frac{A(x)\, \varepsilon(x)\, A(x)^T}{\det A(x)}, \qquad \mu'(y) = \frac{A(x)\, \mu(x)\, A(x)^T}{\det A(x)}.$$
*Transformation optics* is the method of designing a medium as the transformed medium of a known one under a chosen map $F$.
It rests on this fact, at a fixed frequency.
Let $E, H$ be fields on $\Omega$, and define fields on $\Omega'$ by
$$E'(y) = A(x)^{-T} E(x), \qquad H'(y) = A(x)^{-T} H(x).$$
Then $E, H$ solve the source-free [[Maxwell equations|9BWWD4QK8Y]] in the medium $(\varepsilon, \mu)$ if and only if $E', H'$ solve them in the medium $(\varepsilon', \mu')$.

## Remarks

Example: let $\Omega = \Omega' = \R^3$, let the medium be vacuum, $\varepsilon = \varepsilon_0 I$ and $\mu = \mu_0 I$, and let $F(x) = 2x$.
Then $A = 2I$ and $\det A = 8$, so $\varepsilon' = \frac{4 \varepsilon_0}{8} I = \frac{\varepsilon_0}{2} I$ and $\mu' = \frac{\mu_0}{2} I$.
The new medium has refractive index $\sqrt{\varepsilon' \mu' / (\varepsilon_0 \mu_0)} = 1/2$: lengths are doubled and the index is halved, so optical path lengths do not change.

Non-example: the folding map $F(x_1, x_2, x_3) = (\abs{x_1}, x_2, x_3)$ is not injective and not smooth on the plane $x_1 = 0$.
So it is not a diffeomorphism, and the rule does not apply to it as stated.
Applied locally on the half-space $x_1 < 0$, where $\det A = -1$, the same formula gives negative parameters; this is how complementary media are described.

The transformed medium is in general anisotropic.
If $\mu$ is a constant multiple of $\varepsilon$, then $\mu'$ is the same multiple of $\varepsilon'$, so the impedance is preserved.
In the language of differential geometry, the rule says that $\varepsilon$ and $\mu$ transform as tensor densities.

## Explanations

### L1 human

To bend light in a chosen way, first draw how you want space to be deformed.
The formula then tells you which material, at each point, makes light move as if space were deformed.
The price is that the material is usually anisotropic and varies from point to point.
