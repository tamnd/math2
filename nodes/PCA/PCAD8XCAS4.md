---
tag: PCAD8XCAS4
kind: definition
name: Uniform theory of diffraction
msc: [78A45, 78M35]
defines: P9Z364ZNDA
uses: [ES9KPGJAGS, D0TQ9F2ZDW, 8BQYB8H5CT]
sources:
  - url: https://en.wikipedia.org/wiki/Uniform_theory_of_diffraction
---

## Definition

Consider time-harmonic [[scattering|8BQYB8H5CT]] of a wave of wave number $k$ by a perfectly conducting body with edges.
Assume that $k L \gg 1$ for every length $L$ of the geometry.
Use the time factor $e^{j\omega t}$ of the engineering literature.
The *uniform theory of diffraction* approximates the total field at a point $P$ by the sum of these ray contributions:

1. the incident and reflected fields of geometrical optics, each present only where its ray reaches $P$;
2. the diffracted fields. Let a diffracted ray from an edge point $Q$ reach $P$ at distance $s$. It contributes
$$E^d(P) = E^i(Q) \cdot \mathbf{D} \, \sqrt{\frac{\rho}{s (\rho + s)}} \, e^{-j k s},$$
where $\rho$ is the caustic distance of the diffracted ray and $\mathbf{D}$ is a dyadic diffraction coefficient.

The coefficients $\mathbf{D}$ are those of [[Keller's geometrical theory of diffraction|ES9KPGJAGS]], with one change.
Each term that is singular at a shadow or reflection boundary is multiplied by a transition function.
That function is
$$F(X) = 2 j \sqrt{X} \, e^{j X} \int_{\sqrt{X}}^{\infty} e^{-j \tau^2} \, d\tau, \qquad X > 0,$$
and its argument $X$ tends to $0$ at that boundary.

## Remarks

$F$ is a complementary [[Fresnel integral|D0TQ9F2ZDW]] times an elementary factor.
For large $X$, away from the boundaries, $F(X) \to 1$, and the diffracted field reduces to that of Keller's theory.
Near a boundary the product of $F$ with the singular coefficient stays bounded, and its jump cancels the jump of the geometrical-optics field, so the total field is continuous.

Example: take a straight edge of a perfectly conducting wedge.
The dyadic coefficient splits into scalar soft and hard coefficients, each a sum of four cotangent terms, and each term carries its own transition function.

Non-example: Keller's original wedge coefficients, without the factor $F$, give a diffracted field that is infinite on the shadow boundary, so they do not form a uniform method.

## Explanations

### L1 human

The total field is a sum over rays: direct, reflected and diffracted by edges.
Each diffracted ray gets an amplitude from a diffraction coefficient and decays as it spreads.
The transition function is a correction that matters only near shadow borders, where it keeps the sum smooth.
