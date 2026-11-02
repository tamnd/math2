---
tag: CDMXAH4A7G
kind: statement
role: proposition
name: Dormand–Prince method
msc: [65L06, 65L05, 65L50]
uses: [7DBPJKYC6C, RH8BD7PW5F, T220HF0562, 6MREWBZR7R]
about: [7DBPJKYC6C]
sources:
  - url: https://en.wikipedia.org/wiki/Dormand%E2%80%93Prince_method
same_as:
  wikidata: Q5298067
  wikipedia: Dormand–Prince method
---

## Statement

Consider the explicit seven-stage [[Butcher tableau|RH8BD7PW5F]] with two weight rows
$$\begin{array}{c|ccccccc}
0 \\
\frac15 & \frac15 \\
\frac{3}{10} & \frac{3}{40} & \frac{9}{40} \\
\frac45 & \frac{44}{45} & -\frac{56}{15} & \frac{32}{9} \\
\frac89 & \frac{19372}{6561} & -\frac{25360}{2187} & \frac{64448}{6561} & -\frac{212}{729} \\
1 & \frac{9017}{3168} & -\frac{355}{33} & \frac{46732}{5247} & \frac{49}{176} & -\frac{5103}{18656} \\
1 & \frac{35}{384} & 0 & \frac{500}{1113} & \frac{125}{192} & -\frac{2187}{6784} & \frac{11}{84} \\
\hline
b^{T} & \frac{35}{384} & 0 & \frac{500}{1113} & \frac{125}{192} & -\frac{2187}{6784} & \frac{11}{84} & 0 \\
\hat b^{T} & \frac{5179}{57600} & 0 & \frac{7571}{16695} & \frac{393}{640} & -\frac{92097}{339200} & \frac{187}{2100} & \frac{1}{40}
\end{array}$$
Then:

1. The [[Runge–Kutta method|7DBPJKYC6C]] with weights $b$ has order $5$, and the one with weights $\hat b$ has order $4$.
2. The last row of the matrix equals $b^{T}$ and $c_7 = 1$.
   So the seventh stage of a step equals $f(t_{n+1}, y_{n+1})$, which is the first stage of the next step.
3. The difference $y_{n+1} - \hat y_{n+1}$ of the two results equals the [[local truncation error|T220HF0562]] of the fourth-order step up to a term $O(h^6)$, for $f$ smooth enough.

## Remarks

Clause 1 is checked against Butcher's order conditions on rooted trees; for example $\sum b_i = \sum \hat b_i = 1$ and $\sum b_i c_i^4 = \frac15$, while $\sum \hat b_i c_i^4 \ne \frac15$.
Clause 2 is the "first same as last" property: an accepted step needs only six new evaluations of $f$.
The method propagates the fifth-order value $y_{n+1}$, a practice called local extrapolation, and uses the error estimate of clause 3 for [[adaptive step size|6MREWBZR7R]] control.
John Dormand and Peter Prince published the pair in 1980, choosing the free coefficients to make the error constants of the fifth-order formula small.

## Explanations

### L1 human

The Dormand–Prince method is a Runge–Kutta method that computes two answers per step, one of order five and one of order four.
Their difference tells the solver how large the error is, so it can adjust the step size.
It reuses its last slope evaluation as the first of the next step, which saves work.

### L2 human

This pair, often called DOPRI5 or RK45, is the default non-stiff solver in many software packages, for example the ode45 function of MATLAB.
Compared with the [[Runge–Kutta–Fehlberg method|6D73FFD9DC]], it advances with the more accurate formula and has smaller error coefficients.
It also admits a dense output, a polynomial interpolant that gives accurate values between the grid points.
For stiff problems it needs very small steps, and implicit methods are preferred.
