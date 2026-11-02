---
tag: DZEQY398HQ
kind: definition
name: Schubert variety
msc: [14M15, 14N15]
defines: Z014Q8KPDD
uses: [CYPA882RB9, NHRWCQQKTH, 5JSYA1JNCC]
sources:
  - url: https://en.wikipedia.org/wiki/Schubert_variety
---

## Definition

Let $k$ be a field, let $1 \le d < n$, and let $\mathrm{Gr}(d, n)$ be the [[Grassmannian|CYPA882RB9]] of $d$-dimensional subspaces of $k^n$.
Fix a full flag $F_1 \subset F_2 \subset \cdots \subset F_n = k^n$ with $\dim F_j = j$.
Let $\lambda = (\lambda_1, \ldots, \lambda_d)$ be a partition with $n - d \ge \lambda_1 \ge \cdots \ge \lambda_d \ge 0$.
The *Schubert variety* $X_\lambda$ is
$$X_\lambda = \set{\Lambda \in \mathrm{Gr}(d, n) : \dim(\Lambda \cap F_{n - d + i - \lambda_i}) \ge i \text{ for } i = 1, \ldots, d}.$$

## Remarks

$X_\lambda$ is a closed irreducible subvariety of codimension $\abs{\lambda} = \lambda_1 + \cdots + \lambda_d$.

Example: $\lambda = 0$ gives all of $\mathrm{Gr}(d, n)$.
Indeed $\dim(\Lambda \cap F_{n - d + i}) \ge d + (n - d + i) - n = i$ holds for every $\Lambda$.
For $d = 2$, $n = 4$ and $\lambda = (1, 0)$, the conditions reduce to $\dim(\Lambda \cap F_2) \ge 1$.
In projective terms these are the lines in $\mathbb{P}^3$ that meet a fixed line, a hypersurface in $\mathrm{Gr}(2, 4)$.

Non-example: the set of $\Lambda \in \mathrm{Gr}(2, 4)$ with $\Lambda \cap F_2 = 0$ is open and dense, and it is not closed.
So it is not a Schubert variety; it is the open Schubert cell.

General form: let $G$ be a connected reductive group with a [[Borel subgroup|5JSYA1JNCC]] $B$ and a parabolic subgroup $P \supseteq B$.
A Schubert variety in the [[flag variety|NHRWCQQKTH]] $G / P$ is the Zariski closure of a $B$-orbit.
