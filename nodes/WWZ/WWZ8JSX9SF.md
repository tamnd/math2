---
tag: WWZ8JSX9SF
kind: definition
name: Engel subalgebra
msc: [17B05, 17B30]
defines: PM39E26ZG6
uses: [5JJYBJ6A8K, 54XSPNAM1J, WKSSTQ69AK, 0AJ035ZTZE, BB098JPWGA, 1ZAT1Z967A, 0PF6TM8TWT, 1ZB13N78XW]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_subalgebra
---

## Definition

Let $\mathfrak g$ be a finite-dimensional [[Lie algebra|5JJYBJ6A8K]] over a field $k$, and let $x \in \mathfrak g$.
Let $\operatorname{ad} x \colon \mathfrak g \to \mathfrak g$ be the map $y \mapsto [x, y]$ of the [[adjoint representation|54XSPNAM1J]].
The *Engel subalgebra* of $x$ is
$$E_{\mathfrak g}(x) = \set{y \in \mathfrak g : (\operatorname{ad} x)^n y = 0 \text{ for some } n \ge 1}.$$

## Remarks

The set $E_{\mathfrak g}(x)$ is the [[generalised eigenspace|0AJ035ZTZE]] of $\operatorname{ad} x$ for the eigenvalue $0$.
It is a [[subalgebra|WKSSTQ69AK]] by the Leibniz rule $(\operatorname{ad} x)^n [y, z] = \sum_{i=0}^{n} \binom{n}{i} [(\operatorname{ad} x)^i y, (\operatorname{ad} x)^{n-i} z]$, and it contains $x$.

Example: in the [[special linear Lie algebra|1ZAT1Z967A]] $\mathfrak{sl}_2(k)$ with $\operatorname{char} k \ne 2$ and basis $e, h, f$, the map $\operatorname{ad} h$ sends $e \mapsto 2e$, $h \mapsto 0$ and $f \mapsto -2f$.
So $E(h) = kh$.
Since $\operatorname{ad} e$ is nilpotent, with $(\operatorname{ad} e)^3 = 0$, one gets $E(e) = \mathfrak{sl}_2(k)$.

Non-example: $kh + ke$ is a subalgebra containing $h$, but it is not $E(h)$, since $(\operatorname{ad} h)^n e = 2^n e \ne 0$ for all $n$.

If $k$ is an [[algebraically closed field|0PF6TM8TWT]] of [[characteristic|1ZB13N78XW]] $0$, the Engel subalgebras of smallest dimension are [[Cartan subalgebras|BB098JPWGA]].
