---
tag: DTGW5YRMAE
kind: statement
role: theorem
name: LSZ reduction formula
msc: [81U20, 81T05]
uses: [YDC9XBJDE1, AYCCDQWCJF, K9SR95P4NJ]
about: [YDC9XBJDE1]
sources:
  - url: https://en.wikipedia.org/wiki/LSZ_reduction_formula
same_as:
  wikidata: Q267449
  wikipedia: LSZ reduction formula
---

## Statement

Let $\phi$ be a Hermitian scalar field on Minkowski space with signature $(+,-,-,-)$, vacuum $\lvert \Omega \rangle$ and $\langle \Omega \rvert \phi(x) \lvert \Omega \rangle = 0$.
Assume its spectrum has an isolated one-particle mass shell of mass $m > 0$.
Let $\lvert k \rangle$ be the one-particle states, with $\langle k \rvert \phi(x) \lvert \Omega \rangle = \sqrt{Z}\, e^{ik\cdot x}$ for a constant $Z > 0$.
Let $k_1, \dots, k_r$ be incoming and $p_1, \dots, p_s$ outgoing momenta on the mass shell, with no $p_i$ equal to any $k_j$.
Assume that $\phi$ tends, in the weak sense, to $\sqrt{Z}$ times free in- and out-fields as $t \to \mp\infty$.
Then the [[S-matrix|YDC9XBJDE1]] element is
$$\langle p_1 \dots p_s; \text{out} \vert k_1 \dots k_r; \text{in} \rangle = \left(\frac{i}{\sqrt{Z}}\right)^{r+s} \int \prod_{j=1}^{r} d^4y_j \, e^{-ik_j \cdot y_j} (\square_{y_j} + m^2) \prod_{i=1}^{s} d^4x_i \, e^{ip_i \cdot x_i} (\square_{x_i} + m^2) \; G(x, y).$$
Here $\square = \partial_t^2 - \nabla^2$ and $G(x, y) = \langle \Omega \rvert T\{\phi(x_1)\cdots\phi(x_s)\phi(y_1)\cdots\phi(y_r)\} \lvert \Omega \rangle$.

## Remarks

The idea of the proof: write the creation operator of an in-particle as a limit as $t \to -\infty$.
The limit is taken of an integral over space of the field against a positive-energy solution of the [[Klein–Gordon equation|AYCCDQWCJF]].
The difference between the limits at $t = +\infty$ and $t = -\infty$ is an integral of a total time derivative, which equals the integral of $(\square + m^2)\phi$.
Repeating this for each particle and time-ordering the fields gives the formula.

In momentum space the formula says: Fourier transform $G$, multiply by $(p^2 - m^2)$ for each external leg, and take the limit to the mass shell.
Only the parts of $G$ with a pole $i\sqrt{Z}/(p^2 - m^2)$ in each external momentum survive.
In perturbation theory this is the rule that amputates the external [[propagators|K9SR95P4NJ]] of Feynman diagrams.
The rigorous form, in the Wightman framework, is Haag–Ruelle scattering theory.

## Explanations

### L1 human

Experiments measure scattering: particles come in, collide and fly out.
Theory most easily computes correlation functions of fields.
The LSZ formula is the bridge: it turns correlation functions into scattering amplitudes.

### L2 human

LSZ is why one computes time-ordered correlation functions in quantum field theory.
It needs the field only to create the particle from the vacuum with nonzero amplitude, so any such field, even a composite one, gives the same S-matrix.
The factor $\sqrt{Z}$ for each leg is the field strength renormalization, so the formula also explains how renormalized fields enter scattering amplitudes.
