---
tag: SV5EEBF861
kind: definition
name: Cusp form
msc: [11F11]
defines: A50Y012RBP
uses: [GWKN5VG78A, VEKV1EM77B, 1H6R856P3C]
sources:
  - url: https://en.wikipedia.org/wiki/Cusp_form
---

## Definition

Let $k$ be an integer and let $f$ be a [[modular form|GWKN5VG78A]] of weight $k$ for the [[modular group|VEKV1EM77B]] $\mathrm{SL}_2(\Z)$, with $q$-expansion $f(\tau) = \sum_{n \ge 0} a_n q^n$, where $q = e^{2 \pi i \tau}$.
Then $f$ is a *cusp form* if $a_0 = 0$.
Equivalently, $f(\tau) \to 0$ as $\operatorname{Im} \tau \to \infty$.

## Remarks

For a [[congruence subgroup|1H6R856P3C]] $\Gamma$, a modular form $f$ for $\Gamma$ of weight $k$ is a cusp form if $(c\tau + d)^{-k} f(\gamma \tau) \to 0$ as $\operatorname{Im} \tau \to \infty$, for every $\gamma = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \in \mathrm{SL}_2(\Z)$.
Example: $\Delta = (E_4^3 - E_6^2) / 1728$ is a cusp form of weight $12$; the constant terms of $E_4^3$ and $E_6^2$ are both $1$, so they cancel.
Non-example: the [[Eisenstein series|EYREVY31BN]] $E_4 = 1 + 240 q + \cdots$ is a modular form but not a cusp form, since its constant term is $1$.
For $\mathrm{SL}_2(\Z)$, $S_k = 0$ for $k < 12$ and $S_{12} = \C \Delta$.
