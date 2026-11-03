---
tag: 16CVEM8NHD
kind: definition
name: Near and far field
msc: [78A40, 78A50]
defines: TVH1J6B1G9
uses: [AC6R5A3M1C, 9BWWD4QK8Y]
sources:
  - url: https://en.wikipedia.org/wiki/Near_and_far_field
---

## Definition

Let time-harmonic sources of angular frequency $\omega$ be contained in a ball of diameter $D$ centred at the origin.
Let the medium be homogeneous and lossless, with wavenumber $k = 2\pi/\lambda$ and wave impedance $\eta$.
Let $(\mathbf{E}, \mathbf{H})$ be the radiating solution of [[Maxwell's equations|9BWWD4QK8Y]] outside the ball.
Then there is a vector field $\mathbf{F}$ on the unit sphere, the *far-field pattern*, with $\hat{\mathbf{r}} \cdot \mathbf{F}(\hat{\mathbf{r}}) = 0$, such that
$$\mathbf{E}(r\hat{\mathbf{r}}) = \frac{e^{ikr}}{r}\left( \mathbf{F}(\hat{\mathbf{r}}) + O(1/r) \right), \qquad \mathbf{H} = \frac{1}{\eta}\, \hat{\mathbf{r}} \times \mathbf{E} + O(1/r^2), \qquad r \to \infty.$$
The *far field*, or Fraunhofer region, is the region where the leading term is an accurate approximation.
By the usual engineering convention it is $r > 2D^2/\lambda$ together with $r \gg D$ and $r \gg \lambda$.
The *near field* is the region close to the source where the $O(1/r)$ correction is not negligible.
Its inner part $r \lesssim \lambda/(2\pi)$ is the *reactive near field*, dominated by the terms of order $1/r^2$ and $1/r^3$.

## Remarks

The thresholds $2D^2/\lambda$ and $\lambda/(2\pi)$ are conventions, not sharp boundaries; the region between them is often called the radiating near field or Fresnel region.
The bound $2D^2/\lambda$ is the distance at which the path lengths from points of the source to a far point differ from their parallel-ray approximation by at most $\lambda/16$.
Example: for the [[Hertzian dipole|K0NV8SE4QV]], $H_\varphi$ has a term in $1/r$ and a term in $1/r^2$, and their ratio is $kr$.
At $kr = 10$ the near-field term is a tenth of the far-field one.
Non-example: at $kr = 0.1$ the $1/r^2$ term is ten times larger, so the point lies in the reactive near field and the far-field formula is wrong there.
In the far field the time-averaged Poynting vector is radial with size $\abs{\mathbf{F}}^2/(2\eta r^2)$, which is the [[electromagnetic radiation|AC6R5A3M1C]] carried to infinity.
