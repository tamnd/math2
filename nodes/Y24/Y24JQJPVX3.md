---
tag: Y24JQJPVX3
kind: statement
role: theorem
name: Norton's theorem
msc: [94C05]
uses: [FD73GQDXYR, 8FDMEJ4VRH]
about: [FD73GQDXYR]
sources:
  - url: https://en.wikipedia.org/wiki/Norton%27s_theorem
same_as:
  wikidata: Q651593
  wikipedia: Norton's theorem
---

## Statement

Let $N$ be a circuit of linear resistors and independent sources with terminals $a$ and $b$ that satisfies the hypotheses of [[Thévenin's theorem|FD73GQDXYR]].
So $v = V_{\mathrm{th}} + R_{\mathrm{th}} i$ for the terminal voltage $v$ and the current $i$ driven into $a$ and out of $b$.
Assume $R_{\mathrm{th}} \ne 0$.
Put $R_{\mathrm{N}} = R_{\mathrm{th}}$ and $I_{\mathrm{N}} = V_{\mathrm{th}} / R_{\mathrm{th}}$.
Then
$$i = \frac{v}{R_{\mathrm{N}}} - I_{\mathrm{N}} \quad \text{for all } i \in \R,$$
so $N$ behaves at its terminals like a current source $I_{\mathrm{N}}$ in parallel with a resistor $R_{\mathrm{N}}$.
The number $I_{\mathrm{N}}$ is the short-circuit current: the current that flows out of $a$ through a wire joining $a$ to $b$.

## Remarks

The formula is Thévenin's relation solved for $i$, which needs $R_{\mathrm{th}} \ne 0$.
Setting $v = 0$ gives $i = -I_{\mathrm{N}}$, which is the short-circuit statement.
Example: a battery $E$ in series with a resistor $r$ has $V_{\mathrm{th}} = E$ and $R_{\mathrm{th}} = r$, so $I_{\mathrm{N}} = E / r$, the current through a short across the terminals.
When $R_{\mathrm{th}} = 0$, as for an ideal voltage source, there is no Norton equivalent.
The conversion between the two forms is called a source transformation.

## Explanations

### L1 human

Norton's theorem is the twin of Thévenin's theorem.
Instead of a battery with a resistor in series, it replaces the circuit by a constant current source with a resistor beside it.
Both pictures give the same voltage and current at the terminals for every load.

### L2 human

The Norton form is convenient for loads in parallel, because conductances in parallel add.
In [[nodal analysis|9NW7KCBSME]], voltage sources with series resistors are often first turned into Norton form, so that all sources become current sources.
