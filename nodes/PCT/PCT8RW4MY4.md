---
tag: PCT8RW4MY4
kind: definition
name: Digamma function
msc: ["33B15"]
defines: HWRRXB0YXS
uses: [0H5SYBSED9, 0ZZ7ZYDR8W]
sources:
  - url: https://en.wikipedia.org/wiki/Digamma_function
---

## Definition

Let $\Gamma$ be the [[gamma function|0H5SYBSED9]], viewed as a [[meromorphic function|0ZZ7ZYDR8W]] on $\C$ with poles at $0, -1, -2, \ldots$ and no zeros.
The *digamma function* is the meromorphic function
$$\psi(z) = \frac{\Gamma'(z)}{\Gamma(z)} = \frac{d}{dz} \log \Gamma(z), \qquad z \in \C \setminus \set{0, -1, -2, \ldots}.$$

## Remarks

Example: from $\Gamma(z+1) = z\,\Gamma(z)$, taking logarithmic derivatives gives $\psi(z+1) = \psi(z) + \frac1z$.
With $\psi(1) = \Gamma'(1) = -\gamma$, where $\gamma$ is the [[Euler–Mascheroni constant|00C5P9JZBK]], this gives $\psi(n+1) = H_n - \gamma$ for every integer $n \ge 1$, where $H_n = 1 + \frac12 + \cdots + \frac1n$ is the [[harmonic number|0NANDX7V02]].
Another value is $\psi(\frac12) = -\gamma - 2\ln 2$.

Non-example of a valid argument: $z = 0$ is a pole of $\Gamma$, so $\psi$ is not defined there.
In fact $\psi$ has a simple pole with residue $-1$ at each of $0, -1, -2, \ldots$.

The function $\psi$ has no other poles, because $\Gamma$ has no zeros.
