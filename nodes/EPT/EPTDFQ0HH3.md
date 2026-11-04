---
tag: EPTDFQ0HH3
kind: proof
name: Proof of Selberg trace formula for compact hyperbolic surfaces
proves: 7CHW554E10
sources:
  - wikipedia: en:981694@r1371813961
    locator: Selberg trace formula, section The general Selberg trace formula for cocompact quotients > Proof
    note: adopted
    mention: wikipedia://en/981694#I01Z
    sections: [Proof]
---

## Proof

Define the following operator on compactly supported functions on $\Gamma\backslash G$:

$$R(\phi) = \int_G \phi(x)R(x)\,dx.$$

It extends continuously to $L^2(\Gamma\setminus G)$ and for $f\in L^2(\Gamma\setminus G)$ we have:

$$(R(\phi)f)(x) = \int_G\phi(y)f(xy)\,dy = \int_{\Gamma\setminus G}\left(\sum_{\gamma\in\Gamma}\phi(x^{-1}\gamma y)\right)f(y)\,dy$$

after a change of variables. Assuming $\Gamma\setminus G$ is compact, the operator $R(\phi)$ is trace-class and the trace formula is the result of computing its trace in two ways as explained below.

The trace of $R(\phi)$can be expressed as the integral of the kernel $K(x,y)=\sum_{\gamma\in\Gamma}\phi(x^{-1}\gamma y)$ along the diagonal, that is:

$$\operatorname{tr}R(\phi) = \int_{\Gamma\setminus G}\sum_{\gamma\in\Gamma}\phi(x^{-1}\gamma x)\,dx.$$

Let $\{\Gamma\}$ denote a collection of representatives of conjugacy classes in $\Gamma$, and $\Gamma^\gamma$ and $G^\gamma$ the respective centralizers of $\gamma$. Then the above integral can, after manipulation, be written

$$\operatorname{tr}R(\phi) = \sum_{\gamma\in\{\Gamma\}} a_\Gamma^G(\gamma)\int_{G^\gamma\setminus G}\phi(x^{-1}\gamma x)\,dx.$$

This gives the *geometric side* of the trace formula.

The *spectral side* of the trace formula comes from computing the trace of $R(\phi)$ using the decomposition of the regular representation of $G$ into its irreducible components. Thus

$$\operatorname{tr}R(\phi) = \sum_{\pi\in\hat G}a_\Gamma^G(\pi)\operatorname{tr}\pi(\phi)$$

where $\hat G$ is the set of irreducible unitary representations of $G$ (recall that the positive integer $a_\Gamma^G(\pi)$ is the multiplicity of $\pi$ in the unitary representation $R$ on $L^2(\Gamma\setminus G)$).
