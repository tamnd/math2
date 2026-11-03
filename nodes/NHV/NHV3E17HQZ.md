---
tag: NHV3E17HQZ
kind: problem
name: Inverse heat conduction problem
msc: [80A23, 35R30, 35K05]
uses: [VP2HN86VAG, PCMW7KN5P4, W09B9NZ9B5, M68V0M5A3R]
about: [PCMW7KN5P4, VP2HN86VAG]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_problem
history:
  posed_by: "G. Stolz"
  first_stated: "1960"
  notes: "Stolz published one of the earliest treatments in 1960, computing surface heat flux in quenching from interior temperatures; the attribution is to this earliest known formulation. James V. Beck developed the problem systematically from 1962 on."
---

## Problem

Consider a rod $0 \le x \le L$ of a homogeneous material with thermal diffusivity $\kappa > 0$.
Its temperature $u(x, t)$ satisfies the [[heat equation|VP2HN86VAG]] $u_t = \kappa u_{xx}$ for $0 < x < L$ and $0 < t \le T$, with a known initial temperature $u(x, 0)$.
The end $x = L$ is insulated, so $u_x(L, t) = 0$, and the temperature $g(t) = u(L, t)$ at this end is measured for $0 \le t \le T$.
The end $x = 0$ is not accessible.
The *inverse heat conduction problem* asks: from the measured data $g$, recover the unknown boundary temperature $f(t) = u(0, t)$, or the boundary heat flux $-u_x(0, t)$, for $0 \le t \le T$.

## Remarks

This is an [[inverse problem|PCMW7KN5P4]]: the forward problem, which computes $g$ from $f$, is a standard boundary value problem for the heat equation and is [[well-posed|W09B9NZ9B5]].
The inverse problem is ill-posed in the sense of Hadamard.
The forward map smooths the boundary data strongly.
A component of $f$ with high frequency $\omega$ reaches the far end damped by a factor of order $e^{-c\sqrt{\omega}}$, for some $c > 0$.
So small errors in $g$ can cause very large errors in the recovered $f$, and the solution does not depend continuously on the data.
Under mild conditions the solution is unique when it exists, so the difficulty is stability, not uniqueness.
In practice it is solved with regularization methods, such as [[Tikhonov regularization|M68V0M5A3R]] or the mollification of the data.
Engineers also use sequential function specification methods.
The same name is used for related tasks, such as recovering an unknown heat source, an initial temperature (the backward heat problem), or a thermal conductivity from temperature measurements.

## Explanations

### L1 human

Imagine a metal wall whose outer face is in a furnace, where no sensor can survive.
A thermometer on the inner face records how the temperature there changes in time.
The question is what happened on the hot side, given only these readings.
Heat flow blurs sharp changes, so a quick spike on the hot side reaches the thermometer as a faint, smooth bump.
Undoing this blur also blows up the tiny errors of the thermometer, and that is why the problem is hard.
