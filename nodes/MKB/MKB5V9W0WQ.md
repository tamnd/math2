---
tag: MKB5V9W0WQ
kind: statement
role: lemma
name: Aubin–Lions lemma
msc: ["46E35", "46E40", 35K90]
uses: [06GZ956657, NN8RWPC8WG, SASP14MA1Z, MHSMQ097GP]
about: [SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Aubin%E2%80%93Lions_lemma
same_as:
  wikidata: Q4819058
  wikipedia: Aubin–Lions lemma
---

## Statement

Let $X_0 \subseteq X \subseteq X_1$ be three [[Banach spaces|06GZ956657]] such that $X_0$ and $X_1$ are [[reflexive|NN8RWPC8WG]], the inclusion $X_0 \to X$ is compact, and the inclusion $X \to X_1$ is continuous.
Let $T > 0$ and $1 < p, q < \infty$.
Let $L^p(0, T; X_0)$ be the [[Lebesgue space|SASP14MA1Z]] of [[Bochner-integrable|MHSMQ097GP]] functions with values in $X_0$, and let $u'$ be the weak time derivative.
Let $W = \set{ u \in L^p(0, T; X_0) : u' \in L^q(0, T; X_1) }$.
Give $W$ the norm $\norm{u}_W = \norm{u}_{L^p(0, T; X_0)} + \norm{u'}_{L^q(0, T; X_1)}$.
Then the inclusion of $W$ into $L^p(0, T; X)$ is compact.

## Remarks

Proof idea: by Ehrling's lemma, for every $\eta > 0$ there is $C_\eta$ with $\norm{v}_X \le \eta \norm{v}_{X_0} + C_\eta \norm{v}_{X_1}$ for all $v \in X_0$.
A bounded set in $W$ is bounded in $L^p(0, T; X_0)$ and equicontinuous in time with values in $X_1$, because of the bound on $u'$.
This gives a subsequence that converges in $L^p(0, T; X_1)$, and Ehrling's lemma upgrades the convergence to $L^p(0, T; X)$.

Example: let $\Omega \subseteq \R^n$ be a bounded Lipschitz domain, $X_0 = H^1(\Omega)$, $X = L^2(\Omega)$ and $X_1 = (H^1(\Omega))'$, the dual space.
The [[Rellich–Kondrachov theorem|YM3JZ34PME]] gives the compact inclusion.
So a sequence of approximate solutions of a parabolic equation, bounded in $L^2(0, T; H^1(\Omega))$ with time derivatives bounded in $L^2(0, T; (H^1)')$, has a subsequence that converges strongly in $L^2(0, T; L^2(\Omega))$.
This strong convergence lets one pass to the limit in nonlinear terms, as in the construction of [[Leray weak solutions|DHHR5PZZ7E]] of the Navier–Stokes equations.

Both hypotheses are needed.
If $X_0 = X = X_1$ is an infinite-dimensional Hilbert space, the constant functions $u_k(t) = e_k$, for an orthonormal sequence $(e_k)$, are bounded in $W$ with $u_k' = 0$, but no subsequence converges in $L^p(0, T; X)$.
If the bound on $u'$ is dropped, the functions $u_k(t) = \sin(kt) v$ with a fixed $v \ne 0$ are bounded in $L^p(0, T; X_0)$, but they converge weakly to $0$ and not strongly.

## Explanations

### L1 human

Bounds in space alone or in time alone do not give compactness for functions of time and space.
The lemma says that a bound on spatial derivatives together with a weak bound on time derivatives is enough to extract a strongly convergent subsequence.

### L2 human

The lemma is the standard compactness tool for evolution equations.
One builds approximate solutions, for example by the Galerkin method.
Energy estimates bound them in $L^2(0, T; H^1)$ and their time derivatives in a dual space.
The lemma then gives strong convergence in $L^2(0, T; L^2)$.
It plays for time-dependent problems the role that the Rellich–Kondrachov theorem plays for stationary ones.
