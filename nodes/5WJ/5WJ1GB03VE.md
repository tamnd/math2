---
tag: 5WJ1GB03VE
kind: statement
role: fact
name: Drucker–Prager yield criterion
msc: [74C05, 74L10]
uses: [CWWCEXZ8BH, X8AKXSA2RV]
about: [CWWCEXZ8BH]
sources:
  - url: https://en.wikipedia.org/wiki/Drucker–Prager_yield_criterion
same_as:
  wikidata: Q421507
  wikipedia: Drucker–Prager yield criterion
---

## Statement

Let $\sigma$ be the Cauchy stress at a point of an isotropic material, $I_1 = \tr \sigma$ its first invariant, $s = \sigma - \tfrac13 I_1 I$ its [[deviatoric part|X8AKXSA2RV]], and $J_2 = \tfrac12 s : s$.
Let $A$ and $B$ be material constants.
The Drucker–Prager criterion states that the material yields when
$$\sqrt{J_2} = A + B I_1.$$

## Remarks

The criterion is a constitutive assumption, proposed by Drucker and Prager in 1952 for soils, not a theorem.
Its [[yield surface|CWWCEXZ8BH]] in principal stress space is a circular cone with axis the line $\sigma_1 = \sigma_2 = \sigma_3$, so it is pressure dependent.
With tensile stresses positive, a material that is stronger under compression has $B < 0$, so that $\sqrt{J_2}$ at yield grows as $I_1$ becomes more negative.
If $B = 0$ it reduces to the [[von Mises criterion|V82XMG8WPE]] with $A = \sigma_y / \sqrt{3}$.
The constants are often chosen so that the cone passes through the corners of a [[Mohr–Coulomb|Q5CF1Z6179]] pyramid; the cone is then a smooth approximation of the Mohr–Coulomb surface.
Example: with $B = 0$ and $A = \sigma_y/\sqrt3$, uniaxial tension $\sigma_1 = \sigma$ gives $J_2 = \sigma^2/3$, so yield at $\sigma = \sigma_y$.

## Explanations

### L1 human

Soils, rocks and concrete can carry more shear when they are squeezed.
The Drucker–Prager criterion builds this into the von Mises criterion: the shear needed to yield grows linearly with the pressure.
Its shape in stress space is a cone instead of a cylinder.

### L2 human

The cone is smooth except at its apex, which makes it convenient in finite element codes for geomaterials.
Used with an associated flow rule, it predicts that plastic shearing comes with a growth of volume, called dilatancy.
The predicted dilatancy is usually too large for real soils, so a non-associated flow rule is often used instead.
It is a member of a family of pressure-sensitive criteria that also contains the Mohr–Coulomb criterion and the cap models.
