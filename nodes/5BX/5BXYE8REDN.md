---
tag: 5BXYE8REDN
kind: definition
name: Modal mu-calculus
msc: [03B45, 03B70, 68Q60]
defines: MZ0M2KR9S0
uses: [C3RZY20ETK, NGHWZ9Y7ZV, DBD64TH52D, RHXP3HA64M, 0A7KV2WB7A]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_%CE%BC-calculus
---

## Definition

Let $P$ be a set of propositions, $A$ a set of actions and $\mathcal{V}$ a set of variables.
The formulas of the *modal $\mu$-calculus* are given by the grammar
$$\varphi ::= p \mid Z \mid \neg\varphi \mid \varphi \land \varphi \mid \langle a \rangle \varphi \mid \mu Z.\,\varphi, \qquad p \in P,\ a \in A,\ Z \in \mathcal{V}.$$
In a formula $\mu Z.\,\varphi$, every free occurrence of $Z$ in $\varphi$ must lie under an even number of negations.

A model is a labelled transition system $\mathcal{M} = (S, \set{\xrightarrow{a}}_{a \in A}, V)$ with a valuation $V \colon P \to \mathcal{P}(S)$.
Given an assignment $\rho \colon \mathcal{V} \to \mathcal{P}(S)$, the set $\|\varphi\|_\rho \subseteq S$ is defined by induction:

1. $\|p\|_\rho = V(p)$ and $\|Z\|_\rho = \rho(Z)$;
2. $\|\neg\varphi\|_\rho = S \setminus \|\varphi\|_\rho$ and $\|\varphi \land \psi\|_\rho = \|\varphi\|_\rho \cap \|\psi\|_\rho$;
3. $\|\langle a \rangle \varphi\|_\rho = \set{s \in S : s \xrightarrow{a} t \text{ for some } t \in \|\varphi\|_\rho}$;
4. $\|\mu Z.\,\varphi\|_\rho = \bigcap \set{T \subseteq S : \|\varphi\|_{\rho[Z \mapsto T]} \subseteq T}$.

Here $\rho[Z \mapsto T]$ agrees with $\rho$ except that it sends $Z$ to $T$.

## Remarks

The restriction on negations makes $T \mapsto \|\varphi\|_{\rho[Z \mapsto T]}$ a [[monotone function|0A7KV2WB7A]] on the [[complete lattice|D7A0ZGZT5S]] $\mathcal{P}(S)$.
By the [[Knaster–Tarski theorem|RHXP3HA64M]], clause 4 is then its [[least fixed point|DBD64TH52D]].
The greatest fixed point is $\nu Z.\,\varphi = \neg \mu Z.\,\neg\varphi[\neg Z / Z]$, and the box is $[a]\varphi = \neg\langle a \rangle \neg\varphi$.

Example: $\|\mu Z.\,(p \lor \langle a \rangle Z)\|$ is the set of states from which a finite path of $a$-steps reaches $V(p)$.
This set $T$ satisfies $V(p) \cup \set{s : s \xrightarrow{a} t,\ t \in T} \subseteq T$, and every set with this property contains it.

Non-example: $\mu Z.\,\neg Z$ is not a formula, since $Z$ occurs under one negation.
The map $T \mapsto S \setminus T$ is not monotone, and it has no fixed point when $S \neq \emptyset$.
