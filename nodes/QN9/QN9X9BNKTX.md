---
tag: QN9X9BNKTX
kind: example
name: Logistic map
msc: ["37E05", "37G15", "37N25"]
instance_of: [5AA9AJEARJ]
uses: [5AA9AJEARJ, R6QVS6P21N, NQDTTZ59X8, D0A22MEB1F, HNXXAPQKG3, 0CC4VC7KR3]
sources:
  - url: https://en.wikipedia.org/wiki/Logistic_map
same_as:
  wikidata: Q587182
  wikipedia: Logistic map
---

## Example

For a parameter $r \in [0, 4]$, the *logistic map* is
$$f_r \colon [0, 1] \to [0, 1], \qquad f_r(x) = r x (1 - x).$$
It is a [[discrete-time dynamical system|5AA9AJEARJ]] on $[0, 1]$: the maximum of $f_r$ on $[0, 1]$ is $f_r(1/2) = r/4 \le 1$ and $f_r \ge 0$ there, so $f_r$ maps $[0, 1]$ into itself.

Check of the first bifurcations.
The [[fixed points|R6QVS6P21N]] are $0$ and, for $r > 1$, $x_r = 1 - 1/r$.
Since $f_r'(x) = r(1 - 2x)$, one gets $f_r'(0) = r$ and $f_r'(x_r) = 2 - r$.
So for $1 < r < 3$ the fixed point $x_r$ attracts nearby points.
At $r = 3$ its derivative is $-1$, and the map has a [[period-doubling bifurcation|NQDTTZ59X8]].
For $r$ slightly above $3$ an attracting orbit of period $2$ appears.

## Remarks

As $r$ grows further, attracting orbits of periods $4, 8, 16, \dots$ appear at parameters that accumulate at $r_\infty \approx 3.5699$.
For $r = 4$ the map is [[topologically conjugate|HNXXAPQKG3]] to the full [[tent map|D0A22MEB1F]] $T(y) = 1 - \abs{1 - 2y}$ by $h(y) = \sin^2(\pi y / 2)$.
Indeed $f_4(h(y)) = 4 \sin^2(\pi y/2) \cos^2(\pi y/2) = \sin^2(\pi y)$, and $h(T(y)) = \sin^2(\pi y)$ for $y \le 1/2$ and $\sin^2(\pi - \pi y) = \sin^2(\pi y)$ for $y > 1/2$.
For $r = 4$ the measure with density $\frac{1}{\pi \sqrt{x(1 - x)}}$ on $(0, 1)$ is invariant.
The map is the discrete-time analogue of the [[logistic equation|0CC4VC7KR3]] of population growth.

## Explanations

### L1 human

The logistic map is a toy model of a population from one year to the next: it grows when small and is held back when large.
One step takes just two multiplications and a subtraction.
Yet as $r$ increases the long-run behaviour goes from a steady state to a cycle of $2$ years, then $4$, $8$, and then to chaos.
It became famous as the simplest example of how chaos can arise from a very simple rule.
