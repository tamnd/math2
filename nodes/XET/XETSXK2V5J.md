---
tag: XETSXK2V5J
kind: definition
name: Brown–Douglas–Fillmore theory
msc: [19K33, 46L80, 47A53]
defines: ZTDC9MC2Y4
uses: [6FE7JZ2VF1, 2WAZF1RV2Y, 2V9Q4KHY1T, 41XX3KF72X]
sources:
  - url: https://en.wikipedia.org/wiki/Calkin_algebra
---

## Definition

Let $H$ be a separable infinite-dimensional Hilbert space and $\mathcal{K}$ the [[ideal of compact operators|2WAZF1RV2Y]] on $H$.
Let $Q = B(H)/\mathcal{K}$ be the [[Calkin algebra|6FE7JZ2VF1]], and let $X$ be a compact metric space.
An *extension* of $C(X)$ by $\mathcal{K}$ is an injective unital $*$-homomorphism $\tau \colon C(X) \to Q$.
Two extensions $\tau_1, \tau_2$ are equivalent if there is a unitary $u \in B(H)$ with $\tau_2(f) = \pi(u) \tau_1(f) \pi(u)^*$ for all $f \in C(X)$, where $\pi \colon B(H) \to Q$ is the quotient map.
Let $\operatorname{Ext}(X)$ be the set of equivalence classes of extensions of $C(X)$ by $\mathcal{K}$.
*Brown–Douglas–Fillmore theory* is the study of $\operatorname{Ext}(X)$ with the addition
$$[\tau_1] + [\tau_2] = [\tau_1 \oplus \tau_2],$$
defined through an identification $H \oplus H \cong H$.

## Remarks

BDF proved that $\operatorname{Ext}(X)$ is an abelian group, with neutral element the class of the trivial extensions, those of the form $\pi \circ \rho$ for a unital $*$-homomorphism $\rho \colon C(X) \to B(H)$.
For $X \subseteq \C$ compact, $\operatorname{Ext}(X)$ is isomorphic to the group of integer-valued functions on the bounded components of $\C \setminus X$, through $[\tau] \mapsto \big(\lambda \mapsto \operatorname{ind}(T - \lambda)\big)$, where $T \in B(H)$ is any lift of $\tau(z)$.
Example: the unilateral shift $S$ gives the extension $\tau(z) = \pi(S)$ of $C(\mathbb{T})$; the [[Fredholm index|2V9Q4KHY1T]] of $S - 0$ is $-1$, so $[\tau] \ne 0$ in $\operatorname{Ext}(\mathbb{T}) \cong \Z$.
Example of the zero class: for a normal operator $N$ with $\sigma(N) = \sigma_{\mathrm{ess}}(N) = X$, the extension $f \mapsto \pi(f(N))$ is of the form $\pi \circ \rho$ with $\rho(f) = f(N)$, so it is trivial.
Call $T$ essentially normal if $T^* T - T T^*$ is compact.
Consequence: such a $T$ is a compact perturbation of a normal operator if and only if $\operatorname{ind}(T - \lambda) = 0$ for all $\lambda$ outside its essential spectrum.
The group $\operatorname{Ext}(X)$ is the odd [[K-homology|41XX3KF72X]] group $K_1(X) = K^1(C(X))$.
