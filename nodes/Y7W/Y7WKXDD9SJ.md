---
tag: Y7WKXDD9SJ
kind: statement
role: theorem
name: Voigt and Reuss bounds
msc: [74Q20, "74E30", 74Q05]
uses: [5RSREPYN0F, SX32X1D537, 8QS6QMJF5Z]
about: [5RSREPYN0F, SX32X1D537]
sources:
  - url: https://en.wikipedia.org/wiki/Rule_of_mixtures
---

## Statement

Let $Y = [0,1)^3$ be the unit cell, and let $C(y)$ be a $Y$-periodic, measurable field of [[elasticity tensors|SX32X1D537]] with the usual symmetries.
Assume that $C$ is uniformly bounded and uniformly positive definite on symmetric matrices.
Write $\langle g \rangle = \int_Y g \, dy$ for the average over the cell.
Let $C^*$ be the homogenized elasticity tensor.
For every symmetric $3 \times 3$ matrix $E$ it satisfies
$$E : C^* : E = \min_{w} \left\langle (E + e(w)) : C : (E + e(w)) \right\rangle,$$
where $w$ runs over $Y$-periodic $H^1$ displacement fields and $e(w)$ is the symmetric part of $\nabla w$.
Then, in the sense of quadratic forms on symmetric matrices,
$$\langle C^{-1} \rangle^{-1} \le C^* \le \langle C \rangle.$$
If the composite consists of $n$ phases with constant tensors $C_1, \dots, C_n$ and volume fractions $f_1, \dots, f_n$, this reads
$$\Big( \sum_{i=1}^n f_i C_i^{-1} \Big)^{-1} \le C^* \le \sum_{i=1}^n f_i C_i.$$

## Remarks

The upper (Voigt) bound follows by inserting the trial field $w = 0$, that is a uniform [[strain|8QS6QMJF5Z]] $E$, into the minimum principle.
The lower (Reuss) bound follows in the same way from the dual principle of minimum complementary energy, with a uniform stress as trial field.
The same argument bounds the effective conductivity $\sigma^*$ of a composite of phases with conductivities $\sigma_i$ and volume fractions $f_i$.
It gives $\big(\sum_i f_i / \sigma_i\big)^{-1} \le \sigma^* \le \sum_i f_i \sigma_i$.
For conductivity the upper bound is attained by a laminate in the direction along the layers and the lower bound in the direction across them.
So these bounds cannot be improved without more information on the geometry.
Model a fibre composite in one dimension as springs in parallel or in series, with Young's moduli $E_f$, $E_m$ and fibre fraction $f$.
The same averages then give the rule of mixtures $f E_f + (1-f) E_m$ and the inverse rule $(f/E_f + (1-f)/E_m)^{-1}$.

## Explanations

### L1 human

A mixture of a stiff and a soft material is never stiffer than the average of their stiffnesses, and never softer than the average of their softnesses.
The first average assumes that all parts stretch by the same amount, the second that all parts carry the same force.
These two simple guesses bracket the true stiffness of any mixture.

### L2 human

These bounds are the first step in the theory of bounds on [[effective properties|VSBFY8EN2H]].
They use only the volume fractions, which is why they are far apart when the phases differ a lot.
Adding the information that the composite is isotropic gives the much sharper [[Hashin–Shtrikman bounds|FZGYFV69HK]].
The proof is a direct use of the variational characterization of the homogenized tensor from [[homogenization|5RSREPYN0F]].
