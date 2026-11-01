---
tag: Q5QFYKD004
kind: statement
role: theorem
name: Hahn–Mazurkiewicz theorem
msc: [54F15, 54C05]
uses: [0S1FJ8VEX9, 0X3WGX95FE, 01RVCMSN5N, 0TVJZYB6SH, 0V032VWTHD, FDVAHRJKF3, 03PPNCM9GG]
about: [NJQ196M1WR, FDVAHRJKF3]
sources:
  - url: https://en.wikipedia.org/wiki/Space-filling_curve
---

## Statement

Let $X$ be a nonempty [[Hausdorff space|0S1FJ8VEX9]].
Then there is a [[continuous|0X3WGX95FE]] [[surjection|01RVCMSN5N]] $[0, 1] \to X$ if and only if $X$ is [[compact|0TVJZYB6SH]], [[connected|0V032VWTHD]], [[locally connected|FDVAHRJKF3]] and [[second-countable|03PPNCM9GG]].

## Remarks

A continuous image of $[0, 1]$ in a Hausdorff space is compact, connected and metrizable, and the map is a quotient map, which carries local connectedness over to $X$.
For the converse, $X$ is metrizable by the [[Urysohn metrization theorem|HBFHDH4EJX]], so it is a locally connected [[continuum|NJQ196M1WR]].
The [[Cantor set|0BXNDZFQME]] maps continuously onto every compact metric space.
Local connectedness lets one join the images of the ends of each removed interval by small arcs, which extends the map to all of $[0, 1]$.
For example, the square $[0, 1]^2$ satisfies the conditions, so there is a [[space-filling curve|QPRHC4DZ20]] onto it.
The [[Warsaw circle|17VG475BRV]] is compact, connected and metrizable but not locally connected, so it is not a continuous image of $[0, 1]$.

## Explanations

### L1 human

The theorem says exactly which spaces can be traced by a single continuous curve that passes through every point.
They are the compact spaces in one piece that are also connected at small scales near every point.
So squares, cubes and even the Hilbert cube can be filled by a curve.

### L2 human

The metric spaces in the theorem are the Peano continua, the locally connected continua.
The theorem turns the surprise of the Peano curve into a general rule.
It shows that a continuous image of an interval can have any finite dimension.
A related fact is that every Peano continuum is arcwise connected.
