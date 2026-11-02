---
tag: 3CJ8XA1VAB
kind: definition
name: Internal language
msc: [03G30, 18B25, 03B38]
defines: WH48X83YPJ
uses: [6837RS7N82, NKP5TPQ79X, RHWD8DY41R, S5744QZV4N, Q05K04QJ71]
sources:
  - url: https://en.wikipedia.org/wiki/Categorical_logic
---

## Definition

Let $\mathcal{E}$ be a [[topos|6837RS7N82]] with [[subobject classifier|NKP5TPQ79X]] $\top \colon 1 \to \Omega$, and write $PX$ for the [[exponential object|RHWD8DY41R]] $\Omega^X$.
The *internal language* (Mitchell–Bénabou language) of $\mathcal{E}$ is the typed language described as follows.

1. The types are the objects of $\mathcal{E}$; the type of a [[product|S5744QZV4N]] $X \times Y$ is the product type, and $PX$ is the power type of $X$.
2. There are variables of each type, and each morphism $f \colon X \to Y$ is a function symbol from type $X$ to type $Y$.
3. Terms are built from variables by function symbols and by pairing $\langle \sigma, \tau \rangle$.
For terms $\sigma, \tau$ of the same type, $\sigma = \tau$ is a term of type $\Omega$.
For $\sigma$ of type $X$ and $\tau$ of type $PX$, the membership $\sigma \in \tau$ is a term of type $\Omega$.
For a term $\varphi$ of type $\Omega$, the comprehension $\set{x \in X \mid \varphi}$ is a term of type $PX$.
4. A *formula* is a term of type $\Omega$.

A term $\tau$ of type $Y$ whose free variables are $x_1 : X_1, \dots, x_n : X_n$ is interpreted as a morphism $X_1 \times \cdots \times X_n \to Y$.
Variables are interpreted by projections, function symbols by composition, $\sigma = \tau$ by the characteristic morphism of the diagonal $Y \to Y \times Y$, and $\sigma \in \tau$ by the evaluation morphism $X \times PX \to \Omega$.
A formula $\varphi$ is *valid* in $\mathcal{E}$ when its interpretation equals $\top$ composed with the unique morphism $X_1 \times \cdots \times X_n \to 1$.

## Remarks

The connectives $\wedge, \vee, \Rightarrow, \neg$ and the quantifiers $\forall, \exists$ are definable from equality, membership and comprehension; on subobjects they act as the Heyting algebra operations and as the adjoints to [[pullback|Q05K04QJ71]].
The valid formulas are closed under the rules of higher-order intuitionistic logic, but not in general under the law of excluded middle.
Example: in $\mathbf{Set}$, a formula is valid exactly when it is true for all values of its variables in the usual sense.
Example: a morphism $f \colon X \to Y$ is a monomorphism exactly when the formula $\forall x, x' \in X\, (f(x) = f(x') \Rightarrow x = x')$ is valid.
Non-example: in the topos $\mathrm{Sh}(\R)$ of sheaves on the real line, the formula $\forall p \in \Omega\, (p \vee \neg p)$ is not valid, so excluded middle is not part of the internal logic.
