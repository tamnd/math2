---
tag: MB8EPS233V
kind: definition
name: Vincenty's formulae
msc: [86A30, 53A05]
defines: YY1941K7CB
uses: [KA7Z56ZFPQ, NE1PZM0HBN, 6QBV95NG6E]
sources:
  - url: https://en.wikipedia.org/wiki/Vincenty%27s_formulae
    locator: Inverse problem
---

## Definition

Let an ellipsoid have semi-major axis $a$, [[flattening|NE1PZM0HBN]] $f$ and semi-minor axis $b = (1 - f)a$.
Let two points have [[geodetic coordinates|6QBV95NG6E]] $(\varphi_1, L_1)$ and $(\varphi_2, L_2)$, and set $L = L_2 - L_1$.
Their reduced latitudes are $U_i = \arctan\big((1 - f)\tan\varphi_i\big)$.
*Vincenty's inverse method* starts from $\lambda = L$ and repeats the following steps until $\lambda$ stops changing:
$$\sin\sigma = \sqrt{(\cos U_2 \sin\lambda)^2 + (\cos U_1 \sin U_2 - \sin U_1 \cos U_2 \cos\lambda)^2},$$
$$\cos\sigma = \sin U_1 \sin U_2 + \cos U_1 \cos U_2 \cos\lambda, \quad \sigma = \operatorname{atan2}(\sin\sigma, \cos\sigma),$$
$$\sin\alpha = \frac{\cos U_1 \cos U_2 \sin\lambda}{\sin\sigma}, \quad \cos 2\sigma_m = \cos\sigma - \frac{2\sin U_1 \sin U_2}{\cos^2\alpha},$$
$$C = \frac{f}{16}\cos^2\alpha\,\big(4 + f(4 - 3\cos^2\alpha)\big),$$
$$\lambda = L + (1 - C) f \sin\alpha \Big(\sigma + C\sin\sigma\big(\cos 2\sigma_m + C\cos\sigma(-1 + 2\cos^2 2\sigma_m)\big)\Big).$$
With the final values, set $u^2 = \cos^2\alpha \,(a^2 - b^2)/b^2$ and
$$A = 1 + \frac{u^2}{16384}\Big(4096 + u^2\big(-768 + u^2(320 - 175u^2)\big)\Big), \quad B = \frac{u^2}{1024}\Big(256 + u^2\big(-128 + u^2(74 - 47u^2)\big)\Big),$$
$$\Delta\sigma = B\sin\sigma\Big(\cos 2\sigma_m + \frac{B}{4}\Big(\cos\sigma(-1 + 2\cos^2 2\sigma_m) - \frac{B}{6}\cos 2\sigma_m(-3 + 4\sin^2\sigma)(-3 + 4\cos^2 2\sigma_m)\Big)\Big).$$
The output distance is $s = bA(\sigma - \Delta\sigma)$.
The azimuth at the first point is $\alpha_1 = \operatorname{atan2}(\cos U_2 \sin\lambda, \cos U_1 \sin U_2 - \sin U_1 \cos U_2 \cos\lambda)$.
*Vincenty's direct method* solves the direct problem with the same series and an iteration on $\sigma$.

## Remarks

Example: for $f = 0$ one gets $C = 0$, so $\lambda = L$ after one step, and $u = 0$ gives $A = 1$, $B = 0$; then $s = a\sigma$ is the great-circle distance.
Non-example: for some nearly antipodal pairs of points, the iteration on $\lambda$ does not converge, so the method gives no answer.
The variable $\alpha$ is the azimuth of the geodesic where it crosses the equator, and $\sigma$ is the arc length on the auxiliary sphere.
If $\cos^2\alpha = 0$, both points lie on the equator and the term with $\cos 2\sigma_m$ is dropped.
