---
tag: SKYARQEH3R
kind: definition
name: Quantum chromodynamics
msc: [81V05, 81T13]
defines: SEE8XD0APW
uses: [M71M5DQY86, CZCWFPNS4N, XNZX7VXXR2, TDPX0D7ZD0, SANYJGZ311]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_chromodynamics
---

## Definition

Work on Minkowski space $\R^{1,3}$ with signature $(+,-,-,-)$ and units $\hbar = c = 1$.
Let $\gamma^\mu$ be the [[gamma matrices|TDPX0D7ZD0]].
Let $N_f \ge 1$ be the number of quark flavours, with masses $m_1, \dots, m_{N_f} \ge 0$, and let $g > 0$ be the strong coupling constant.
The fields are:

1. a gluon field $A_\mu$, with values in the traceless Hermitian $3 \times 3$ matrices, the Lie algebra of [[$SU(3)$|CZCWFPNS4N]] times $i$;
2. for each flavour $f$, a quark field $\psi_f$, a Dirac spinor with values in $\C^4 \otimes \C^3$, where $SU(3)$ acts on $\C^3$ by matrix multiplication.

*Quantum chromodynamics* is the quantization of the [[Yang–Mills theory|A0J2688KZF]] with gauge group $SU(3)$ and these quarks, with [[Lagrangian density|SANYJGZ311]]
$$\mathcal{L} = \sum_{f=1}^{N_f} \bar\psi_f \left( i\gamma^\mu D_\mu - m_f \right) \psi_f - \frac{1}{2} \mathrm{tr}\left( F_{\mu\nu} F^{\mu\nu} \right),$$
where $D_\mu = \partial_\mu - i g A_\mu$ and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu - i g [A_\mu, A_\nu]$.

## Remarks

Gauge invariance: for a function $U$ with values in $SU(3)$, the transformation $\psi_f \mapsto U\psi_f$, $A_\mu \mapsto U A_\mu U^{-1} - \frac{i}{g} (\partial_\mu U) U^{-1}$ gives $D_\mu \psi_f \mapsto U D_\mu \psi_f$ and $F_{\mu\nu} \mapsto U F_{\mu\nu} U^{-1}$.
So each term of $\mathcal{L}$ is unchanged, because the trace is invariant under conjugation.
In a basis $T^a$ of the Hermitian traceless matrices with $\mathrm{tr}(T^a T^b) = \frac12 \delta^{ab}$, the gluon term is $-\frac14 F^a_{\mu\nu} F^{a\,\mu\nu}$, with $8$ gluon fields $A^a_\mu$.

Non-example: replacing $SU(3)$ by $U(1)$ gives a theory of the form of [[quantum electrodynamics|M85BQEPQ7B]], whose gauge field has no self-interaction, because the commutator term in $F_{\mu\nu}$ vanishes.

In nature $N_f = 6$, with the up, down, strange, charm, bottom and top quarks.
The theory is asymptotically free when $N_f \le 16$, as found by Gross, Wilczek and Politzer in 1973.
A rigorous construction of QCD is open, like the [[Yang–Mills existence problem|VXC1Y32FD6]].
