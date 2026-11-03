---
tag: GS9W0JDBW8
kind: statement
role: fact
name: Le Chatelier's principle
msc: [80A10, 80A50]
uses: [5EKTEE00FZ, 2KMN67HYNC, YYQRRFQAQP]
about: [5EKTEE00FZ, 2KMN67HYNC]
sources:
  - url: https://en.wikipedia.org/wiki/Le_Chatelier's_principle
same_as:
  wikidata: Q192690
  wikipedia: Le Chatelier's principle
---

## Statement

Let a system be in stable [[thermodynamic equilibrium|5EKTEE00FZ]].
Change one of the external conditions that fix the equilibrium, such as temperature, pressure or the amount of a species, by a small amount.
Then the system reaches a new equilibrium.
In it, the internal change partly counteracts the imposed change.

## Remarks

In this qualitative form the principle is a rule of thumb; its precise content is the set of [[thermodynamic stability conditions|YYQRRFQAQP]].
For example, positive heat capacity means that heat added to a system raises its temperature, which then reduces the further flow of heat into it.
Positive compressibility means that a rise of external pressure reduces the volume, which raises the internal pressure.

For a [[chemical equilibrium|2KMN67HYNC]] of ideal gases it gives two standard predictions.
At fixed temperature, raising the pressure shifts the equilibrium toward the side with fewer moles of gas; for $\mathrm{N_2} + 3\,\mathrm{H_2} \rightleftharpoons 2\,\mathrm{NH_3}$ the yield of ammonia increases.
At fixed pressure, raising the temperature shifts the equilibrium toward the endothermic direction, because $d \ln K / dT = \Delta H^\circ / (R T^2)$ for the equilibrium constant $K$, the standard reaction enthalpy $\Delta H^\circ$ and the gas constant $R$.

The stability hypothesis is necessary: near an unstable state a small change can trigger a large change in the same direction.
The naive reading can fail when the disturbance is not a single conjugate variable.
For ammonia synthesis at fixed temperature and pressure, adding nitrogen shifts the equilibrium toward decomposition of ammonia when the mole fraction of nitrogen exceeds $1/2$.

## Explanations

### L1 human

If you disturb a system at rest, it reacts so as to soften the disturbance.
Heat it, and it absorbs heat by favouring processes that take in heat.
Compress it, and it favours states that take less room.
Chemists use this to choose temperature and pressure that push a reaction toward the product they want.

### L2 human

The principle was formulated in chemistry, and in general it is too vague to be a theorem.
Its sharp versions follow from the convexity of the internal energy, which gives $C_V > 0$ and $\kappa_T > 0$.
For reactions, the van 't Hoff equation gives the temperature dependence of an equilibrium constant.
A refined version, often called the Le Chatelier–Braun principle, compares responses.
The response of a variable is largest when the other variables are free to adjust, and smaller when they are held fixed.
Examples are $C_p \ge C_V$ and $\kappa_T \ge \kappa_S$.
