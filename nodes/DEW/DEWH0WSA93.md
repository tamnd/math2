---
tag: DEWH0WSA93
kind: definition
name: KMS state
msc: [46L55, 82B10, 46L60]
defines: HJ7TMS0WKY
uses: [F7MB2WREBJ, M2WFY1D3SZ, 081WKEDK6C]
sources:
  - url: https://en.wikipedia.org/wiki/KMS_state
---

## Definition

Let $A$ be a [[C*-algebra|M2WFY1D3SZ]].
Let $(\tau_t)_{t \in \R}$ be a one-parameter group of $*$-automorphisms of $A$ such that $t \mapsto \tau_t(a)$ is norm continuous for every $a \in A$.
Let $\beta > 0$, and let $D_\beta = \set{z \in \C : 0 \le \operatorname{Im} z \le \beta}$.
A [[state|F7MB2WREBJ]] $\omega$ on $A$ is a *$(\tau, \beta)$-KMS state* if for all $a, b \in A$ there is a function $F_{a, b} \colon D_\beta \to \C$ such that:

1. $F_{a, b}$ is bounded and continuous on $D_\beta$, and [[analytic|081WKEDK6C]] in the interior of $D_\beta$;
2. $F_{a, b}(t) = \omega(a \, \tau_t(b))$ for all $t \in \R$;
3. $F_{a, b}(t + i \beta) = \omega(\tau_t(b) \, a)$ for all $t \in \R$.

## Remarks

Every KMS state is invariant: $\omega \circ \tau_t = \omega$ for all $t$.
Example: let $A = M_n(\C)$, let $H$ be a Hermitian matrix, and let $\tau_t(b) = e^{itH} b e^{-itH}$.
The Gibbs state $\omega(a) = \tr(e^{-\beta H} a) / \tr(e^{-\beta H})$ satisfies the condition with $F_{a, b}(z) = \tr(e^{-\beta H} a e^{izH} b e^{-izH}) / \tr(e^{-\beta H})$.
At $z = t + i \beta$, cyclicity of the trace turns this into $\omega(\tau_t(b) \, a)$; for this $A$ and $\tau$ the Gibbs state is the only KMS state.
Non-example: if $H$ is not a multiple of the identity, the normalized trace $\frac{1}{n} \tr$ is not a $(\tau, \beta)$-KMS state for $\beta > 0$.
For $a$ and $b$ entire analytic for $\tau$, the condition reads $\omega(a \, \tau_{i \beta}(b)) = \omega(b a)$.
