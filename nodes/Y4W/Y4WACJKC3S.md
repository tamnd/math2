---
tag: Y4WACJKC3S
kind: definition
name: Attainable null space
msc: [46-XX]
defines: RK2N3QP4FQ
sources:
  - arxiv: 2610.14906v1
    locator: Definition 3.1
    mention: ax://paper/2610.14906#2P92
    licence: cc-by
    note: the paper that states the item (corpus arxiv AX9.2)
history:
  notes: The source is arXiv:2610.14906v1 (2026-10), by Michael Unser. A paper also restates older results, so this is not the first statement until a person or a later pass confirms it.
inventory: [6YTCGV56SP]
uses: [FP5GVCN8GV, CG9JEATW3Q, AES2T5JPFP]
---

## Definition

Let $\mathcal{S}$ be the [[Schwartz space|CG9JEATW3Q]], and let $\mathcal{S}'$ be the space of its [[tempered distributions|AES2T5JPFP]]. Give $\mathcal{S}'$ the topology of convergence against each element of $\mathcal{S}$.

Let $q$ be a continuous [[seminorm|FP5GVCN8GV]] on $\mathcal{S}$.

The **attainable null space** of $q$ is the set

$$\mathcal{N}_q = \{\, p \in \mathcal{S}' : p = \lim_{k} \chi_k \text{ in } \mathcal{S}' \text{ for some sequence } (\chi_k) \subset \mathcal{S} \text{ with } q(\chi_k) \to 0 \,\}.$$

Let $\mathrm{B} \colon \mathcal{S} \to \mathcal{S}'$ be a positive-semi-definite operator. This means that $\langle \mathrm{B}\varphi, \varphi \rangle$ is real and nonnegative for every $\varphi \in \mathcal{S}$.

The seminorm induced by $\mathrm{B}$ is $|\varphi|_{\mathrm{B}} = \langle \mathrm{B}\varphi, \varphi \rangle^{1/2}$.

For this case, $\mathcal{N}_{\mathrm{B}}$ denotes the attainable null space of $|\cdot|_{\mathrm{B}}$.
