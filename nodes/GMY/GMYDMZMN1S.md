---
tag: GMYDMZMN1S
kind: statement
role: theorem
name: Levi's extension theorem for meromorphic functions
msc: [32D15, 32A20]
uses: [W6FTSF57T1, DJBWP7D3M8]
about: [W6FTSF57T1]
sources:
  - url: https://en.wikipedia.org/wiki/Hartogs%27s_extension_theorem
---

## Statement

Let $n \ge 2$ and write $z = (z', z_n)$ with $z' \in \C^{n-1}$ and $\abs{z'} = \max_{j < n} \abs{z_j}$.
Let $\Delta^n$ be the unit [[polydisc|DJBWP7D3M8]] in $\C^n$, let $0 < r < 1$ and $0 < s < 1$, and let
$$H = \set{z \in \Delta^n : \abs{z'} < r \text{ or } \abs{z_n} > s}.$$
Then every [[meromorphic function|W6FTSF57T1]] on $H$ is the restriction of a unique meromorphic function on $\Delta^n$.

## Remarks

The set $H$ is the [[Hartogs figure|GHJC53RFBT]].
For holomorphic functions the extension is given by a Cauchy integral in $z_n$ over a circle in the shell $s < \abs{z_n} < 1$.
For meromorphic functions one must also control the poles of the one-variable functions $z_n \mapsto f(z', z_n)$ as $z'$ varies, which makes the proof harder.
Uniqueness follows from the identity theorem, since $H$ is a nonempty open subset of the connected set $\Delta^n$.

Example: $f(z) = 1/(z_n - z_1)$ is meromorphic on $H$, and it extends to the meromorphic function $1/(z_n - z_1)$ on $\Delta^n$.
When $r \le s$, its polar set $\set{z_n = z_1}$ passes through the region between the column and the shell.

The hypothesis $n \ge 2$ is needed: in one variable, $e^{1/z}$ is holomorphic on the annulus $s < \abs{z} < 1$ but has no meromorphic extension to the unit disc.

## Explanations

### L1 human

Hartogs's extension theorem says that holomorphic functions on a Hartogs figure fill in the missing region.
Levi's theorem says the same for meromorphic functions, which are allowed to have poles.
The poles can run through the missing region, but the function still extends there as a quotient of holomorphic functions.

### L2 human

The theorem shows that extension phenomena in several variables are not limited to holomorphic functions.
Many continuation arguments in several variables move a Hartogs figure step by step through a domain.
Levi's theorem lets these arguments run for meromorphic functions as well as for holomorphic ones.
It is used, for example, in the study of meromorphic functions on complex manifolds and of the singularities of meromorphic maps.
