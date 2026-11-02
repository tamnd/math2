---
tag: 7YEJ79ZMV5
kind: definition
name: Barrier
msc: [31B20, 31B25, 35J25]
defines: ED0SZS1VED
uses: [X4V2S56YQQ, 02BH3MCBQB, 05D5EGMFYV, 0X3WGX95FE]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]], and let $\xi$ be a point of its [[boundary|05D5EGMFYV]] $\partial\Omega$.
A *barrier* at $\xi$ is a function $w \colon \overline{\Omega} \to \R$ such that:

1. $w$ is [[continuous|0X3WGX95FE]] on $\overline{\Omega}$;
2. $w$ is [[superharmonic|X4V2S56YQQ]] on $\Omega$;
3. $w(\xi) = 0$ and $w(x) > 0$ for every $x \in \overline{\Omega} \setminus \set{\xi}$.

## Remarks

Example: suppose there is a closed ball $\overline{B}(y, R)$ with $\overline{B}(y, R) \cap \overline{\Omega} = \set{\xi}$, and let $n \ge 3$.
Then $w(x) = R^{2-n} - \abs{x - y}^{2-n}$ is a barrier at $\xi$.
It is continuous on $\overline{\Omega}$ and harmonic on $\Omega$, since $y \notin \overline{\Omega}$; it vanishes at $\xi$ because $\abs{\xi - y} = R$; and $\abs{x - y} > R$ for the other points $x \in \overline{\Omega}$, which gives $w(x) > 0$.
For $n = 2$ the function $w(x) = \log(\abs{x - y}/R)$ plays the same role.
Non-example: $w(x) = \abs{x - \xi}^2$ satisfies clauses 1 and 3, but $\Delta w = 2n > 0$, so it is strictly subharmonic and fails clause 2.
A *local barrier* is a function with these properties on $\overline{\Omega} \cap N$ for some neighbourhood $N$ of $\xi$.
A local barrier yields a barrier, so the two notions give the same regular points.
