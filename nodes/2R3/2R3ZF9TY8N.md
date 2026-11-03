---
tag: 2R3ZF9TY8N
kind: statement
role: theorem
name: Malliavin's theorem on failure of spectral synthesis
msc: [43A45, 43A46]
uses: [ZR09S9R3AW, FMW57WNPDB, 6GD25S53ND, JBHTE03V78]
about: [JBHTE03V78]
sources:
  - url: https://en.wikipedia.org/wiki/Paul_Malliavin
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] that is not compact, so that its [[Pontryagin dual|FMW57WNPDB]] $\widehat{G}$ is not discrete.
Then [[spectral synthesis|JBHTE03V78]] fails for $G$: there is a closed set $E \subseteq \widehat{G}$ that is not a set of spectral synthesis.
Equivalently, there are two different closed ideals of the [[group algebra|6GD25S53ND]] $L^1(G)$ with the same hull.

## Remarks

The hypothesis is necessary: when $G$ is compact, $\widehat{G}$ is discrete and every subset of $\widehat{G}$ is a set of spectral synthesis.

Proof idea: Malliavin constructs a real-valued function $\varphi$ in the algebra of Fourier transforms on $\widehat{G}$ whose exponentials $e^{it\varphi}$, $t \in \R$, grow slowly in norm as $\abs{t} \to \infty$.
This growth condition yields a closed set, a level set of $\varphi$, and a bounded functional that separates two closed ideals with this hull.

Before Malliavin's theorem, Laurent Schwartz had shown that the unit sphere in $\R^3$ is not a set of synthesis for $\R^3$.
Malliavin's theorem shows that failure happens already for $G = \R$, where the dual is again $\R$.

## Explanations

### L1 human

For a closed set of frequencies, one can ask whether the functions whose spectrum avoids it all come from the simplest construction.
Wiener's theorem says yes when the set is empty.
Malliavin showed that on the real line, and on every non-compact abelian group, the answer is no for some closed sets.

### L2 human

The theorem answered negatively the problem of spectral synthesis for $L^1(\R)$.
It means that closed ideals of $L^1(G)$ cannot in general be classified by their zero sets, in contrast with the maximal regular ideals, which are classified by points of $\widehat{G}$.
