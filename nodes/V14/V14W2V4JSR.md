---
tag: V14W2V4JSR
kind: statement
role: fact
name: First law of thermodynamics
msc: [80A05, 80A10]
uses: [GYNNJBMTCP, F6JVQ12X43, CY4GJQGF06, S8H21RWQ86, T8J5XRYBZZ]
about: [F6JVQ12X43]
sources:
  - url: https://en.wikipedia.org/wiki/First_law_of_thermodynamics
same_as:
  wikidata: Q179380
  wikipedia: First law of thermodynamics
---

## Statement

Let a closed [[thermodynamic system|GYNNJBMTCP]] pass by some process from an equilibrium state $A$ to an equilibrium state $B$.
Let $Q$ be the [[heat|CY4GJQGF06]] supplied to the system and let $W$ be the [[work|S8H21RWQ86]] done by the system during the process.
Then there is a [[state function|T8J5XRYBZZ]] $U$, the [[internal energy|F6JVQ12X43]], such that
$$U(B) - U(A) = Q - W.$$
In particular, $Q - W$ depends only on the states $A$ and $B$ and not on the process that joins them.
For an infinitesimal process this reads $dU = \delta Q - \delta W$, where $\delta Q$ and $\delta W$ are small amounts of heat and work that are not differentials of state functions.

## Remarks

The first law is a law of nature, not a theorem: it expresses the conservation of energy for thermodynamic systems.
Its experimental basis is that the work needed to take an adiabatically enclosed system from $A$ to $B$ does not depend on the way it is done.
This fixes $U$ up to an additive constant, and then the heat of any process is $Q = U(B) - U(A) + W$.
For a cycle, $A = B$, so the net heat taken in equals the net work done.
For example, the internal energy of an ideal gas depends only on its temperature.
So in an isothermal expansion $U(B) = U(A)$, and the gas gives out as work exactly the heat it takes in.
Some books let $W$ be the work done on the system; then the law reads $U(B) - U(A) = Q + W$.

## Explanations

### L1 human

Energy is not created or destroyed, it only changes form.
A system can gain energy by being heated, and it can lose energy by doing work, for example by pushing a piston.
The change of its stored energy is what came in as heat minus what went out as work.
So no engine can run in a cycle and give out work without taking in at least as much energy.

### L2 human

The first law turns the internal energy $U$ into a state function, while heat and work are quantities of a process.
In a quasistatic process of a fluid with pressure $p$ and volume $V$, the work is $\delta W = p \, dV$, so $dU = \delta Q - p \, dV$.
Combined with the second law, which gives $\delta Q = T \, dS$ for reversible processes, it yields the fundamental relation $dU = T \, dS - p \, dV$.
At constant volume the heat taken in equals the change of $U$; this is how heat capacities at constant volume are measured.
