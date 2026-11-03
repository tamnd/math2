---
tag: GJXVXRV77R
kind: definition
name: Sliding mode control
msc: [93B12, 93C10, 93B52]
defines: FRYAQABP4P
uses: [ZPDTVZQN5K, PJWK0PKN6Q, 9ZSMF6NYKM, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Sliding_mode_control
---

## Definition

Let $f, g \colon \R^n \to \R^n$ be smooth and consider the control-affine [[control system|ZPDTVZQN5K]] $x' = f(x) + g(x) u$ with scalar input $u$.
Let $s \colon \R^n \to \R$ be [[smooth|0V33BNKZ9S]] with $L_g s(x) = \nabla s(x) \cdot g(x) \ne 0$ for all $x$; the set $S = \set{x : s(x) = 0}$ is the *sliding surface*.
Let $u = k(x)$ be a feedback that is continuous on $\set{s > 0}$ and on $\set{s < 0}$ and may be discontinuous on $S$.
It is a *sliding mode controller* for $S$ if there is $\eta > 0$ with
$$s(x)\, \nabla s(x) \cdot \big(f(x) + g(x) k(x)\big) \le -\eta\, \abs{s(x)} \quad \text{for all } x \notin S.$$
This inequality is the *reaching condition*.
The motion of the closed loop on $S$, in the sense of Filippov, is the *sliding mode*.
On $S$ it is governed by the *equivalent control*
$$u_{\mathrm{eq}}(x) = -\frac{L_f s(x)}{L_g s(x)}, \qquad L_f s = \nabla s \cdot f.$$

## Remarks

Along a solution off $S$, the reaching condition gives $\frac{d}{dt} \abs{s} \le -\eta$, so the state reaches $S$ within time $\abs{s(x(0))}/\eta$ and cannot leave it afterwards.
On $S$, the vector field $f + g u_{\mathrm{eq}}$ is tangent to $S$, and this is the Filippov solution of the discontinuous system, given by a [[differential inclusion|9ZSMF6NYKM]].
Example: for $x_1' = x_2$, $x_2' = u$, choose $s(x) = x_2 + c\, x_1$ with $c > 0$ and $k(x) = -c\, x_2 - \eta \sgn(s(x))$.
Then $\frac{d}{dt} s = c\, x_2 + u = -\eta \sgn(s)$, so $s\, \frac{d}{dt} s = -\eta \abs{s}$ and the reaching condition holds.
On $S$ one has $x_2 = -c\, x_1$, so $x_1' = -c\, x_1$ and the state slides to the origin.
Non-example: the continuous feedback $k(x) = -c\, x_2 - s(x)$ gives $\frac{d}{dt} s = -s$; then $s\, \frac{d}{dt} s = -s^2$, and no $\eta > 0$ satisfies $-s^2 \le -\eta \abs{s}$ for small $\abs{s}$, so $S$ is approached only asymptotically.
In practice the switching is fast but not infinitely fast, and the state chatters around $S$.
