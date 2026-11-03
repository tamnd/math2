---
tag: PQ4D33P7EE
kind: statement
role: theorem
name: Law of mass action
msc: [80A50, 80A30, "92E20"]
uses: [2KMN67HYNC, WVH4PVW64P, N7R0H2VNDJ, RBG5ZBM35Y]
about: [2KMN67HYNC]
sources:
  - url: https://en.wikipedia.org/wiki/Law_of_mass_action
same_as:
  wikidata: Q899494
  wikipedia: Law of mass action
---

## Statement

Consider a reaction $\sum_{i=1}^k \nu_i A_i = 0$ among species that form a mixture of [[ideal gases|N7R0H2VNDJ]] at temperature $T$, with stoichiometric coefficients $\nu_i$ and partial pressures $p_i > 0$.
Let $p^\circ$ be a fixed standard pressure, and let $\Delta_r G^\circ(T) = \sum_i \nu_i \mu_i^\circ(T)$, where $\mu_i^\circ(T)$ is the [[chemical potential|WVH4PVW64P]] of pure $A_i$ at $T$ and $p^\circ$.
If the mixture is in [[chemical equilibrium|2KMN67HYNC]], then
$$\prod_{i=1}^k \left(\frac{p_i}{p^\circ}\right)^{\nu_i} = K(T), \qquad K(T) = \exp\left(-\frac{\Delta_r G^\circ(T)}{RT}\right).$$
The equilibrium constant $K(T)$ depends only on $T$, not on the composition or the total pressure.

## Remarks

In an ideal gas mixture $\mu_i = \mu_i^\circ(T) + RT \ln(p_i/p^\circ)$.
The equilibrium condition $\sum_i \nu_i \mu_i = 0$ becomes $\Delta_r G^\circ(T) + RT \sum_i \nu_i \ln(p_i/p^\circ) = 0$, and taking exponentials gives the law.
For $\mathrm{N_2} + 3\,\mathrm{H_2} \rightleftharpoons 2\,\mathrm{NH_3}$ it reads $\dfrac{(p_{\mathrm{NH_3}}/p^\circ)^2}{(p_{\mathrm{N_2}}/p^\circ)(p_{\mathrm{H_2}}/p^\circ)^3} = K(T)$; raising the total pressure therefore favours ammonia, since the left side has total degree $-2$ in the pressures.
For non-ideal mixtures, the same law holds with activities in place of $p_i/p^\circ$.
The [[Gibbs free energy|RBG5ZBM35Y]] change $\Delta_r G^\circ$ is negative exactly when $K > 1$.

## Explanations

### L1 human

The law of mass action says that at equilibrium a certain ratio of the amounts of products to reactants is always the same number at a given temperature.
If you add more of one reactant, the other amounts shift until the ratio is back to that number.
It turns a balance of energies into a simple algebraic equation for the composition.

### L2 human

This is the thermodynamic, equilibrium form of the law; it is how one computes the composition of a reacting mixture from tabulated standard Gibbs energies.
There is also a kinetic form, due to Guldberg and Waage, about the rate of an elementary reaction.
It says that the rate is proportional to the product of the reactant concentrations, each raised to its stoichiometric coefficient.
For an elementary reversible reaction, setting the forward and reverse rates equal recovers the equilibrium form.
The equilibrium constant, written in concentrations, is then the ratio of the forward and reverse rate constants.
The kinetic form is the basis of the differential equations of chemical reaction networks.
The temperature dependence of $K$ is given by the [[van 't Hoff equation|MET15VK1F8]].
