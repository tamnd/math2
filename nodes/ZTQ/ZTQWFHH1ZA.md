---
tag: ZTQWFHH1ZA
kind: definition
name: Simply typed lambda calculus
msc: [03B40, 68N18, 03B38]
defines: 2DP940895E
uses: [BD756KR8FM, AVVQEG0MRJ, Y9B9CVY6SJ]
sources:
  - url: https://en.wikipedia.org/wiki/Simply_typed_lambda_calculus
---

## Definition

Fix a set $B$ of base types and a countable set of variables.
The *simple types* are given by the grammar $\tau ::= b \mid \tau \to \tau$ with $b \in B$.
The *terms* are given by the grammar $t ::= x \mid \lambda x{:}\tau.\, t \mid t\, t$, where $x$ is a variable and $\tau$ is a simple type.
A *context* $\Gamma$ is a finite list $x_1 : \tau_1, \dots, x_n : \tau_n$ of distinct variables with types.
The typing relation $\Gamma \vdash t : \tau$ is the least relation closed under these three rules.

1. Variable: if $x : \tau$ occurs in $\Gamma$, then $\Gamma \vdash x : \tau$.
2. Abstraction: if $\Gamma, x : \sigma \vdash t : \tau$, then $\Gamma \vdash (\lambda x{:}\sigma.\, t) : \sigma \to \tau$.
3. Application: if $\Gamma \vdash t : \sigma \to \tau$ and $\Gamma \vdash u : \sigma$, then $\Gamma \vdash t\, u : \tau$.

The *simply typed lambda calculus* is this typing system together with [[beta reduction|Y9B9CVY6SJ]] $(\lambda x{:}\sigma.\, t)\, u \to t[u/x]$ on typed terms.

## Remarks

Example: for a base type $b$, the term $\lambda f{:}b \to b.\, \lambda x{:}b.\, f\,(f\, x)$ has type $(b \to b) \to b \to b$.
The check: in the context $f : b \to b, x : b$, rule 1 gives $f : b \to b$ and $x : b$.
Rule 3 gives $f\, x : b$, then $f\,(f\, x) : b$ by rule 3 again, and two uses of rule 2 give the arrow type.

Non-example: no annotation makes $\lambda x{:}\sigma.\, x\, x$ typable.
Rule 3 would need $\sigma = \sigma \to \tau$ for some $\tau$, and no finite type equals a longer type that contains it.

The arrow associates to the right, so $\sigma \to \tau \to \rho$ means $\sigma \to (\tau \to \rho)$.
The form above, with types written on bound variables, is the Church style.
In the Curry style, terms are untyped and the rules assign types to them.
It is one instance of a [[type system|AVVQEG0MRJ]].
