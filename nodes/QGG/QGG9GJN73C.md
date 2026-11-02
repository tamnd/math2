---
tag: QGG9GJN73C
kind: definition
name: Monoidal functor
msc: [18M05, 18A22]
defines: PY430TXMG0
uses: [M3MSQ3NKAE, 28NQ0KRHD3, KYCPCC57FT]
sources:
  - url: https://en.wikipedia.org/wiki/Monoidal_functor
---

## Definition

Let $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ and $(\mathcal{D}, \otimes', I', \alpha', \lambda', \rho')$ be [[monoidal categories|M3MSQ3NKAE]].
A (lax) *monoidal functor* from $\mathcal{C}$ to $\mathcal{D}$ is a [[functor|28NQ0KRHD3]] $F \colon \mathcal{C} \to \mathcal{D}$ together with:

1. a morphism $\varepsilon \colon I' \to F(I)$;
2. a [[natural transformation|KYCPCC57FT]] $\mu$ with components $\mu_{A,B} \colon F(A) \otimes' F(B) \to F(A \otimes B)$;

such that for all objects $A, B, C$ of $\mathcal{C}$:

1. associativity: $F(\alpha_{A,B,C}) \circ \mu_{A \otimes B, C} \circ (\mu_{A,B} \otimes' \id_{F(C)}) = \mu_{A, B \otimes C} \circ (\id_{F(A)} \otimes' \mu_{B,C}) \circ \alpha'_{F(A),F(B),F(C)}$;
2. left unitality: $F(\lambda_A) \circ \mu_{I,A} \circ (\varepsilon \otimes' \id_{F(A)}) = \lambda'_{F(A)}$;
3. right unitality: $F(\rho_A) \circ \mu_{A,I} \circ (\id_{F(A)} \otimes' \varepsilon) = \rho'_{F(A)}$.

The functor is *strong monoidal* if $\varepsilon$ and all $\mu_{A,B}$ are isomorphisms, and *strict monoidal* if they are identities.

## Remarks

Example: the forgetful functor $U \colon (\mathbf{Ab}, \otimes, \Z) \to (\mathbf{Set}, \times, \set{*})$ with $\mu_{A,B}(a, b) = a \otimes b$ and $\varepsilon(*) = 1$.
Both sides of the associativity axiom send $((a, b), c)$ to $a \otimes (b \otimes c)$, and the left unit axiom reads $1 \otimes a \mapsto a$.
It is lax but not strong, since $A \times B \to A \otimes B$ is not a bijection in general.
Non-example: the forgetful functor from $\R$-vector spaces with $\otimes$ to $(\mathbf{Set}, \times)$, with $\mu(u, v) = u \otimes v$ but with $\varepsilon(*) = 0$.
The left unit axiom fails: it would send $(*, v)$ to $0 \otimes v = 0$, while $\lambda'$ sends it to $v$.
Some authors say "monoidal functor" for strong monoidal functors only; the lax version is then called lax monoidal.
