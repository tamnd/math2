---
tag: A127WFVYKW
kind: statement
role: theorem
name: Hodge theorem
msc: [58A14, 58A12, 58J05]
uses: [7CBT4SM83Y, 0E3G0GRPZ6, 0ZHSTAG8ZY, 1Y4WX4XQWJ, GX74C07T0G, 913WEQERBE]
about: [GX74C07T0G, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Hodge_theory
---

## Statement

Let $(M, g)$ be a compact [[oriented|913WEQERBE]] [[Riemannian manifold|7CBT4SM83Y]] without boundary, of dimension $n$.
For $0 \le k \le n$, let $\Omega^k(M)$ be the space of smooth $k$-[[forms|0E3G0GRPZ6]] and $d$ the [[exterior derivative|0ZHSTAG8ZY]].
Let $\delta = (-1)^{n(k+1)+1} \star d \star$ be the codifferential on $k$-forms, where $\star$ is the [[Hodge star|1Y4WX4XQWJ]].
Let $\Delta = d\delta + \delta d$ be the Hodge Laplacian.
Let $\mathcal{H}^k = \set{\omega \in \Omega^k(M) : \Delta\omega = 0}$ be the space of harmonic $k$-forms.
Then:

1. $\mathcal{H}^k$ is finite-dimensional.
2. There is a decomposition, orthogonal for the $L^2$ inner product $(\alpha, \beta) = \int_M \alpha \wedge \star\beta$:
$$\Omega^k(M) = \mathcal{H}^k \oplus d\,\Omega^{k-1}(M) \oplus \delta\,\Omega^{k+1}(M).$$
3. Each class of the [[de Rham cohomology|GX74C07T0G]] group $H^k_{dR}(M)$ contains exactly one harmonic form, so $\mathcal{H}^k \cong H^k_{dR}(M)$.

## Remarks

The idea of the proof: $\delta$ is the $L^2$ adjoint of $d$, so $(\Delta\omega, \omega) = \norm{d\omega}^2 + \norm{\delta\omega}^2$, and $\omega$ is harmonic if and only if $d\omega = 0$ and $\delta\omega = 0$.
The operator $\Delta$ is elliptic, and elliptic regularity with the Rellich compactness theorem gives part 1 and the decomposition $\Omega^k = \mathcal{H}^k \oplus \Delta(\Omega^k)$, from which part 2 follows.
For part 3, a closed form is orthogonal to $\delta\Omega^{k+1}$, so it is its harmonic part plus an exact form.

Example: on the flat torus $\R^n / \Z^n$ the harmonic $k$-forms are the forms with constant coefficients in $dx^{i_1} \wedge \dots \wedge dx^{i_k}$.
So $\dim H^k_{dR} = \binom{n}{k}$.

Compactness is needed: on $\R$, every function $a x + b$ is harmonic, and the space of harmonic $0$-forms is $2$-dimensional while $H^0_{dR}(\R)$ is $1$-dimensional.

## Explanations

### L1 human

Each cohomology class, a kind of "hole" of the manifold, has many representing forms.
The Hodge theorem picks a best one: the unique harmonic form, which minimizes the energy in its class.
So topology is captured by solutions of a differential equation.

### L2 human

Since $\star$ maps harmonic $k$-forms to harmonic $(n-k)$-forms, the theorem gives Poincaré duality $b_k = b_{n-k}$ for the Betti numbers.
Combined with Weitzenböck identities, it turns curvature conditions into vanishing of cohomology, as in Bochner's theorem.
On compact Kähler manifolds a refinement gives the Hodge decomposition of complex cohomology into $(p, q)$-types.
