---
tag: E46ZSSFR1H
kind: statement
role: theorem
name: Kirchhoff's theorem for directed multigraphs
sources:
  - wikipedia: en:1270691@r1374532193
    locator: Kirchhoff's theorem, section Particular cases and generalizations > Kirchhoff's theorem for directed multigraphs
    note: adopted
    mention: wikipedia://en/1270691#6V5P
    sections: [Statement]
inventory: [WX9M246EJX]
---

## Statement

Kirchhoff's theorem can be modified to give the number of oriented spanning trees in directed multigraphs. The matrix *Q* is constructed as follows:

- The entry *q<sub>i,j</sub>* for distinct *i* and *j* equals −*m*, where *m* is the number of edges from *i* to *j*;
- The entry *q<sub>i,i</sub>* equals the indegree of *i* minus the number of loops at *i*.

The number of oriented spanning trees rooted at a vertex *i* is the determinant of the matrix gotten by removing the *i*th row and column of *Q*
