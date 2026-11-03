---
tag: HGK2QVG790
kind: statement
role: proposition
name: Millman's theorem
msc: [94C05]
uses: [9B0V41V2F8]
about: [9B0V41V2F8]
sources:
  - url: https://en.wikipedia.org/wiki/Millman%27s_theorem
same_as:
  wikidata: Q588736
  wikipedia: Millman's theorem
---

## Statement

Let $n \ge 1$, and let two nodes $a$ and $b$ be joined by $n$ parallel branches and nothing else.
For $k = 1, \dots, n$, branch $k$ is an ideal voltage source $E_k \in \R$ in series with a resistor $R_k > 0$.
Each source is oriented so that it raises the potential from $b$ to $a$.
Then the voltage $V = \varphi(a) - \varphi(b)$ between the two nodes is
$$V = \frac{\sum_{k=1}^{n} E_k / R_k}{\sum_{k=1}^{n} 1 / R_k}.$$

## Remarks

The current flowing from the source side into node $a$ through branch $k$ is $(E_k - V)/R_k$ by Ohm's law.
The current law of [[Kirchhoff's circuit laws|9B0V41V2F8]] at $a$ gives $\sum_k (E_k - V)/R_k = 0$, and solving for $V$ gives the formula.
So $V$ is the weighted mean of the source voltages with weights the conductances $1/R_k$.
A branch with only a resistor counts with $E_k = 0$.
Example: two batteries of $12$ and $6$ volts, each with internal resistance $1$ ohm, in parallel give $V = (12 + 6)/2 = 9$ volts.
The same formula holds for complex amplitudes and impedances in sinusoidal steady state.

## Explanations

### L1 human

When several batteries with internal resistances are connected side by side, the common voltage is an average of their voltages.
Batteries with lower resistance pull the average harder towards their own voltage.

### L2 human

Millman's theorem is the simplest case of [[nodal analysis|9NW7KCBSME]]: there is a single unknown node voltage.
It also follows from the Norton form of each branch: the source currents $E_k / R_k$ add, the conductances add, and the voltage is their quotient.
