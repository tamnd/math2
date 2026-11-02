---
tag: XJMGD9V64J
kind: definition
name: Curvelet
msc: [42C40, 42C15, 94A08]
defines: VEVPDJ8S7B
uses: [DPVM34ADZV, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Curvelet
---

## Definition

This is the second-generation curvelet system on $\R^2$.
Let $W \colon (0,\infty) \to [0,\infty)$ and $V \colon \R \to [0,\infty)$ be smooth windows with $W$ supported in $(1/2, 2)$ and $V$ supported in $[-1, 1]$, such that
$$\sum_{j \in \Z} W(2^j r)^2 = 1 \text{ for } r > 0, \qquad \sum_{l \in \Z} V(t - l)^2 = 1 \text{ for } t \in \R.$$
For an integer $j \ge 0$, let $\varphi_j$ be the function whose [[Fourier transform|DPVM34ADZV]] is, in polar coordinates $(r, \theta)$ of the frequency plane,
$$\hat\varphi_j(r, \theta) = 2^{-3j/4} \, W(2^{-j} r) \, V\left(\frac{2^{\floor{j/2}}\theta}{2\pi}\right).$$
Let $R_\theta$ be the rotation of $\R^2$ by the angle $\theta$.
For $l$ with $0 \le l < 2^{\floor{j/2}}$, put $\theta_l = 2\pi \cdot 2^{-\floor{j/2}} \, l$.
For $k = (k_1, k_2) \in \Z^2$, put $x_k^{(j,l)} = R_{\theta_l}^{-1}(k_1 2^{-j}, k_2 2^{-j/2})$.
The *curvelet* at scale $2^{-j}$, orientation $\theta_l$ and position $x_k^{(j,l)}$ is
$$\varphi_{j,l,k}(x) = \varphi_j\left(R_{\theta_l}\left(x - x_k^{(j,l)}\right)\right), \qquad x \in \R^2.$$
The curvelet coefficients of $f \in L^2(\R^2)$ are $c(j,l,k) = \ip{f}{\varphi_{j,l,k}}$.

## Remarks

Each $\hat\varphi_j$ lives on a polar wedge with radial size about $2^j$ and angular width about $2^{-j/2}$.
In space, $\varphi_j$ is then a needle of length about $2^{-j/2}$ and width about $2^{-j}$.
This is parabolic scaling: width $\approx$ length$^2$.
The number of orientations doubles at every second scale.
Together with a coarse-scale family at low frequencies, the curvelets form a tight frame of $L^2(\R^2)$ in the sense that $\sum \abs{c(j,l,k)}^2 = \norm{f}_2^2$.

Example: any pair of smooth windows with these supports and partition conditions, such as the Meyer-type windows used for the Meyer wavelet, gives a curvelet system.

Non-example: if the angular window is not narrowed with scale, that is, $V(2^{\floor{j/2}}\theta/(2\pi))$ is replaced by a fixed angular window, the elements keep the same aspect ratio at all scales.
They then behave like directional wavelets and lose the parabolic scaling, which is the defining feature of curvelets.

## Explanations

### L1 human

Curvelets are built in frequency space from wedges of a polar grid.
Finer scales use wedges farther out and narrower in angle, and the inverse Fourier transform turns each wedge into a thin oriented needle in the plane.
