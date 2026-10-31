---
records:
    - id: WWM9XRK9VZ
      kind: monograph
      title: Applications of Lie Groups to Differential Equations
      creators:
        - name: Peter J. Olver
          role: author
      date: "1986"
      expressions:
        - key: e1
          kind: edition
          date: "1986"
          ids:
            doi:
                - 10.1007/978-1-4612-4350-2
                - 10.1007/978-1-4684-0274-2
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1993"
              ids:
                isbn:
                    - "9780387950006"
                    - "9781461243502"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1986"
              ids:
                isbn:
                    - "9781468402766"
                    - "9781468402742"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-4350-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0274-2
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
