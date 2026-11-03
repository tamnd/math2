---
tag: ZEG1M8YWJ2
kind: definition
name: E-theory
msc: [19K35, 46L80]
defines: Y989RVQ66M
uses: [M2WFY1D3SZ, M2NEP1K5AE]
sources:
  - url: https://en.wikipedia.org/wiki/KK-theory
---

## Definition

Let $A$ and $B$ be separable [[C*-algebras|M2WFY1D3SZ]].
An *asymptotic morphism* from $A$ to $B$ is a family of maps $\varphi_t \colon A \to B$, $t \in [1, \infty)$, with the following properties.
For every $a \in A$, the map $t \mapsto \varphi_t(a)$ is norm-continuous.
For all $a, b \in A$ and $\lambda \in \C$:
$$\lim_{t \to \infty} \norm{\varphi_t(a + \lambda b) - \varphi_t(a) - \lambda \varphi_t(b)} = 0, \qquad \lim_{t \to \infty} \norm{\varphi_t(a b) - \varphi_t(a) \varphi_t(b)} = 0,$$
$$\lim_{t \to \infty} \norm{\varphi_t(a^*) - \varphi_t(a)^*} = 0.$$
Two asymptotic morphisms from $A$ to $B$ are *homotopic* if they are the evaluations at $0$ and $1$ of one asymptotic morphism into $C([0, 1], B)$.
Let $[\![A, B]\!]$ be the set of homotopy classes.
Let $\mathcal{K}$ be the C*-algebra of [[compact operators|M2NEP1K5AE]] on a separable infinite-dimensional Hilbert space and $SA = C_0(\R) \otimes A$ the suspension.
The *E-theory group* is
$$E(A, B) = [\![SA \otimes \mathcal{K}, SB \otimes \mathcal{K}]\!].$$

## Remarks

$E(A, B)$ is an abelian group, with the addition given by direct sum after an identification $\mathcal{K} \oplus \mathcal{K} \subseteq M_2(\mathcal{K}) \cong \mathcal{K}$.
Composition of asymptotic morphisms, defined up to homotopy, gives an associative product $E(A, D) \times E(D, B) \to E(A, B)$.
Example: every $*$-homomorphism $\varphi \colon A \to B$ is an asymptotic morphism (constant in $t$), and $\id_{S} \otimes \varphi \otimes \id_{\mathcal{K}}$ gives a class in $E(A, B)$.
Example: every extension $0 \to I \to A \to A/I \to 0$ of separable C*-algebras gives an asymptotic morphism from $C_0(\R) \otimes (A/I)$ to $I$.
It is built from a quasicentral approximate unit of $I$ in $A$, and it is the source of the exactness properties of E-theory.
Non-example: a family $\varphi_t = t \cdot \varphi$ with $\varphi$ a nonzero $*$-homomorphism is not an asymptotic morphism, since $\norm{\varphi_t(a b) - \varphi_t(a)\varphi_t(b)} = \abs{t - t^2} \norm{\varphi(ab)}$ does not tend to $0$ when $\varphi(ab) \neq 0$.
