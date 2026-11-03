---
tag: 907YMZ4GPN
kind: statement
role: theorem
name: Holevo's theorem
msc: [81P45, 94A15, 81P17]
uses: [V1JTB52E8C, 33BRW6TMY4, H53TSRFWQ4, G11KFW51F6, 51898Y35PP]
about: [H53TSRFWQ4, 33BRW6TMY4]
sources:
  - url: https://en.wikipedia.org/wiki/Holevo%27s_theorem
same_as:
  wikidata: Q3984018
  wikipedia: Holevo's theorem
---

## Statement

Let $H$ be a complex Hilbert space of finite dimension $d$.
Let $X$ be a random variable with values in a finite set $\mathcal{X}$ and distribution $(p_x)_{x \in \mathcal{X}}$.
For each $x \in \mathcal{X}$ let $\rho_x$ be a [[density operator|V1JTB52E8C]] on $H$, and let $\rho = \sum_x p_x \rho_x$.
Let $\set{E_y}_{y \in \mathcal{Y}}$ be a [[POVM|33BRW6TMY4]] on $H$ with finite outcome set $\mathcal{Y}$.
Let $Y$ be the outcome of this measurement on $\rho_X$, so that $\Pr(Y = y \mid X = x) = \tr(E_y \rho_x)$.
Then the classical mutual information of $X$ and $Y$ satisfies
$$I(X : Y) \le \chi, \qquad \chi = S(\rho) - \sum_{x} p_x S(\rho_x),$$
where $S$ is the [[von Neumann entropy|H53TSRFWQ4]].
The quantity $\chi$ is the *Holevo quantity* of the ensemble $\set{p_x, \rho_x}$.

## Remarks

Proof idea: encode $X$ in the classical-quantum state $\sigma_{XQ} = \sum_x p_x \lvert x \rangle\langle x \rvert \otimes \rho_x$.
Its [[quantum mutual information|G11KFW51F6]] is $I(X:Q)_\sigma = \chi$.
The measurement is a quantum channel on $Q$ that turns $\sigma_{XQ}$ into the classical state of $(X, Y)$.
Quantum mutual information does not increase under local channels, a consequence of [[strong subadditivity|51898Y35PP]], so $I(X:Y) \le \chi$.

Since $\chi \le S(\rho) \le \log d$, at most $\log_2 d$ bits about $X$ can be read out of a $d$-dimensional system.
For $n$ qubits, $d = 2^n$, so $n$ qubits carry at most $n$ bits of accessible classical information.
Example: if the $\rho_x$ are pure states, then $\chi = S(\rho)$.
For the two non-orthogonal states $\lvert 0 \rangle$ and $\lvert + \rangle = (\lvert 0 \rangle + \lvert 1 \rangle)/\sqrt 2$ sent with probability $1/2$ each, $\chi = S(\rho) < 1$ bit, so they can never be told apart perfectly.

## Explanations

### L1 human

A quantum system can be prepared in infinitely many states, so one might hope to store unlimited information in one qubit.
Holevo's theorem says this hope fails when the information has to be read out.
The information that any measurement can extract is bounded by an entropy quantity.
For $n$ qubits the bound is $n$ bits, the same as for $n$ classical bits.

### L2 human

The Holevo quantity $\chi$ is the main tool for classical communication over quantum channels.
The Holevo–Schumacher–Westmoreland theorem shows that $\chi$, maximised over input ensembles, is achievable with many uses of a channel, so $\chi$ is the one-shot building block of the classical capacity.
The proof by monotonicity of mutual information is a typical use of strong subadditivity.
The bound $I(X:Y) \le \chi$ is usually strict; the maximum of $I(X:Y)$ over all measurements is called the accessible information.
