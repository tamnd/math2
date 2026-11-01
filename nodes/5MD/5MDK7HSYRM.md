---
tag: 5MDK7HSYRM
kind: statement
role: theorem
name: Itô isometry
msc: [60H05]
uses: [22735FGJV6, JA95NH206E, 0DCT0QZVQ1]
about: [JA95NH206E]
sources:
  - url: https://en.wikipedia.org/wiki/It%C3%B4_isometry
same_as:
  wikidata: Q6095356
  wikipedia: Itô isometry
---

## Statement

Let $(B_t)_{t \ge 0}$ be a [[Brownian motion|22735FGJV6]] for a filtration $(\mathcal{F}_t)$, and let $T > 0$.
Let $H$ be a progressively measurable process with $E\left[\int_0^T H_t^2 \, dt\right] < \infty$.
Then the [[Itô integral|JA95NH206E]] satisfies
$$E\left[\left(\int_0^T H_t \, dB_t\right)^2\right] = E\left[\int_0^T H_t^2 \, dt\right],$$
where $E$ is the [[expected value|0DCT0QZVQ1]].

## Remarks

For a simple process $H = \sum_i \xi_i \mathbf{1}_{(t_i, t_{i+1}]}$, expand the square of $\sum_i \xi_i \Delta B_i$.
A cross term $E[\xi_i \xi_j \Delta B_i \Delta B_j]$ with $i < j$ vanishes, because $\Delta B_j$ has mean zero and is independent of $\mathcal{F}_{t_j}$.
A diagonal term equals $E[\xi_i^2] (t_{i+1} - t_i)$, because $\Delta B_i$ is independent of $\mathcal{F}_{t_i}$ with variance $t_{i+1} - t_i$.
The general case follows by approximation, and this is how the integral is defined.
Example: for $H_t = B_t$ with $B_0 = 0$, the right side is $\int_0^T t \, dt = T^2/2$, and indeed $\int_0^T B_t \, dB_t = \tfrac12 (B_T^2 - T)$ has variance $\tfrac14 (3T^2 - 2T^2 + T^2) = T^2/2$.

## Explanations

### L1 human

The Itô integral of $H$ is a random number with mean zero.
Its variance equals the expected total of $H^2$ over time.
So the size of the integral can be computed by an ordinary integral, without the random noise.

### L2 human

The isometry is the key step in the construction of the Itô integral: it extends the integral from simple processes to all square-integrable adapted ones.
Its polarised form gives $E\left[\int H \, dB \int K \, dB\right] = E\left[\int H K \, dt\right]$.
For a general continuous martingale $M$ in place of $B$, the same identity holds with $dt$ replaced by $d\langle M \rangle_t$.
