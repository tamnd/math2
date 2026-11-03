---
tag: MET15VK1F8
kind: statement
role: theorem
name: Van 't Hoff equation
msc: [80A50, 80A10]
uses: [PQ4D33P7EE, 3DDVWE0J2V, 722RZK72P5, 2KMN67HYNC]
about: [2KMN67HYNC]
sources:
  - url: https://en.wikipedia.org/wiki/Van_%27t_Hoff_equation
same_as:
  wikidata: Q574862
  wikipedia: Van 't Hoff equation
---

## Statement

Let $\Delta_r G^\circ(T)$ be the standard reaction Gibbs energy of a reaction at temperature $T$.
Let $K(T) = \exp(-\Delta_r G^\circ(T)/(RT))$ be its equilibrium constant, as in the [[law of mass action|PQ4D33P7EE]].
Let $\Delta_r H^\circ(T)$ be the standard reaction [[enthalpy|722RZK72P5]].
Then
$$\frac{d \ln K}{dT} = \frac{\Delta_r H^\circ(T)}{R T^2}.$$

## Remarks

Since $\ln K = -\Delta_r G^\circ/(RT)$, the claim is $\frac{d}{dT}\left(\frac{\Delta_r G^\circ}{T}\right) = -\frac{\Delta_r H^\circ}{T^2}$, which is the [[Gibbs–Helmholtz equation|3DDVWE0J2V]] applied to each species and summed with the stoichiometric coefficients.
If $\Delta_r H^\circ$ is constant over a range of temperatures, integration gives $\ln\frac{K(T_2)}{K(T_1)} = -\frac{\Delta_r H^\circ}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$.
For an exothermic reaction, $\Delta_r H^\circ < 0$, so $K$ decreases as $T$ increases; the synthesis of ammonia is an example, and this is why its yield falls at high temperature.
A plot of $\ln K$ against $1/T$, the van 't Hoff plot, is then nearly a straight line of slope $-\Delta_r H^\circ/R$.

## Explanations

### L1 human

The van 't Hoff equation tells how the balance point of a reaction shifts with temperature.
Reactions that give off heat are pushed back when you heat them, and reactions that absorb heat are pushed forward.
The size of the shift is set by how much heat the reaction exchanges.

### L2 human

It is the quantitative form of [[Le Chatelier's principle|GS9W0JDBW8]] for temperature changes.
It has the same shape as the [[Clausius–Clapeyron relation|4XEQ5FA5P9]], which is the special case of an evaporation "reaction" from liquid to vapour with $K$ proportional to the vapour pressure.
In practice it is used in both directions: to predict $K$ at a new temperature, or to measure $\Delta_r H^\circ$ from equilibrium data at several temperatures.
