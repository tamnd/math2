---
tag: QQTPD2TZ0Z
kind: definition
name: Triangulation
msc: [57Q15, 55U10]
defines: YH170WBQ6M
uses: [0CQHFPGJ45, V8GZ0W1ZZ5, 0QT00PB5G2]
sources:
  - url: https://en.wikipedia.org/wiki/Triangulation_(topology)
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A *triangulation* of $X$ is a pair $(K, h)$ with $K$ a [[simplicial complex|V8GZ0W1ZZ5]].
The map $h \colon \abs{K} \to X$ must be a [[homeomorphism|0QT00PB5G2]] from the geometric realization $\abs{K}$ of $K$ onto $X$.
$X$ is *triangulable* if it has a triangulation.

## Remarks

Let $K$ be the simplicial complex of all proper faces of a $3$-simplex in $\R^3$, with $4$ vertices, $6$ edges and $4$ triangles.
Radial projection from the barycentre onto the sphere centred there is a homeomorphism $\abs{K} \to S^2$, so $K$ with this map is a triangulation of $S^2$.

The CW structure of $S^2$ with one $0$-cell and one $2$-cell is not a triangulation.
Its $2$-cell is glued to the point along its whole boundary circle, while in a simplicial complex each triangle has three distinct vertices and three edges.

Some authors allow only finite or locally finite complexes $K$, and some require $h$ to be piecewise linear in a given structure.
Every smooth manifold is triangulable, while some topological $4$-manifolds, such as the $E_8$ manifold, are not.
