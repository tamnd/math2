---
records:
    - id: CD968TZKF9
      kind: monograph
      title: Riemannsche Geometrie im Großen
      creators:
        - name: Detlef Gromoll
          role: author
        - name: Wilhelm Klingenberg
          role: author
        - name: Wolfgang Meyer
          role: author
      date: "1968"
      expressions:
        - key: e1
          kind: edition
          date: "1968"
          ids:
            doi:
                - 10.1007/978-3-540-35901-2
                - 10.1007/bfb0079185
          manifestations:
            - key: m1
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1968"
              ids:
                isbn:
                    - "9783540042259"
                    - "9783540359012"
            - key: m2
              kind: print
              publisher: Springer Berlin Heidelberg
              date: "1975"
              ids:
                isbn:
                    - "9783540071334"
                    - "9783540358527"
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-3-540-35901-2
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/bfb0079185
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
