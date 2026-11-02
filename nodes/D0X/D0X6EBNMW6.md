---
tag: D0X6EBNMW6
kind: definition
name: Chromatic homotopy theory
msc: [55P42, 55Q51, 55P60]
defines: 300V40FC1B
uses: [1GHF4EKBXS, 26GTNMAF7B, S8S72AA9C8, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Chromatic_homotopy_theory
---

## Definition

Fix a [[prime number|01826KMG2H]] $p$ and work with $p$-local [[spectra|1GHF4EKBXS]] in the [[stable homotopy category|26GTNMAF7B]].
For a spectrum $E$, a spectrum $X$ is *$E$-acyclic* if $E \wedge X \simeq 0$, and *$E$-local* if every map from an $E$-acyclic spectrum to $X$ is null.
The *Bousfield localization* $X \to L_E X$ is the map to an $E$-local spectrum whose fibre is $E$-acyclic; it exists and is unique up to equivalence.
For $n \ge 1$, let $E(n)$ be the Johnson–Wilson spectrum, with $\pi_* E(n) = \Z_{(p)}[v_1, \ldots, v_n, v_n^{-1}]$, a quotient of [[Brown–Peterson cohomology|S8S72AA9C8]] with $v_n$ inverted; let $E(0) = H\Q$.
Write $L_n = L_{E(n)}$.
Since $E(n-1)$-local spectra are $E(n)$-local, there are natural maps $L_n X \to L_{n-1} X$.
The *chromatic tower* of $X$ is
$$X \to \cdots \to L_n X \to L_{n-1} X \to \cdots \to L_0 X = X \wedge H\Q.$$
Let $K(n)$ be the $n$-th Morava K-theory, with $\pi_* K(n) = \mathbb{F}_p[v_n, v_n^{-1}]$ and $\abs{v_n} = 2(p^n - 1)$.
*Chromatic homotopy theory* is the study of spectra through their chromatic towers, their *monochromatic layers* $M_n X = \operatorname{fib}(L_n X \to L_{n-1} X)$, and their localizations $L_{K(n)} X$.

## Remarks

Example: for the $p$-local sphere spectrum $S$, the layer $L_0 S = H\Q$ records the rational stable homotopy, which is $\Q$ in degree $0$ only.
The layer $L_1 S$ is computed from K-theory and contains the image of the J-homomorphism.

Non-example: the Eilenberg–MacLane spectrum $H\mathbb{F}_p$ is not $E(n)$-local for any $n$.
Indeed $E(n) \wedge H\mathbb{F}_p \simeq 0$, so $H\mathbb{F}_p$ is a nonzero $E(n)$-acyclic spectrum, and its identity map is not null.
So all terms of its chromatic tower vanish.

By the chromatic convergence theorem of Hopkins and Ravenel, a finite $p$-local spectrum is the homotopy limit of its chromatic tower.
The example of $H\mathbb{F}_p$ shows that this fails without finiteness.
