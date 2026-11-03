---
tag: 8QAKE5E9DJ
kind: example
name: Oregonator
msc: ["92E20", 37N25, 34C25]
illustrates: [0AAQ73WRFB]
uses: [KCGE92DJ1W, 0AAQ73WRFB, 2NHWCM0DK8]
sources:
  - url: https://en.wikipedia.org/wiki/Oregonator
same_as:
  wikidata: Q536710
  wikipedia: Oregonator
---

## Example

The *Oregonator* is a model of the oscillating [[Belousov–Zhabotinsky reaction|ST0ZG2FQYZ]], built by Field and Noyes from the detailed mechanism of Field, Körös and Noyes.
It is the [[reaction network|KCGE92DJ1W]]
$$A + Y \to X + P, \quad X + Y \to 2P, \quad A + X \to 2X + 2Z, \quad 2X \to A + P, \quad B + Z \to \tfrac{f}{2} Y,$$
with rate constants $k_1, \dots, k_5$ and a stoichiometric factor $f > 0$.
Here $X$ is bromous acid $\mathrm{HBrO_2}$, $Y$ is bromide $\mathrm{Br^-}$ and $Z$ is the oxidized form of the metal catalyst.
Further, $A$ is bromate $\mathrm{BrO_3^-}$, $B$ is the organic species, and $P$ is a product.
Holding $A$ and $B$ constant, mass-action kinetics gives
$$\dot X = k_1 A Y - k_2 X Y + k_3 A X - 2 k_4 X^2,$$
$$\dot Y = -k_1 A Y - k_2 X Y + \tfrac{f}{2} k_5 B Z,$$
$$\dot Z = 2 k_3 A X - k_5 B Z.$$
Each term is read off from one reaction: for example, $A + X \to 2X + 2Z$ runs at rate $k_3 A X$, raises $X$ by $1$ and raises $Z$ by $2$.
For a range of values of $f$ and of the other parameters, the equilibrium with positive concentrations is unstable.
Then the system has a stable [[limit cycle|0AAQ73WRFB]].
The oscillation is a [[relaxation oscillation|2NHWCM0DK8]]: slow phases alternate with fast jumps, because the rate constants differ by orders of magnitude.

## Explanations

### L1 human

The Oregonator is the simplest realistic model of a famous chemical clock.
It keeps only five reactions out of the many in the real mechanism, but it still oscillates.
Bromous acid $X$ makes more of itself, bromide $Y$ blocks this, and the catalyst $Z$ slowly brings bromide back.
This loop of growth, block and recovery repeats, and the colour of the solution flips back and forth.
