---
tag: SM0D3C0A2C
kind: statement
role: proposition
name: Reisner's criterion
sources:
  - wikipedia: en:24394535@r1367373436
    locator: Stanley–Reisner ring, section Cohen–Macaulay condition and the upper bound conjecture > Reisner's criterion
    note: adopted
    mention: wikipedia://en/24394535#KS3V
    sections: [Statement]
inventory: [E76ZVD5RCM]
---

## Statement

A simplicial complex Δ is Cohen–Macaulay over **k** if and only if for all simplices *σ* ∈ Δ, all reduced simplicial homology groups of the link of *σ* in Δ with coefficients in **k** are zero, except the top dimensional one:

$$\tilde{H}_{i}(\operatorname{link}_\Delta(\sigma); k)=0\quad \text{for all} \quad i<\dim \operatorname{link}_\Delta(\sigma).$$

A result due to Munkres then shows that the Cohen–Macaulayness of Δ over **k** is a [[topological property|02SMVGC690]]: it depends only on the [[homeomorphism|0QT00PB5G2]] class of the simplicial complex Δ. Namely, let |Δ| be the geometric realization of Δ. Then the vanishing of the simplicial homology groups in Reisner's criterion is equivalent to the following statement about the reduced and relative singular homology groups of |Δ|:

$$\text{For all } p\in|\Delta|\text{ and for all } i<\dim |\Delta| = d-1, \quad \tilde{H}_i(\operatorname |\Delta|; k) = H_i(\operatorname |\Delta|, \operatorname |\Delta| - p; k) = 0.$$

In particular, if the complex Δ is a simplicial sphere, that is, |Δ| is homeomorphic to a sphere, then it is Cohen–Macaulay over any field. This is a key step in Stanley's proof of the Upper Bound Conjecture. By contrast, there are examples of simplicial complexes whose Cohen–Macaulayness depends on the characteristic of the field **k**.
