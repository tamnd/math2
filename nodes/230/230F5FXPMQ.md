---
tag: 230F5FXPMQ
kind: statement
role: theorem
name: Weyl character formula for compact groups
msc: ["22E46", 22C05, 17B10]
uses: [9TFC6ADC1C, 3JVGZVVTB0, EZGTEK3HQN, RMWMYBY8TC, FX3NEFYFFN]
about: [RMWMYBY8TC, 9TFC6ADC1C]
sources:
  - url: https://en.wikipedia.org/wiki/Weyl_character_formula
---

## Statement

Let $G$ be a connected [[compact Lie group|9TFC6ADC1C]], and let $T$ be a [[maximal torus|3JVGZVVTB0]] with Lie algebra $\mathfrak{t}$.
Let $W$ be the [[Weyl group|EZGTEK3HQN]], acting on the dual space $\mathfrak{t}^*$.
Identify each continuous character of $T$ with the linear form $\mu \in \mathfrak{t}^*$ such that the character sends $\exp H$ to $e^{i\mu(H)}$ for $H \in \mathfrak{t}$.
Let $\Phi \subset \mathfrak{t}^*$ be the roots of $G$, choose a set $\Phi^+$ of positive roots, and let $\rho = \frac{1}{2}\sum_{\alpha \in \Phi^+} \alpha$.
For $w \in W$ let $\varepsilon(w) = \det(w) \in \set{1, -1}$.
Let $V$ be a finite-dimensional [[irreducible|FX3NEFYFFN]] continuous representation of $G$ with highest weight $\lambda$, and let $\chi_V$ be its [[character|RMWMYBY8TC]].
Then for every $H \in \mathfrak{t}$ with $\prod_{\alpha \in \Phi^+} \sin(\alpha(H)/2) \ne 0$,
$$\chi_V(\exp H) = \frac{\sum_{w \in W} \varepsilon(w)\, e^{i (w(\lambda + \rho))(H)}}{\sum_{w \in W} \varepsilon(w)\, e^{i (w\rho)(H)}}.$$

## Remarks

The denominator equals $\prod_{\alpha \in \Phi^+} \left(e^{i\alpha(H)/2} - e^{-i\alpha(H)/2}\right)$, by the Weyl denominator formula.
One proof multiplies $\chi_V$ by the denominator and notes that the product is $W$-alternating with integer coefficients.
The [[Weyl integration formula|QMH530N27M]] and $\int_G \abs{\chi_V}^2 \, dg = 1$ then show that only the term $\lambda + \rho$ and its $W$-images survive, each with coefficient $\pm 1$.
Example: for $G = SU(2)$ and $H = \operatorname{diag}(i\theta, -i\theta)$, there is one positive root with $\alpha(H) = 2\theta$, $\rho(H) = \theta$, and the representation of dimension $n + 1$ has $\lambda(H) = n\theta$.
The formula gives $\chi(\exp H) = \frac{e^{i(n+1)\theta} - e^{-i(n+1)\theta}}{e^{i\theta} - e^{-i\theta}} = \frac{\sin((n+1)\theta)}{\sin\theta}$, which is $e^{in\theta} + e^{i(n-2)\theta} + \cdots + e^{-in\theta}$.
Letting $H \to 0$ gives the Weyl dimension formula $\dim V = \prod_{\alpha \in \Phi^+} \frac{\ip{\lambda + \rho}{\alpha}}{\ip{\rho}{\alpha}}$ for a $W$-invariant inner product on $\mathfrak{t}^*$.

## Explanations

### L1 human

The character of a representation records the trace of each group element, and it determines the representation.
The Weyl formula gives this character in closed form, as a ratio of two alternating sums of exponentials.
Only the highest weight $\lambda$ of the representation enters, together with data of the group: its roots and its Weyl group.

### L2 human

By [[conjugacy of maximal tori|BE3XK5ERC1]], a character is determined by its values on $T$, so the formula gives it everywhere.
Together with the [[Peter–Weyl theorem|6VC9QE39XH]] it gives the theorem of the highest weight: irreducible representations of $G$ correspond to dominant integral weights.
The dimension formula and Kostant's multiplicity formula follow from it, and the [[Borel–Weil–Bott theorem|K10YADF5XV]] gives a geometric realisation of the same representations.
For $G = U(n)$ the formula expresses irreducible characters as Schur polynomials in the eigenvalues.
