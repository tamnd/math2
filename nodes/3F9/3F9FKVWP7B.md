---
tag: 3F9FKVWP7B
kind: statement
role: fact
name: De Vaucouleurs's law
msc: [85A15]
uses: [K4HT790E83]
about: [K4HT790E83]
sources:
  - url: https://en.wikipedia.org/wiki/De_Vaucouleurs%27s_law
same_as:
  wikidata: Q1179455
  wikipedia: De Vaucouleurs's law
---

## Statement

Let $I(R)$ be the surface brightness of an elliptical galaxy, or of the bulge of a spiral galaxy, at projected radius $R$.
Then $I$ is well approximated by
$$I(R) = I_e \exp\left( -b_4 \left[ \left( \frac{R}{R_e} \right)^{1/4} - 1 \right] \right), \qquad b_4 \approx 7.669,$$
where $R_e$ is the radius that contains half of the total light and $I_e = I(R_e)$.
Equivalently, in magnitudes per unit area,
$$\mu(R) = \mu_e + 8.327 \left[ \left( \frac{R}{R_e} \right)^{1/4} - 1 \right].$$

## Remarks

This is an empirical law, found by Gérard de Vaucouleurs from photometry of elliptical galaxies, not a theorem.
It is the [[Sérsic profile|K4HT790E83]] with index $n = 4$, and $b_4$ solves $\gamma(8, b_4) = \frac{1}{2}\Gamma(8)$.
The constant in the magnitude form is $2.5 \log_{10}(e) \, b_4 \approx 1.0857 \times 7.669 \approx 8.327$.
The total luminosity is $L = 8 \pi \, \Gamma(8) \, e^{b_4} b_4^{-8} \, I_e R_e^2 \approx 7.215 \, \pi I_e R_e^2$.

Example: at $R = 16 R_e$, $(R/R_e)^{1/4} = 2$, so the surface brightness is $8.327$ magnitudes fainter than at $R_e$, a factor of about $e^{7.669} \approx 2100$.

Many ellipticals are fitted better by Sérsic profiles with other indices, with larger $n$ for brighter galaxies, so the law is a good approximation rather than an exact rule.

## Explanations

### L1 human

The light of an elliptical galaxy fades from its centre outward in a very regular way.
De Vaucouleurs found that the logarithm of the brightness falls in a straight line when it is plotted against the fourth root of the distance.
This one rule describes a huge range of galaxies with only two numbers, a size and a brightness.

### L2 human

The law is the case $n = 4$ of the Sérsic family, which later extended it to disks ($n = 1$) and to other galaxies.
It is used to measure effective radii and luminosities of galaxies, which enter scaling relations such as the fundamental plane.
Deprojecting the profile into a three-dimensional density gives no elementary closed form, so approximate models such as the Hernquist and Jaffe profiles are used for dynamics.
