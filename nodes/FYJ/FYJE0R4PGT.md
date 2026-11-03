---
tag: FYJE0R4PGT
kind: statement
role: theorem
name: Kesten's criterion for amenability
msc: ["43A07", "60G50", "20F65"]
uses: [G5S1M9, 059TJN0NZ1, 04VZE3FZXF, CEAT9BESKK, 9V7YQA85PC]
about: [CEAT9BESKK, 04VZE3FZXF]
sources:
  - url: https://en.wikipedia.org/wiki/Amenable_group
---

## Statement

Let $G$ be a countable [[group|G5S1M9]] with identity $e$.
Let $\mu$ be a [[probability measure|059TJN0NZ1]] on $G$ that is symmetric, $\mu(g) = \mu(g^{-1})$ for all $g$, and whose support generates $G$ as a group.
Let $\mu^{*n}$ be the $n$-fold convolution power of $\mu$.
So $\mu^{*n}(e)$ is the probability that the [[random walk|04VZE3FZXF]] with steps distributed by $\mu$ is back at $e$ after $n$ steps.
Then $G$ is [[amenable|CEAT9BESKK]] if and only if
$$\limsup_{n \to \infty} \mu^{*n}(e)^{1/n} = 1.$$

## Remarks

The left side is the [[spectral radius|9V7YQA85PC]] of the random walk.
It equals the norm of the self-adjoint convolution operator $\lambda(\mu) \colon \xi \mapsto \mu * \xi$ on $\ell^2(G)$, because $\mu^{*2n}(e) = \ip{\lambda(\mu)^{2n} \delta_e}{\delta_e}$.
So the criterion is the case of [[Hulanicki's theorem|P18JWQ7Y84]] for this measure: $G$ is amenable exactly when $\norm{\lambda(\mu)} = 1$.

Example: for $G = \Z$ and $\mu = \frac12(\delta_1 + \delta_{-1})$, one has $\mu^{*2n}(0) = \binom{2n}{n} 4^{-n}$, which is about $1/\sqrt{\pi n}$, and its $2n$-th root tends to $1$.
For the free group $F_k$ with $k \ge 2$ free generators, and $\mu$ uniform on the generators and their inverses, Kesten computed the spectral radius $\sqrt{2k - 1}/k$, which is less than $1$.
So the return probabilities decay exponentially, and $F_k$ is not amenable.

## Explanations

### L1 human

Take a random walk on a group, with symmetric steps.
On an amenable group, the chance of being back at the start after many steps decays slower than any exponential.
On a non-amenable group it decays exponentially, because the walk escapes too fast.
So one can test amenability by watching a random walker.

### L2 human

Kesten's criterion links amenability with probability and with the spectrum of the Laplacian of a Cayley graph.
Let $S$ be a finite symmetric generating set and let $\mu$ be uniform on $S$.
Then $\lambda(\mu)$ is the Markov operator of the [[Cayley graph|0GYQK9NDJF]], and amenability is equivalent to $1$ lying in its spectrum.
Grigorchuk's cogrowth criterion restates it in terms of the growth of the set of relations.
It was used to show that some groups without free subgroups are not amenable.
