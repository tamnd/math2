---
tag: AB7W6DBA4P
kind: definition
name: Singular integral equation
msc: ["45E05", "45E99"]
defines: E30EA6ETZ4
uses: [R3SG1SN7JQ, 0SYR10HD4R, 012PBA0FMD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Definition

Let $\Gamma$ be a finite union of disjoint smooth closed curves in $\C$.
Let $a$, $b$ and $f$ be [[Hölder continuous|012PBA0FMD]] functions on $\Gamma$, and let $k \colon \Gamma \times \Gamma \to \C$ be Hölder continuous.
A *singular integral equation* with Cauchy kernel on $\Gamma$ is an equation
$$a(t) \, \varphi(t) + \frac{b(t)}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau + \int_\Gamma k(t, \tau) \, \varphi(\tau) \, d\tau = f(t), \quad t \in \Gamma,$$
for an unknown Hölder continuous function $\varphi$ on $\Gamma$.
Here $\mathrm{p.v.}$ is the [[Cauchy principal value|0SYR10HD4R]]: the limit as $\varepsilon \to 0$ of the integral over the part of $\Gamma$ outside the disc $\abs{\tau - t} < \varepsilon$.
The equation is *of normal type* when $a(t)^2 - b(t)^2 \ne 0$ for all $t \in \Gamma$.
The equation with $k = 0$ is its *dominant* or *characteristic* equation.

## Remarks

Example: on the unit circle, with $a = 0$, $b = 1$ and $k = 0$, the equation $\frac{1}{\pi i} \, \mathrm{p.v.} \int_\Gamma \frac{\varphi(\tau)}{\tau - t} \, d\tau = f(t)$ is of normal type, since $a^2 - b^2 = -1$.
For $\varphi(\tau) = \tau^n$ with $n \ge 0$ the left side is $t^n$, and for $n < 0$ it is $-t^n$; so $f(t) = t^2$ is solved by $\varphi(\tau) = \tau^2$.
Non-example: if the kernel is $k(t, \tau)$ alone, continuous, with $b = 0$ and $a = 1$, the equation is a Fredholm equation of the second kind and is not singular.
The term $\frac{1}{\tau - t}$ makes the integral divergent as an ordinary integral at $\tau = t$ unless $\varphi(t) = 0$; the Hölder condition makes the principal value exist.
More generally, the name covers equations with other kernels that are integrated as principal values, including kernels on open arcs and in several variables.
