---
tag: VDGJ2E0EPW
kind: example
name: Navarro–Frenk–White profile
msc: [85A05, 85A15, 85A40]
illustrates: [V4FYBDSGMT]
uses: [V4FYBDSGMT, DWK5N5SKTK]
sources:
  - url: https://en.wikipedia.org/wiki/Navarro%E2%80%93Frenk%E2%80%93White_profile
same_as:
  wikidata: Q6982166
  wikipedia: Navarro–Frenk–White profile
---

## Example

Let $\rho_0 > 0$ be a density and $r_s > 0$ a scale radius.
The *Navarro–Frenk–White profile*, or NFW profile, is the spherical density
$$\rho(r) = \frac{\rho_0}{\dfrac{r}{r_s} \left( 1 + \dfrac{r}{r_s} \right)^2}.$$
The mass inside radius $r$ is, with $x = r/r_s$,
$$M(r) = 4 \pi \rho_0 r_s^3 \left( \ln(1 + x) - \frac{x}{1 + x} \right).$$
Check: the derivative of the bracket in $x$ is $\frac{1}{1+x} - \frac{1}{(1+x)^2} = \frac{x}{(1+x)^2}$, and $\frac{dM}{dr} = 4\pi r^2 \rho(r) = 4\pi \rho_0 r_s^2 \frac{x}{(1+x)^2}$, which agree since $dx/dr = 1/r_s$; both sides of the formula vanish at $r = 0$.

The density falls like $r^{-1}$ for $r \ll r_s$ and like $r^{-3}$ for $r \gg r_s$, so the total mass diverges logarithmically.

## Remarks

The potential, the solution of [[Poisson's equation|DWK5N5SKTK]] that vanishes at infinity, is $\Phi(r) = -4 \pi G \rho_0 r_s^3 \ln(1 + r/r_s)/r$, where $G$ is the gravitational constant.
The circular speed $v_c = \sqrt{G M(r)/r}$ rises, reaches a maximum near $r \approx 2.16 \, r_s$, and then slowly falls, which is the shape of the [[rotation curve|V4FYBDSGMT]] of a dark matter halo of this kind.
Navarro, Frenk and White found that this profile fits the dark matter halos of cosmological $N$-body simulations over a wide range of masses.
In practice the halo is cut off at a radius $r_{200}$ inside which the mean density is $200$ times the critical density, and the ratio $c = r_{200}/r_s$ is called the concentration.

## Explanations

### L1 human

Computer simulations of the universe show that dark matter clumps into roughly spherical halos.
The NFW profile describes their density with one simple formula: steep in the outer parts, shallower near the centre, with a bend at the scale radius $r_s$.
Two numbers, a density and a radius, fix the whole halo, and they are what astronomers fit to rotation curves and lensing data.
