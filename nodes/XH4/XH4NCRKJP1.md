---
tag: XH4NCRKJP1
kind: example
name: Einstein static universe
msc: ["83F05", "83C15"]
instance_of: [H7PS83YCER]
uses: [ECJMS4VDTF, PPHFS2P4G4, WVKKDY9V61, H4FNPG6ZY1]
sources:
  - url: https://en.wikipedia.org/wiki/Static_universe
---

## Example

The *Einstein static universe* is a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]] with positive spatial curvature.
Its scale factor is a constant $a(t) = a_0 > 0$:
$$ds^2 = -dt^2 + a_0^2 \left( d\chi^2 + \sin^2\chi \, d\Omega^2 \right), \qquad 0 \le \chi \le \pi,$$
on $\R \times S^3$, in units with $c = 1$.
Here $d\Omega^2$ is the round metric on the unit sphere, and the curvature constant is $k = 1$.
It is filled with pressureless dust of constant density $\rho > 0$ and has a [[cosmological constant|WVKKDY9V61]] $\Lambda$.

Check: with $\dot a = \ddot a = 0$ and $p = 0$, the second [[Friedmann equation|PPHFS2P4G4]] gives $0 = -\tfrac{4\pi G}{3}\rho + \tfrac{\Lambda}{3}$, so $\Lambda = 4\pi G \rho$.
The first gives $0 = \tfrac{8\pi G}{3}\rho - \tfrac{1}{a_0^2} + \tfrac{\Lambda}{3}$, so $\tfrac{1}{a_0^2} = \tfrac{8\pi G}{3}\rho + \tfrac{4\pi G}{3}\rho = 4\pi G \rho = \Lambda$.
So the metric solves the Einstein equations with [[dust|H4FNPG6ZY1]] exactly when $\Lambda = 4\pi G\rho = 1/a_0^2$.

## Remarks

Einstein proposed this model in 1917, and introduced the cosmological constant to make a static solution possible.
The balance is unstable: a small perturbation of $a$ makes the model either expand or collapse, since $\ddot a$ changes sign with the perturbation.
Without $\Lambda$ no static model with $\rho > 0$ and $p \ge 0$ exists, because the second Friedmann equation then forces $\ddot a < 0$.
Its conformal boundary structure makes it a standard background: Minkowski space is conformal to a relatively compact open region of $\R \times S^3$ with this metric.

## Explanations

### L1 human

Einstein wanted a universe that does not change in time.
Ordinary gravity pulls matter together, so he added a repulsive cosmological constant that exactly balances it.
The result is a closed universe, shaped like a three-dimensional sphere, of fixed size.
The balance is fragile, like a pencil standing on its tip, and the discovery of cosmic expansion made the model obsolete as a description of our universe.
