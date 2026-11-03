---
tag: FZGYFV69HK
kind: statement
role: theorem
name: Hashin–Shtrikman bounds
msc: [74Q20, "74E30", 78A48]
uses: [5RSREPYN0F, PPXM3HCN6Y, J2GWW1NPTC]
about: [5RSREPYN0F]
sources:
  - url: https://en.wikipedia.org/wiki/Effective_medium_approximations
---

## Statement

Consider a statistically isotropic two-phase composite in $\R^3$ whose phases occupy volume fractions $f_1$ and $f_2 = 1 - f_1$.

1. If the phases have conductivities $0 < \sigma_1 \le \sigma_2$, the effective conductivity $\sigma^*$ satisfies
$$\sigma_1 + \frac{f_2}{\frac{1}{\sigma_2 - \sigma_1} + \frac{f_1}{3 \sigma_1}} \le \sigma^* \le \sigma_2 + \frac{f_1}{\frac{1}{\sigma_1 - \sigma_2} + \frac{f_2}{3 \sigma_2}}.$$
2. If the phases are isotropic linear elastic with [[bulk moduli|PPXM3HCN6Y]] $K_1 \le K_2$ and [[shear moduli|J2GWW1NPTC]] $G_1 \le G_2$, all positive, the effective bulk modulus $K^*$ satisfies
$$K_1 + \frac{f_2}{\frac{1}{K_2 - K_1} + \frac{3 f_1}{3 K_1 + 4 G_1}} \le K^* \le K_2 + \frac{f_1}{\frac{1}{K_1 - K_2} + \frac{3 f_2}{3 K_2 + 4 G_2}}.$$
3. Under the same hypotheses, the effective shear modulus $G^*$ satisfies
$$G_1 + \frac{f_2}{\frac{1}{G_2 - G_1} + \frac{6 f_1 (K_1 + 2 G_1)}{5 G_1 (3 K_1 + 4 G_1)}} \le G^* \le G_2 + \frac{f_1}{\frac{1}{G_1 - G_2} + \frac{6 f_2 (K_2 + 2 G_2)}{5 G_2 (3 K_2 + 4 G_2)}}.$$

When $\sigma_1 = \sigma_2$ (or $K_1 = K_2$, or $G_1 = G_2$), the corresponding bounds are read as the common value.

## Remarks

The proof uses the Hashin–Shtrikman variational principle.
It compares the composite with a homogeneous reference medium and optimizes over a polarization field.
Choosing the reference equal to the softer or the stiffer phase gives the lower or the upper bound.
The bounds on conductivity and on the bulk modulus are optimal: they are attained by Hashin's assemblage of coated spheres.
The stiffer phase is the coating for the upper bound, and the softer phase for the lower bound.
They always lie between the [[Voigt and Reuss bounds|Y7WKXDD9SJ]] and are much closer to each other.
For example, with $\sigma_1 = 1$, $\sigma_2 = 10$ and $f_1 = f_2 = 1/2$, they give $2.8 \le \sigma^* \le 4.71$, whereas the harmonic and arithmetic means give $1.82 \le \sigma^* \le 5.5$, to two decimals.
The isotropy hypothesis is needed: a laminate is not isotropic, and its conductivity along the layers is the arithmetic mean, which exceeds the upper bound.

## Explanations

### L1 human

If one knows only how much of each material a mixture contains, and that it looks the same in every direction, its conductivity or stiffness still cannot be anything.
The Hashin–Shtrikman bounds give the narrowest possible range for it.
Mixtures made of tiny coated balls reach the ends of the range.

### L2 human

The bounds are a sharpening of the Voigt and Reuss bounds that uses the isotropy of the composite.
They are a standard test for [[effective medium approximations|VSBFY8EN2H]]: a sound approximation must give values between them.
The [[Mori–Tanaka method|F79NNVV0B1]] for spherical inclusions in a matrix reproduces one of the Hashin–Shtrikman bounds for the bulk modulus.
