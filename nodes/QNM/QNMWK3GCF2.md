---
tag: QNMWK3GCF2
kind: definition
name: Pseudofunctor
msc: [18N10]
defines: 18M8XGY04N
uses: [TAHV24ED74, 28NQ0KRHD3, KYCPCC57FT, CQACXG10JZ, PY430TXMG0]
sources:
  - url: https://en.wikipedia.org/wiki/Pseudo-functor
---

## Definition

Let $\mathcal{B}$ and $\mathcal{B}'$ be [[bicategories|TAHV24ED74]] with associators $\alpha, \alpha'$ and unitors $\lambda, \rho, \lambda', \rho'$.
A *pseudofunctor* $F \colon \mathcal{B} \to \mathcal{B}'$ consists of:

1. for each object $a$ of $\mathcal{B}$, an object $F(a)$ of $\mathcal{B}'$;
2. for each pair $a, b$, a [[functor|28NQ0KRHD3]] $F_{a,b} \colon \mathcal{B}(a, b) \to \mathcal{B}'(F(a), F(b))$;
3. for composable $f \colon a \to b$ and $g \colon b \to c$, invertible 2-morphisms $\phi_{g,f} \colon F(g) \circ F(f) \Rightarrow F(g \circ f)$, [[natural|KYCPCC57FT]] in $f$ and $g$;
4. for each object $a$, an invertible 2-morphism $\phi_a \colon 1_{F(a)} \Rightarrow F(1_a)$.

These data satisfy, for all $f \colon a \to b$, $g \colon b \to c$, $h \colon c \to d$:

1. $F(\alpha_{h,g,f}) \cdot \phi_{h \circ g, f} \cdot (\phi_{h,g} \circ 1_{F(f)}) = \phi_{h, g \circ f} \cdot (1_{F(h)} \circ \phi_{g,f}) \cdot \alpha'_{F(h),F(g),F(f)}$;
2. $F(\lambda_f) \cdot \phi_{1_b, f} \cdot (\phi_b \circ 1_{F(f)}) = \lambda'_{F(f)}$;
3. $F(\rho_f) \cdot \phi_{f, 1_a} \cdot (1_{F(f)} \circ \phi_a) = \rho'_{F(f)}$.

Here $\cdot$ is vertical composition of 2-morphisms.

## Remarks

If the $\phi_{g,f}$ and $\phi_a$ are only required to be 2-morphisms, not invertible, $F$ is called a lax functor; if they are identities, $F$ is a strict 2-functor.
Example: regard the category of rings as a [[2-category|CQACXG10JZ]] with only identity 2-morphisms.
Send a ring $R$ to its category of left modules, and a ring map $u \colon R \to S$ to extension of scalars $S \otimes_R -$.
The canonical isomorphisms $T \otimes_S (S \otimes_R M) \cong T \otimes_R M$ and $R \otimes_R M \cong M$ give $\phi$, and the axioms hold because these isomorphisms are the standard ones on elementary tensors.
Non-example: a monoidal category is a one-object bicategory, and a lax [[monoidal functor|PY430TXMG0]] gives a lax functor.
The forgetful functor $(\mathbf{Ab}, \otimes) \to (\mathbf{Set}, \times)$ with $\phi(a, b) = a \otimes b$ is a lax functor but not a pseudofunctor, since $A \times B \to A \otimes B$ is not invertible.
