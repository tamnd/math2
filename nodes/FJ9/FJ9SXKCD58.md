---
tag: FJ9SXKCD58
kind: definition
name: Syntactic monoid
msc: [20M35, 68Q70]
defines: D47RMDH8MJ
uses: [5MFZ4VNY6D, CV013KHVJG, 0N6R902FG1, DCSXXT4SER]
sources:
  - url: https://en.wikipedia.org/wiki/Syntactic_monoid
---

## Definition

Let $\Sigma$ be an alphabet and let $L \subseteq \Sigma^*$ be a [[formal language|5MFZ4VNY6D]].
The *syntactic congruence* of $L$ is the relation $\equiv_L$ on the [[free monoid|CV013KHVJG]] $\Sigma^*$ defined as follows.
One has $u \equiv_L v$ when, for all $x, y \in \Sigma^*$, $xuy \in L$ if and only if $xvy \in L$.
It is a [[congruence|DCSXXT4SER]] of the monoid $\Sigma^*$.
The *syntactic monoid* of $L$ is the quotient [[monoid|0N6R902FG1]] $M(L) = \Sigma^* / {\equiv_L}$, with product $[u][v] = [uv]$ and identity $[\varepsilon]$.
The map $\eta_L \colon \Sigma^* \to M(L)$, $u \mapsto [u]$, is the *syntactic morphism*.

## Remarks

Example: for $\Sigma = \set{a}$ and $L = \set{a^{2n} : n \ge 0}$, one has $a^i \equiv_L a^j$ exactly when $i \equiv j \pmod 2$, so $M(L) \cong \Z/2\Z$.
Non-example: the one-sided relation $u \sim v$, given by "$uz \in L$ if and only if $vz \in L$ for all $z$", is in general not a congruence.
For $L = \set{ab}$, one has $b \sim bb$, since no continuation puts either word in $L$, but $ab \not\sim abb$, since $ab \in L$ and $abb \notin L$.
So multiplying on the left by $a$ does not preserve $\sim$, and the classes of $\sim$ do not form a quotient monoid.
A monoid $M$ *recognizes* $L$ when $L = \varphi^{-1}(P)$ for some monoid morphism $\varphi \colon \Sigma^* \to M$ and some $P \subseteq M$.
The syntactic monoid recognizes $L$ and divides every monoid that recognizes $L$.
The language $L$ is regular if and only if $M(L)$ is finite, and then $M(L)$ is isomorphic to the transition monoid of the minimal DFA of $L$.
