---
records:
    - id: 8GXK1E6NY4
      kind: monograph
      title: Introduction to Analytic Number Theory
      creators:
        - name: Tom M. Apostol
          role: author
      date: "1976"
      expressions:
        - key: e1
          kind: edition
          date: "1976"
          ids:
            doi:
                - 10.1007/978-1-4757-5579-4
                - 10.1007/978-3-662-28579-4
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1976"
              ids:
                isbn:
                    - "9781441928054"
                    - "9781475755794"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1976"
              ids:
                isbn:
                    - "9783540901631"
                    - "9783662285794"
      relations:
        - kind: part_of
          to: NWQC4TW7S9
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4757-5579-4
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-662-28579-4
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
