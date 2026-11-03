---
tag: TY49WH2PPB
kind: statement
role: fact
name: Principle of maximum entropy in thermodynamics
msc: [80A05, 80A10]
uses: [GYNNJBMTCP, 5EKTEE00FZ, SPY89W0RJ7, F6JVQ12X43, T11MGWEKJ3]
about: [SPY89W0RJ7, 5EKTEE00FZ]
sources:
  - url: https://en.wikipedia.org/wiki/Principle_of_maximum_entropy
---

## Statement

Let an isolated composite [[thermodynamic system|GYNNJBMTCP]] have fixed total [[internal energy|F6JVQ12X43]] $U$, total volume $V$ and total amounts of substance $N$.
Let $x$ denote the internal variables that are left free after some internal constraints are removed, such as the energies or volumes of the subsystems.
Then in [[equilibrium|5EKTEE00FZ]] the values of $x$ maximise the total [[entropy|SPY89W0RJ7]] $S(U, V, N; x)$.
The maximum is over all values of $x$ compatible with the fixed totals.

## Remarks

The principle follows from the [[second law|T11MGWEKJ3]].
After a constraint is removed, the spontaneous processes in the isolated system can only increase $S$, so the system settles where $S$ can increase no further.
Example: two subsystems that can exchange energy only, with entropies $S_1(U_1)$ and $S_2(U_2)$ and $U_1 + U_2 = U$.
Maximising $S_1(U_1) + S_2(U - U_1)$ gives $S_1'(U_1) = S_2'(U_2)$, that is, $1/T_1 = 1/T_2$, so the temperatures become equal.
This thermodynamic principle is distinct from the maximum entropy principle of statistical inference due to Jaynes, which is the subject of the source article.

## Explanations

### L1 human

Leave an isolated system alone and it ends up in the state of highest entropy that its fixed energy and volume allow.
That is why heat spreads until the temperature is uniform.

### L2 human

The maximum entropy principle is the starting point of equilibrium thermodynamics in the style of Callen.
Setting the first variation of $S$ to zero gives the equilibrium conditions: equal temperatures, equal pressures and equal chemical potentials.
The second variation being negative gives the stability conditions, such as positive heat capacity.
