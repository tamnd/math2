---
records:
    - id: ZRSMHPSCXF
      kind: monograph
      title: Geometrical Methods in the Theory of Ordinary Differential Equations
      creators:
        - name: V. I. Arnold
          role: author
      date: "1983"
      expressions:
        - key: e1
          kind: edition
          date: "1983"
          ids:
            doi:
                - 10.1007/978-1-4612-1037-5
                - 10.1007/978-1-4684-0147-9
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1988"
              ids:
                isbn:
                    - "9781461269946"
                    - "9781461210375"
            - key: m2
              kind: print
              publisher: Springer US
              date: "1983"
              ids:
                isbn:
                    - "9781468401493"
                    - "9781468401479"
      relations:
        - kind: part_of
          to: GQFCNY816R
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1037-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-0147-9
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
