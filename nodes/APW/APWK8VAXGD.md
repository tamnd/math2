---
tag: APWK8VAXGD
kind: definition
name: Hindley–Milner type system
msc: [68N18, 68N15, 03B40]
defines: 703R12KENG
uses: [2DP940895E, 6NY149HDKS, NCDZ969V7X, RJJ9D0WF53]
sources:
  - url: https://en.wikipedia.org/wiki/Hindley–Milner_type_system
---

## Definition

Fix a set of type variables $\alpha, \beta, \dots$ and a set of type constructors containing the arrow $\to$.
The *monotypes* are $\tau ::= \alpha \mid C\, \tau_1 \cdots \tau_n$, where $C$ is a type constructor of arity $n$; in particular $\tau_1 \to \tau_2$ is a monotype.
The *type schemes* are $\sigma ::= \tau \mid \forall \alpha.\, \sigma$.
The terms are $e ::= x \mid e\, e \mid \lambda x.\, e \mid \mathsf{let}\ x = e\ \mathsf{in}\ e$.
A context $\Gamma$ assigns type schemes to finitely many variables.
A monotype $\tau$ is an *instance* of $\forall \alpha_1 \dots \alpha_n.\, \tau_0$ if $\tau = \tau_0[\tau_1/\alpha_1, \dots, \tau_n/\alpha_n]$ for some monotypes $\tau_i$.
The typing relation $\Gamma \vdash e : \tau$ of the *Hindley–Milner type system* is the least relation closed under these rules.

1. Variable: if $x : \sigma$ is in $\Gamma$ and $\tau$ is an instance of $\sigma$, then $\Gamma \vdash x : \tau$.
2. Application: if $\Gamma \vdash e_1 : \tau_1 \to \tau_2$ and $\Gamma \vdash e_2 : \tau_1$, then $\Gamma \vdash e_1\, e_2 : \tau_2$.
3. Abstraction: if $\Gamma, x : \tau_1 \vdash e : \tau_2$ with $\tau_1$ a monotype, then $\Gamma \vdash \lambda x.\, e : \tau_1 \to \tau_2$.
4. Let: if $\Gamma \vdash e_1 : \tau_1$ and $\Gamma, x : \mathrm{gen}_\Gamma(\tau_1) \vdash e_2 : \tau_2$, then $\Gamma \vdash \mathsf{let}\ x = e_1\ \mathsf{in}\ e_2 : \tau_2$.

Here $\mathrm{gen}_\Gamma(\tau_1) = \forall \alpha_1 \dots \alpha_n.\, \tau_1$, where $\alpha_1, \dots, \alpha_n$ are the type variables free in $\tau_1$ but not free in $\Gamma$.

## Remarks

Example: $\vdash \mathsf{let}\ i = \lambda x.\, x\ \mathsf{in}\ i\, i : \beta \to \beta$.
The check: rule 3 gives $\lambda x.\, x : \alpha \to \alpha$, and rule 4 gives $i$ the scheme $\forall \alpha.\, \alpha \to \alpha$.
By rule 1 the first $i$ gets the instance $(\beta \to \beta) \to \beta \to \beta$ and the second gets $\beta \to \beta$, so rule 2 gives $i\, i : \beta \to \beta$.

Non-example: $\lambda i.\, i\, i$ has no type.
Rule 3 gives the bound variable $i$ a single monotype $\tau_1$, and $i\, i$ would need $\tau_1 = \tau_1 \to \tau_2$, which no monotype satisfies.
So polymorphism is available for $\mathsf{let}$-bound names but not for $\lambda$-bound ones.

Algorithm W of Damas and Milner computes a principal type of every typable term by [[unification|RJJ9D0WF53]] of monotypes.
This makes [[type inference|6NY149HDKS]] decidable for the system.
