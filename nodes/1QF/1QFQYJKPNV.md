---
tag: 1QFQYJKPNV
kind: statement
role: theorem
name: Tsirelson's bound
msc: [81P40, 81P05]
uses: [HM2HHE3J51, EY0X2NKA3S, 0NEGN5CRSC, V1JTB52E8C, Y7W23FTBK5]
about: [Y7W23FTBK5]
sources:
  - url: https://en.wikipedia.org/wiki/Tsirelson%27s_bound
same_as:
  wikidata: Q56324150
  wikipedia: Tsirelson's bound
---

## Statement

Let $\mathcal{H}_A$ and $\mathcal{H}_B$ be complex [[Hilbert spaces|HM2HHE3J51]].
Let $A_0, A_1$ be bounded [[self-adjoint operators|0NEGN5CRSC]] on $\mathcal{H}_A$ and $B_0, B_1$ bounded self-adjoint operators on $\mathcal{H}_B$, all of operator norm at most $1$.
Let $\rho$ be a [[density operator|V1JTB52E8C]] on the [[tensor product|EY0X2NKA3S]] $\mathcal{H}_A \otimes \mathcal{H}_B$, and put
$$C = A_0 \otimes (B_0 + B_1) + A_1 \otimes (B_0 - B_1).$$
Then $\abs{\tr(\rho C)} \le 2\sqrt{2}$.
The bound is attained for $\mathcal{H}_A = \mathcal{H}_B = \C^2$.

## Remarks

By convexity it is enough to treat a pure state, a unit vector $\psi$.
Put $x_i = (A_i \otimes I)\psi$ and $y_j = (I \otimes B_j)\psi$, vectors of norm at most $1$.
Since the operators are self-adjoint, $\langle \psi, C\psi \rangle = \langle x_0, y_0 + y_1 \rangle + \langle x_1, y_0 - y_1 \rangle$.
By the Cauchy–Schwarz inequality, its modulus is at most $\norm{y_0 + y_1} + \norm{y_0 - y_1} \le \sqrt{2}\,\big(2\norm{y_0}^2 + 2\norm{y_1}^2\big)^{1/2} \le 2\sqrt{2}$.
Example: let $\psi = (e_0 \otimes e_0 + e_1 \otimes e_1)/\sqrt2$, $A_0 = Z$, $A_1 = X$, $B_0 = (Z + X)/\sqrt2$ and $B_1 = (Z - X)/\sqrt2$, with $X, Z$ Pauli matrices.
Then $B_0 + B_1 = \sqrt2\, Z$ and $B_0 - B_1 = \sqrt2\, X$, so $C = \sqrt2\,(Z \otimes Z + X \otimes X)$.
Since $\langle \psi, (Z \otimes Z)\psi \rangle = \langle \psi, (X \otimes X)\psi \rangle = 1$, this gives $\langle \psi, C\psi \rangle = 2\sqrt{2}$.
Without the norm bound on the operators there is no bound at all, since scaling them scales $C$.

## Explanations

### L1 human

The [[CHSH inequality|Y7W23FTBK5]] says that a certain combination of correlations is at most $2$ when outcomes are fixed in advance.
Quantum mechanics can exceed $2$, but not by an arbitrary amount: the combination is at most $2\sqrt{2}$, about $2.83$.
This is Tsirelson's bound, and a pair of entangled qubits already reaches it.

### L2 human

Boris Tsirelson proved the bound in 1980.
When $A_i^2 = I$ and $B_j^2 = I$, one also has $C^2 = 4I - [A_0, A_1] \otimes [B_0, B_1]$, whose norm is at most $8$, giving another proof.
The gap between $2\sqrt2$ and the algebraic maximum $4$ shows that quantum correlations are limited even though they are nonlocal.
Upper bounds on the quantum maximum of other Bell expressions can be computed by semidefinite programming.
