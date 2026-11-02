---
tag: 83H3AMTXST
kind: definition
name: Poincaré–Lindstedt method
msc: ["34E10", 34C15]
defines: YHJHPRKQ6D
uses: [0NT64JV96A, FHNDX22WMK, Q26QN6GYZX]
sources:
  - url: https://en.wikipedia.org/wiki/Poincar%C3%A9%E2%80%93Lindstedt_method
---

## Definition

Let $\omega_0 > 0$, let $f$ be smooth, and consider the [[ordinary differential equation|0NT64JV96A]]
$$x'' + \omega_0^2 x = \varepsilon f(x, x'),$$
with a small parameter $\varepsilon$, for which one seeks [[periodic solutions|FHNDX22WMK]].
The *Poincaré–Lindstedt method* proceeds as follows.

1. Introduce the scaled time $\tau = \omega t$, where the unknown frequency is expanded as $\omega = \omega_0 + \varepsilon \omega_1 + \varepsilon^2 \omega_2 + \cdots$.
2. Seek $x$ as a $2\pi$-periodic function of $\tau$, expanded as $x = x_0(\tau) + \varepsilon x_1(\tau) + \varepsilon^2 x_2(\tau) + \cdots$.
3. Insert both expansions in the equation, written as $\omega^2 \frac{d^2 x}{d\tau^2} + \omega_0^2 x = \varepsilon f\bigl(x, \omega \frac{dx}{d\tau}\bigr)$, and collect powers of $\varepsilon$.
4. At each order $k \ge 1$, the equation has the form $\omega_0^2 (x_k'' + x_k) = g_k(\tau)$.
   Choose $\omega_k$, and the free constants of earlier orders, so that $g_k$ has no Fourier component in $\cos \tau$ and $\sin \tau$.

Step 4 removes *secular terms* such as $\tau \sin \tau$, so every $x_k$ is periodic.
The result is an [[asymptotic expansion|Q26QN6GYZX]] of the periodic solution and its frequency.

## Remarks

Example: the Duffing equation $x'' + x + \varepsilon x^3 = 0$, with $\omega_0 = 1$, $x(0) = a$, $x'(0) = 0$.
Order $0$ gives $x_0 = a \cos \tau$.
Order $1$ gives $x_1'' + x_1 = 2 \omega_1 a \cos \tau - a^3 \cos^3 \tau = \bigl(2 \omega_1 a - \tfrac{3}{4} a^3\bigr) \cos \tau - \tfrac{1}{4} a^3 \cos 3\tau$, using $\cos^3 \tau = \frac{3}{4} \cos \tau + \frac{1}{4} \cos 3 \tau$.
Removing the $\cos \tau$ term gives $\omega_1 = \frac{3}{8} a^2$, so $\omega = 1 + \frac{3}{8} \varepsilon a^2 + O(\varepsilon^2)$.

Non-example: the naive expansion $x = x_0(t) + \varepsilon x_1(t)$ in the original time, step 1 omitted, gives $x_1$ containing $-\frac{3}{8} a^3 t \sin t$.
This term grows without bound, so the expansion is not uniformly valid for $t$ of order $1/\varepsilon$.

## Explanations

### L1 human

The method expands both the motion and its frequency, and it fixes the frequency so that no term grows forever.
