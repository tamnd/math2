---
tag: 3FBF628XEF
kind: statement
role: theorem
name: T(1) theorem
msc: [42B20, 47G10]
uses: [78N6AXP9VV, 3SCXCW4AH3, QJYTXFT8Y4, SASP14MA1Z]
about: [3SCXCW4AH3]
sources:
  - url: https://en.wikipedia.org/wiki/T(1)_theorem
same_as:
  wikidata: Q7667741
  wikipedia: T(1) theorem
---

## Statement

Let $n \ge 1$, let $\mathcal{D}$ be the space of smooth functions with compact support on $\R^n$, and let $\mathcal{D}'$ be its dual, the space of distributions.
Let $T \colon \mathcal{D} \to \mathcal{D}'$ be a continuous linear operator with transpose $T^t$, defined by $\langle T^t f, g \rangle = \langle Tg, f \rangle$ for $f, g \in \mathcal{D}$.
Assume that $T$ is associated with a [[Calderón–Zygmund kernel|78N6AXP9VV]] $K$: for $f, g \in \mathcal{D}$ with disjoint supports,
$$\langle Tf, g \rangle = \int\!\!\int K(x, y) f(y) g(x) \, dy \, dx.$$
Then $T$ extends to a bounded operator on $L^2(\R^n)$ if and only if the following three conditions hold:

1. $T(1)$ lies in the space $\mathrm{BMO}$ of functions of [[bounded mean oscillation|QJYTXFT8Y4]];
2. $T^t(1)$ lies in $\mathrm{BMO}$;
3. $T$ has the weak boundedness property.

Here $T(1)$ and $T^t(1)$ are defined as elements of $\mathrm{BMO}$ modulo constants, using the kernel bounds.
The weak boundedness property means that there are constants $C$ and $N$ with the following property.
Let $B$ be a ball of radius $R$, and let $\phi, \psi \in \mathcal{D}$ be supported in $B$ with $\norm{\partial^\alpha\phi}_\infty, \norm{\partial^\alpha\psi}_\infty \le R^{-\abs{\alpha}}$ for $\abs{\alpha} \le N$.
Then $\abs{\langle T\phi, \psi \rangle} \le C R^n$.

## Remarks

Guy David and Jean-Lin Journé proved the theorem in 1984.
The three conditions are necessary.
An $L^2$-bounded operator with a Calderón–Zygmund kernel maps $L^\infty$ into $\mathrm{BMO}$, and so does its transpose.
The weak boundedness property follows from the $L^2$ bound and the Cauchy–Schwarz inequality.
For sufficiency, one subtracts paraproducts with symbols $T(1)$ and $T^t(1)$, which are $L^2$ bounded, and reduces to the case $T(1) = T^t(1) = 0$.
That case is handled by an almost orthogonality argument, such as the Cotlar–Stein lemma, applied to a Littlewood–Paley decomposition of $T$.

Example: for an antisymmetric kernel, $K(x, y) = -K(y, x)$, with $T$ defined as a principal value, the weak boundedness property holds automatically.
Then the theorem reduces to the single condition $T(1) \in \mathrm{BMO}$.
A model case is the Hilbert transform, for which $T(1) = 0$.

Without conditions 1 and 2 the conclusion fails: the kernel bounds alone do not give $L^2$ boundedness, since they carry no information on the cancellation of $T$.

## Explanations

### L1 human

For a singular integral operator, the hard part is to show that it is bounded on $L^2$; the rest of the theory then gives $L^p$ bounds.
The $T(1)$ theorem reduces this hard question to testing the operator on the constant function $1$.
If $T$ and its transpose send $1$ to functions of bounded mean oscillation, and $T$ is mild on bump functions, then $T$ is bounded on $L^2$.

### L2 human

The theorem turns $L^2$ bounds for non-convolution operators, which cannot be checked with the Fourier transform, into simple tests.
It gives a short proof of the $L^2$ boundedness of the Cauchy integral on Lipschitz curves and of the Calderón commutators.
Its output, an $L^2$-bounded operator with a Calderón–Zygmund kernel, is a [[Calderón–Zygmund operator|3SCXCW4AH3]], hence bounded on $L^p$ for $1 < p < \infty$.
There are versions with $T(b)$ in place of $T(1)$, for suitable accretive functions $b$.
