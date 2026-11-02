---
tag: S8FNWJYVXM
kind: definition
name: Incidence structure
msc: [51A05, 05B25]
defines: FGKNAFNHA3
uses: [05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Incidence_structure
---

## Definition

An *incidence structure* is a triple $(P, L, I)$ in which $P$ and $L$ are disjoint sets and $I \subseteq P \times L$ is a [[binary relation|05AVARPXA2]] from $P$ to $L$.
The elements of $P$ are the *points*, the elements of $L$ are the *lines* (or *blocks*), and $I$ is the *incidence relation*.
A point $p$ and a line $\ell$ are *incident*, and one says that $p$ lies on $\ell$, when $(p, \ell) \in I$.

## Remarks

Example: let $P = \set{1, 2, 3}$, let $L = \set{a, b}$, and let $I = \set{(1, a), (2, a), (2, b), (3, b)}$.
Check: $P$ and $L$ are disjoint and $I$ is a subset of $P \times L$, so $(P, L, I)$ is an incidence structure, a path of two lines meeting at the point $2$.

Non-example: with the same $P$ and $L$, a set $I$ that contains the pair $(1, 2)$ is not an incidence relation, because $(1, 2)$ is not in $P \times L$.

The *dual* of $(P, L, I)$ is $(L, P, I^{\top})$, where $(\ell, p) \in I^{\top}$ exactly when $(p, \ell) \in I$.
An *isomorphism* from $(P, L, I)$ to $(P', L', I')$ is a pair of bijections $P \to P'$ and $L \to L'$ that preserves incidence in both directions.
Often lines are taken to be subsets of $P$, with incidence given by membership.
The general definition also allows two different lines with the same set of points.
A finite incidence structure is described by its [[incidence matrix|9DNFN8M83X]].
