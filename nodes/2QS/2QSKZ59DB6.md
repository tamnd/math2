---
tag: 2QSKZ59DB6
kind: definition
name: Étale morphism of rings
msc: [13B40, 14B25]
defines: FTRW0679E2
uses: [0310REJJY8, DPBJ04JMH8, 764GZHTGV8, 096Z9MP2ME, 0VTH8KPCG2, 8KPDNVKX7B, 286G0P1B69, GY3QA6NH0E, 73RYYEVDKA, 7HCFARHG7D, 0WCX7NB4N7]
sources:
  - url: https://en.wikipedia.org/wiki/Étale_algebra
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $A$ be a commutative [[$R$-algebra|DPBJ04JMH8]].
Then $A$ is *étale* over $R$, and the structure map $R \to A$ is an *étale morphism*, if both conditions hold:

1. $A$ is a [[finitely presented|764GZHTGV8]] $R$-algebra.
2. $A$ is formally étale over $R$, in the following sense.

Let $C$ be a commutative $R$-algebra, let $J \subseteq C$ be an [[ideal|096Z9MP2ME]] with $J^2 = 0$, and let $u \colon A \to C/J$ be an $R$-algebra [[homomorphism|0VTH8KPCG2]].
Then there is exactly one $R$-algebra homomorphism $v \colon A \to C$ whose composite with $C \to C/J$ is $u$.

## Remarks

Condition 2 says that the lift required by [[formal smoothness|8KPDNVKX7B]] exists and is unique.
Equivalent forms: $A$ is [[smooth|286G0P1B69]] and [[unramified|GY3QA6NH0E]] over $R$; or $A$ is finitely presented, [[flat|73RYYEVDKA]] and unramified over $R$.

Example: let $f \in R[x]$ be monic and let $A = R[x]/(f)$; if the class of $f'$ is a unit in $A$, then $A$ is étale over $R$.
For instance, $R[x]/(x^2 - a)$ is étale when $2a$ is a unit of $R$, since $(2x)^2 = 4a$ in $A$.
Over a field $k$, a finite [[separable extension|0WCX7NB4N7]] $L$ of $k$ is étale, and the étale $k$-algebras are exactly the finite products of such fields.

Non-example: $A = k[x]$ over a field $k$ is smooth and finitely presented, but a map $A \to C/J$ has many lifts: $x$ may go to any preimage of $u(x)$.
So uniqueness in clause 2 fails; accordingly $\Omega_{A/k} = A \, dx \ne 0$, see [[Kähler differentials|7HCFARHG7D]].
