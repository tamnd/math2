---
tag: 6D73FFD9DC
kind: statement
role: proposition
name: Runge–Kutta–Fehlberg method
msc: [65L06, 65L05, 65L50]
uses: [7DBPJKYC6C, RH8BD7PW5F, T220HF0562, 6MREWBZR7R]
about: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Runge%E2%80%93Kutta%E2%80%93Fehlberg_method
same_as:
  wikidata: Q7379856
  wikipedia: Runge–Kutta–Fehlberg method
---

## Statement

Consider the explicit six-stage [[Butcher tableau|RH8BD7PW5F]] with two weight rows
$$\begin{array}{c|cccccc}
0 \\
\frac14 & \frac14 \\
\frac38 & \frac{3}{32} & \frac{9}{32} \\
\frac{12}{13} & \frac{1932}{2197} & -\frac{7200}{2197} & \frac{7296}{2197} \\
1 & \frac{439}{216} & -8 & \frac{3680}{513} & -\frac{845}{4104} \\
\frac12 & -\frac{8}{27} & 2 & -\frac{3544}{2565} & \frac{1859}{4104} & -\frac{11}{40} \\
\hline
b^{T} & \frac{25}{216} & 0 & \frac{1408}{2565} & \frac{2197}{4104} & -\frac15 & 0 \\
\hat b^{T} & \frac{16}{135} & 0 & \frac{6656}{12825} & \frac{28561}{56430} & -\frac{9}{50} & \frac{2}{55}
\end{array}$$
Then:

1. the [[Runge–Kutta method|7DBPJKYC6C]] with weights $b$ has order $4$, and the one with weights $\hat b$ has order $5$;
2. both use the same six stages $K_1, \ldots, K_6$, so a step gives $y_{n+1} = y_n + h \sum_i b_i K_i$ and $\hat y_{n+1} = y_n + h \sum_i \hat b_i K_i$ for six evaluations of $f$;
3. the difference $\hat y_{n+1} - y_{n+1}$ equals the [[local truncation error|T220HF0562]] of the fourth-order step up to a term $O(h^6)$, for $f$ smooth enough.

## Remarks

Clause 1 is checked against Butcher's order conditions.
There are $8$ conditions for the trees with at most $4$ vertices, for $b$, and $17$ for the trees with at most $5$ vertices, for $\hat b$.
For instance $\sum b_i = \sum \hat b_i = 1$ and $\sum \hat b_i c_i^4 = \frac15$.
Clause 3 follows from clause 1: the local errors of the two steps are $O(h^5)$ and $O(h^6)$, so their difference is the first one up to $O(h^6)$.
The estimate drives [[adaptive step size|6MREWBZR7R]] control: a step is accepted when the estimate is below the tolerance, and the next step is scaled by about $(\mathrm{tol}/\mathrm{err})^{1/5}$.
Erwin Fehlberg proposed such embedded pairs in 1969; in his original use the fourth-order value is propagated, while many codes propagate the fifth-order value.

## Explanations

### L1 human

To choose good step sizes, a solver must know how large its error is.
The Fehlberg method computes two answers of different accuracy from the same six slope evaluations.
Their difference estimates the error at almost no extra cost, and the step is then made longer or shorter.

### L2 human

This is the classic example of an embedded Runge–Kutta pair, often called RKF45.
It was largely replaced in modern software by the [[Dormand–Prince method|CDMXAH4A7G]], whose coefficients are tuned to make the error of the fifth-order solution small and which reuses the last stage.
The idea of embedding, two weight vectors on one set of stages, is the basis of nearly all explicit adaptive ODE solvers.
