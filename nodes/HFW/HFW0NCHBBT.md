---
tag: HFW0NCHBBT
kind: statement
role: theorem
name: Mukai's Theorem
sources:
  - wikipedia: en:7045490@r1353719203
    locator: Dual abelian variety, section Mukai's Theorem
    note: adopted
    mention: wikipedia://en/7045490#RXRX
    sections: [Statement]
inventory: [2F6RCBFXK4]
---

## Statement

A celebrated theorem of Mukai states that there is an isomorphism of derived categories $D^b(A) \cong D^b(A^\vee)$, where $D^b(X)$ denotes the bounded derived category of coherent sheaves on *X*. Historically, this was the first use of the Fourier-Mukai transform and shows that the bounded derived category cannot necessarily distinguish non-isomorphic varieties.

Recall that if *X* and *Y* are varieties, and $\mathcal{K} \in D^b(X \times Y)$ is a complex of coherent sheaves, we define the **Fourier-Mukai transform** $\Phi^{X \to Y}_{\mathcal{K}}: D^b(X) \to D^b(Y)$ to be the composition $\Phi^{X \to Y}_{\mathcal{K}}(\cdot) = Rq_*(\mathcal{K} \otimes_L Lp^*(\cdot))$, where *p* and *q* are the projections onto *X* and *Y* respectively.

Note that $p$ is flat and hence $p^*$ is exact on the level of coherent sheaves, and in applications $\mathcal{K}$ is often a line bundle so one may usually leave the left derived functors underived in the above expression. Note also that one can analogously define a Fourier-Mukai transform $\Phi_{\mathcal{K}}^{Y \to X}$ using the same kernel, by just interchanging the projection maps in the formula.

The statement of Mukai's theorem is then as follows.
