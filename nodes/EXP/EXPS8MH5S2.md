---
tag: EXPS8MH5S2
kind: definition
name: De Rham cohomology of varieties
msc: [14F40, 14F10]
defines: 13F5JZPDD0
uses: [5A35TYZD02, EXKGG9X6J0, 6VC6HQTFSA, RG6WFFW7K3, PQ6Q143ARJ]
sources:
  - url: https://en.wikipedia.org/wiki/K%C3%A4hler_differential
---

## Definition

Let $k$ be a field and let $X$ be a [[scheme|5A35TYZD02]] that is [[smooth|EXKGG9X6J0]] over $k$.
For $p \ge 0$ let $\Omega^p_{X/k} = \bigwedge^p \Omega^1_{X/k}$, where $\Omega^1_{X/k}$ is the [[sheaf of differentials|6VC6HQTFSA]], built from [[Kähler differentials|RG6WFFW7K3]].
The exterior derivative $d \colon \Omega^p_{X/k} \to \Omega^{p+1}_{X/k}$ is the unique $k$-linear map with $d(f) = df$ on functions, $d \circ d = 0$, and $d(\alpha \wedge \beta) = d\alpha \wedge \beta + (-1)^p \alpha \wedge d\beta$ for $\alpha$ of degree $p$.
The complex $\Omega^\bullet_{X/k} = (\Omega^0_{X/k} \to \Omega^1_{X/k} \to \Omega^2_{X/k} \to \cdots)$ is the *algebraic de Rham complex*.
The *algebraic de Rham cohomology* of $X$ is the hypercohomology $H^i_{\mathrm{dR}}(X/k) = \mathbb{H}^i(X, \Omega^\bullet_{X/k})$.
This is the $i$-th [[sheaf cohomology|PQ6Q143ARJ]] of the complex $\Omega^\bullet_{X/k}$, computed from an injective resolution of the complex.

## Remarks

If $X = \operatorname{Spec} A$ is affine, the sheaves $\Omega^p_{X/k}$ are quasi-coherent and have no higher cohomology.
Then $H^i_{\mathrm{dR}}(X/k)$ is the $i$-th cohomology of the complex of $A$-modules $\Omega^\bullet_{A/k}$.
Example: let $k$ have characteristic $0$ and $A = k[t, t^{-1}]$.
Then $\Omega^1_{A/k} = A \, dt$ and $d(t^n) = n t^{n-1} dt$.
The kernel of $d$ on $A$ is $k$, and the image of $d$ contains $t^m \, dt$ for every $m \ne -1$.
So $H^0_{\mathrm{dR}} = k$ and $H^1_{\mathrm{dR}}$ is spanned by the class of $dt/t$.
Non-example of good behaviour: if $k$ has characteristic $p > 0$ and $A = k[t]$, then $d(t^p) = 0$.
So $H^0_{\mathrm{dR}}(\mathbb{A}^1_k/k) = k[t^p]$ is infinite-dimensional, and the theory does not count connected components as in characteristic $0$.
Grothendieck's comparison theorem: if $X$ is smooth over $\C$, then $H^i_{\mathrm{dR}}(X/\C) \cong H^i(X(\C), \C)$ for all $i$.
