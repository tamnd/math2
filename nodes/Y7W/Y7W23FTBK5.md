---
tag: Y7W23FTBK5
kind: statement
role: theorem
name: CHSH inequality
msc: [81P40, 81P05, 60A05]
uses: [059TJN0NZ1, QRW6NE1VY7]
about: [QRW6NE1VY7]
sources:
  - url: https://en.wikipedia.org/wiki/CHSH_inequality
same_as:
  wikidata: Q5011347
  wikipedia: CHSH inequality
---

## Statement

Let $(\Lambda, \mathcal{F}, \mu)$ be a [[probability space|059TJN0NZ1]].
Let $A_0, A_1, B_0, B_1 \colon \Lambda \to [-1, 1]$ be measurable functions.
Write $E(A_i B_j) = \int_\Lambda A_i B_j \, d\mu$.
Then
$$\abs{E(A_0 B_0) + E(A_0 B_1) + E(A_1 B_0) - E(A_1 B_1)} \le 2.$$

## Remarks

For each $\lambda \in \Lambda$, the integrand is $A_0(B_0 + B_1) + A_1(B_0 - B_1)$, evaluated at $\lambda$.
Its absolute value is at most $\abs{B_0 + B_1} + \abs{B_0 - B_1} = 2\max(\abs{B_0}, \abs{B_1}) \le 2$, and integrating gives the inequality.
In a local [[hidden-variable theory|QRW6NE1VY7]], $\lambda$ is the hidden variable and $A_i(\lambda)$, $B_j(\lambda)$ are the outcomes of measurement $i$ on one side and $j$ on the other.
The essential hypotheses are that one measure $\mu$ serves for all four pairs and that $A_i$ does not depend on $j$, nor $B_j$ on $i$.
Without them the bound fails: four independent pairs with correlations $1, 1, 1, -1$ give the value $4$.
Example: for the two-qubit state $(\lvert 00 \rangle + \lvert 11 \rangle)/\sqrt{2}$, suitable spin measurements give the value $2\sqrt{2}$, so the quantum correlations have no such model.

## Explanations

### L1 human

Two players, far apart, each get one of two questions and must answer $+1$ or $-1$.
If their answers are fixed in advance by shared instructions, a simple sum of four average products of answers can never exceed $2$.
Quantum particles that are entangled can push this sum up to about $2.83$.
So the inequality gives an experimental test that separates quantum mechanics from any theory with preassigned local answers.

### L2 human

The inequality was published by Clauser, Horne, Shimony and Holt in 1969, as a version of Bell's inequality suited to real experiments.
Its proof needs only boundedness of the outcomes, not perfect correlations.
The quantum maximum $2\sqrt{2}$ is [[Tsirelson's bound|1QFQYJKPNV]], and the algebraic maximum $4$ is reached by hypothetical nonlocal boxes.
The CHSH inequality is the key step in the usual proof of [[Bell's theorem|7X9M1G56VP]], and it is the basis of device-independent quantum cryptography.
