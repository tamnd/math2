---
tag: PSAX8W3ZYV
kind: example
name: Rudin–Shapiro polynomials
msc: [42A05, 11B83]
instance_of: [5A16A9W335]
uses: [5A16A9W335]
sources:
  - url: https://en.wikipedia.org/wiki/Rudin%E2%80%93Shapiro_sequence
---

## Example

Define polynomials $P_m$ and $Q_m$ by $P_0(z) = Q_0(z) = 1$ and, for $m \ge 0$,
$$P_{m+1}(z) = P_m(z) + z^{2^m} Q_m(z), \qquad Q_{m+1}(z) = P_m(z) - z^{2^m} Q_m(z).$$
These are the *Rudin–Shapiro polynomials*.
By induction, $P_m$ and $Q_m$ have degree $2^m - 1$, and all $2^m$ of their coefficients are $+1$ or $-1$.
Indeed $P_m$ fills the coefficients of $1, \ldots, z^{2^m - 1}$ and $z^{2^m} Q_m$ fills those of $z^{2^m}, \ldots, z^{2^{m+1} - 1}$.
So they are [[Littlewood polynomials|5A16A9W335]].
The first ones are $P_1(z) = 1 + z$, $Q_1(z) = 1 - z$ and $P_2(z) = 1 + z + z^2 - z^3$.

For $\abs{z} = 1$, the parallelogram law $\abs{u + v}^2 + \abs{u - v}^2 = 2\abs{u}^2 + 2\abs{v}^2$ with $\abs{z^{2^m}} = 1$ gives
$$\abs{P_{m+1}(z)}^2 + \abs{Q_{m+1}(z)}^2 = 2 \left( \abs{P_m(z)}^2 + \abs{Q_m(z)}^2 \right).$$
Hence $\abs{P_m(z)}^2 + \abs{Q_m(z)}^2 = 2^{m+1}$, and
$$\max_{\abs{z} = 1} \abs{P_m(z)} \le \sqrt{2} \cdot \sqrt{2^m}.$$

## Remarks

Since the mean square of $\abs{P_m}$ on the circle is $2^m$, the maximum is at most $\sqrt 2$ times the root mean square.
For a polynomial with $N$ coefficients $\pm 1$, the maximum on the circle is always at least $\sqrt N$, so this is optimal up to the factor $\sqrt 2$.
A random choice of signs typically gives a maximum of order $\sqrt{N \log N}$, so the Rudin–Shapiro signs are much better than random.
The coefficients of the $P_m$ form the Rudin–Shapiro sequence, an automatic sequence.

## Explanations

### L1 human

The Rudin–Shapiro polynomials are built by a doubling rule.
Glue the old polynomial to a shifted copy of its partner, once with a plus sign and once with a minus sign.
All coefficients stay $\pm 1$.
The rule keeps the sum of the squared sizes of the pair exactly doubling at every point of the circle.
So neither polynomial can ever be much larger than its average size, which makes them almost flat from above.
