---
tag: GHJC53RFBT
kind: example
name: Hartogs figure
msc: [32D15, 32D10, 32Q02]
illustrates: [FSGES670AZ, 4487CSC0MB]
uses: [DJBWP7D3M8, 507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Hartogs%27s_extension_theorem
---

## Example

Let $n \ge 2$ and write a point of $\C^n$ as $z = (z', z_n)$ with $z' \in \C^{n-1}$, and $\abs{z'} = \max_{j < n} \abs{z_j}$.
Let $\Delta^n = \set{z : \abs{z'} < 1, \abs{z_n} < 1}$ be the unit [[polydisc|DJBWP7D3M8]], and fix $0 < r < 1$ and $0 < s < 1$.
The *Hartogs figure* is the connected open set
$$H = \set{z \in \Delta^n : \abs{z'} < r \text{ or } \abs{z_n} > s}.$$
It is the union of a thin column $\set{\abs{z'} < r}$ and a shell $\set{s < \abs{z_n} < 1}$ inside $\Delta^n$.

Every [[holomorphic function|507C34W0ZT]] $f$ on $H$ extends to a holomorphic function on all of $\Delta^n$.
Fix $t$ with $s < t < 1$ and put
$$F(z', z_n) = \frac{1}{2\pi i} \int_{\abs{\zeta} = t} \frac{f(z', \zeta)}{\zeta - z_n} \, d\zeta \quad \text{for } \abs{z'} < 1, \ \abs{z_n} < t.$$
The circle $\abs{\zeta} = t$ lies in the shell, so the integrand is defined, and $F$ is holomorphic by differentiation under the integral sign.
For $\abs{z'} < r$, the one-variable function $\zeta \mapsto f(z', \zeta)$ is holomorphic on the whole unit disc, so the Cauchy integral formula gives $F = f$ there.
The sets where $F$ and $f$ are both defined form a connected open set, so the identity theorem gives $F = f$ on all of it.
Gluing $F$ and $f$ gives the extension to $\Delta^n$.

## Remarks

So $H$ is not a [[domain of holomorphy|4487CSC0MB]]: every holomorphic function on $H$ continues to the larger set $\Delta^n$.
This is the basic instance of [[Hartogs's extension theorem|FSGES670AZ]].
The extra variables are essential: in one variable the shell alone is the annulus $s < \abs{z} < 1$, and $1/z$ is holomorphic there but does not extend to the unit disc.

## Explanations

### L1 human

Picture a solid cylinder made of a thin vertical pole together with a thick outer ring, with the space between them missing.
In several complex variables, every holomorphic function defined on this shape automatically extends to fill the missing part.
The reason is that values on the outer ring determine, through Cauchy's integral, a function on the whole cylinder.
This picture is the starting point for all extension phenomena in several variables.
