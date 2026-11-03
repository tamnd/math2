---
tag: N9GEGKY2AP
kind: definition
name: Equatorial wave theory of Matsuno
msc: [76U60, 86A10, 86A05]
defines: CA3TV3V6TJ
uses: [NT73Y95RY5, F2D7MXW8V1, QERM9Y9QSJ, 52VS07H6GK, 6N1MQMA9TM]
sources:
  - url: https://en.wikipedia.org/wiki/Equatorial_wave
---

## Definition

Consider the [[shallow water equations|NT73Y95RY5]] linearised about rest on the equatorial [[beta plane|F2D7MXW8V1]].
The Coriolis parameter is $f = \beta y$ with $\beta > 0$, $y$ is the distance north of the equator and $c > 0$ is the gravity wave speed.
Let $L_{eq} = \sqrt{c / \beta}$ be the equatorial deformation radius.
The *equatorial waves* of Matsuno's theory are the solutions of the form $(u, v, \eta) = \operatorname{Re}[(\hat u(y), \hat v(y), \hat\eta(y)) e^{i(kx - \omega t)}]$ with $k$ real and $\omega \ne 0$ that are bounded as $\abs{y} \to \infty$.
They are classified as follows.

1. For each integer $n \ge 0$, there are solutions with $\hat v(y) \propto H_n(y / L_{eq}) \, e^{-y^2 / (2 L_{eq}^2)}$, where $H_n$ is the Hermite polynomial of degree $n$, whose frequency satisfies
$$\frac{\omega^2}{c^2} - k^2 - \frac{\beta k}{\omega} = (2n + 1) \frac{\beta}{c}.$$
2. For $n \ge 1$, this cubic in $\omega$ has two roots of large $\abs{\omega}$, the eastward and westward *inertia-gravity waves*. It has one root of small $\abs{\omega}$, the westward-propagating *equatorial Rossby wave*.
3. For $n = 0$, the admissible root with $\omega \ne -ck$ gives the *mixed Rossby–gravity wave*, also called the Yanai wave.
4. In addition, there is the equatorial [[Kelvin wave|QERM9Y9QSJ]], with $\hat v \equiv 0$, $\hat\eta \propto e^{-y^2 / (2 L_{eq}^2)}$ and $\omega = c k$, which is often labelled $n = -1$.

## Remarks

Elimination of $u$ and $\eta$ gives the equation $\hat v'' + \left( \omega^2 / c^2 - k^2 - \beta k / \omega - \beta^2 y^2 / c^2 \right) \hat v = 0$.
It has the form of the quantum harmonic oscillator, and its bounded solutions are the [[Hermite functions|52VS07H6GK]], which gives the dispersion relation in clause 1.
For $n = 0$ the cubic factors as $(\omega / c - k - \beta / \omega)(\omega / c + k) = 0$; the root $\omega = -ck$ is spurious, since it makes $\hat u$ and $\hat\eta$ unbounded.

Example: for the Rossby roots $\abs{\omega}$ is small, and neglecting $\omega^2 / c^2$ gives $\omega \approx -\beta k / (k^2 + (2n + 1) \beta / c)$.
In the long-wave limit $k \to 0$ this is $\omega \approx -c k / (2n + 1)$: for $n = 1$ a non-dispersive westward wave three times slower than the Kelvin wave.

Non-example: the solution $\hat v \propto e^{+y^2 / (2 L_{eq}^2)}$ of the same differential equation is unbounded and is not an equatorial wave.

On the Earth $\beta \approx 2.3 \times 10^{-11}$ m$^{-1}$ s$^{-1}$ at the equator, so a speed $c = 20$ m/s gives a trapping scale $L_{eq} \approx 930$ km.
