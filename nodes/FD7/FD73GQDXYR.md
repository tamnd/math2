---
tag: FD73GQDXYR
kind: statement
role: theorem
name: Thévenin's theorem
msc: [94C05]
uses: [9B0V41V2F8, 8FDMEJ4VRH]
about: [9B0V41V2F8]
sources:
  - url: https://en.wikipedia.org/wiki/Th%C3%A9venin%27s_theorem
same_as:
  wikidata: Q241868
  wikipedia: Thévenin's theorem
---

## Statement

Let $N$ be a circuit of linear resistors and independent sources, with two distinguished nodes $a$ and $b$, the terminals.
Connect an external current source that drives a current $i$ into $N$ at $a$ and draws it out at $b$.
Let $v = \varphi(a) - \varphi(b)$ be the voltage across the terminals, where $\varphi$ is the node potential.
Assume that for every $i \in \R$ the resulting circuit has exactly one solution of [[Kirchhoff's circuit laws|9B0V41V2F8]] and the element laws.
Then there are real numbers $V_{\mathrm{th}}$ and $R_{\mathrm{th}}$ such that
$$v = V_{\mathrm{th}} + R_{\mathrm{th}} \, i \quad \text{for all } i \in \R.$$
Here $V_{\mathrm{th}}$ is the open-circuit voltage, the value of $v$ at $i = 0$.
The number $R_{\mathrm{th}}$ is the terminal voltage for $i = 1$ when all independent sources of $N$ are set to zero.

## Remarks

By the [[superposition theorem|8FDMEJ4VRH]], $v$ is a linear function of the internal source values and of $i$.
The part coming from the internal sources is $V_{\mathrm{th}}$, and the part coming from $i$ is $R_{\mathrm{th}} i$.
So, seen from the terminals, $N$ behaves exactly like a voltage source $V_{\mathrm{th}}$ in series with a resistor $R_{\mathrm{th}}$.
Example: let a battery $E$ in series with a resistor $r_1 > 0$ join $b$ to $a$, and let a resistor $r_2 > 0$ also join $a$ and $b$.
This voltage divider has $V_{\mathrm{th}} = E r_2 / (r_1 + r_2)$ and $R_{\mathrm{th}} = r_1 r_2 / (r_1 + r_2)$.
The hypothesis matters: an ideal current source between $a$ and $b$ fixes the terminal current, so the circuit has no solution for most $i$ and no Thévenin equivalent exists.
With capacitors and inductors in sinusoidal steady state, the same holds with complex amplitudes and a complex impedance $Z_{\mathrm{th}}$.

## Explanations

### L1 human

However complicated a linear circuit is, from the outside it looks like one battery with one resistor in series.
To find the battery voltage, measure the voltage at the terminals with nothing attached.
To find the resistance, switch off all the sources inside and measure the resistance between the terminals.

### L2 human

Thévenin's theorem lets you replace the fixed part of a circuit by two numbers and then study many different loads quickly.
It is the dual of [[Norton's theorem|Y24JQJPVX3]], which uses a current source in parallel with a resistor.
It gives the setting of the [[maximum power transfer theorem|B4YK5AE501]].
The resistance $R_{\mathrm{th}}$ is the effective resistance between $a$ and $b$ of the network of resistors.
