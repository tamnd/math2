---
tag: P101AX1ZSC
kind: concept
name: Hölder space
msc: ["46E15", 35B65]
sources:
  - url: https://en.wikipedia.org/wiki/H%C3%B6lder_condition
---

## Summary

The Hölder space $C^{k,\alpha}$ consists of the functions whose derivatives up to order $k$ are bounded.
In addition, the derivatives of order $k$ must be [[Hölder continuous|012PBA0FMD]] with exponent $\alpha$, where $0 < \alpha \le 1$.
With the natural norm it is a [[Banach space|06GZ956657]].
Hölder spaces are the setting of the classical regularity theory of elliptic and parabolic equations, as in the [[Schauder estimates|HSEKZMAH1V]].
They fill the gaps between the spaces $C^k$ of $k$ times continuously differentiable functions.

## Explanations

### L1 human

A Hölder continuous function cannot change faster than a fixed power of the distance: $\abs{u(x) - u(y)} \le C \abs{x - y}^\alpha$.
The exponent $\alpha$ measures roughness: $\alpha = 1$ means Lipschitz, and small $\alpha$ allows sharp spikes like $\sqrt{\abs{x}}$.
The space $C^{k,\alpha}$ asks this of the $k$-th derivatives.
For example, $x \abs{x}$ is in $C^{1,1}$ on $(-1, 1)$, because its derivative $2 \abs{x}$ is Lipschitz, but it is not twice differentiable at $0$.
