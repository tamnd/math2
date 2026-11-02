---
tag: 8CV1KW9AJ8
kind: definition
name: Geometric integrator
msc: [37M15, 65P10, 65L06]
defines: VQ2BTYFST4
uses: [06738GGWWK, 0262JP0NV9, 0EDKGA2FAK]
sources:
  - url: https://en.wikipedia.org/wiki/Geometric_integrator
---

## Definition

Let $U \subseteq \R^d$ be open, let $f \colon U \to \R^d$ be smooth, and let $\varphi_t$ be the [[flow|06738GGWWK]] of the equation $y' = f(y)$.
Let $\mathcal{P}$ be a property of maps $U \to \R^d$ that every $\varphi_t$ has.
Standard choices of $\mathcal{P}$ are:

1. symplecticity, when the equation is a [[Hamiltonian system|0EDKGA2FAK]];
2. the conservation of a given [[first integral|0262JP0NV9]] $I$, that is, $I \circ \Phi = I$;
3. the preservation of volume, when $f$ has divergence zero;
4. reversibility with respect to a linear involution $\rho$, that is, $\rho \circ \Phi = \Phi^{-1} \circ \rho$, when $f \circ \rho = -\rho \circ f$.

Let $\Phi_h$ be a one-step numerical method with step size $h$.
It is a *geometric integrator* for $\mathcal{P}$ if $\Phi_h$ has the property $\mathcal{P}$ for every equation of the class and every small enough $h > 0$.

## Remarks

Example: take the harmonic oscillator $q' = p$, $p' = -q$.
The symplectic Euler method $p_{n+1} = p_n - h q_n$, $q_{n+1} = q_n + h p_{n+1}$ is the linear map
$$\begin{pmatrix} q_{n+1} \\ p_{n+1} \end{pmatrix} = \begin{pmatrix} 1 - h^2 & h \\ -h & 1 \end{pmatrix} \begin{pmatrix} q_n \\ p_n \end{pmatrix}.$$
Its determinant is $1$, and in dimension $2$ this means that the map is symplectic.
So the method is a geometric integrator for property 1.
Non-example: the explicit Euler method $q_{n+1} = q_n + h p_n$, $p_{n+1} = p_n - h q_n$ has matrix determinant $1 + h^2 \ne 1$, so it is not symplectic for any $h > 0$.
A method may be geometric for one property and not another.
The implicit midpoint rule is symplectic and conserves all quadratic first integrals.
But no Runge–Kutta method conserves all polynomial first integrals of degree $3$ or more.

## Explanations

### L1 human

A geometric integrator copies a structural feature of the true motion exactly, not only approximately.
The feature is chosen in advance: a conserved quantity, area in phase space, or symmetry under reversing time.
