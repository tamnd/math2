---
tag: NWQ9Y7ZEAW
kind: definition
name: Lemniscate elliptic functions
msc: ["33E05"]
defines: TQDZQ964AZ
uses: [V5A2S8QYQQ, FF9ZPCZ59K, 0M3YQJ81NB]
sources:
  - url: https://en.wikipedia.org/wiki/Lemniscate_elliptic_functions
---

## Definition

Let $\varpi = 2\int_0^1 dt/\sqrt{1 - t^4}$ be the [[lemniscate constant|V5A2S8QYQQ]].
The map $x \mapsto \int_0^x dt/\sqrt{1 - t^4}$ is a strictly increasing bijection from $[-1, 1]$ onto $[-\varpi/2, \varpi/2]$.
The *lemniscate sine* $\operatorname{sl}$ is the inverse map on $[-\varpi/2, \varpi/2]$, extended to $\R$ by $\operatorname{sl}(x + \varpi) = -\operatorname{sl}(x)$.
It extends further to a meromorphic function on $\C$ by [[analytic continuation|0M3YQJ81NB]].
The *lemniscate cosine* is $\operatorname{cl}(z) = \operatorname{sl}(\varpi/2 - z)$.

## Remarks

The function $\operatorname{sl}$ is odd, satisfies $\operatorname{sl}(0) = 0$, $\operatorname{sl}(\varpi/2) = 1$, and $(\operatorname{sl}')^2 = 1 - \operatorname{sl}^4$.
It is an [[elliptic function|FF9ZPCZ59K]] whose periods form the lattice spanned by $(1 + i)\varpi$ and $(1 - i)\varpi$; in particular $2\varpi$ and $2i\varpi$ are periods.
It satisfies $\operatorname{sl}(iz) = i\operatorname{sl}(z)$.
The two functions are linked by $\operatorname{sl}^2 + \operatorname{cl}^2 + \operatorname{sl}^2\operatorname{cl}^2 = 1$.
Example: at $z = \varpi/2$ one has $\operatorname{sl} = 1$ and $\operatorname{cl} = \operatorname{sl}(0) = 0$, and indeed $1 + 0 + 0 = 1$.
Non-example: the inverse of $\int_0^x dt/\sqrt{1 - t^2}$ is $\sin$, which is not the lemniscate sine: it has the single period $2\pi$ and satisfies $(\sin')^2 = 1 - \sin^2$ instead of $1 - \operatorname{sl}^4$.
In terms of the [[Jacobi elliptic functions|P071B692JF]], $\operatorname{sl}(z) = \operatorname{sn}(z; k)$ with $k^2 = -1$, since this $\operatorname{sn}$ solves the same equation $(y')^2 = (1 - y^2)(1 + y^2)$ with $y(0) = 0$, $y'(0) = 1$.
