---
tag: YDEM84WFYD
kind: statement
role: proposition
name: Goldman equation
msc: [92C05, 92C20]
uses: [04DXAFN2ES, B9JD74Y5C3]
about: [RMWR3MDW0T]
sources:
  - url: https://en.wikipedia.org/wiki/Goldman_equation
same_as:
  wikidata: Q1535911
  wikipedia: Goldman equation
---

## Statement

Let a membrane of thickness $L$ separate an inside and an outside solution at absolute temperature $T$.
Let $R$ be the gas constant and $F$ the Faraday constant.
Let the permeant ions be $\mathrm{K}^+$, $\mathrm{Na}^+$ and $\mathrm{Cl}^-$, with permeabilities $P_{\mathrm{K}}, P_{\mathrm{Na}}, P_{\mathrm{Cl}} \ge 0$, not all zero.
Their concentrations $[\,\cdot\,]_{\mathrm{in}}$ inside and $[\,\cdot\,]_{\mathrm{out}}$ outside are positive.
Assume that the ions move independently, that the electric field in the membrane is constant, and that each ion flux obeys the Nernst–Planck equation.
Then the membrane potential $V = V_{\mathrm{in}} - V_{\mathrm{out}}$ at which the total electric current is zero is
$$V = \frac{RT}{F} \ln \frac{P_{\mathrm{K}} [\mathrm{K}^+]_{\mathrm{out}} + P_{\mathrm{Na}} [\mathrm{Na}^+]_{\mathrm{out}} + P_{\mathrm{Cl}} [\mathrm{Cl}^-]_{\mathrm{in}}}{P_{\mathrm{K}} [\mathrm{K}^+]_{\mathrm{in}} + P_{\mathrm{Na}} [\mathrm{Na}^+]_{\mathrm{in}} + P_{\mathrm{Cl}} [\mathrm{Cl}^-]_{\mathrm{out}}}.$$

## Remarks

Under the constant field assumption, the Nernst–Planck equation for each ion is a linear first-order equation in the position across the membrane.
Solving it gives the flux of each ion as an explicit function of $V$ (the Goldman–Hodgkin–Katz current equation).
Adding the currents of the three ions and setting the sum to zero gives the formula; the anion appears with inside and outside swapped because its charge is $-1$.
If only one permeability is nonzero, say $P_{\mathrm{Na}} = P_{\mathrm{Cl}} = 0$, the formula reduces to the [[Nernst equation|B9JD74Y5C3]] for potassium.
At rest a typical neuron has $P_{\mathrm{K}} : P_{\mathrm{Na}} : P_{\mathrm{Cl}}$ roughly $1 : 0.05 : 0.45$, which gives a potential near $-70$ mV, between the potassium and sodium reversal potentials.
The formula as written holds only for monovalent ions; ions of other valences such as $\mathrm{Ca}^{2+}$ lead to a different equation.

## Explanations

### L1 human

A real membrane lets several kinds of ions through, each pulling the voltage towards its own Nernst potential.
The Goldman equation says where the tug of war ends: at a weighted logarithmic average, with weights given by how easily each ion crosses.
The ion with the largest permeability wins the most.

### L2 human

At rest the membrane is mostly permeable to potassium, so the resting potential lies close to the potassium Nernst potential.
During an action potential the sodium permeability rises sharply, and the Goldman equation predicts a swing of the voltage toward the sodium Nernst potential.
This is the steady-state counterpart of the current-based description in the Hodgkin–Huxley model.
