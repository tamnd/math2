---
tag: TYJWPFGZ2C
kind: definition
name: Topological cyclic homology
msc: [19D55, 55P42, 55P91]
defines: 6RQS843SE5
uses: [PFW77RAAY3, BAW0T68GWK, 04EAFVFTF7]
sources:
  - url: https://en.wikipedia.org/wiki/Topological_Hochschild_homology
---

## Definition

Let $R$ be a connective associative [[ring spectrum|BAW0T68GWK]], and let $T$ be the [[circle group|04EAFVFTF7]].
Let $X = THH(R)$ be its [[topological Hochschild homology|PFW77RAAY3]], with its $T$-action.
For a group $G$ acting on a spectrum $Y$, write $Y^{hG}$ for the homotopy fixed points.
For finite $G$, write $Y^{tG}$ for the Tate construction, the cofiber of the norm map $Y_{hG} \to Y^{hG}$.
The spectrum $X$ is cyclotomic: for each prime $p$ there is a $T$-equivariant Frobenius map $\varphi_p \colon X \to X^{tC_p}$, where $C_p \subseteq T$ is the subgroup of order $p$.
Applying $(-)^{hT}$ gives maps $\varphi_p^{hT} \colon X^{hT} \to (X^{tC_p})^{hT}$.
There are also canonical maps $\mathrm{can}_p \colon X^{hT} \to (X^{tC_p})^{hT}$.
The *topological cyclic homology* of $R$ is the fiber
$$TC(R) = \operatorname{fib}\Big( X^{hT} \xrightarrow{\ (\varphi_p^{hT} - \mathrm{can}_p)_p\ } \prod_p (X^{tC_p})^{hT} \Big).$$

## Remarks

This formula is due to Nikolaus and Scholze.
It recovers, in the $p$-complete setting, the original definition of Bökstedt, Hsiang and Madsen as a homotopy limit of fixed point spectra of $THH(R)$ under restriction and Frobenius maps.
The spectrum $X^{hT}$ is also written $TC^-(R)$.
Example: after $p$-completion, $\pi_* TC(\mathbb{F}_p)$ is $\Z_p$ in degrees $0$ and $-1$ and zero otherwise.
Non-example: $TC$ is not algebraic K-theory, since $\pi_{-1} TC(\mathbb{F}_p)^\wedge_p \neq 0$, while the K-theory of a ring has no negative homotopy in this case.
